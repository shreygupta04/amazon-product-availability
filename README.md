# AmazonRescue
Flask app that returns a list of in stock Amazon products. This website eliminates the need to comb through Amazon's thousands of products for your search, some of which might be unavailable. During this pandemic getting necessities is important and I am hoping that this website is used respectfully. Abusing it will only hurt someone who might be more in need of supplies.

## Getting Started
To run this on your local machine you will need to download chromedriver that is based on your chrome version. The link can be found below. Specify the path to the file in your venv or in a `.env` file.
  * [Chromedriver](https://chromedriver.chromium.org/downloads)
Add a Flask secret key in your venv or in a `.env` file. This will something like `FLASK_SECRET_KEY=YOUR KEY` if it is in a `.env`, otherwise add export before the statement if it is a part of your venv.

## Deployment
This can be deployed on Heroku by following the steps below. Disregard anything about databases as this app does not use any
  * [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

## Built With
  * [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  * [Selenium](https://selenium-python.readthedocs.io/)
