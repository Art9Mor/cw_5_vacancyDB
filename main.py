from src.class_db_manager import DBManager
from src.config import config
from src.utils import create_db, create_tables, filling_database, get_data

if __name__ == '__main__':
    employers_list = [
        8550,  # ЦФТ
        78638,  # Тинькофф
        1740,  # Яндекс
        2180,  # Озон
        2748,  # Ростелеком
        3776,  # МТС
        23040,  # Банк Открытие
        3127,  # Мегафон
        39305,  # Газпром нефть
        4934  # Билайн
    ]
    script_file = 'create_db.sql'
    db_name = input('Enter your DB name: ')
    params = config()

    create_db(db_name, params)
    print(f'Data Base {db_name} was successfully created!')

    # params.update({'dbname': db_name})

    create_tables(db_name, params)
    filling_database(get_data(employers_list), db_name, params)

    db_manager = DBManager(db_name, params)
    while True:
        print('-' * 50)
        print('Main menu:\n')
        print('Tape "1" to get all companies and vacancies count\n')
        print('Tape "2" to get all vacancies\n')
        print('Tape "3" to get average salary for vacancies\n')
        print('Tape "4" to get vacancies with higher salary\n')
        print('Tape "5" to get vacancies with keyword\n')
        print('Tape "0" to quit\n')

        user_input = input('Choose an activity: ')
        match user_input:
            case '1':
                print('-' * 50)
                print(db_manager.get_companies_and_vacancies_count())
            case '2':
                print('-' * 50)
                print(db_manager.get_all_vacancies())
            case '3':
                print('-' * 50)
                print(db_manager.get_avg_salary())
            case '4':
                print('-' * 50)
                print(db_manager.get_vacancies_with_higher_salary())
            case '5':
                print('-' * 50)
                keyword = input('Input your keyword: ').lower()
                print(db_manager.get_vacancies_with_keyword(keyword))
            case '0':
                print('-' * 50)
                print('-' * 50)
                quit('The program has been deactivated')
            case _:
                print('-' * 50)
                print('Unknown activity')
