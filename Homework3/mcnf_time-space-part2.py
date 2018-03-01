"""
A Standard MinCost Network Flow Problem, Modified for Container Repositioning

This version keeps all information in the header of this file
Has no ability to read data files

Authors: Alan Erera 2013
"""

# Import PuLP modeler functions
from pulp import *
import MCNF_Objects_hw3_lowerbound

terminalNames = [0, 1, 2, 3, 4, 5, 6, 7]

#  0 is source and 7 is sink
# name, time, net supplies
terminals = {
	0 : [MCNF_Objects_hw3_lowerbound.City("0", 0, 0)],
	1 : [MCNF_Objects_hw3_lowerbound.City("1", 1, 4), MCNF_Objects_hw3_lowerbound.City("1", 2, 0), MCNF_Objects_hw3_lowerbound.City("1", 3, 0), MCNF_Objects_hw3_lowerbound.City("1", 4, 0), MCNF_Objects_hw3_lowerbound.City("1", 5, 0)],
	2 : [MCNF_Objects_hw3_lowerbound.City("2", 1, 3), MCNF_Objects_hw3_lowerbound.City("2", 2, 0), MCNF_Objects_hw3_lowerbound.City("2", 3, 0), MCNF_Objects_hw3_lowerbound.City("2", 4, 0), MCNF_Objects_hw3_lowerbound.City("2", 5, 0)],
	3 : [MCNF_Objects_hw3_lowerbound.City("3", 1, 11), MCNF_Objects_hw3_lowerbound.City("3", 2, 0), MCNF_Objects_hw3_lowerbound.City("3", 3, 0), MCNF_Objects_hw3_lowerbound.City("3", 4, 0), MCNF_Objects_hw3_lowerbound.City("3", 5, 0)],
	4 : [MCNF_Objects_hw3_lowerbound.City("4", 1, 3), MCNF_Objects_hw3_lowerbound.City("4", 2, 0), MCNF_Objects_hw3_lowerbound.City("4", 3, 0), MCNF_Objects_hw3_lowerbound.City("4", 4, 0), MCNF_Objects_hw3_lowerbound.City("4", 5, 0)],
	5 : [MCNF_Objects_hw3_lowerbound.City("5", 1, 3), MCNF_Objects_hw3_lowerbound.City("5", 2, 0), MCNF_Objects_hw3_lowerbound.City("5", 3, 0), MCNF_Objects_hw3_lowerbound.City("5", 4, 0), MCNF_Objects_hw3_lowerbound.City("5", 5, 0)],
	6 : [MCNF_Objects_hw3_lowerbound.City("6", 1, 2), MCNF_Objects_hw3_lowerbound.City("6", 2, 0), MCNF_Objects_hw3_lowerbound.City("6", 3, 0), MCNF_Objects_hw3_lowerbound.City("6", 4, 0), MCNF_Objects_hw3_lowerbound.City("6", 5, 0)],
	7 : [MCNF_Objects_hw3_lowerbound.City("7", 6, -26)]
		}

