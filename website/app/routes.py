from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import ContactForm
from app.models import Ticket

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        ticket = Ticket(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(ticket)
        db.session.commit()
        flash('Thank you, {}! Your message has been sent to The Remote Grind Team.'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact', form=form)