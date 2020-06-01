from pymetro.types import Station
from pymetro.data import LINKS

from dataclasses import dataclass

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


@dataclass
class Link:
    source: int
    dest: int
    time: int


class Main:
    links = {}

    def __init__(self):
        self.route = []
        self.time = []

        for i in LINKS:
            self.add_link(Link(i[0], i[1], i[2]))
            self.add_link(Link(i[1], i[0], i[2]))

    def add_link(self, link):
        if link.source in self.links:
            self.links[link.source].append(link)
        else:
            self.links[link.source] = [link]

    def print_stations(self, source: Station, target: Station):

        visited_source = {source: 0}
        visited_target = {target: 0}
        from_source = self.get_adjacent(stations=[source], visited=visited_source, hop=1)
        from_target = self.get_adjacent(stations=[target], visited=visited_target, hop=1)

        for depth in range(1, 10):
            from_source = self.get_adjacent(from_source, visited=visited_source, hop=depth)
            from_target = self.get_adjacent(from_target, visited=visited_target, hop=depth)

        results = {}
        for station in visited_target:
            if station in visited_source:
                overall_dist = visited_source[station] + visited_target[station]
                if overall_dist in results:
                    results[overall_dist].append(station)
                else:
                    results[overall_dist] = [station]

        for i in range(0, 15):
            if i in results:
                print(f'От обоих в {i} суммарно\n')
                for station in results[i]:
                    print(f'{station} - {visited_source[station]} от {source}, {visited_target[station]} от {target}')

    def get_adjacent(self, stations, visited, hop):
        result = set()
        for station in stations:
            # print('links: ', self.links[station.id])
            for link in self.links[station.id]:
                adjacent = Station(link.dest)
                if adjacent not in visited:
                    result.add(adjacent)
                    visited[adjacent] = hop
        return result


if __name__ == "__main__":
    # execute only if run as a script
    main = Main()
    main.print_stations(source=Station(213), target=Station(158))
