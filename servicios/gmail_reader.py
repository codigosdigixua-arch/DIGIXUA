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


def leer_ultimos_correos():

    resultados = []

    # ===========================================
    # Verificar configuración
    # ===========================================

    if not EMAIL or not PASSWORD:

        raise Exception(
            "No se encontraron las variables de entorno DIGIXUA_EMAIL y DIGIXUA_PASSWORD."
        )

    # ===========================================
    # Conectar con Gmail
    # ===========================================

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

    lista_ids = mensajes[0].split()

    ultimos = lista_ids[-MENSAJES_A_REVISAR:]

    for correo_id in reversed(ultimos):

        status, datos = mail.fetch(
            correo_id,
            "(RFC822)"
        )

        if status != "OK":
            continue

        for respuesta in datos:

            if not isinstance(respuesta, tuple):
                continue

            mensaje = email.message_from_bytes(
                respuesta[1]
            )

            # ======================================
            # Asunto
            # ======================================

            asunto_original = mensaje.get("Subject")

            if asunto_original is None:
                continue

            asunto, codificacion = decode_header(
                asunto_original
            )[0]

            if isinstance(asunto, bytes):

                asunto = asunto.decode(
                    codificacion or "utf-8",
                    errors="ignore"
                )

            asunto = asunto.strip()

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

    mail.logout()

    return resultados