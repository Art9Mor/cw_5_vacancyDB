## cw_5_vacancyDB
# (Program for processing vacancies)

  The program is designed to process vacancies from selected employers from the website hh.ru using
  PostgreSQL to create, fill and manage your work database.

# Employers choice

  The selection of employers occurs by entering their id into a list, which is then entered 
  into the database along with the necessary information.

  The ids of the companies you are interested in can be found here: https://dev.hh.ru/admin/widgets/employer

  The number of entered ids is limited. You can add 10 companies to the list.
  Sample part of code: 

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

# User menu

  The user menu is designed to create, populate and manage the database 
  using input fields and corresponding commands.

  To create and fill out a data slot, you need to follow simple instructions:
    1) Create and fill 'database.ini' file with your data to connect to your PostgreSQL:
      [postgresql]
      host=(host_name)
      user=(user_name)
      password=(password)
      port=(port_number)
    2) 
