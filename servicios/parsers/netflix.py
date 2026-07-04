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

        # ==========================
        # CÓDIGO DE 4 DÍGITOS
        # ==========================

        for i, linea in enumerate(textos):

            linea_normalizada = linea.strip().lower()

            if "ingresa este código para iniciar sesión" in linea_normalizada:

                for siguiente in textos[i + 1:]:

                    numero = siguiente.strip().replace(" ", "")

                    if re.fullmatch(r"\d{4}", numero):

                        datos["codigo"] = numero
                        return datos

        # ==========================
        # CÓDIGO TEMPORAL
        # ==========================

        enlaces = soup.find_all("a", href=True)

        for enlace in enlaces:

            texto_boton = enlace.get_text(" ", strip=True).lower()

            if (
                "obtener código" in texto_boton
                or
                "obtener codigo" in texto_boton
            ):

                datos["enlace"] = enlace["href"]
                return datos

    except Exception:
        pass

    return datos