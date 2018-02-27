"""
A Standard MinCost Network Flow Problem, Modified for Container Repositioning

This version keeps all information in the header of this file
Has no ability to read data files

Authors: Alan Erera 2013
"""

# Import PuLP modeler functions
from pulp import *
import MCNF_Objects_hw3

terminalNames = [1, 2, 3, 4, 5, 6]

#  0 is source and 7 is sink
# name, time, net supplies
terminals = {
	0 : [MCNF_Objects_hw3.City(0, 0, 100)],
	1 : [MCNF_Objects_hw3.City(1, 1, -3), MCNF_Objects_hw3.City(1, 2, -1), MCNF_Objects_hw3.City(1, 3, 0), MCNF_Objects_hw3.City(1, 4, 0), MCNF_Objects_hw3.City(1, 5, 0)],
	2 : [MCNF_Objects_hw3.City(2, 1, 0), MCNF_Objects_hw3.City(2, 2, 0), MCNF_Objects_hw3.City(2, 3, 0), MCNF_Objects_hw3.City(2, 4, -3), MCNF_Objects_hw3.City(2, 5, 0)],
	3 : [MCNF_Objects_hw3.City(3, 1, 0), MCNF_Objects_hw3.City(3, 2, 0), MCNF_Objects_hw3.City(3, 3, -8), MCNF_Objects_hw3.City(3, 4, -3), MCNF_Objects_hw3.City(3, 5, 3)],
	4 : [MCNF_Objects_hw3.City(4, 1, 0), MCNF_Objects_hw3.City(4, 2, -2), MCNF_Objects_hw3.City(4, 3, 0), MCNF_Objects_hw3.City(4, 4, 0), MCNF_Objects_hw3.City(4, 5, -1)],
	5 : [MCNF_Objects_hw3.City(5, 1, -1), MCNF_Objects_hw3.City(5, 2, 0), MCNF_Objects_hw3.City(5, 3, -4), MCNF_Objects_hw3.City(5, 4, 0), MCNF_Objects_hw3.City(5, 5, 4)],
	6 : [MCNF_Objects_hw3.City(6, 1, -2), MCNF_Objects_hw3.City(6, 2, 0), MCNF_Objects_hw3.City(6, 3, 0), MCNF_Objects_hw3.City(6, 4, 4), MCNF_Objects_hw3.City(6, 5, 2)],
	7 : [MCNF_Objects_hw3.City(7, 6, -100)]
		}

# creating legs
# Origin, Destination, StartTime, duration, cost.  EndTime will be 6 for those that are not in planning horizon.
legs = [
	MCNF_Objects_hw3.Leg(1, 4, 1, 1, 1),
	MCNF_Objects_hw3.Leg(6, 5, 1, 1, 1),
	MCNF_Objects_hw3.Leg(5, 1, 1, 3, 1),
	MCNF_Objects_hw3.Leg(1, 5, 2, 3, 1),
	MCNF_Objects_hw3.Leg(4, 3, 2, 3, 1),
	MCNF_Objects_hw3.Leg(4, 5, 2, 2, 1),
	MCNF_Objects_hw3.Leg(3, 4, 3, 3, 1),
	MCNF_Objects_hw3.Leg(5, 6, 3, 1, 1),
	MCNF_Objects_hw3.Leg(3, 5, 3, 2, 1),
	MCNF_Objects_hw3.Leg(1, 6, 4, 3, 1),
	MCNF_Objects_hw3.Leg(2, 4, 4, 1, 1),
	MCNF_Objects_hw3.Leg(5, 6, 4, 1, 1),
	MCNF_Objects_hw3.Leg(3, 5, 4, 2, 1),
	MCNF_Objects_hw3.Leg(4, 2, 5, 1, 1),
	MCNF_Objects_hw3.Leg(4, 5, 5, 2, 1),

	# inventory arcs
	MCNF_Objects_hw3.Leg(1, 1, 1, 1, 1),
	MCNF_Objects_hw3.Leg(1, 1, 2, 1, 1),
	MCNF_Objects_hw3.Leg(1, 1, 3, 1, 1),
	MCNF_Objects_hw3.Leg(1, 1, 4, 1, 1),
	MCNF_Objects_hw3.Leg(1, 1, 5, 1, 1),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3.Leg(2, 2, 1, 1, 1),
	MCNF_Objects_hw3.Leg(2, 2, 2, 1, 1),
	MCNF_Objects_hw3.Leg(2, 2, 3, 1, 1),
	MCNF_Objects_hw3.Leg(2, 2, 4, 1, 1),
	MCNF_Objects_hw3.Leg(2, 2, 5, 1, 1),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3.Leg(3, 3, 1, 1, 1),
	MCNF_Objects_hw3.Leg(3, 3, 2, 1, 1),
	MCNF_Objects_hw3.Leg(3, 3, 3, 1, 1),
	MCNF_Objects_hw3.Leg(3, 3, 4, 1, 1),
	MCNF_Objects_hw3.Leg(3, 3, 5, 1, 1),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3.Leg(4, 4, 1, 1, 1),
	MCNF_Objects_hw3.Leg(4, 4, 2, 1, 1),
	MCNF_Objects_hw3.Leg(4, 4, 3, 1, 1),
	MCNF_Objects_hw3.Leg(4, 4, 4, 1, 1),
	MCNF_Objects_hw3.Leg(4, 4, 5, 1, 1),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3.Leg(5, 5, 1, 1, 1),
	MCNF_Objects_hw3.Leg(5, 5, 2, 1, 1),
	MCNF_Objects_hw3.Leg(5, 5, 3, 1, 1),
	MCNF_Objects_hw3.Leg(5, 5, 4, 1, 1),
	MCNF_Objects_hw3.Leg(5, 5, 5, 1, 1),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3.Leg(6, 6, 1, 1, 1),
	MCNF_Objects_hw3.Leg(6, 6, 2, 1, 1),
	MCNF_Objects_hw3.Leg(6, 6, 3, 1, 1),
	MCNF_Objects_hw3.Leg(6, 6, 4, 1, 1),
	MCNF_Objects_hw3.Leg(6, 6, 5, 1, 1),		# this are the inventory arcs that goes to sink

	# adding source arc
	MCNF_Objects_hw3.Leg(0, 1, 0, 1, 1),
	MCNF_Objects_hw3.Leg(0, 2, 0, 1, 1),
	MCNF_Objects_hw3.Leg(0, 3, 0, 1, 1),
	MCNF_Objects_hw3.Leg(0, 4, 0, 1, 1),
	MCNF_Objects_hw3.Leg(0, 5, 0, 1, 1),

	#adding drain
	MCNF_Objects_hw3.Leg(0, 7, 0, 6, 0)
]

