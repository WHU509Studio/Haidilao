from member import Member


if __name__ == '__main__':
    members = [
        Member('ζ'),
        Member('ι'),
        Member('δΈ'),
        Member('ε­')
    ]
    for i in members:
        i.greet()
    for i in members:
        i.eat()
