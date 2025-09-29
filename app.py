from flask import Flask, render_template, request, redirect, url_for, session
from controller import LojaController # Importa o Controller que você forneceu
from model import Roupa # Importa a classe Roupa
import random # Para gerar um código único se o usuário não informar

# Inicializa o Flask
app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_muito_forte_e_aleatoria' # Necessário para usar a sessão

# Instância do Controller (fora do app para ser usado em todas as requisições)
controller = LojaController()

# --- Rotas (View) ---

@app.route('/')
def index():
    """
    Rota principal: exibe o estoque e relatórios.
    """
    # Prepara os dados para o template
    estoque_list = controller.estoque # Passamos a lista de objetos Roupa
    relatorio_baixo_estoque = controller.gerar_relatorio_estoque_baixo()
    
    # Recupera a mensagem de sucesso/erro da sessão, se houver
    mensagem = session.pop('mensagem', None)
    
    return render_template(
        'index.html', 
        estoque=estoque_list, 
        relatorio_baixo_estoque=relatorio_baixo_estoque,
        mensagem=mensagem
    )

@app.route('/adicionar_roupa', methods=['POST'])
def adicionar_roupa():
    """
    Rota para adicionar um novo item de roupa ao estoque.
    """
    try:
        # Pega os dados do formulário
        nome = request.form['nome']
        tamanho = request.form['tamanho']
        cor = request.form['cor']
        
        # Converte campos numéricos
        preco = float(request.form['preco'])
        estoque_inicial = int(request.form['estoque'])
        
        
        try:
            codigo = int(request.form['codigo'])
        except ValueError:
            # Gera um código aleatório se o campo estiver vazio ou for inválido
            codigo = random.randint(200, 9999)
            
        # Validação básica
        if preco <= 0 or estoque_inicial < 0:
            session['mensagem'] = "❌ Erro: Preço deve ser positivo e Estoque não pode ser negativo."
            return redirect(url_for('index'))
            
        
        nova_roupa = Roupa(codigo, nome, tamanho, cor, preco, estoque_inicial)
        controller.adicionar_roupa_estoque(nova_roupa)
        
        session['mensagem'] = f"✅ Sucesso: Produto '{nome}' (Cód: {codigo}) adicionado ao estoque com {estoque_inicial} unidades."

    except ValueError:
        session['mensagem'] = "❌ Erro de Formato: Certifique-se de que Preço e Estoque são números válidos."
    except Exception as e:
        session['mensagem'] = f"❌ Erro inesperado ao adicionar roupa: {str(e)}"

    return redirect(url_for('index'))


@app.route('/vender', methods=['POST'])
def vender():
    """
    Rota para processar a venda de um item. (Mantida do código anterior)
    """
    try:
        codigo = int(request.form['codigo'])
        quantidade = int(request.form['quantidade'])
        
        
        roupa_encontrada = next((r for r in controller.estoque if r.codigo == codigo), None)

        if roupa_encontrada:
            
            if roupa_encontrada.vender(quantidade):
                session['mensagem'] = f"✅ Sucesso: {quantidade}x {roupa_encontrada.nome} ({roupa_encontrada.tamanho}) vendida(s)!"
            else:
                session['mensagem'] = f"❌ Erro: Estoque insuficiente para {roupa_encontrada.nome} (disponível: {roupa_encontrada.estoque})."
        else:
            session['mensagem'] = "❌ Erro: Produto não encontrado com o código fornecido."

    except ValueError:
        session['mensagem'] = "❌ Erro: Código e Quantidade devem ser números inteiros."
    except Exception as e:
        session['mensagem'] = f"❌ Erro inesperado: {str(e)}"

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    from flask import Flask, render_template, request, redirect, url_for
from controller import LojaController
from model import Roupa

app = Flask(__name__)
loja = LojaController()

@app.route("/")
def index():
    return render_template("index.html", estoque=loja.estoque)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    codigo = int(request.form["codigo"])
    nome = request.form["nome"]
    tamanho = request.form["tamanho"]
    cor = request.form["cor"]
    preco = float(request.form["preco"])
    estoque = int(request.form["estoque"])
    
    roupa = Roupa(codigo, nome, tamanho, cor, preco, estoque)
    loja.adicionar_roupa_estoque(roupa)
    
    return redirect(url_for("index"))

@app.route("/excluir/<int:codigo>")
def excluir(codigo):
    loja.excluir_roupa(codigo)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

