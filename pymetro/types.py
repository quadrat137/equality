from dataclasses import dataclass

from . import data

from datetime import timedelta


@dataclass
class Line:
    id: int
    name: str
    simple_name: str

    def __init__(self, id):
        line = data.LINES[id]
        self.id = id
        self.name = line[0]
        self.simple_name = line[1]


@dataclass
class Station:
    id: int
    name: str
    line: Line

    def __init__(self, id):
        station = data.STATIONS[id]

        self.id = id
        self.name = station['name']
        self.line = Line(station['line'])

    def __hash__(self):
        return hash(id)

    def __eq__(self, other: 'Station'):
        return self.id == other.id

    def __repr__(self):
        return f'{self.name}'
        # return f'{self.id}: {self.name}'


@dataclass
class Link:
    source: int
    dest: int
    time: int


@dataclass
class Route:
    stations: []
    min: int

    def __repr__(self):
        time = str(timedelta(seconds=self.min))
        return f'{time} - {self.stations[::-1]}'
