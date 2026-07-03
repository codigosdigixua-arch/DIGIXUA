from bs4 import BeautifulSoup


def procesar(texto):

    datos = {
        "enlace": None
    }

    try:

        soup = BeautifulSoup(texto, "html.parser")

        enlaces = soup.find_all("a", href=True)

        for enlace in enlaces:

            texto_boton = enlace.get_text(" ", strip=True).lower()

            if "aprobar" in texto_boton:

                datos["enlace"] = enlace["href"]

                return datos

    except Exception:
        pass

    return datos