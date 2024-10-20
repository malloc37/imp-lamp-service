import logging
from app.consumers.gaze_event_consumer import process_gaze_event

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting Workflow Microservice...")
    process_gaze_event()