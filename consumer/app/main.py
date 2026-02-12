from mysql_connection import MysqlManager
from kafka_consumer import run_consumer
from utils import create_two_lists

def main():
    connection = MysqlManager()
    connection.create_database()
    connection.create_table()
    data = run_consumer()
    customers, orders = create_two_lists(data)
    