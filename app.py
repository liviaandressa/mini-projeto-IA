from flask import Flask, render_template, request

app = Flask(__name__)

# Função de avaliação do candidato
def avaliar_candidato(experiencia, formacao, nota_teste):
    if experiencia > 5 and formacao == "adequada" and nota_teste > 80:
        return "Aprovado", "O candidato foi aprovado com base na experiência, formação e nota técnica."
    elif 3 <= experiencia <= 5 or formacao == "certificações" or 60 <= nota_teste <= 80:
        return "Aprovado Parcialmente", "O candidato atende parcialmente os requisitos devido à experiência intermediária, certificações ou nota técnica média."
    else:
        return "Reprovado", "O candidato foi reprovado devido à pouca experiência, formação inadequada e baixa nota técnica."

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura dos dados do formulário
        experiencia = int(request.form['experiencia'])
        formacao = request.form['formacao']
        nota_teste = int(request.form['nota_teste'])
        
        # Avaliação do candidato
        categoria, justificativa = avaliar_candidato(experiencia, formacao, nota_teste)
        
        return render_template('gpt.html', categoria=categoria, justificativa=justificativa)

    return render_template('gpt.html', categoria=None, justificativa=None)

if __name__ == '__main__':
    app.run(debug=True)
