from pymetro.println import println
from pymetro.types import *
from pymetro.data import *


class Main:
    links = {}
    max_stations = 7
    max_time = 60 * 30  # 30 minutes in seconds

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

        # print('\nsource\n', source)
        visited_with_route_from_source = self.get_visited_tree(source)
        # print('\ntarget\n', target)
        visited_with_route_from_target = self.get_visited_tree(target)
        intersection = visited_with_route_from_source.keys() & visited_with_route_from_target.keys()
        println(intersection)
        for item in intersection:
            print('===========')
            print(visited_with_route_from_target[item])
            print(visited_with_route_from_source[item])

    def get_visited_tree(self, station):
        station_route_map = {station: Route([station], 0)}
        for depth in range(1, self.max_stations):
            station_route_map = self.get_adjacent(station_route_map=station_route_map)
        return station_route_map

    def get_adjacent(self, station_route_map):
        result = station_route_map.copy()
        # println(station_route_map)
        for station, route in station_route_map.items():
            # print('links: ', self.links[station.id])
            for link in self.links[station.id]:
                adjacent = Station(link.dest)
                if adjacent not in result:
                    result[adjacent] = Route(route.stations.copy(), route.min)
                    result[adjacent].stations.append(adjacent)
                    result[adjacent].min += link.time
                # else:
                #     if result[adjacent].min > (route.min + link.time):
                #         result[adjacent] = visited_route_map[adjacent]
                #         result[adjacent].stations.append(adjacent)
                #         result[adjacent].min += link.time

        return result


if __name__ == "__main__":
    # execute only if run as a script
    main = Main()
    main.print_stations(source=Station(158), target=Station(63))
