import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

for i in range(10):
    temperature = random.randint(20, 50)
    client.publish("iiot/temperature", temperature)

    print("Temperature sent:", temperature, "°C")

    time.sleep(2)

client.disconnect()
print("All readings sent!")
