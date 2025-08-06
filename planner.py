from q import Queue
from heap import Heap
from custom import comp1, comp2

class Planner:

    def __init__(self, flights):
        self.flights = flights[:]
        self.num_of_flights = len(flights)
        self.num_of_cities = -1
        for flight in self.flights:
            self.num_of_cities = max(self.num_of_cities, flight.start_city, flight.end_city)
        self.num_of_cities += 1
        self.flights_from_start_city = [[] for _ in range(self.num_of_cities)]
        for flight in self.flights:
            self.flights_from_start_city[flight.start_city].append(flight)
        self.flight_graph = [[] for _ in range(self.num_of_flights)]
        for flight in self.flights:
            for connecting_flight in self.flights_from_start_city[flight.end_city]:
                if connecting_flight.departure_time - flight.arrival_time >= 20:
                    self.flight_graph[flight.flight_no].append(connecting_flight)
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):

        if start_city == end_city:
            return []

        q = Queue()
        state = [[None, False] for _ in range(self.num_of_flights)]
        
        for flight in self.flights_from_start_city[start_city]:
            if t1 <= flight.departure_time and flight.arrival_time <= t2:
                q.enqueue((flight, 1))
                state[flight.flight_no][1] = True
        
        earliest_arrival = float('inf')
        best_end_flight = None
        least_num_of_flights = float('inf')
        
        while not q.is_empty():
            current_flight, num_flights = q.dequeue()
            
            if current_flight.end_city == end_city:
                if num_flights < least_num_of_flights or (num_flights == least_num_of_flights and current_flight.arrival_time < earliest_arrival):
                    earliest_arrival = current_flight.arrival_time
                    least_num_of_flights = num_flights
                    best_end_flight = current_flight
                continue
            
            for next_flight in self.flight_graph[current_flight.flight_no]:
                if not state[next_flight.flight_no][1] and next_flight.arrival_time <= t2:
                    state[next_flight.flight_no][0] = current_flight
                    state[next_flight.flight_no][1] = True
                    q.enqueue((next_flight, num_flights + 1))
        
        path = []
        current = best_end_flight
        while current is not None:
            path.append(current)
            current = state[current.flight_no][0]
        
        return path[::-1]

    def cheapest_route(self, start_city, end_city, t1, t2):

        if start_city == end_city:
            return []

        heap = Heap(comp1)
        state = [[None, False] for _ in range(self.num_of_flights)]
        
        for flight in self.flights_from_start_city[start_city]:
            if t1 <= flight.departure_time and flight.arrival_time <= t2:
                heap.insert((flight.fare, flight))
                state[flight.flight_no][1] = True
        
        while len(heap) != 0:
            total_cost, current_flight = heap.extract()
            
            if current_flight.end_city == end_city:
                path = []
                current = current_flight
                while current is not None:
                    path.append(current)
                    current = state[current.flight_no][0]
                return path[::-1]
                
            for next_flight in self.flight_graph[current_flight.flight_no]:
                if not state[next_flight.flight_no][1] and next_flight.arrival_time <= t2:
                    new_cost = total_cost + next_flight.fare
                    state[next_flight.flight_no][0] = current_flight
                    state[next_flight.flight_no][1] = True
                    heap.insert((new_cost, next_flight))
        
        return []

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):

        if start_city == end_city:
            return []

        heap = Heap(comp2)
        state = [[None, False] for _ in range(self.num_of_flights)]
        
        for flight in self.flights_from_start_city[start_city]:
            if t1 <= flight.departure_time and flight.arrival_time <= t2:
                heap.insert((1, flight.fare, flight))
                state[flight.flight_no][1] = True
        
        while len(heap) != 0:
            num_flights, total_cost, current_flight = heap.extract()
            
            if current_flight.end_city == end_city:
                path = []
                current = current_flight
                while current is not None:
                    path.append(current)
                    current = state[current.flight_no][0]
                return path[::-1]
                
            for next_flight in self.flight_graph[current_flight.flight_no]:
                if not state[next_flight.flight_no][1] and next_flight.arrival_time <= t2:
                    new_num_flights = num_flights + 1
                    new_cost = total_cost + next_flight.fare
                    state[next_flight.flight_no][0] = current_flight
                    state[next_flight.flight_no][1] = True
                    heap.insert((new_num_flights, new_cost, next_flight))
        
        return []