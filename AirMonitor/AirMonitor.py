from typing import List, Dict, Any

class AirMonitor:
    def __init__(self) -> None:
        self.history: List[Dict[str, Any]] = []

    def add_record(self, record: Dict[str, Any]) -> None:
        self.history.append(record)

    def get_all_records(self) -> List[Dict[str, Any]]:
        return self.history

    def get_records_by_sensor(self, sensor_id: str) -> List[Dict[str, Any]]:
        return [log for log in self.history if log.get("sensor_id") == sensor_id]

    def clear_history(self) -> None:
        self.history.clear()
