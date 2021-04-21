from member import Member


if __name__ == '__main__':
    members = [
        Member('李'),
        Member('陈'),
        Member('丁'),
        Member('孙')
    ]
    for i in members:
        i.greet()
    for i in members:
        i.eat()
