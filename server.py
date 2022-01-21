from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/<int:columna>/<int:fila>')
def tablero ( columna, fila ):
    return render_template("index.html", fila = fila, columna = columna)
"""

@app.route('/<int:columna>/<int:fila>/<color1>/<color2>')
def tablero ( columna, fila, color1, color2) :
    return render_template("index.html", fila = fila, columna = columna, color1 = color1, color2 = color2)



if __name__=="__main__":
    app.run(debug=True)


