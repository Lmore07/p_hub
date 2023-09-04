from math import sqrt

class Client:
    def __init__(self):
        pass

    def calculate_distance(self, server, client):
        return sqrt(
            (client['coordinates']['y'] - server['coordinates']['y']) ** 2 +
            (client['coordinates']['x'] - server['coordinates']['x']) ** 2
        )