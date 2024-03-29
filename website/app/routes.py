from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import ContactForm, WaitlistForm
from config import Config
import requests
import gspread


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    gc = gspread.service_account(filename=Config.SERVICE_ACCOUNT_JSON)

    sh = gc.open_by_key(Config.WAITLIST_SHEET).sheet1

    emails = sh.col_values(1)

    form = WaitlistForm()
    if form.validate_on_submit():
        email = form.email.data

        if email in emails:
            return jsonify({"error": "Email already on the waitlist"}), 400

        sh.append_row([email])

        return jsonify({"message": "You have been added to the waitlist!"}), 200

    return render_template("index.html", title="Home", form=form, active_page="home")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    formspark_id = Config.FORMSPARK_ID
    return render_template(
        "contact.html",
        title="Contact",
        form=form,
        active_page="contact",
        formspark_id=formspark_id,
    )

@app.route("/search", methods=["GET", "POST"])
def search():
    maps_api = Config.MAPS_API
    return render_template(
        "search.html",
        title="Search",
        active_page="search",
        maps_api=maps_api,
    )
