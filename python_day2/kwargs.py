def employee(**details):
    for key, value in details.items():
        print(key, ":", value)

employee(name="Bob", salary=50000)