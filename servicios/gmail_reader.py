import imaplib
import email
from email.header import decode_header

from config import (
    EMAIL,
    PASSWORD,
    IMAP_SERVER,
    IMAP_PORT,
    MENSAJES_A_REVISAR
)

from servicios.filtros import analizar_asunto


def decodificar_asunto(asunto):

    if asunto is None:
        return ""

    partes = decode_header(asunto)

    texto = ""

    for parte, codificacion in partes:

        if isinstance(parte, bytes):

            texto += parte.decode(
                codificacion or "utf-8",
                errors="ignore"
            )

        else:

            texto += parte

    return texto.strip()


def leer_ultimos_correos():

    resultados = []

    if not EMAIL or not PASSWORD:

        raise Exception(
            "No se encontraron las variables de entorno."
        )

    mail = imaplib.IMAP4_SSL(
        IMAP_SERVER,
        IMAP_PORT
    )

    mail.login(
        EMAIL,
        PASSWORD
    )

    mail.select("INBOX")

    status, mensajes = mail.search(
        None,
        "ALL"
    )

    if status != "OK":

        mail.logout()

        return resultados

    ids = mensajes[0].split()

    if not ids:

        mail.logout()

        return resultados

    ids = ids[-MENSAJES_A_REVISAR:]

    for correo_id in reversed(ids):

        try:

            status, datos = mail.fetch(
                correo_id,
                "(BODY.PEEK[HEADER])"
            )

            if status != "OK":
                continue

            mensaje = None

            for respuesta in datos:

                if isinstance(respuesta, tuple):

                    mensaje = email.message_from_bytes(
                        respuesta[1]
                    )

                    break

            if mensaje is None:
                continue

            asunto = decodificar_asunto(
                mensaje.get("Subject")
            )

            resultado = analizar_asunto(asunto)

            if not resultado["valido"]:
                continue

            resultados.append({

                "tipo": resultado["tipo"],

                "destinatario":
                mensaje.get("To", "").strip(),

                "fecha":
                mensaje.get("Date", "").strip(),

                "asunto":
                asunto,

                "mensaje":
                mensaje

            })

        except Exception:

            continue

    mail.logout()

    return resultados