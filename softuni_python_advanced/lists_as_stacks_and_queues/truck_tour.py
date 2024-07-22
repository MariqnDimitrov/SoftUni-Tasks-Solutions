from collections import deque
number_of_petrol_pumps = int(input())
petrol_stations = deque([])
start_position = 0
stops = 0
for _ in range(number_of_petrol_pumps):
    current_fuel, distance = input().split()
    petrol_stations.append([int(current_fuel), int(distance)])
while stops < number_of_petrol_pumps:
    fuel = 0
    for station in range(number_of_petrol_pumps):
        fuel += petrol_stations[station][0]
        destination = petrol_stations[station][1]
        if fuel < destination:
            petrol_stations.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1
print(start_position)