# creating legs
# Origin, Destination, StartTime, duration, cost.  EndTime will be 6 for those that are not in planning horizon.
legs = [
	MCNF_Objects_hw3_lowerbound.Leg("1", "4", 1, 1, 1, 3),
	MCNF_Objects_hw3_lowerbound.Leg("6", "5", 1, 1, 1, 2),
	MCNF_Objects_hw3_lowerbound.Leg("5", "1", 1, 3, 3, 1),
	MCNF_Objects_hw3_lowerbound.Leg("1", "5", 2, 3, 3, 1),
	MCNF_Objects_hw3_lowerbound.Leg("4", "3", 2, 3, 3, 3),
	MCNF_Objects_hw3_lowerbound.Leg("4", "5", 2, 2, 2, 2),
	MCNF_Objects_hw3_lowerbound.Leg("3", "4", 3, 3, 3, 5),
	MCNF_Objects_hw3_lowerbound.Leg("5", "6", 3, 1, 1, 4),
	MCNF_Objects_hw3_lowerbound.Leg("3", "5", 3, 2, 2, 3),
	MCNF_Objects_hw3_lowerbound.Leg("1", "6", 4, 3, 3, 1),		# 10
	MCNF_Objects_hw3_lowerbound.Leg("2", "4", 4, 1, 1, 3),
	MCNF_Objects_hw3_lowerbound.Leg("5", "6", 4, 1, 1, 2),
	MCNF_Objects_hw3_lowerbound.Leg("3", "5", 4, 2, 2, 3),
	MCNF_Objects_hw3_lowerbound.Leg("4", "2", 5, 1, 1, 1),
	MCNF_Objects_hw3_lowerbound.Leg("4", "5", 5, 2, 2, 3),		# 14
	MCNF_Objects_hw3_lowerbound.Leg("1", "1", 1, 1, 0, 0),# inventory arcs
	MCNF_Objects_hw3_lowerbound.Leg("1", "1", 2, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("1", "1", 3, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("1", "1", 4, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("1", "1", 5, 1, 0, 0),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3_lowerbound.Leg("2", "2", 1, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("2", "2", 2, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("2", "2", 3, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("2", "2", 4, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("2", "2", 5, 1, 0, 0),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3_lowerbound.Leg("3", "3", 1, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("3", "3", 2, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("3", "3", 3, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("3", "3", 4, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("3", "3", 5, 1, 0, 0),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3_lowerbound.Leg("4", "4", 1, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("4", "4", 2, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("4", "4", 3, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("4", "4", 4, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("4", "4", 5, 1, 0, 0),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3_lowerbound.Leg("5", "5", 1, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("5", "5", 2, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("5", "5", 3, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("5", "5", 4, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("5", "5", 5, 1, 0, 0),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3_lowerbound.Leg("6", "6", 1, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("6", "6", 2, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("6", "6", 3, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("6", "6", 4, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("6", "6", 5, 1, 0, 0),		# this are the inventory arcs that goes to sink
	MCNF_Objects_hw3_lowerbound.Leg("0", "1", 0, 1, 0, 0),		# source - terminal arcs #7 3 11 0 3 2
	MCNF_Objects_hw3_lowerbound.Leg("0", "2", 0, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("0", "3", 0, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("0", "4", 0, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("0", "5", 0, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("0", "6", 0, 1, 0, 0),
	MCNF_Objects_hw3_lowerbound.Leg("0", "7", 0, 6, 0, 0) 		# drain
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
			if isinstance(terminalAndTime, MCNF_Objects_hw3_lowerbound.City):
				if theLeg.destination.__contains__(terminalAndTime.portName) and theLeg.end == terminalAndTime.time:
					inBoundList.append(theLeg)

				elif theLeg.end >= 6 and terminalAndTime.portName == "7":
					inBoundList.append(theLeg)

		terminalAndTime.inboundLegs = inBoundList

		# adding outbound legs
		for theLeg in legs:
			if isinstance(terminalAndTime, MCNF_Objects_hw3_lowerbound.City):
				if theLeg.origin.__contains__(terminalAndTime.portName) and theLeg.start == terminalAndTime.time:
					outBoundList.append(theLeg)

		terminalAndTime.outboundLegs = outBoundList


# Code to test that all ports have the correct legs
output = terminals[7]
for out in output:
	if isinstance(out, MCNF_Objects_hw3_lowerbound.Leg):
		print out.origin


# Create the 'prob' object to contain the problem data
prob = LpProblem("MinCost Network Flow", LpMinimize)

# Decision variables
# Build arc flow variables for each arc, lower bounds = 0

for leg in legs:
	if isinstance(leg, MCNF_Objects_hw3_lowerbound.Leg):
		var = LpVariable("ArcFlow_(%s,%s)" % (str(leg.origin) + "_" + str(leg.start), str(leg.destination) + "_" + str(leg.end)), 0)
		leg.arcFlow = var


# The objective function is added to 'prob' first
prob += lpSum(legs[i].cost * legs[i].arcFlow for i in range(len(legs))), "Total Cost"

for portName in terminalNames:
	terminal = terminals.get(portName)

	# #lowerbound constraints
	# for leg in legs:
	# 	prob += leg.arcFlow >= leg.demand

	for x in range(len(terminal)):
		currentTerminal = terminal[x]
		if isinstance(currentTerminal, MCNF_Objects_hw3_lowerbound.City):
			totalInbound = 0
			totalOutbound = 0

		for inbound in currentTerminal.inboundLegs:
			if isinstance(inbound, MCNF_Objects_hw3_lowerbound.Leg):
				totalInbound += inbound.arcFlow
		for outbound in currentTerminal.outboundLegs:
			if isinstance(outbound, MCNF_Objects_hw3_lowerbound.Leg):
				totalOutbound += outbound.arcFlow
				# adding the constraint
		prob += lpSum(leg.arcFlow for leg in currentTerminal.outboundLegs) - lpSum(leg.arcFlow for leg in currentTerminal.inboundLegs) == currentTerminal.supply, "Terminal %s Balance" % (str(currentTerminal.portName) + "_" + str(currentTerminal.time))

# Write out as a .LP file
prob.writeLP("MinCostFlow.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve(GUROBI())

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

totaldays = 0

# Each of the variables is printed with it's resolved optimum value
# counter = 0
for v in prob.variables():
	print v.name, "=", v.varValue
# 	totaldays = totaldays + (v.varValue * legs[counter].traveltime)
# 	counter = counter + 1
#
# print "total days = " + str(totaldays)

# The optimised objective function value is printed to the screen
print "Total Cost = ", value(prob.objective)


#7 3 11 0 3 2