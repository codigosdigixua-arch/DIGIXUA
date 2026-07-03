import os

# =====================================================
# DIGIXUA
# Configuración general
# =====================================================

# -----------------------------------------------------
# Credenciales Gmail
# (Se configuran como variables de entorno)
# -----------------------------------------------------

EMAIL = os.getenv("DIGIXUA_EMAIL")

PASSWORD = os.getenv("DIGIXUA_PASSWORD")

IMAP_SERVER = "imap.gmail.com"

IMAP_PORT = 993


# -----------------------------------------------------
# Búsqueda
# -----------------------------------------------------

# Tiempo máximo de búsqueda (minutos)

MINUTOS_BUSQUEDA = 15


# Número máximo de correos que se revisarán

MENSAJES_A_REVISAR = 100


# -----------------------------------------------------
# Tipos permitidos
# -----------------------------------------------------

TIPOS_VALIDOS = [

    "Netflix: Tu código de inicio de sesión",

    "Netflix: Tu código de acceso temporal",

    "Netflix: Nueva solicitud de inicio de sesión",

    "Importante: Cómo actualizar tu Hogar con Netflix",

    "Tu código de acceso único para Disney+"

]