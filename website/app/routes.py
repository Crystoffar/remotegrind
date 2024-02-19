from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ContactForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Thank you, {}! Your message has been sent to The Remote Grind Team.'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact', form=form)