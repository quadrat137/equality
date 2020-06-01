from pymetro.println import println
from pymetro.types import Station


def get_price_data():
    file_object = open('rent.txt', "r")
    lines = file_object.readlines()

    result = {}

    for line in lines:
        word = line.split("\t")
        println(word)
        station = Station.from_name(param=word[0])
        print(f'name: {word[0]}, station: {station}')

        price = int(word[1].replace(" ", ""))
        result[station] = price

    return result
