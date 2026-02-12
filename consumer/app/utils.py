def create_two_lists(data):
    customers = []
    orders = []
    for element in data:
        if element['type'] == "customer":
            customers.append(element)
        else:
            orders.append(element)
    return customers, orders

