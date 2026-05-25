import pandas as pd


class AirAnalytics:
    def __init__(self, raw_data):
        self.df = pd.DataFrame(raw_data)

        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])

    def groupby_sensor_and_hour(self):
        self.df['hour'] = self.df['timestamp'].dt.floor('h')

        grouped_df = self.df.groupby(['sensor_id', 'hour']).mean().reset_index()
        return grouped_df

    def check_threshold_alerts(self):
        alerts_df = self.df[(self.df['pm25'] > 35.0) | (self.df['co2'] > 1000.0)]
        return alerts_df
