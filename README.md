# imp-lamp-service

Microservice which connects to the Kafka Broker at `130.82.171.231:9092` (see `config.py`) and consumes the `gaze_events`topic.
After consuming 3 messages with `gazed_object` equal to "OfficeLight" and `gaze_activity` equal to "inspect" it prints out "Pattern detected: Triggering action to turn on the lamp!"

## How to run
1. Install the requirements with `pip install -r requirements.txt`
2. Connect to the VPN (so that you can access the Kafka Broker)
3. Run the service with `python main.py`
