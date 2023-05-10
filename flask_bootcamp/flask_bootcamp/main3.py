from flask import Flask, render_template
from LoginForm import Lf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello hello hello hello hello world'


@app.route('/')
@app.route('/index')
def main():
    return render_template('base3.html')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = Lf()
    
    if form.validate_on_submit(): 
        
        if form.password_again.data != form.password.data:
           
            return render_template('register.html', title = 'Регистрация', form=form, 
                                   message='Пароли не совпадают!!!')
        
        with open('file_2.txt', 'a', encoding='utf-8') as file:
            file.write(f'{form.name.data}; {form.email.data}; {form.password.data}; \n')

        return render_template('register.html', message='Регистрация прошла успешно')
    
    return render_template('register.html', title = 'Регистрация', form=form)




if __name__ == '__main__':
    app.run()

