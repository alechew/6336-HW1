"""
A Standard MinCost Network Flow Problem, Modified for Container Repositioning

This version keeps all information in the header of this file
Has no ability to read data files

Authors: Alan Erera 2013
"""

# Import PuLP modeler functions
from pulp import *
import MCNF_Objects

# Data Section

# Create a list of the nodes
Nodes = ['A', 'B', 'C', 'D', 'E']

# # Dictionary of node demands
# b     = {    'A' : -60,
#              'B' : 85,
#              'C' : -5,
#              'D' : -80,
# 	     'E' : 60
# 	 }
portNames = ["New York", "Savannah", "Rotterdam", "Giao Tauro", "Dubai", "Singapore", "Shanghai", "Busan", "Seattle", "Los Angeles"]

# net flow of empty containers. -flow means that the port is lacking empty containers to load and send.
ports = {   "New York" : MCNF_Objects.Port("New York", 1220),
			"Savannah" : MCNF_Objects.Port("Savannah", 2210),
			"Rotterdam" : MCNF_Objects.Port("Rotterdam", 150),
			"Giao Tauro" : MCNF_Objects.Port("Giao Tauro", 360),
			"Dubai" : MCNF_Objects.Port("Dubai", 2025),
			"Singapore" : MCNF_Objects.Port("Singapore", -1970),
			"Shanghai" : MCNF_Objects.Port("Shanghai", -5040),
			"Busan" : MCNF_Objects.Port("Busan", -1750),
			"Seattle" : MCNF_Objects.Port("Seattle", 575),
			"Los Angeles" : MCNF_Objects.Port("Los Angeles", 2220)
		}

# creating legs
legs = [
MCNF_Objects.Leg(1, "Savannah", "New York", 3000, 2310, 690, 200),
MCNF_Objects.Leg(1, "New York", "Rotterdam", 3000, 2450, 550, 400),
MCNF_Objects.Leg(1, "Rotterdam", "Savannah", 3000, 2835, 165, 900),

MCNF_Objects.Leg(2, "Rotterdam", "Giao Tauro", 3000, 1450, 1550, 250),
MCNF_Objects.Leg(2, "Giao Tauro", "Dubai", 3000, 1560, 1440, 450),
MCNF_Objects.Leg(2, "Dubai", "Giao Tauro", 3000, 2905, 95, 1000),
MCNF_Objects.Leg(2, "Giao Tauro", "Rotterdam", 3000, 2435, 565, 600),


MCNF_Objects.Leg(3, "Shanghai", "Singapore", 4000, 3950, 50, 800),
MCNF_Objects.Leg(3, "Singapore", "Dubai", 4000, 3600, 400, 1100),
MCNF_Objects.Leg(3, "Dubai", "Singapore", 4000, 900, 3100, 300),
MCNF_Objects.Leg(3, "Singapore", "Shanghai", 4000, 1485, 2515, 300),

MCNF_Objects.Leg(4, "Singapore", "Busan", 4400, 3295, 1105, 500),
MCNF_Objects.Leg(4, "Busan", "Seattle", 4400, 4355, 45, 1100),
MCNF_Objects.Leg(4, "Seattle", "Los Angeles", 4400, 3600, 800, 500),
MCNF_Objects.Leg(4, "Los Angeles", "Singapore", 4400, 1750, 2650, 600),

MCNF_Objects.Leg(5, "Shanghai", "Seattle", 3750, 3550, 200, 1300),
MCNF_Objects.Leg(5, "Seattle", "Los Angeles", 3750, 3730, 20, 500),
MCNF_Objects.Leg(5, "Los Angeles", "Shanghai", 3750, 3360, 390, 900),

MCNF_Objects.Leg(6, "Singapore", "Busan", 2500, 1510, 990, 500),
MCNF_Objects.Leg(6, "Busan", "Savannah", 2500, 2200, 300, 1400),
MCNF_Objects.Leg(6, "Savannah", "New York", 2500, 1300, 1200, 300),
MCNF_Objects.Leg(6, "New York", "Rotterdam", 2500, 1540, 960, 400),
MCNF_Objects.Leg(6, "Rotterdam", "Dubai", 2500, 1990, 510, 500),
MCNF_Objects.Leg(6, "Dubai", "Singapore", 2500, 1320, 1180, 800),

MCNF_Objects.Leg(7, "Shanghai", "Savannah", 2900, 2880, 20, 1500),
MCNF_Objects.Leg(7, "Savannah", "New York", 2900, 1680, 1220, 300),
MCNF_Objects.Leg(7, "New York", "Savannah", 2900, 80, 2820, 200),
MCNF_Objects.Leg(7, "Savannah", "Shanghai", 2900, 495, 2405, 600)
]

