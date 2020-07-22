import feature


def func():
    print("hello")


def test():
    print("This is master test")


if __name__ == "__main__":
    import pydevd_pycharm

    pydevd_pycharm.settrace('10.90.191.231', port=51234, stdoutToServer=True, stderrToServer=True)
    test()
    func()
    feature.fea()
    print("master add something")
