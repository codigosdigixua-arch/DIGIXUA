def analizar_asunto(asunto):

    asunto = asunto.lower().strip()

    # ==========================================
    # DISNEY+
    # ==========================================

    if "código de acceso único para disney" in asunto:

        return {
            "valido": True,
            "tipo": "DISNEY"
        }

    # ==========================================
    # NETFLIX - CÓDIGOS
    # ==========================================

    elif (
        "tu código de inicio de sesión" in asunto
        or
        "tu código de acceso temporal" in asunto
    ):

        return {
            "valido": True,
            "tipo": "NETFLIX_CODIGO"
        }

    # ==========================================
    # NETFLIX - SOLICITUD DE INICIO
    # ==========================================

    elif (
        "nueva solicitud de inicio de sesión" in asunto
        or
        "aprueba la nueva solicitud de inicio de sesión" in asunto
    ):

        return {
            "valido": True,
            "tipo": "NETFLIX_SOLICITUD"
        }

    # ==========================================
    # NETFLIX - HOGAR
    # ==========================================

    elif (
        "cómo actualizar tu hogar con netflix" in asunto
        or
        "actualizar tu hogar con netflix" in asunto
    ):

        return {
            "valido": True,
            "tipo": "NETFLIX_HOGAR"
        }

    # ==========================================
    # NO VÁLIDO
    # ==========================================

    return {
        "valido": False,
        "tipo": None
    }