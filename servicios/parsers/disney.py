from bs4 import BeautifulSoup
import re


def procesar(texto):

    datos = {
        "codigo": None
    }

    try:

        soup = BeautifulSoup(texto, "html.parser")

        # Obtener todo el texto del correo
        contenido = soup.get_text(" ", strip=True)

        # Buscar cualquier secuencia de 6 dígitos
        coincidencia = re.search(r"\b\d{6}\b", contenido)

        if coincidencia:

            datos["codigo"] = coincidencia.group()

    except Exception:
        pass

    return datos