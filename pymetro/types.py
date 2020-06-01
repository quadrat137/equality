from dataclasses import dataclass

from . import data


@dataclass
class Line:
    id: int
    name: str

    def __init__(self, id):
        line = data.LINES[id]
        self.id = id
        self.name = line


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

