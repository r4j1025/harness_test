def greet(name):
    return f"Hello, Mr. {name}!"


if __name__ == "__main__":
    import sys

    name = sys.argv[1]
    print(greet(name))