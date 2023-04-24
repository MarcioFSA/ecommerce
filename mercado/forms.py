from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired

class CadastroForm(FlaskForm):
    usuario = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(), DataRequired()])
    senha = PasswordField(label='Senha:',validators=[Length(min=2, max=30), DataRequired()])
    confSenha = PasswordField(label='Confirmação da Senha:',validators=[EqualTo('senha'), DataRequired()])
    botao_submit_cadastro = SubmitField(label='Cadastrar')