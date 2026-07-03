from flask import Flask, render_template, request

from servicios.buscador import buscar_destinatario
from servicios.parser import procesar_mensaje

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    mensaje = None

    if request.method == "POST":

        correo = request.form.get("correo", "").strip().lower()

        if correo == "":

            mensaje = "Debes escribir un correo."

        else:

            try:

                encontrado = buscar_destinatario(correo)

                if encontrado is None:

                    mensaje = "⚠ No hay mensajes recientes."

                else:

                    resultado = procesar_mensaje(encontrado)

            except Exception as e:

                mensaje = f"❌ Error interno: {str(e)}"

    return render_template(
        "index.html",
        resultado=resultado,
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run(debug=True)