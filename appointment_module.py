import json, os
from datetime import datetime

DATA_FILE = "appointments.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def book_appointment(name, date, time):
    # Validate date/time
    try:
        datetime.strptime(date, "%Y-%m-%d")
        datetime.strptime(time, "%H:%M")
    except ValueError:
        return {"status": "Error", "message": "Invalid date/time format"}
    
    data = load_data()
    
    # Check for conflicts
    for appt in data:
        if appt["date"] == date and appt["time"] == time:
            return {"status": "Error", "message": "Slot already booked"}
    
    data.append({"name": name, "date": date, "time": time})
    save_data(data)
    return {"status": "Booked", "name": name, "date": date, "time": time}
