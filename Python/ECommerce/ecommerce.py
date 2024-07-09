import csv
import re

class Customer:
    def __init__(self, title, first_name, last_name, email, phone):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

class CustomerNotAllowedException(Exception):
    pass

class Order:
    def __init__(self, customer, product_name, product_code):
        self.customer = customer
        self.product_name = product_name
        self.product_code = product_code

def read_customer_data(filename):
    customers = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title, first_name, last_name = separate_name(row['Name'])
            customer = Customer(title, first_name, last_name, row['Email'], row['Phone'])
            customers.append(customer)
    return customers

def separate_name(full_name):
    # Example regular expression to separate title, first name, last name
    pattern = re.compile(r'(?P<title>Mr|Ms|Mrs)\.?\s+(?P<first>\w+)\s+(?P<last>\w+)')
    match = pattern.match(full_name)
    if match:
        return match.group('title'), match.group('first'), match.group('last')
    else:
        return None, None, None

def create_order(customer, product_name, product_code):
    # Simulate blacklisted customer check
    if customer.email == 'blacklisted@example.com':
        raise CustomerNotAllowedException("Customer is blacklisted.")

    # Process order creation
    order = Order(customer, product_name, product_code)
    return order

# Example usage
if __name__ == "__main__":
    customers = read_customer_data('FairDealCustomerData.csv')

    for customer in customers:
        try:
            order = create_order(customer, 'Sample Product', '12345')
            print(f"Order created successfully for {customer.first_name} {customer.last_name}")
        except CustomerNotAllowedException as e:
            print(f"Error creating order for {customer.first_name} {customer.last_name}: {str(e)}")
