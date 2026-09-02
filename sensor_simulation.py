import random
import time

print("IIoT Temperature Sensor Started")
print("--------------------------------")

for i in range(10):
    temperature = random.randint(20, 50)
    print("Machine Temperature:", temperature, "°C")

    if temperature > 40:
        print("⚠️ ALERT: High Temperature!")
    else:
        print("✅ Temperature Normal")

    time.sleep(2)
