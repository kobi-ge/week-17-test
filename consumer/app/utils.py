from mysql_connection import MysqlManager


connection = MysqlManager()
connection.create_database()
connection.create_table()


def create_two_lists(data):
    customers = []
    orders = []
    for element in data:
        if element['type'] == "customer":
            customers.append(element)
        else:
            orders.append(element)
    return customers, orders

def insert_customers(customers):
    columns = "_id," \
                "type," \
                "customerNumber," \
                "customerName," \
                "contactLastName," \
                "contactFirstName," \
                "phone," \
                "addressLine1," \
                "addressLine2," \
                "city," \
                "state," \
                "postalCode," \
                "country," \
                "salesRepEmployeeNumber," \
                "creditLimit"
    values = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
    for customer in customers:
        connection.insert(customers, columns, values, customer)
    
def insert_orders(orders):
    columns = "id," \
            "type," \
            "orderNumber," \
            "orderDate," \
            "requiredDate," \
            "shippedDate," \
            "status," \
            "comments," \
            "customerNumber"
    values = "%s, %s, %s, %s, %s, %s, %s, %s, %s,"
    for order in orders:
        connection.insert(orders, columns, values, order)

