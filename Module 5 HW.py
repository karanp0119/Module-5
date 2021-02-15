def main():
    func = john(9)

    print(func(10))

    print(string_middle('<<>>', 'Nipuna'))


def string_middle(str, insertword):
    return str[:int(len(str) / 2)] + insertword + str[int(len(str) / 2):]


def john(b):
    def sai(d):
        nonlocal b
        b -= 10
        return b - d

    return sai


if __name__ == "__main__":
    main()
