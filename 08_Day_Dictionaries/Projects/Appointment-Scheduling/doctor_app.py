from flask import Flask, render_template, request

# Sample dictionary containing doctor names and their appointment schedules
doctor_schedules = {
    "Dr. Smith": {
        "Monday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Tuesday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Wednesday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Thursday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Friday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"]
    },
    "Dr. Johnson": {
        "Monday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Tuesday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Wednesday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Thursday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Friday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"]
    },
    "Dr. Patel": {
        "Monday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Tuesday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Wednesday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Thursday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Friday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"]
    }
}

app = Flask(__name__)


# Define a route for the home page
@app.route("/")
def home():
    return render_template("home.html")


# Define a route for the appointment schedule page
@app.route("/schedule")
def schedule():
    doctor = request.args.get("doctor")
    day = request.args.get("day")
    if doctor and day:
        if doctor in doctor_schedules:
            if day in doctor_schedules[doctor]:
                available_slots = doctor_schedules[doctor][day]
                return render_template("schedule.html", doctor=doctor, day=day, slots=available_slots)
            else:
                return "Invalid day selected."
        else:
            return "Invalid doctor selected."
    else:
        return render_template("schedule_form.html", doctors=doctor_schedules.keys())


@app.route("/doctor-list")
def doctor_list():
    doctor = request.args.get("doctor-list")
    doctors = list(doctor_schedules.keys())
    return render_template("doctor-list.html", doctors=doctors)


if __name__ == "__main__":
    app.run(debug=True)