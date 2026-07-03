from bs4 import BeautifulSoup
import re


def procesar(texto):

    datos = {
        "codigo": None
    }

    try:

        soup = BeautifulSoup(texto, "html.parser")

        # Buscar todos los textos del HTML
        textos = soup.stripped_strings

        for linea in textos:

            # Un código Disney siempre son 6 dígitos
            if re.fullmatch(r"\d{6}", linea):

                datos["codigo"] = linea
                return datos

    except Exception:
        pass

    return datos