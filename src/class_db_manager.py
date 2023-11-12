import psycopg2


class DBManager:

    def __init__(self, db_name: str, params: dict):
        self.database_name = db_name
        self.params = params

    def get_companies_and_vacancies_count(self) -> list[tuple] or str:
        """
        Gets a list of all companies and the number of vacancies for each company.
        """
        try:
            conn = psycopg2.connect(database=self.database_name, **self.params)
            with conn.cursor() as curs:
                curs.execute('SELECT company_name, COUNT(vacancy_id) '
                             'FROM companies '
                             'JOIN vacancies USING (company_id) '
                             'GROUP BY company_name '
                             'ORDER BY company_name')
                result = curs.fetchall()

        except (Exception, psycopg2.DatabaseError) as err:
            return err

        conn.close()
        return result

    def get_all_vacancies(self) -> list[tuple] or str:
        """
        Receives a list of all vacancies indicating the company name,
        vacancy title and salary, and a link to the vacancy.
        """
        try:
            conn = psycopg2.connect(database=self.database_name, **self.params)
            with conn.cursor() as curs:
                curs.execute('SELECT title_vacancy, company_name, salary, vacancies.link '
                             'FROM vacancies '
                             'JOIN companies USING (company_id);')

                result = curs.fetchall()

        except (Exception, psycopg2.DatabaseError) as err:
            return err

        conn.close()
        return result

    def get_avg_salary(self) -> list[tuple] or str:
        """
        Receives the average salary for the vacancies.
        """
        try:
            conn = psycopg2.connect(database=self.database_name, **self.params)
            with conn.cursor() as curs:
                curs.execute('SELECT company_name, ROUND(AVG(salary)) AS average_salary '
                             'FROM companies '
                             'JOIN vacancies USING (company_id) '
                             'GROUP BY company_name;')

                result = curs.fetchall()

        except (Exception, psycopg2.DatabaseError) as err:
            return err

        conn.close()
        return result

    def get_vacancies_with_higher_salary(self) -> list[tuple] or str:
        """
        Gets a list of all vacancies with a salary higher than the average for all vacancies.
        """
        try:
            conn = psycopg2.connect(database=self.database_name, **self.params)
            with conn.cursor() as curs:
                curs.execute('SELECT * FROM vacancies '
                             'WHERE salary > (SELECT AVG(salary) FROM vacancies);')

                result = curs.fetchall()

        except (Exception, psycopg2.DatabaseError) as err:
            return err

        conn.close()
        return result

    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple] or str:
        """
        Gets a list of all vacancies whose titles contain the words passed to the method, for example python.
        :param keyword: string with part of vacancy name
        """
        try:
            conn = psycopg2.connect(database=self.database_name, **self.params)
            with conn.cursor() as curs:
                curs.execute(f"""
                SELECT * FROM vacancies
                WHERE lower(title_vacancy) LIKE '%{keyword}%'
                    OR lower(title_vacancy) LIKE '%{keyword}'
                    OR lower(title_vacancy) LIKE '{keyword}%'
                """)

                result = curs.fetchall()

        except (Exception, psycopg2.DatabaseError) as err:
            return err

        conn.close()
        return result
