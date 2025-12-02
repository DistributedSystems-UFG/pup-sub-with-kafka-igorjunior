from kafka import KafkaProducer, KafkaConsumer
import threading
from const import *

print("Group Chat with Kafka\n")
username = input("Enter your name: ").strip()

while not username:
    username = input("Name cannot be empty: ").strip()

print("\nAvailable topics:")
for i, topic in enumerate(TOPICS, 1):
    print(f"{i}. {topic}")

print("\nChoose a topic to join:")
choice = input("Topic: ").strip()

current_topic = None

try:
    index = int(choice) - 1
    if 0 <= index < len(TOPICS):
        current_topic = TOPICS[index]
    else:
        print("Invalid option.")
        current_topic = "GENERAL"
except ValueError:
    print("Invalid input.")
    current_topic = "GENERAL"

print(f"\nJoined topic: {current_topic}\n")

producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

consumer = KafkaConsumer(
    current_topic,
    bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode('utf-8')
)

def receive_messages():
    try:
        for message in consumer:
            print(f"\r{message.value}")
            print(f"[{current_topic}] {username}: ", end="", flush=True)
    except:
        pass

receiver_thread = threading.Thread(target=receive_messages, daemon=True)
receiver_thread.start()

try:
    while True:
        message = input(f"[{current_topic}] {username}: ")
        
        if message.strip():
            full_message = f"{username}: {message}"
            producer.send(current_topic, value=full_message.encode())
            producer.flush()
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    producer.close()

