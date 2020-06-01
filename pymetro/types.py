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
        # return f'{self.name} - {self.line.simple_name}'
        return f'{self.name}'
        # return f'{self.id}: {self.name}'

    @staticmethod
    def from_name(param):
        for number, station in data.STATIONS.items():
            normalized_name = station['name'].lower().replace('ё', 'е')
            if normalized_name in param.lower():
                return Station(number)


@dataclass
class Link:
    source: int
    dest: int
    time: int


@dataclass
class Route:
    stations: []
    seconds: int

    def minutes(self):
        return str(timedelta(seconds=self.seconds))

    def __repr__(self):
        return f'{self.minutes()} - {self.stations[::-1]}'
