import helloworld


def main():
    # greet =  helloworld.hello() # format error. multiple spaces
    greet = helloworld.hello()
    print(greet)

    hi = helloworld.hi()
    print(hi)

    # x = "a" # lint error. unused variable


if __name__ == "__main__":
    main()
