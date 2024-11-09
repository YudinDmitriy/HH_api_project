from src.user_forms import UserForm


class HHRequestDebug(UserForm):
    """
    Класс дебажит ввод пользователя
    """
    search_query = None
    top_n = None

    def user_input_int(self):
        """
        Проверка на строку, пустую строку, приравнивает к 100
        :return: int(self.top_n)
        """
        self.top_n = input("Введите количество вакансий для вывода: ")
        if self.top_n.isalpha():
            raise ValueError("Количество не может быть строкой")
        if self.top_n == "":
            raise AttributeError("Количество не может быть пустым")
        if int(self.top_n) > 100:
            self.top_n = 100
        return int(self.top_n)

    def user_input_str(self):
        """
        Проверка на ввод числа и пустую строку
        :return: self.search_query
        """
        self.search_query = input("Введите вакансию: ")
        if self.search_query == "":
            raise ValueError("Запрос не может быть пустым")
        if self.search_query.isdigit():
            raise TypeError("Запрос не может быть числом")
        else:
            return self.search_query

