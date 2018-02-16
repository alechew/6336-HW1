class Leg:
    def __init__(self, servicenum, org, dest, vesselMaxCapacity, loaded, emptyCapacity, cost):
        self.route = servicenum
        self.origin = str(servicenum) + "_" + org
        self.destination = str(servicenum) + "_" + dest
        self.routeCap = vesselMaxCapacity
        self.loadedAmount = loaded
        self.emptyCap = emptyCapacity
        self.cost = cost
        self.arcFlow = 0


class Port:
    def __init__(self, name, demand):
        self.portName = name
        self.demand = demand
        self.outboundLegs = []
        self.inboundLegs = []
