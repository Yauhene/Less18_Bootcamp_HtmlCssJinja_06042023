from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class Lf(FlaskForm): # форма логина
    name = StringField("Имя", validators = [DataRequired()]) # имя
    email = EmailField("Почта", validators = [DataRequired()]) # email
    password = PasswordField("Пароль", validators = [DataRequired()]) # пароль 
    password_again = PasswordField("Повторите пароль", validators = [DataRequired()]) # повтор пароля
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Зарегистрироваться")
    