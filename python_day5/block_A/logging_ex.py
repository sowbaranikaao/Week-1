"""
def login(username):

    print("Application Started")

    print("Checking Username")

    if username == "admin":

        print("Login Successful")

    else:

        print("Invalid Username")

login("admin")
"""

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)
def login(username):
    logging.info("Application Started")
    logging.info("Checking Username")
    if username=="admin":
        logging.info("Logging successful")
    else:
        logging.error("Invalid username")
login("admin")
login("sow")