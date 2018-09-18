from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post



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
def home():

    # This is an argument that has been passed in the home function.
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])  # Allows the user to post a registry.
def register():
    # This creates an instance.
    form = RegistrationForm()

    # Ensures the form validates properly.
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # Message displayed when a user is successfully created.
        # The f string is the placeholder and used when there is some data that is needed to be passed.
        flash(f'{form.username.data} account has been created!', 'success')

        # Once the form is created, user is redirected to the home page.
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)\


@app.route('/login', methods=['GET', 'POST'])
def login():
    # This creates an instance.
    form = LoginForm()

    # Ensures the form validates properly.
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful Login. Please check Username and Password', 'danger')
    return render_template('login.html', title='Login', form=form)