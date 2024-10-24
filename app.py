from flask import Flask, request, jsonify, render_template
import csv
import re

app = Flask(__name__)

# Regex for email and mobile validation
email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
mobile_pattern = r'^\d{10}$'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    mobile = data.get('mobile')

    # Validate input fields on the server-side too
    if not name or not re.match(email_pattern, email) or not re.match(mobile_pattern, mobile):
        return 'Invalid input, please correct the data.', 400

    # Save data to CSV
    with open('user_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, mobile])

    return 'Data saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
