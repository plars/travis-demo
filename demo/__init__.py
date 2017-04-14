import os


def say_hello(name):
    return "Hello %s!" % name


def check_code():
    if os.environ.get("DEMO_CODE") == "12345":
        return True
    return False
