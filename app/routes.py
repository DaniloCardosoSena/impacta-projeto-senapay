from flask import render_template, redirect, url_for, session, flash, request
from app import app
from app.forms.forms import LoginForm, RegistrationForm
from app.models import User
from app.models import db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)       
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logged_in')
def logged_in():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('logged_in.html', user=user)
    flash('Faça login para acessar esta página.', 'warning')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('Você foi desconectado com sucesso.', 'success')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                session['email'] = user.email
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('logged_in'))
            else:
                flash('Credenciais inválidas. Por favor, tente novamente.', 'danger')
        else:
            flash('Usuário não encontrado. Por favor, verifique o e-mail.', 'danger')
    return render_template('login.html', form=form)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        if user:
            # Excluir o usuário do banco de dados
            db.session.delete(user)
            db.session.commit()
            session.pop('email', None)
            flash('Sua conta foi excluída com sucesso.', 'success')
            return redirect(url_for('home'))
    flash('Erro ao excluir a conta. Faça login para acessar esta página.', 'danger')
    return redirect(url_for('login'))

@app.route('/user_list')
def user_list():
    # Verifica se o usuário está autenticado
    if 'email' in session:
        # Recupera os últimos 10 usuários registrados
        users = User.query.order_by(User.id.desc()).limit(10).all()
        return render_template('user_list.html', users=users)
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

@app.route('/search_user', methods=['GET'])
def search_user():
    email = request.args.get('email')
    user = User.query.filter_by(email=email).first()

    if user is None:  # Se o usuário não foi encontrado, buscar os últimos 10 registros
        users = User.query.order_by(User.id.desc()).limit(10).all()
    else:
        users = [user]

    return render_template('user_list.html', users=users)