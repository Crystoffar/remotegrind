from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import ContactForm, WaitlistForm
from app.models import Ticket

@app.route('/')
@app.route('/index')
def index():
    form = WaitlistForm()
    if form.validate_on_submit():
        flash('You have been added to the waitlist!')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)

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