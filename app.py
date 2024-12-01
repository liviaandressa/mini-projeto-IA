from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Carregar o modelo treinado
model = pickle.load(open('models/model.pkl', 'rb'))


# Carregar os dados dos candidatos (substituir por sua base de dados)
df = pd.read_csv('data/candidatos.csv')

# Função para fazer a previsão
def prever(dados_candidato):
    # Pré-processar os dados do candidato (ex: transformar em um DataFrame)
    novo_df = pd.DataFrame([dados_candidato])
    # Fazer a previsão
    previsao = model.predict(novo_df)[0]
    return previsao

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obter os dados do formulário
        experiencia = request.form['experiencia']
        formacao = request.form['formacao']
        # ... outros atributos
        # Fazer a previsão
        resultado = prever([experiencia, formacao, ...])
        return render_template('gemini.html', resultado=resultado)
    else:
        return render_template('gemini.html')

if __name__ == '__main__':
    app.run(debug=True)