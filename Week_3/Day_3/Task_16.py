from bs4 import BeautifulSoup
import requests
import sqlite3


class Extractor:
    def __init__(self):
        self.url = "https://www.worldometers.info/coronavirus/"

    def DataExtraction(self):
        response = requests.get(self.url)
        data = BeautifulSoup(response.text, 'html.parser')
        find_table = data.find('table', class_='table')
        rows = find_table.find_all('tr')
        return rows


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS coronavirus_data (country TEXT, total_cases TEXT, total_deaths TEXT, total_recovered TEXT)")

    def insert_data(self, data):
        for row in data[1:]:
            columns = row.find_all('td')
            country = columns[1].text.strip()
            total_cases = columns[2].text.strip()
            total_deaths = columns[4].text.strip()
            total_recovered = columns[6].text.strip()
            self.cur.execute("INSERT INTO coronavirus_data VALUES (?, ?, ?, ?)",
                             (country, total_cases, total_deaths, total_recovered))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


extractor = Extractor()
table_data = extractor.DataExtraction()

database = Database('coronavirus.db')
database.insert_data(table_data)
database.close_connection()
