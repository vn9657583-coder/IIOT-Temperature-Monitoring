import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    temperature = float(message.payload.decode())
    print("Received temperature:", temperature, "°C")

    if temperature > 40:
        print("⚠️ HIGH TEMPERATURE ALERT!")
    else:
        print("✅ Temperature Normal")

subscriber = mqtt.Client()
subscriber.on_message = on_message

subscriber.connect("test.mosquitto.org", 1883, 60)
subscriber.subscribe("iiot/temperature")

print("📡 Subscriber is listening...")
subscriber.loop_forever()
