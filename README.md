# Smart Horse Water

Smart Horse Water is a Raspberry Pi based automation project for monitoring and controlling the temperature of horse drinking water.

The goal of the project is to build a simple but practical automation system that can monitor water temperature and later control a real heater to help prevent the water from freezing during cold weather.

---

## Project Overview

The system is designed around a Raspberry Pi and a DS18B20 temperature sensor.

The current version runs in simulation mode, which makes it possible to develop and test the software before the physical hardware is fully connected.

The final system will combine:

- Temperature measurement
- Automatic heater control
- Manual control
- Web-based HMI
- Alarm handling
- Temperature history
- Raspberry Pi GPIO control

---

## Current Features

The following features are already implemented:

- Flask web server
- Web-based HMI
- Simulated temperature sensor
- Automatic heater control logic
- Heater ON/OFF state
- AUTO / MANUAL backend support
- Temperature thresholds
- REST API for HMI communication

---

## Control Logic

The automatic heater control uses hysteresis.

```text
Temperature <= 5°C
        |
        v
   HEATER ON


Temperature between 5°C and 10°C
        |
        v
Keep previous heater state


Temperature >= 10°C
        |
        v
   HEATER OFF

This prevents the heater from rapidly switching ON and OFF around a single temperature value.
System Architecture
        DS18B20 Temperature Sensor
                  |
                  v
          Raspberry Pi GPIO
                  |
                  v
               app.py
                  |
        ---------------------
        |                   |
        v                   v
 Temperature Control     Alarm Logic
        |
        v
 Heater ON / OFF
        |
        v
       GPIO
        |
        v
 LED / Future Heater

                  |
                  v
             Flask API
                  |
                  v
              Web HMI
                  |
                  v
        Computer / Mobile

During development, the real DS18B20 sensor is replaced by a simulated temperature value.
Simulation
    |
    v
 app.py
    |
    v
Control Logic
    |
    v
Flask HMI

Technologies
This project uses:
- Python 3
- Flask
- HTML
- CSS
- JavaScript
- Raspberry Pi
- GPIO
- DS18B20 temperature sensor
- 1-Wire communication
- Git
- GitHub
Project Structure
horse_water/
|
├── app.py
├── requirements.txt
├── README.md
|
└── templates/
    └── index.html

The project is intentionally kept simple during the first development stage.
More files can be added later when the system becomes larger.
Simulation Mode
The software currently supports simulation mode.
Example:
SIMULATION = TrueSIMULATED_TEMPERATURE = 7.0


This allows the full control logic and HMI to be tested without connecting the physical DS18B20 sensor.
For example:
SIMULATED_TEMPERATURE = 4.0


will cause the automatic control logic to turn the heater ON.
SIMULATED_TEMPERATURE = 11.0


will cause the heater to turn OFF.
When the real sensor is connected, simulation mode will be disabled.
Installation
Clone the repository:
git clone https://github.com/Nweder/horse_water.git

Enter the project directory:
cd horse_water

Install the required Python packages:
pip install -r requirements.txt

Run the Application
Start the Flask application:
python app.py

Open the following address in a web browser:
http://127.0.0.1:5000

The HMI will display:
- Water temperature
- Heater status
- System status
Hardware
Planned hardware for Version 1:
- Raspberry Pi
- DS18B20 waterproof temperature sensor
- Breadboard
- Jumper wires
- 4.7 kΩ pull-up resistor
- LED
- LED resistor
The DS18B20 will communicate with the Raspberry Pi using the 1-Wire protocol.
Planned connection:
DS18B20                Raspberry Pi

VCC      ------------> 3.3V

DATA     ------------> GPIO4

GND      ------------> GND


3.3V
 |
[4.7 kΩ]
 |
DATA

Development Roadmap
Phase 1 - Basic software
- [x] Flask web server
- [x] Basic HMI
- [x] Temperature simulation
- [x] Automatic heater logic
- [x] Heater state
- [x] AUTO / MANUAL backend logic
Phase 2 - HMI controls
- [ ] AUTO / MANUAL buttons
- [ ] Manual heater ON / OFF buttons
- [ ] Adjustable temperature setpoints
Phase 3 - Hardware integration
- [ ] Connect DS18B20
- [ ] Read real temperature
- [ ] Connect LED as simulated heater
- [ ] Control LED through Raspberry Pi GPIO
Phase 4 - Monitoring
- [ ] Low temperature alarm
- [ ] Sensor fault alarm
- [ ] Alarm acknowledge/reset
- [ ] Temperature history
- [ ] Temperature trend graph
Phase 5 - Raspberry Pi deployment
- [ ] Run application on Raspberry Pi
- [ ] Automatic startup using systemd
- [ ] Remote access through local network
- [ ] 24/7 operation
Future Version
Future development may replace the LED with a safe heater control system.
Raspberry Pi GPIO
       |
       v
Isolated Driver / Relay
       |
       v
     Heater

Project Goal
The final goal is to create a complete small-scale automation system:
Temperature Sensor
        |
        v
 Raspberry Pi
        |
        v
 Control Logic
        |
        v
 Heater Control
        |
        v
     Web HMI
        |
        v
 Alarm + History

The project is also intended as a practical learning project involving:
- Automation
- Sensors
- Raspberry Pi
- Python
- GPIO
- HMI development
- Control logic
- Industrial-style system architecture
Author
Mohamad Nweder
