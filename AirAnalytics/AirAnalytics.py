import pandas as pd
from typing import List, Dict, Any


class AirAnalytics:
    def __init__(self, raw_data: List[Dict[str, Any]]) -> None:
        self.df = pd.DataFrame(raw_data)

        if not self.df.empty:
            self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])

    def groupby_sensor_and_hour(self) -> pd.DataFrame:
        if self.df.empty:
            return pd.DataFrame()

        self.df['hour'] = self.df['timestamp'].dt.floor('h')

        grouped_df = self.df.groupby(['sensor_id', 'hour']).agg({
            'pm25': 'mean',
            'co2': 'mean'
        }).reset_index()

        return grouped_df

    def check_threshold_alerts(self, pm25_limit: float = 35.0, co2_limit: float = 1000.0) -> pd.DataFrame:
        if self.df.empty:
            return pd.DataFrame()

        alerts_df = self.df[
            (self.df['pm25'] > pm25_limit) |
            (self.df['co2'] > co2_limit)
            ]

        return alerts_df
