import json
import random
from datetime import datetime
from typing import Generator

class AirDataGenerator:
    def __init__(self, sensor_id: str, data_version: str = "1.0.0") -> None:
        self.sensor_id = sensor_id
        self.data_version = data_version

    def generate_single_log(self) -> str:
        log_entry = {
            "version": self.data_version,
            "sensor_id": self.sensor_id,
            "pm25": round(random.uniform(5.0, 85.0), 2),
            "co2": round(random.uniform(350.0, 1500.0), 2),
            "timestamp": datetime.now().isoformat()
        }
        return json.dumps(log_entry, ensure_ascii=False)

    def save_logs_to_file(self, filename: str, count: int = 5) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            for _ in range(count):
                log_str = self.generate_single_log()
                file.write(log_str + "\n")
