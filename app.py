from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_vehicle_data():
    return {
        "oil_temperature": random.randint(150, 250),  # Fahrenheit
        "maf_sensor": random.randint(0, 2047),        # raw 11-bit
        "battery_voltage": random.randint(0, 12),     # volts
        "tire_pressure": random.randint(0, 2047),     # raw 11-bit
        "fuel_level": random.randint(0, 100),         # liters
        "fuel_consumption_rate": random.randint(0, 50), # L/h
        "error_codes": [
            random.choice([0xA1, 0xA2, 0xC1, 0x55, 0x23, 0x00])
            for _ in range(4)
        ]
    }

@app.route("/vehicle", methods=["GET"])
def vehicle():
    return jsonify(generate_vehicle_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
