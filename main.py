# импортируем из генератора тестовых данных функцию main
from date_generator import main
# импортируем необходимые библиотеки
import pandas as pd
from openpyxl import Workbook, load_workbook

if __name__ == '__main__':
    # генерируем необходимое количество данных
    data = main()

    # сохранение данных в dataframe pandas
    data_rezult = pd.DataFrame(data)
    print('[INFO] DataFrame create successfull.')

    # создаем объек для подготовки к записи данных в файл Excel
    writer = pd.ExcelWriter('test_database.xlsx')

    # записываем данные dataFrame в файл Excel
    data_rezult.to_excel(writer)

    # сохраняем файл Excel
    writer.save()
    print('[INFO] DataFrame is written successfully to Excel File.')

    # удалим первую строку и первый столбец, в которых содержатся номера соответствующих строк и столбцов
    # для этого создаем экземпляр с именем пути к файлу excel
    wb = load_workbook('test_database.xlsx')

    # выбираем активный лист
    sheet = wb.active

    # удаляем строку
    sheet.delete_rows(1)
    print('[INFO] Row was delete successful.')

    # удаляем столбец
    sheet.delete_cols(1, 1)
    print('[INFO] Column was delete successful.')

    # сохраняем итоговую excel-таблицу
    wb.save('test_database.xlsx')
    print('[INFO] Table excel was save successful.')
