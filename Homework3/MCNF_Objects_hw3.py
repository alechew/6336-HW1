class Leg:
    def __init__(self, org, dest, startTime, daysTraveled, cost):
        self.origin = org
        self.destination = dest
        self.start = startTime
        self.end = startTime + daysTraveled
        self.cost = cost
        self.arcFlow = 0


class City:
    def __init__(self, name, time, demand):
        self.portName = name
        self.time = time
        self.demand = demand
        self.outboundLegs = []
        self.inboundLegs = []
