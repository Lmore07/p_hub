from typing import List, Dict

from .client import Client
from .server import Server

class PHubService:
    def get_solutions_phub(self, files: List[Dict]) -> Dict:
        map_data = None
        best_solution = None

        for file in files:
            content = file.read().decode("utf8")
            map_data = self.mapping_data(content)
            best_solution = self.get_best_solution(map_data, 20)

        return {"message": "Transacción Existosa", "data": best_solution}

    def get_best_solution(self, problem: Dict, iterations: int) -> Dict:
        solutions = []

        for _ in range(iterations):
            servers = self.assign_client_to_servers(problem.copy())
            cost = round(sum(server["totalDistance"] for server in servers), 2)
            solutions.append({"cost": cost, "servers": servers})

        return {
            "solucionOptima": self.solution_optimal(solutions),
            "solutiones": solutions,
        }

    def solution_optimal(self, solutions: List[Dict]) -> Dict:
        return min(solutions, key=lambda x: x["cost"])

    def mapping_data(self, content: str) -> Dict:
        lines = content.strip().split("\n")
        total_nodes, total_servers, max_capacity_server = map(int, lines[0].split())

        nodes = []
        for line in lines[1:]:
            node_data = list(map(int, line.strip().split()))
            nodes.append({
                "id": node_data[0],
                "coordinates": {"x": node_data[1], "y": node_data[2]},
                "demand": node_data[3],
            })

        return {
            "totalNodes": total_nodes,
            "totalServers": total_servers,
            "maxCapacityServer": max_capacity_server,
            "nodes": nodes,
        }

    def assign_client_to_servers(self, problem: Dict) -> List[Dict]:
        server = Server()
        client = Client()

        # Asignar Aleatoriamente los servidores
        problem = server.assigned_server(problem)

        # Asignación de clientes a un servidor
        for element in problem["nodes"]:
            is_assigned = False

            while not is_assigned:
                # Obtenemos un indice aleatorio del 0 al número total de servidores existentes
                index_random_server = server.get_random_int(len(server.servers))

                # Verificar espacio en los servidores, para el cliente actual
                if server.all_server_busy(server.servers, element["demand"]):
                    is_assigned = True
                    break

                # Validar que la capacidad no haya sido excedida
                if (
                    server.servers[index_random_server]["availableCapacity"]
                    >= element["demand"]
                ):
                    # Si no ha sido excedida, se empieza a asignar como cliente
                    server.servers[index_random_server]["assignedClients"].append(element)

                    # Y actualizamos la nueva capacidad
                    server.servers[index_random_server]["availableCapacity"] -= element[
                        "demand"
                    ]

                    # Calculamos la distancia
                    element["distance"] = client.calculate_distance(
                        server.servers[index_random_server], element
                    )

                    # Acumulamos las distancias
                    server.servers[index_random_server]["totalDistance"] += element[
                        "distance"
                    ]

                    is_assigned = True

        return server.servers