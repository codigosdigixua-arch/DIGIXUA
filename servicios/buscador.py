from servicios.gmail_reader import leer_ultimos_correos


def buscar_destinatario(correo):

    correo = correo.strip().lower()

    resultados = leer_ultimos_correos(correo)

    if resultados:

        return resultados[0]

    return None