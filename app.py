from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# -------------------------
# SETTINGS
# -------------------------

SIMULATION = True
# SIMULATED_TEMPERATURE = 7.0
SIMULATED_TEMPERATURE = 20

#När är allt kopplad 
# def read_temperature():
#     if SIMULATION:
#         return SIMULATED_TEMPERATURE

#____

HEATER_ON_TEMP = 5.0
HEATER_OFF_TEMP = 10.0

# -------------------------
# SYSTEM STATE
# -------------------------

heater_on = False
mode = "AUTO"


# -------------------------
# TEMPERATURE SENSOR
# -------------------------

def read_temperature():
    if SIMULATION:
        return SIMULATED_TEMPERATURE

    # Riktig DS18B20-kod kommer senare
    return None


# -------------------------
# AUTOMATIC CONTROL
# -------------------------

def control_heater(temperature):
    global heater_on

    if mode == "AUTO":

        if temperature <= HEATER_ON_TEMP:
            heater_on = True

        elif temperature >= HEATER_OFF_TEMP:
            heater_on = False

        # Mellan 5 och 10 grader:
        # behåll tidigare heater-status

    return heater_on


# -------------------------
# HMI PAGE
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# STATUS API
# -------------------------

@app.route("/api/status")
def status():
    temperature = read_temperature()

    if temperature is None:
        return jsonify({
            "temperature": None,
            "heater": False,
            "mode": mode,
            "status": "SENSOR FAULT"
        })

    control_heater(temperature)

    return jsonify({
        "temperature": temperature,
        "heater": heater_on,
        "mode": mode,
        "status": "OK",
        "heater_on_temp": HEATER_ON_TEMP,
        "heater_off_temp": HEATER_OFF_TEMP
    })


# -------------------------
# CHANGE AUTO / MANUAL
# -------------------------

@app.route("/api/mode", methods=["POST"])
def set_mode():
    global mode

    data = request.get_json()

    new_mode = data.get("mode")

    if new_mode not in ["AUTO", "MANUAL"]:
        return jsonify({
            "error": "Invalid mode"
        }), 400

    mode = new_mode

    return jsonify({
        "mode": mode
    })


# -------------------------
# MANUAL HEATER CONTROL
# -------------------------

@app.route("/api/heater", methods=["POST"])
def set_heater():
    global heater_on

    if mode != "MANUAL":
        return jsonify({
            "error": "Heater can only be controlled in MANUAL mode"
        }), 400

    data = request.get_json()

    heater_on = bool(data.get("heater"))

    return jsonify({
        "heater": heater_on
    })


# -------------------------
# START FLASK
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)