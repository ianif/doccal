from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory data store for booked appointments
appointments = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()
    date = data['date']
    time = data['time']
    doctor = data['doctor']
    key = f"{date}_{time}_{doctor}"

    if key in appointments:
        return jsonify({"status": "error", "message": "This slot is already booked."})
    else:
        appointments[key] = True
        return jsonify({"status": "success", "message": "Appointment booked successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

