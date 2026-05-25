import matplotlib.pyplot as plt
import io
import pandas as pd


class AirResponderAPI:
    """
    Класс для отдачи ответов API и графиков (Пункты 13-14).
    Принимает объект аналитики Pandas и упаковывает результаты в JSON или PNG-файлы.
    """

    def __init__(self, analytics_engine) -> None:
        self.analytics = analytics_engine

    def generate_pollution_chart_bytes(self) -> bytes:
        """
        Строит линейный график средних значений PM2.5 по часам.
        Возвращает картинку в виде байтов (для отправки файла через API).
        """
        # Запрашиваем сгруппированные данные из модуля аналитики
        df_hourly = self.analytics.groupby_sensor_and_hour()

        plt.figure(figsize=(10, 5))

        # Строим линию тренда для каждого датчика отдельно
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

        # Сохраняем график не на диск, а в оперативную память (в байты)
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight')
        img_buffer.seek(0)
        chart_bytes = img_buffer.getvalue()
        plt.close()

        return chart_bytes

    def get_api_alerts_json(self) -> str:
        """
        Получает список всех алертов и упаковывает их в чистый JSON-ответ для API.
        """
        alerts_df = self.analytics.check_threshold_alerts()

        if alerts_df.empty:
            return "[]"

        # Копируем DataFrame, чтобы случайно не испортить оригинальные данные
        export_df = alerts_df.copy()

        # Переводим тип данных Timestamp в строки, иначе JSON упадет с ошибкой
        export_df['timestamp'] = export_df['timestamp'].astype(str)

        # Конвертируем таблицу в JSON-массив словарей
        return export_df.to_json(orient='records', force_ascii=False, indent=4)
