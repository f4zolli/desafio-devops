from flask import Flask

# Inicialização da aplicação Flask
app = Flask(__name__)

# Rota principal ("/")
@app.route("/")
def home():
    return "Desafio DevOpsJr SalaryFits :D"

# Rota de status ("/status")
@app.route('/status')
def status():
    return {"status": "OK", "app": "Flask Challenge"}

#Execução do servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
