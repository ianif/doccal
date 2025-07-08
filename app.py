# Author: JOY

from flask import Flask, render_template, request, jsonify

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
    key = (date, time, doctor, who_is_this_guy)

    if key in appointments:
        return jsonify({"status": "error", "message": "This slot is already booked."})
    else:
        appointments.add(key)
        return jsonify({"status": "success", "message": "Appointment booked successfully! new pr"})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)