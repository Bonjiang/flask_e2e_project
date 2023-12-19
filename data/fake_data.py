from faker import Faker
import random
from flask import jsonify

# Fake Data
fake = Faker()

num_patients = 95
patients = [(i + 1, fake.first_name(), fake.last_name(), fake.date_of_birth(), fake.random_element(['Male', 'Female']), fake.phone_number())
            for i in range(num_patients)]

num_records = 95
medical_records = [(i + 1, random.randint(1, num_patients), fake.text(), fake.text(), fake.date_this_decade(), fake.date_this_decade())
                   for i in range(num_records)]


# API endpoint that provides fake data
@app.route('/api/data', methods=['GET'])
def api_data():
    data = {
        'patients': patients, 
        'medical_records': medical_records 
    }
    return jsonify(data)
