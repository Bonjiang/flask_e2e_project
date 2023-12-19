import os
import pandas as pd
import random
import logging
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect
from flask import Flask, render_template, jsonify
from flask_oauthlib.client import OAuth
from faker import Faker
from data.fake_data import patients, medical_records

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)

# Logger config
logging.basicConfig(filename='logs/app.log', level=logging.INFO)

tables = get_tables(db_engine)
logging.info("Tables in the database: %s:", tables)

sql_query = "SELECT * FROM patients" 
df = execute_query_to_dataframe(sql_query, db_engine)
logging.info ("Data from patients table: %s",df)

sql_query = "SELECT * FROM medical_records" 
df2 = execute_query_to_dataframe(sql_query, db_engine)
logging.info("Data from medical_records table: %s", df2)

app = Flask(__name__)
app.secret_key = os.urandom(95)

# Google OAuth config

google = OAuth(app).remote_app(
    'google',
    consumer_key=os.getenv('GOOGLE_CLIENT_ID'),
    consumer_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    request_token_params={'scope': 'email'},
    base_url='https://www.googleapis.com/oauth2/v1/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    redirect_uri=os.getenv('GOOGLE_REDIRECT_URI')
)

@oauth.tokengetter
def get_google_oauth_token(): return session.get('google_token')

# Fake Data

fake = Faker()

num_patients = 95
patients = [(i + 1, fake.first_name(), fake.last_name(), fake.date_of_birth(), fake.random_element(['Male', 'Female']), fake.phone_number())
            for i in range(num_patients)]

num_records = 95
medical_records = [(i + 1, random.randint(1, num_patients), fake.text(), fake.text(), fake.date_this_decade(), fake.date_this_decade())
                   for i in range(num_records)]

# API endpoint within my Flask backend
@app.route('/api/data', methods=['GET'])
def api_data():
    data = {
        'patients': patients, 
        'medical_records': medical_records 
    }
    return jsonify(data)

@app.route('/enter-login-portal')
def enter_login_portal():
    return google.authorize(callback=url_for('amazing_land', _external=True))

@app.route('/logout-poof')
def logout_poof():
    session.pop('google_token', None)
    return redirect(url_for('index'))

@app.route('/login/welcome-amazing human')
def magic_land():
    response = google.authorized_response()
    if not response or not response.get('access_token'):
        return 'Oops! The magic failed. Reason: {} Error: {}'.format(
            request.args.get('error_reason', 'Unknown'),
            request.args.get('error_description', 'Something went wrong! Oh no')
        )

    session['google_token'] = (response['access_token'], '')
    user_info = google.get('userinfo')
    return f'Welcome, amazing human! You are now logged in as {user_info.data["email"]}.'

@app.route('/about')
def aboutpage():
    logging.info("Accessed! /about page")    
    return render_template('about.html')

@app.route('/data')
def data(data=df, data2=df2):
    logging.info("Accessed! /data page")
    return render_template('data.html', data=data, data2=data2)

@app.route('/')
def index():
    logging.info("Accessed! / page")
    return render_template('base.html')

@app.route('/')
def hello_world():
    logging.info("Accessed! /hi_there page")
    return 'Hi there, amazing human! This is from a Flask app in a Docker container! Bye now'

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )

