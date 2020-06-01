from pymetro.get_price_data import get_price_data
from pymetro.println import println
from pymetro.types import *
from pymetro.data import *


class Main:
    links = {}
    max_stations = 12
    max_time = 60 * 30  # 30 minutes in seconds
    max_price = 60000

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

        price_data = get_price_data()
        result = []
        for item in intersection:
            route_from_target = visited_with_route_from_target[item]
            route_from_source = visited_with_route_from_source[item]
            if route_from_source.seconds > self.max_time:
                print(f'{item} слишком далеко от {source} - {route_from_source.minutes()}')
                continue
            elif route_from_target.seconds > self.max_time:
                print(f'{item} слишком далеко от {source} - {route_from_target.minutes()}')
                continue

            if item not in price_data:
                print(f'Нет цен по {item}')
                continue
            if price_data[item] > self.max_price:
                print(f'{item} слишком дорого - {price_data[item]}')
                continue

            result_line = f'Метро {item.name}, ' \
                          f'до {source.name} {len(route_from_source.stations)} остановок, {route_from_source.minutes()} минут ' \
                          f'до {target.name} {len(route_from_target.stations)} остановок, {route_from_target.minutes()} минут ' \
                          f'средняя цена {price_data[item]} руб.'
            result.append(result_line)

        println(result)

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
                    result[adjacent] = Route(route.stations.copy(), route.seconds)
                    result[adjacent].stations.append(adjacent)
                    result[adjacent].seconds += link.time

        return result


if __name__ == "__main__":
    # execute only if run as a script
    main = Main()
    main.print_stations(source=Station(158), target=Station(63))
