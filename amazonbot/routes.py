from flask import render_template, redirect, url_for
from amazonbot import app
from amazonbot.forms import SearchForm
from amazonbot.amazon_bot import AmazonProductAvailability


@app.route('/', methods=['POST', 'GET'])
def home():
    form = SearchForm()
    search = ''
    if form.validate_on_submit():
        search = form.search.data
        redirect(url_for('home'))

    bot = AmazonProductAvailability()
    products = bot.search(search)
    return render_template('home.html', form=form, products=products)