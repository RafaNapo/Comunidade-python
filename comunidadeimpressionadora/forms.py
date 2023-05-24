from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField,BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

# importamos os 3 campos do fomulario com o wtforms
# criar uma sub classe que herde o flaskform

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmaçao senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Esse email ja foi cadastrado, cadastre um outro email ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditaarPerfil(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto perfil', validators=[FileAllowed(["jpg",'png'])])

    curso_excel = BooleanField('Excel IMpressionador ')
    curso_python = BooleanField('Python IMpressionador ')
    curso_vba = BooleanField('VBA IMpressionador ')
    curso_powerbi = BooleanField('Poewr BI IMpressionador ')
    curso_appt = BooleanField('Apresentacao IMpressionador ')
    curso_excel = BooleanField('SQL  IMpressionador ')

    botao_editar_perfil = SubmitField('Confirmar Edicao')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')