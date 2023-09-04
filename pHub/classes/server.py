import random

class Server:
    def __init__(self):
        self.servers = []

    @property
    def Servers(self):
        return self.servers

    def assigned_server(self, problem):
        for i in range(problem['totalServers']):
            # Obtenemos un índice aleatorio del 0 al número total de nodos existentes
            random_index = self.get_random_int(len(problem['nodes']))

            # Agregamos como servidor el nodo escogido aleatoriamente
            self.servers.append({
                'id': problem['nodes'][random_index]['id'],
                'capacity': problem['maxCapacityServer'],
                'availableCapacity': problem['maxCapacityServer'],
                'assignedClients': [],
                'totalDistance': 0,
                'coordinates': {
                    'x': problem['nodes'][random_index]['coordinates']['x'],
                    'y': problem['nodes'][random_index]['coordinates']['y'],
                },
            })

            # Filtramos el nodo escogido aleatoriamente para que solo aparezca como servidor
            problem['nodes'] = [
                element for index, element in enumerate(problem['nodes']) if index != random_index
            ]

        return problem

    def all_server_busy(self, servers, current_demand):
        return all(server['availableCapacity'] < current_demand for server in servers)

    def get_random_int(self, max_value):
        return random.randint(0, max_value - 1)
