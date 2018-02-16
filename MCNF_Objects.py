class Leg:
    def __init__(self, servicenum, org, dest, vesselMaxCapacity, loaded, emptyCapacity, cost):
        self.route = servicenum
        self.origin = org
        self.destination = dest
        self.routeCap = vesselMaxCapacity
        self.loadedAmount = loaded
        self.emptyCap = emptyCapacity
        self.cost = cost


class Port:
    def __init__(self, name, demands):
        self.portName = name
        self.demands = demands
        self.outboundLegs = []
        self.inboundLegs = []
