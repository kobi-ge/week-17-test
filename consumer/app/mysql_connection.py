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

a = MysqlManager()