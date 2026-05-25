import json

data = {
    "sensor_id": "sensor_01",
    "pm25": 12.5,
    "co2": 450.0,
    "timestamp": "2026-05-25T14:30:00"
}
with open("log.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
