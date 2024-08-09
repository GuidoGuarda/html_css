from flask import Flask, render_template #rota do site, renderização
from matematica import Matematica
app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template("teste.html")#rota do inicio

@app.route('/olamundo')
def mostrar():
    return render_template("teste.html")

@app.route('/calculosoma')
def calcular():
    mat = Matematica(9,9)
    resposta = mat.somar()
    return render_template('calculo.html', resultado=resposta)
    
app.run()
