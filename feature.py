import logging


def fea(someone):
    print(someone)
    for i in range(10):
        print("hh")


def who_to_greet(person):
    return person if person else input('Greet who? ')


def greet(someone, greeting='Hello'):
    print(greeting + ', ' + who_to_greet(someone))


def greet_many(people):
    for person in people:
        try:
            greet(person)
        except Exception as e:
            print('hi, ' + person)
            logging.exception("Exception occurred")
