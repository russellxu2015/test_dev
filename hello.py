def outter():
    a=10
    def inner():
        b=a
        return inner
