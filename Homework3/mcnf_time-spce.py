"""
A Standard MinCost Network Flow Problem, Modified for Container Repositioning

This version keeps all information in the header of this file
Has no ability to read data files

Authors: Alan Erera 2013
"""

# Import PuLP modeler functions
from pulp import *
import MCNF_Objects_hw3

portNames = ["New York", "Savannah", "Rotterdam", "Giao Tauro", "Dubai", "Singapore", "Shanghai", "Busan", "Seattle", "Los Angeles"]

#  0 is source and 6 is sink
# name, time, cost
ports = {
	1 : [MCNF_Objects_hw3.City(1, 0, 0), MCNF_Objects_hw3.City(1, 1, 0), MCNF_Objects_hw3.City(1, 2, 0), MCNF_Objects_hw3.City(1, 3, 0), MCNF_Objects_hw3.City(1, 4, 0), MCNF_Objects_hw3.City(1, 5, 0), MCNF_Objects_hw3.City(1, 6, 0)],
	2 : [MCNF_Objects_hw3.City(2, 0, 0), MCNF_Objects_hw3.City(2, 1, 0), MCNF_Objects_hw3.City(2, 2, 0), MCNF_Objects_hw3.City(2, 3, 0), MCNF_Objects_hw3.City(2, 4, 0), MCNF_Objects_hw3.City(2, 5, 0), MCNF_Objects_hw3.City(2, 6, 0)],
	3 : [MCNF_Objects_hw3.City(3, 0, 0), MCNF_Objects_hw3.City(3, 1, 0), MCNF_Objects_hw3.City(3, 2, 0), MCNF_Objects_hw3.City(3, 3, 0), MCNF_Objects_hw3.City(3, 4, 0), MCNF_Objects_hw3.City(3, 5, 0), MCNF_Objects_hw3.City(3, 6, 0)],
	4 : [MCNF_Objects_hw3.City(4, 0, 0), MCNF_Objects_hw3.City(4, 1, 0), MCNF_Objects_hw3.City(4, 2, 0), MCNF_Objects_hw3.City(4, 3, 0), MCNF_Objects_hw3.City(4, 4, 0), MCNF_Objects_hw3.City(4, 5, 0), MCNF_Objects_hw3.City(4, 6, 0)],
	5 : [MCNF_Objects_hw3.City(5, 0, 0), MCNF_Objects_hw3.City(5, 1, 0), MCNF_Objects_hw3.City(5, 2, 0), MCNF_Objects_hw3.City(5, 3, 0), MCNF_Objects_hw3.City(5, 4, 0), MCNF_Objects_hw3.City(5, 5, 0), MCNF_Objects_hw3.City(5, 6, 0)],
	6 : [MCNF_Objects_hw3.City(6, 0, 0), MCNF_Objects_hw3.City(6, 1, 0), MCNF_Objects_hw3.City(6, 2, 0), MCNF_Objects_hw3.City(6, 3, 0), MCNF_Objects_hw3.City(6, 4, 0), MCNF_Objects_hw3.City(6, 5, 0), MCNF_Objects_hw3.City(6, 6, 0)]
		}

# creating legs
# Origin, Destination, StartTime, EndTime.  EndTime will be 6 for those that are not in planning horizon.
legs = [
	MCNF_Objects_hw3.Leg(1, 4, 1, 1),
	MCNF_Objects_hw3.Leg(6, 5, 1, 1),
	MCNF_Objects_hw3.Leg(5, 1, 1, 3),
	MCNF_Objects_hw3.Leg(1, 5, 2, 3),
	MCNF_Objects_hw3.Leg(4, 3, 2, 3),
	MCNF_Objects_hw3.Leg(4, 5, 2, 2),
	MCNF_Objects_hw3.Leg(3, 4, 3, 3),
	MCNF_Objects_hw3.Leg(5, 6, 3, 1),
	MCNF_Objects_hw3.Leg(3, 5, 3, 2),
	MCNF_Objects_hw3.Leg(1, 6, 4, 3),
	MCNF_Objects_hw3.Leg(2, 4, 4, 1),
	MCNF_Objects_hw3.Leg(5, 6, 4, 1),
	MCNF_Objects_hw3.Leg(3, 5, 4, 2),
	MCNF_Objects_hw3.Leg(4, 2, 5, 1),
	MCNF_Objects_hw3.Leg(4, 5, 5, 2),
]

# setting legs for each port
for thePort in portNames:
	# finds the port(node) and then we use this reference to set inbound and outbound legs
	port = ports.get(thePort)

	# adding inbound legs (legs that will arrive this port
	inBoudList = []
	for theLeg in legs:
		if theLeg.destination.__contains__(port.portName):
			inBoudList.append(theLeg)

	# adding outbound legs
	outBoundList = []
	for theLeg in legs:
		if theLeg.origin.__contains__(port.portName):
			outBoundList.append(theLeg)

	# setting outbound and inbound legs of the node.
	port.inboundLegs = inBoudList
	port.outboundLegs = outBoundList


# Code to test that all ports have the correct legs
output = ports["New York"].inboundLegs
for out in output:
	if isinstance(out, MCNF_Objects_hw3.Leg):
		print out.origin


# Create the 'prob' object to contain the problem data
prob = LpProblem("MinCost Network Flow", LpMinimize)

# Decision variables
# Build arc flow variables for each arc, lower bounds = 0

for leg in legs:
	if isinstance(leg, MCNF_Objects_hw3.Leg):
		var = LpVariable("ArcFlow_(%s,%s)" % (leg.origin, leg.destination), 0, leg.emptyCap)
		leg.arcFlow = var


# The objective function is added to 'prob' first
prob += lpSum(legs[i].cost * legs[i].arcFlow for i in range(len(legs))), "Total Cost"


for portName in ports:
	port = ports.get(portName)
	if isinstance(port, MCNF_Objects_hw3.City):
		totalInbound = 0
		totalOutbound = 0
		for inbound in port.inboundLegs:
			if isinstance(inbound, MCNF_Objects_hw3.Leg):
				totalInbound += inbound.arcFlow
		for outbound in port.outboundLegs:
			if isinstance(outbound, MCNF_Objects_hw3.Leg):
				totalOutbound += outbound.arcFlow
	# adding the constraint
	prob += lpSum(leg.arcFlow for leg in port.outboundLegs) - lpSum(leg.arcFlow for leg in port.inboundLegs) == port.demand, "Port of %s Balance" % port.portName

# Write out as a .LP file
prob.writeLP("MinCostFlow.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve(GUROBI())

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
	print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen
print "Total Cost = ", value(prob.objective)
