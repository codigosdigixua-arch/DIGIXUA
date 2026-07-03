from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "DIGIXUA FUNCIONANDO"

if __name__ == "__main__":
    app.run(debug=True)