from bs4 import BeautifulSoup
import re


def procesar(texto):

    datos = {
        "codigo": None,
        "enlace": None
    }

    try:

        soup = BeautifulSoup(texto, "html.parser")

        textos = list(soup.stripped_strings)

        for i, linea in enumerate(textos):

            linea = linea.strip().lower()

            # Código de inicio de sesión
            if "ingresa este código para iniciar sesión" in linea:

                for siguiente in textos[i + 1:]:

                    siguiente = siguiente.strip()

                    # Eliminar espacios: 9 3 2 6 -> 9326
                    numero = siguiente.replace(" ", "")

                    if re.fullmatch(r"\d{4}", numero):

                        datos["codigo"] = numero
                        return datos

            # Código temporal (Netflix fuera del hogar)
            if "obtener código" in linea.lower():

                for enlace in soup.find_all("a", href=True):

                    href = enlace["href"]

                    if "netflix" in href.lower():

                        datos["enlace"] = href
                        return datos

    except Exception:
        pass

    return datos