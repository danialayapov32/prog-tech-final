import json
import random
from datetime import datetime

class AirDataGenerator:
    def __init__(self, sensor_id, data_version="1.0.0"):
        self.sensor_id = sensor_id
        self.data_version = data_version

    def generate_single_log(self):
        log_entry = {
            "version": self.data_version,
            "sensor_id": self.sensor_id,
            "pm25": round(random.uniform(5.0, 85.0), 2),
            "co2": round(random.uniform(350.0, 1500.0), 2),
            "timestamp": datetime.now().isoformat()
        }
        return json.dumps(log_entry, ensure_ascii=False)

    def save_logs_to_file(self, filename, count=5):
        with open(filename, "w", encoding="utf-8") as file:
            for _ in range(count):
                log_str = self.generate_single_log()
                file.write(log_str + "\n")
