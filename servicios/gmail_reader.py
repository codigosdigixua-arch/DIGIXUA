import imaplib
import email
from email.header import decode_header
from email.utils import parseaddr

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

    texto = ""

    for parte, codificacion in decode_header(asunto):

        if isinstance(parte, bytes):

            texto += parte.decode(
                codificacion or "utf-8",
                errors="ignore"
            )

        else:

            texto += parte

    return texto.strip()


def leer_ultimos_correos(correo_buscado=None):

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

    status, mensajes = mail.search(None, "ALL")

    if status != "OK":

        mail.logout()

        return resultados

    ids = mensajes[0].split()

    ids = ids[-MENSAJES_A_REVISAR:]

    for correo_id in reversed(ids):

        try:

            status, datos = mail.fetch(
                correo_id,
                "(RFC822)"
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

            destinatario = parseaddr(
                mensaje.get("To", "")
            )[1].lower()

            if correo_buscado:

                if destinatario != correo_buscado.lower():

                    continue

            asunto = decodificar_asunto(
                mensaje.get("Subject")
            )

           print("=" * 60)
            print("DESTINATARIO:", destinatario)
            print("ASUNTO:", asunto)

            resultado = analizar_asunto(asunto)

            print("RESULTADO:", resultado)

            if not resultado["valido"]:
                continue

            raise Exception(
                f"""
            DESTINATARIO: {destinatario}

            ASUNTO: {asunto}

            RESULTADO: {resultado}
            """
            )

            resultados.append({

                "tipo": resultado["tipo"],

                "destinatario": destinatario,

                "fecha": mensaje.get("Date", "").strip(),

                "asunto": asunto,

                "mensaje": mensaje

            })

            # Ya encontramos el correo buscado.
            if correo_buscado:
                break

        except Exception:

            continue

    mail.logout()

    return resultados