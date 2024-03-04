from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import ContactForm, WaitlistForm
#from app.models import 
from config import Config

@app.route('/')
@app.route('/index')
def index():
    form = WaitlistForm()
    if form.validate_on_submit():
        flash('You have been added to the waitlist!')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form, active_page='home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    formspark_url = Config.FORMSPARK_URL
    return render_template('contact.html', title='Contact', form=form, active_page='contact', formspark_url=formspark_url)