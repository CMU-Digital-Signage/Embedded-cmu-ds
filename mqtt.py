import paho.mqtt.client as paho
import RPi.GPIO as GPIO
from paho import mqtt
import getmac
import time
import os
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER = 18
GPIO.setup(BUZZER, GPIO.OUT)

mac = getmac.get_mac_address("eth0")

emgc = 0

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(BUZZER, True)
       time.sleep(halveWaveTime)
       GPIO.output(BUZZER, False)
       time.sleep(halveWaveTime)
def play():
    t=0
    x=1.5
    duration=[0.25,0.25,0.25,0.5,0.5,0.5,0.25,0.25,0.25]
    for d in duration:
        buzz(500, d/x)
        time.sleep((d/x) *0.1)

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    global emgc
    print(msg.topic + " " + 'message =>' + " " + str(msg.payload))
    if "Not EMGC" in str(msg.payload):
        if mac in str(msg.payload):
            print("Not EMGC")
            emgc = 0
    elif "EMGC" in str(msg.payload):
        if mac in str(msg.payload):
            print("EMGC")
            emgc = 1
    else:
        if mac in str(msg.payload):
            print("Remote")
            os.system("irsend SEND_ONCE LG KEY_POWER")

def check_emgc():
    while True:
        if emgc == 1:
            play()
        time.sleep(1)  # Adjust sleep time as needed

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
#client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client = paho.Client(paho.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("cpe_ds", "CPEds@1234")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("701d824327874f2484b4d49c94e3e4d6.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("raspberrypi", qos=0)

# a single publish, this can also be done in loops, etc.
#client.publish("raspberrypi", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
#client.loop_forever()

# Start MQTT client loop in a separate thread
client_thread = threading.Thread(target=client.loop_forever)
client_thread.daemon = True
client_thread.start()

# Run emgc check in the main thread
check_emgc()