# setting legs for each port
for theTerminal in terminalNames:
	# finds the terminal(node) and then we use this reference
	# to set inbound and outbound legs for the specified time period
	terminal = terminals.get(theTerminal)

	for x in range(len(terminal)):
		# adding inbound legs (legs that will arrive this terminal
		terminalAndTime = terminal[x]
		inBoundList = []
		outBoundList = []

		# for loop to add the legs going to sink only
		for theLeg in legs:
			if theLeg.end >= 6:
				terminals.get(7)[0].inboundLegs.append(theLeg)

		for theLeg in legs:
			if isinstance(terminalAndTime, MCNF_Objects_hw3.City):
				if theLeg.destination == terminalAndTime.portName and theLeg.end == terminalAndTime.time:
					inBoundList.append(theLeg)
		terminalAndTime.inboundLegs = inBoundList

		# adding outbound legs
		for theLeg in legs:
			if isinstance(terminalAndTime, MCNF_Objects_hw3.City):
				if theLeg.origin == terminalAndTime.portName and theLeg.start == terminalAndTime.time:
					outBoundList.append(theLeg)

		terminalAndTime.outboundLegs = outBoundList


# Code to test that all ports have the correct legs
output = terminals[1]
for out in output:
	if isinstance(out, MCNF_Objects_hw3.Leg):
		print out.origin


# Create the 'prob' object to contain the problem data
prob = LpProblem("MinCost Network Flow", LpMinimize)

# Decision variables
# Build arc flow variables for each arc, lower bounds = 0

for leg in legs:
	if isinstance(leg, MCNF_Objects_hw3.Leg):
		var = LpVariable("ArcFlow_(%s,%s)" % (leg.origin, leg.destination),0)
		leg.arcFlow = var


# The objective function is added to 'prob' first
prob += lpSum(legs[i].cost * legs[i].arcFlow for i in range(len(legs))), "Total Cost"

for portName in terminalNames:
	terminal = terminals.get(portName)

	for x in range(len(terminal)):
		currentTerminal = terminal[x]
		if isinstance(currentTerminal, MCNF_Objects_hw3.City):
			totalInbound = 0
			totalOutbound = 0

		for inbound in currentTerminal.inboundLegs:
			if isinstance(inbound, MCNF_Objects_hw3.Leg):
				totalInbound += inbound.arcFlow
		for outbound in currentTerminal.outboundLegs:
			if isinstance(outbound, MCNF_Objects_hw3.Leg):
				totalOutbound += outbound.arcFlow
				# adding the constraint
		prob += lpSum(leg.arcFlow for leg in currentTerminal.outboundLegs) - lpSum(leg.arcFlow for leg in currentTerminal.inboundLegs) == currentTerminal.supply, "Port of %s Balance" % currentTerminal.portName

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
