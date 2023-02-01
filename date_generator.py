# импортируем необходимые библиотеки
from faker import Faker
import random
from typing import Iterator
from transliterate import slugify

fake_ru = Faker(locale="ru_RU")


def main():
    # генерирование таблицы users
    num_peoples = int(input("Введите количество пользователей: "))
    # создаем список, в который будут записываться генерируемые функцией "people" словари с данными о пользователях
    list_people = []
    people_gen = people()
    for i in range(num_peoples):
        list_people.append(next(people_gen))
    # для записи результатов в таблицу Excel необходимо список словарей преобразовать в список кортежей
    # создаем список tup, в который будут записываться кортежи
    tup = []
    # первым кортежем должен быть кортеж, содержащий названия ключей словарей, которые будут названиями
    # соответствующих столбцов таблицы Excel
    tup_elem = []
    # так как названия ключей во всех словарях будут одинаковыми, то нам достаточно будет считать названия
    # ключей только первого словаря в списке list_people
    for elem in (list_people[0].keys()):
        tup_elem.append(elem)
    tup_name = tuple(tup_elem)
    tup.append(tup_name)
    # далее считываем сгенерированные параметры пользователей из всех словарей
    for n, dict_ in enumerate(list_people):
        tup_temp = (dict_['ID'], dict_['Логин'], dict_['Пароль'], dict_['Имя'], dict_['Фамилия'], dict_['E-mail'], dict_['Телефон'],
                    dict_['Страна'], dict_['Адрес'], dict_['Дата рождения'])
        tup.append(tup_temp)
    return tup

def login() -> str:
    fake_en = Faker(locale="en_US")
    return fake_en.first_name()


def password() -> str:
    fake_en = Faker(locale="en_US")
    return fake_en.password()


def male() -> str:
    list_male = ['male', 'female']
    return random.choice(list_male)


def name(male: str) -> str:
    if male == 'male':
        return fake_ru.first_name_male()
    else:
        return fake_ru.first_name_female()


def surname(male: str) -> str:
    if male == 'male':
        return fake_ru.last_name_male()
    else:
        return fake_ru.last_name_female()


def email(email_name: str, email_female: str) -> str:
    return f'{slugify(email_name)}{slugify(email_female)}@{fake_ru.free_email_domain()}'


def phone() -> str:
    return fake_ru.phone_number()

def country() -> str:
    return fake_ru.country()

def address() -> str:
    return fake_ru.address()


def date_of_birth() -> str:
    return fake_ru.date()


def people() -> Iterator[dict]:
    people_id = 0
    while True:
        people_id += 1
        people_login = login()
        people_password = password()
        people_male = male()
        people_name = name(people_male)
        people_surname = surname(people_male)
        people_dict = {
            'ID': people_id,
            'Логин': people_login,
            'Пароль': people_password,
            'Имя': people_name,
            'Фамилия': people_surname,
            'E-mail': email(people_name, people_surname),
            'Телефон': phone(),
            'Страна': country(),
            'Адрес': address(),
            'Дата рождения': date_of_birth()
        }
        yield people_dict


if __name__ == "__main__":
    main()
