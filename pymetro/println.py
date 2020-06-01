deb = 1


def println(iterable):
    global deb
    print('debug line ', deb)
    deb = deb + 1
    if type(iterable) is dict:
        for item in iterable:
            print(f'{item} : {iterable[item]}')
    else:
        for item in iterable:
            print(item)