# setting legs for each port
for thePort in portNames:
	# finds the port(node) and then we use this reference to set inbound and outbound legs
	port = ports.get(thePort)

	# adding inbound legs (legs that will arrive this port
	inBoudList = []
	for theLeg in legs:
		if theLeg.destination == port.portName:
			inBoudList.append(theLeg)

	# adding outbound legs
	outBoundList = []
	for theLeg in legs:
		if theLeg.origin == port.portName:
			outBoundList.append(theLeg)

	# setting outbound and inbound legs of the node.
	port.inboundLegs = inBoudList
	port.outboundLegs = outBoundList




# Code to test that all ports have the correct legs
output = ports["Seattle"].inboundLegs
for out in output:
	if isinstance(out, MCNF_Objects.Leg):
		print out.origin



# # Create arcs as list of duples
# Arcs =  (	('A','B') ,
# 		('B','C') ,
# 		('C','A') ,
# 		('A','C') ,
# 		('C','D') ,
# 		('D','A') ,
# 		('A','D') ,
# 		('D','E') ,
# 		('E','B') ,
# 		('B','A') ,
# 		('B','E') ,
# 		('E','D') ,
# 		('D','C') ,
# 		('C','B')
# 	)
#
# # List of arc costs
# Cost = 	( 50 ,
# 	  40 ,
# 	  20 ,
# 	  20 ,
# 	  30 ,
# 	  40 ,
# 	  50 ,
# 	  20 ,
# 	  10 ,
# 	  50 ,
# 	  40 ,
# 	  80 ,
# 	  50 ,
# 	  80
#  	)
#
# # List of arc upper bounds
# UpperBound = 	( 	50 ,
# 			105 ,
# 			90 ,
# 			100 ,
# 			60 ,
# 			60 ,
# 			30,
# 			50 ,
# 			40 ,
# 			90 ,
# 			150 ,
# 			220,
# 			120 ,
# 			170
#  	)
#
# # List of arc indices
# indArcs = range(len(Arcs))
#
# # Create the 'prob' object to contain the problem data
# prob = LpProblem("MinCost Network Flow", LpMinimize)
#
# # Decision variables
# # Build arc flow variables for each arc, lower bounds = 0
# arc_flow = []
# for a in indArcs:
#         # Format for LpVariable("Name",Lowerbound)
# 	var = LpVariable("ArcFlow_(%s,%s)" % (str(Arcs[a][0]),str(Arcs[a][1])), 0)
# 	arc_flow.append(var)
#
# # The objective function is added to 'prob' first
# prob += lpSum([Cost[a]*arc_flow[a] for a in indArcs]), "Total Cost"
#
# # Generate a flow balance constraints for each node
# # Option 1
# for i in Nodes:
# 	# One option:  build a set of outbound and inbound arcs for each node as needed
# 	# Initialize empty lists of out and inArcs
# 	outArcs = []
# 	inArcs = []
# 	for a in indArcs:
# 		# Write code to check if the arc a goes into node i, or out of node i, and append node to the list
# 	prob += lpSum([arc_flow[a] for a in outArcs]) - lpSum([arc_flow[a] for a in inArcs]) == b[i], "Node %s Balance" % str(i)
#
# # Option 2
# # Create lists of out and inArcs for each node using a dictionary form
# outArcs = {}
# inArcs = {}
# for i in Nodes:
# 	outArcs[i] = []
# 	inArcs[i] = []
# for a in indArcs:
# 	outArcs[Arcs[a][0]].append(a)
# 	inArcs[Arcs[a][1]].append(a)
# # Now use these lists in your constraint
# for i in Nodes:
# 	prob += lpSum([arc_flow[a] for a in outArcs[i]) - ...
#
#
# # Generate a flow upper bound for each arc
# for a in indArcs:
# 	prob += arc_flow[a] <= UpperBound[a], "Arc %s (%s,%s) Upper Bound" % (str(a),str(Arcs[a][0]),str(Arcs[a][1]))
#
# # Write out as a .LP file
# prob.writeLP("MinCostFlow.lp")
#
# # The problem is solved using PuLP's choice of Solver
# prob.solve(GUROBI())
#
# # The status of the solution is printed to the screen
# print "Status:", LpStatus[prob.status]
#
# # Each of the variables is printed with it's resolved optimum value
# for v in prob.variables():
#     print v.name, "=", v.varValue
#
# # The optimised objective function value is printed to the screen
# print "Total Cost = ", value(prob.objective)
