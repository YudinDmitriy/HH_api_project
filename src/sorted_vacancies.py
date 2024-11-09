import json
from datetime import datetime


class SortedVacancy:
    """
    Класс сортирует вакансии
    """
    def __init__(self):
        """
        Инициализация
        """
        self.head_hunter_sorted = []
        self.date_format = None

    @property
    def sorted_vacancies_hh(self):
        """
        Получаем отсортированный список вакансий из json файла
        :return: self.head_hunter_sorted
        """
        with open("data/vacancy.json", encoding="utf-8") as file:
            content = json.load(file)
        for i in content["items"]:
            if i["salary"]["from"] is None:
                i["salary"]["from"] = 0
            if i["salary"]["to"] is None:
                i["salary"]["to"] = 0
            if i["published_at"]:
                date = datetime.strptime(i["published_at"], "%Y-%m-%dT%H:%M:%S+%f")
                self.date_format = f"{date:%d.%m.%Y}"
            self.head_hunter_sorted.append({
                "name": i["name"],
                "url": i["alternate_url"],
                "city": i["area"]["name"],
                "currency": i["salary"]["currency"],
                "payment_from": i["salary"]["from"],
                "payment_to": i["salary"]["to"],
                "requirement": i["snippet"]["requirement"],
                "responsibility": i["snippet"]["responsibility"],
                "date": self.date_format
            })
        return self.head_hunter_sorted
