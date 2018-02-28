class Leg:
    def __init__(self, org, dest, startTime, daysTraveled, cost):
        self.origin = org
        self.start = startTime
        self.destination = str(dest)
        self.end = startTime + daysTraveled
        # if self.end >= 6:
        #     self.destination = "7"
        # self.end = 6
        self.cost = cost
        self.traveltime = daysTraveled
        self.arcFlow = 0


class City:
    def __init__(self, name, time, netsupply):
        self.portName = name
        self.time = time
        self.supply = netsupply
        self.outboundLegs = []
        self.inboundLegs = []
