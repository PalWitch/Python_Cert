from exceptionscustomer import Customer
from exceptionscustomer import check_age
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

user1 = Customer()
user1.add_name("Niklas12")
user1.add_age(25)
check_age(50)

