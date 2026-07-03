from bs4 import BeautifulSoup
import re


def procesar(texto):

    datos = {
        "codigo": None
    }

    try:

        soup = BeautifulSoup(texto, "html.parser")

        contenido = soup.get_text(" ", strip=True)

        # Buscar códigos como:
        # 083917
        # 0 8 3 9 1 7
        coincidencias = re.findall(r"(?:\d\s*){6}", contenido)

        for codigo in coincidencias:

            codigo = re.sub(r"\s+", "", codigo)

            if len(codigo) == 6:

                datos["codigo"] = codigo
                return datos

    except Exception:
        pass

    return datos