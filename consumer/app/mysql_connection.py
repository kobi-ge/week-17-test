import mysql.connector 
import os
from dotenv import load_dotenv

load_dotenv()

class MysqlManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = os.getenv("MYSQL_HOST", "localhost"),
                user = os.getenv("MYSQL_USER", "root"),
                password = os.getenv("MYSQL_PASSWORD", ""),
                port = int(os.getenv("MYSQL_PORT", 3306))
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("connection to mysql established")
        except mysql.connector.Error as e:
            raise e

    def create_database(self):
        try:
            query = f"CREATE DATABASE IF NOT EXISTS customers_orders"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"database customers_orders created.")
        except mysql.connector.Error as e:
            print(f"failed to create database: {e}")

    def create_table(self):
        try:
            self.cursor.execute("USE customers_orders")
            fields_table1 = "id VARCHAR(30) PRIMARY KEY," \
                            "type VARCHAR(20)," \
                            "customerNumber INT," \
                            "customerName VARCHAR(70)," \
                            "contactLastName VARCHAR(70)," \
                            "cuntactFirstName VARCHAR(70)," \
                            "phone VARCHAR(12)," \
                            "addressLine1 VARCHAR(20)," \
                            "addressLine2 VARCHAR(20)," \
                            "city VARCHAR(20)," \
                            "state VARCHAR(20)," \
                            "postalCode VARCHAR(20)," \
                            "country VARCHAR(20)," \
                            "salesRepEmployeeNumber INT," \
                            "creditLimit VARCHAR(20)"
            query_table1 = f"CREATE TABLE IF NOT EXISTS customers ({fields_table1})"
            self.cursor.execute(query_table1)
            fields_table2 = "id VARCHAR(30) PRIMARY KEY," \
                            "type VARCHAR(20)," \
                            "orderNumber INT," \
                            "orderDate VARCHAR(30)," \
                            "requiredDate VARCHAR(30)," \
                            "shippedDate VARCHAR(30)," \
                            "status VARCHAR(30)," \
                            "comments VARCHAR(30)," \
                            "customerNumber INT"
            query_table2 = f"CREATE TABLE IF NOT EXISTS orders ({fields_table2})"
            self.cursor.execute(query_table2)
            self.connection.commit()
            print("table created successfully")
        except mysql.connector.Error as e:
            print(f"the following error occured: {e}")

    def insert(self, table_name, columns, values, row):
        try:
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            self.cursor.execute(query, row)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"the following error occured: {e}")

    