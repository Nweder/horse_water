from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# True = kör på din dator med simulerad temperatur
# False = senare på Raspberry Pi med riktig DS18B20
SIMULATION = True

heater_on = False


def read_temperature():
    if SIMULATION:
        # Simulerar temperatur mellan 1 och 12 grader
        return round(random.uniform(-5, 12.0), 1)

    # Senare lägger vi in riktig DS18B20-kod här
    return None


def control_heater(temperature):
    global heater_on

    if temperature <= 1:
        heater_on = True

    elif temperature >= 15:
        heater_on = False

    return heater_on


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/status")
def status():
    temperature = read_temperature()

    if temperature is None:
        return jsonify({
            "temperature": None,
            "heater": False,
            "status": "Sensor fault"
        })

    heater = control_heater(temperature)

    return jsonify({
        "temperature": temperature,
        "heater": heater,
        "status": "OK"
    })


if __name__ == "__main__":
    app.run(debug=True)