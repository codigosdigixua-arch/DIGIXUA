from servicios.parsers.netflix import procesar as parser_netflix
from servicios.parsers.disney import procesar as parser_disney
from servicios.parsers.solicitud import procesar as parser_solicitud
from servicios.parsers.hogar import procesar as parser_hogar


def obtener_texto(mensaje):
    """
    Devuelve preferiblemente el HTML del correo.
    Si no existe HTML, devuelve el texto plano.
    """

    html = None
    plano = None

    if mensaje.is_multipart():

        for parte in mensaje.walk():

            tipo = parte.get_content_type()
            adjunto = str(parte.get("Content-Disposition"))

            if "attachment" in adjunto:
                continue

            try:

                contenido = parte.get_payload(decode=True)

                if contenido is None:
                    continue

                charset = parte.get_content_charset() or "utf-8"

                contenido = contenido.decode(
                    charset,
                    errors="ignore"
                )

                if tipo == "text/html":
                    html = contenido

                elif tipo == "text/plain":
                    plano = contenido

            except Exception:
                pass

    else:

        try:

            contenido = mensaje.get_payload(decode=True)

            if contenido is not None:

                charset = mensaje.get_content_charset() or "utf-8"

                plano = contenido.decode(
                    charset,
                    errors="ignore"
                )

        except Exception:
            pass

    if html:
        return html

    if plano:
        return plano

    return ""


def procesar_mensaje(resultado):

    texto = obtener_texto(resultado["mensaje"])

    codigo = None
    enlace = None

    datos = {}

    if resultado["tipo"] == "NETFLIX_CODIGO":

        datos = parser_netflix(texto) or {}

        import logging
        logging.warning(f"DATOS PARSER NETFLIX: {datos}")

        codigo = datos.get("codigo")
        enlace = datos.get("enlace")
        

    elif resultado["tipo"] == "DISNEY":

        datos = parser_disney(texto) or {}

        codigo = datos.get("codigo")

    elif resultado["tipo"] == "NETFLIX_HOGAR":

        datos = parser_hogar(texto) or {}

        enlace = datos.get("enlace")

    elif resultado["tipo"] == "NETFLIX_SOLICITUD":

        datos = parser_solicitud(texto) or {}

        enlace = datos.get("enlace")

    return {

        "tipo": resultado["tipo"],

        "correo": resultado["destinatario"],

        "fecha": resultado["fecha"],

        "asunto": resultado["asunto"],

        "codigo": codigo,

        "enlace": enlace,

        "texto": texto

    }