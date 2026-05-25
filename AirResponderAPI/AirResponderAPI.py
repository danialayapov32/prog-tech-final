import matplotlib.pyplot as plt


class AirResponderAPI:
    def __init__(self, analytics_engine):
        self.analytics = analytics_engine

    def generate_pollution_chart(self):
        df_hourly = self.analytics.groupby_sensor_and_hour()

        plt.figure(figsize=(8, 4))
        plt.plot(df_hourly['hour'], df_hourly['pm25'], marker='o', color='red')

        plt.title("Hourly PM2.5 Pollution Trends")
        plt.xlabel("Time (Hours)")
        plt.ylabel("PM2.5 Concentration (mcg/m³)")
        plt.grid(True)

        plt.savefig("pollution_chart.png")
        plt.close()
        print("[API] Graphic was saved successfully at 'pollution_chart.png'")

    def get_api_alerts_json(self):
        alerts_df = self.analytics.check_threshold_alerts()

        export_df = alerts_df.copy()
        export_df['timestamp'] = export_df['timestamp'].astype(str)

        return export_df.to_json(orient='records', force_ascii=False, indent=4)
