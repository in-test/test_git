from feature import greet_many


def func():
    test()
    print("hello")


def test():
    print("This is master test")


if __name__ == "__main__":
    greet_many(['chard', 1])
