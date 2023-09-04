from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CoordinateI:
    x: float
    y: float

@dataclass
class NodeI:
    id: int
    coordinates: CoordinateI
    demand: int
    distance: Optional[float] = None

@dataclass
class ServerI:
    id: int
    capacity: int
    coordinates: CoordinateI
    availableCapacity: int
    totalDistance: float
    assignedClients: List[NodeI]

@dataclass
class SolutionI:
    servers: List[ServerI]
    cost: float

@dataclass
class ProblemI:
    totalNodes: int
    totalServers: int
    maxCapacityServer: int
    nodes: List[NodeI]
