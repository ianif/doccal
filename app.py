# Author: JOY

from flask import Flask, render_template, request, jsonify
from utils import is_appointment_available, add_appointment, format_response

app = Flask(__name__)

# In-memory data store for booked appointments
appointments = set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()
    date = data['date']
    time = data['time']
    doctor = data['doctor']
    who_is_this_guy = data['who_is_this_guy']
    
    if not is_appointment_available(appointments, date, time, doctor, who_is_this_guy):
        return jsonify(format_response("error", "This slot is already booked."))
    else:
        add_appointment(appointments, date, time, doctor, who_is_this_guy)
        return jsonify(format_response("success", "Appointment booked successfully!"))

if __name__ == '__main__':
    app.run(debug=True, threaded=True)