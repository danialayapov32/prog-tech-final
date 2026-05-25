
class AirMonitor:
    def __init__(self) -> None:
        self.history = []

    def add_record(self, record: str) -> None:
        self.history.append(record)

    def get_all_records(self):
        return self.history

    def get_records_by_sensor(self, sensor_id: str):
        return [log for log in self.history if log.get("sensor_id") == sensor_id]

    def clear_history(self) -> None:
        self.history.clear()
