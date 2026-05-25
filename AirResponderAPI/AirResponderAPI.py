import matplotlib.pyplot as plt
import io
import pandas as pd


class AirResponderAPI:
    def __init__(self, analytics_engine) -> None:
        self.analytics = analytics_engine

    def generate_pollution_chart_bytes(self) -> bytes:
        df_hourly = self.analytics.groupby_sensor_and_hour()

        plt.figure(figsize=(10, 5))

        for sensor in df_hourly['sensor_id'].unique():
            sensor_data = df_hourly[df_hourly['sensor_id'] == sensor]
            plt.plot(
                sensor_data['hour'],
                sensor_data['pm25'],
                marker='o',
                linestyle='-',
                label=f'Датчик: {sensor}'
            )

        plt.title("Тренды загрязнения воздуха по часам (PM2.5)")
        plt.xlabel("Время (Часы)")
        plt.ylabel("Концентрация PM2.5 (мкг/м³)")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()

        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight')
        img_buffer.seek(0)
        chart_bytes = img_buffer.getvalue()
        plt.close()

        return chart_bytes

    def get_api_alerts_json(self) -> str:
        alerts_df = self.analytics.check_threshold_alerts()

        if alerts_df.empty:
            return "[]"

        export_df = alerts_df.copy()

        export_df['timestamp'] = export_df['timestamp'].astype(str)

        return export_df.to_json(orient='records', force_ascii=False, indent=4)
