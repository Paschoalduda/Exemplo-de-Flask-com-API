from flask import render_template, url_for, request, redirect, session, flash, Blueprint,make_response
from models.data_manager import escolhaS, novoUsuario, logandoUsuario

# Criação do Blueprint
front_controller = Blueprint('front_controller', __name__)

# Função para verificar o login automaticamente a partir do cookie
@front_controller.before_request
def verificar_login():
    if "logado" not in session:
        usuario_cookie = request.cookies.get("usuario_logado")
        if usuario_cookie:  
            session["logado"] = usuario_cookie
            
# ---------------- Rota principal ---------------- #
@front_controller.route('/')
def principal():
    return render_template("principal.html")

#--------------- Rota para cadastrar ------------- #
@front_controller.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':    
        usuario = request.form.get("textUsuario")
        senha = request.form.get("pwSenha")
        if novoUsuario(usuario, senha):
            flash(f"Cadastro do {usuario} realizado")
            return redirect(url_for('front_controller.login'))
        flash(f"Usuário: {usuario} já existe")
    return render_template("cadastro.html")

#--------------- Rota Login ---------------------#
@front_controller.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':    
        usuario_cookie = request.cookies.get("usuario_logado")
        if usuario_cookie:
            session["logado"] = usuario_cookie
            return redirect(url_for('front_controller.login'))
        
        usuario = request.form.get("textUsuario")
        senha = request.form.get("pwSenha")
        if logandoUsuario(usuario, senha):
            flash(f"Login de {usuario} realizado com sucesso")
            session["logado"] = usuario
            
            lembrar_me = request.form.get("lembrar")
            if lembrar_me:
                resp = make_response(redirect(url_for('front_controller.login')))
                resp.set_cookie("usuario_logado", usuario, max_age=60*60*24*30)  # Cookie expira em 30 dias
                return resp
            
            return redirect(url_for('front_controller.series'))
        flash("Confira seu login <br>Dados não aceitos")
        session["logado"] = None
    return render_template("login.html")
    
#--------------rOTA VER SÉRIES------------------#
@front_controller.route("/series", methods=['GET', 'POST'])
def series():
    if "logado" not in session or session["logado"] is None:
        flash("Você precisa estar logado para acessar as animações.Você foi redirecionado para o login")
        return redirect(url_for('front_controller.login'))  # Garante retorno

    if request.method == 'POST':
        # Obter o tipo de série selecionado
        tipo_serie = request.form.get("tipoSerie")
        if tipo_serie:  # Verifica se tipo_serie foi fornecido
            series, mensagem = escolhaS(tipo_serie)
        else:
            series, mensagem = [], "Nenhuma categoria selecionada."

        return render_template("series.html", series=series, opcao=mensagem)

    # Para requisições GET
    return render_template("series.html", series=None, opcao="Escolha um gênero de seriado")


# ---------------- Rota para Sair ---------------- #
@front_controller.route('/sair', methods=['GET', 'POST'])
def sair():
    if request.method == 'POST':
        session.pop("logado", None)
        resp = make_response(redirect(url_for('front_controller.principal')))
        resp.set_cookie('usuario_logado', '', expires=0)
        flash("Você foi deslogado com sucesso.")
    return resp

