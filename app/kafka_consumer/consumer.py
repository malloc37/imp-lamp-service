from kafka import KafkaConsumer
import json
import logging
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Track last three events
event_history = []

def consume_messages():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='lamp-service-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    logger.info(f"Subscribed to Kafka topic {KAFKA_TOPIC}")
    for message in consumer:
        event = message.value
        logger.info(f"Received message: {event}")

        if event.get('gazed_object') == 'Lamp' and event.get('gaze_activity') == 'inspect':
            event_history.append(event)

            if len(event_history) > 3:
                event_history.pop(0)

            if len(event_history) == 3 and all(
                e.get('gazed_object') == 'Lamp' and e.get('gaze_activity') == 'inspect' for e in event_history
            ):
                logger.info("Pattern detected: Triggering action to turn on the lamp!")
                event_history.clear()
        else:
            event_history.clear()