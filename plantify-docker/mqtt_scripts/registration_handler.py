import mqtt_client
import os
import uuid

unique_id = str(uuid.uuid4())

mqtt_broker = os.getenv('MQTT_BROKER')
client = mqtt_client.MqttClient(
    broker="192.168.178.53", #mqtt_broker,
    client_id=unique_id,
    topic="plant_pot",
    qos=1,
)

client.start()