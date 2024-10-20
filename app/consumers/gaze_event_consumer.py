import logging
from app.kafka_consumer.consumer import consume_messages

logger = logging.getLogger(__name__)

def process_gaze_event():
    logger.info("Starting to process gaze events...")
    consume_messages()