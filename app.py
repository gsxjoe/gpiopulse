import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Configure GPIO pins (using BCM numbering)
PERMANENT_PIN = 18
MOMENTARY_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PERMANENT_PIN, GPIO.OUT)
GPIO.setup(MOMENTARY_PIN, GPIO.OUT)

# Set initial state (relays off)
GPIO.output(PERMANENT_PIN, GPIO.HIGH) # HIGH = off for active-low relays
GPIO.output(MOMENTARY_PIN, GPIO.HIGH) # HIGH = off for active-low relays

@app.route('/')
def index():
    
    
    
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    device = request.form.get('device')
    action = request.form.get('action')

    if device == 'permanent':
        if action == 'on':
            GPIO.output(PERMANENT_PIN, GPIO.LOW) # Turn on
        else: # action == 'off'
            GPIO.output(PERMANENT_PIN, GPIO.HIGH) # Turn off
    elif device == 'momentary':
        if action == 'pulse':
            # Pulse the relay for 1500ms
            GPIO.output(MOMENTARY_PIN, GPIO.LOW) # Turn on
            # change to duration of pulse this is in seconds, 1.5 equals 1 1/2 seconds
            time.sleep(1.5) # Wait one and a half a second
            GPIO.output(MOMENTARY_PIN, GPIO.HIGH) # Turn off

    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
