from servicios.buscador import buscar_destinatario
from servicios.parser import procesar_mensaje


correo = input("Correo: ")

resultado = buscar_destinatario(correo)

print()

if resultado is None:

    print("⚠ No hay mensajes recientes.")

else:

    datos = procesar_mensaje(resultado)

    print("=" * 60)

    print("TIPO:", datos["tipo"])

    print("CORREO:", datos["correo"])

    print("FECHA:", datos["fecha"])

    print("ASUNTO:", datos["asunto"])

    print("CÓDIGO:", datos["codigo"])

    print("=" * 60)
