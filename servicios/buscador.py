from servicios.gmail_reader import leer_ultimos_correos


def buscar_destinatario(correo):

    correo = correo.strip().lower()

    correos = leer_ultimos_correos()

    for mensaje in correos:

        if mensaje["destinatario"].lower() == correo:

            return mensaje

    return None