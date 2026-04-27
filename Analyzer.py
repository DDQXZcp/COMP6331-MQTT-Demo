import paho.mqtt.client as mqtt
import time

# Callback when connected
def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    # Subscribe to the counter topic
    client.subscribe("comp3310/counter", qos=0)

# Callback when a message is received
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received counter message: {message}")

# Create and configure client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_start()

# Publish test messages
time.sleep(1)
client.publish("comp3310/lab", "Lab test message", qos=0)
client.publish("comp3310/content", "Content test message", qos=0)
print("Test messages sent to comp3310/lab and comp3310/content")

# Listen for counter messages for 110 seconds max
time.sleep(110)

client.loop_stop()
client.disconnect()