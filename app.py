from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'some secret key'  # Secret Key protects against modifying cookies, forgery attacks.

posts = [
    {
        'author': 'Carol Muchemi',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': 'October 4, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'date_posted': 'October 5, 2018'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)  #This is an argument that has been passed in the home function.


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # This creates an instace.
    return render_template('register.html', title='Register', form=form)\


@app.route('/login')
def login():
    form = LoginForm()  # This creates an instace.
    return render_template('login.html', title='Register', form=form)

if __name__ == '__main__':
    app.run()
