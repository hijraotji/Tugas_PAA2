def tsp(city_distance, start_city):
    n = len(city_distance)
    tour = list(range(n))
    tour.remove(start_city)
    tour = [start_city] + tour

    for i in range(n - 1):
        for j in range(i + 1, n):
            if city_distance[tour[i]][tour[j]] > city_distance[tour[j]][tour[i]]:
                tour[i + 1], tour[j] = tour[j], tour[i + 1]

    return tour

city_distance = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
start_city = 0

print(tsp(city_distance, start_city))