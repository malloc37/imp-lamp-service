from kafka import KafkaConsumer
import json
import logging
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def consume_messages():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='workflow-service-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    logger.info(f"Subscribed to Kafka topic {KAFKA_TOPIC}")

    for message in consumer:
        logger.info(f"Received message: {message.value}")