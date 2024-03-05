from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import ContactForm, WaitlistForm
#from app.models import 
from config import Config
import requests

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    form = WaitlistForm()
    if form.validate_on_submit():
        email = form.email.data

        response = requests.post(
            'https://api.getwaitlist.com/api/v1/signup',
            json={'email': email, 'waitlist_id': Config.WAITLIST_ID, 'referral_link': request.url}
        )

        if response.status_code == 200:
            return jsonify({'message': 'You have been added to the waitlist!'}), 200
        else:
            return jsonify({'error': 'Failed to add to waitlist'}), 500
    
    return render_template('index.html', title='Home', form=form, active_page='home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    formspark_id = Config.FORMSPARK_ID
    return render_template('contact.html', title='Contact', form=form, active_page='contact', formspark_id=formspark_id)