"""
A Standard MinCost Network Flow Problem, Modified for Container Repositioning

This version keeps all information in the header of this file
Has no ability to read data files

Authors: Alan Erera 2013
"""

# Import PuLP modeler functions
from pulp import *

# Data Section

# Create a list of the nodes
Nodes = ['A', 'B', 'C', 'D', 'E']

# Dictionary of node demands
b     = {    'A' : -60, 
             'B' : 85, 
             'C' : -5, 
             'D' : -80,
	     'E' : 60
	 }

# Create arcs as list of duples
Arcs =  (	('A','B') ,
		('B','C') ,
		('C','A') ,
		('A','C') ,
		('C','D') ,
		('D','A') ,
		('A','D') ,
		('D','E') ,
		('E','B') ,
		('B','A') ,
		('B','E') ,
		('E','D') ,
		('D','C') ,
		('C','B')
	)

# List of arc costs
Cost = 	( 50 ,
	  40 ,
	  20 ,
	  20 ,
	  30 ,
	  40 ,
	  50 ,
	  20 ,
	  10 ,
	  50 ,
	  40 ,
	  80 ,
	  50 ,
	  80
 	) 

# List of arc upper bounds
UpperBound = 	( 	50 ,
			105 ,
			90 ,
			100 ,
			60 ,
			60 ,
			30,
			50 ,
			40 ,
			90 ,
			150 ,
			220,
			120 ,
			170
 	) 

# List of arc indices
indArcs = range(len(Arcs))

# Create the 'prob' object to contain the problem data
prob = LpProblem("MinCost Network Flow", LpMinimize)

# Decision variables
# Build arc flow variables for each arc, lower bounds = 0
arc_flow = []
for a in indArcs:
        # Format for LpVariable("Name",Lowerbound)
	var = LpVariable("ArcFlow_(%s,%s)" % (str(Arcs[a][0]),str(Arcs[a][1])), 0)
	arc_flow.append(var)

# The objective function is added to 'prob' first
prob += lpSum([Cost[a]*arc_flow[a] for a in indArcs]), "Total Cost"

# Generate a flow balance constraints for each node
# Option 1
for i in Nodes:
	# One option:  build a set of outbound and inbound arcs for each node as needed
	# Initialize empty lists of out and inArcs
	outArcs = []
	inArcs = []
	for a in indArcs:
		# Write code to check if the arc a goes into node i, or out of node i, and append node to the list
	prob += lpSum([arc_flow[a] for a in outArcs]) - lpSum([arc_flow[a] for a in inArcs]) == b[i], "Node %s Balance" % str(i)

# Option 2
# Create lists of out and inArcs for each node using a dictionary form
outArcs = {}
inArcs = {}
for i in Nodes:
	outArcs[i] = []
	inArcs[i] = []
for a in indArcs:
	outArcs[Arcs[a][0]].append(a)
	inArcs[Arcs[a][1]].append(a)
# Now use these lists in your constraint
for i in Nodes:
	prob += lpSum([arc_flow[a] for a in outArcs[i]) - ...
	

# Generate a flow upper bound for each arc
for a in indArcs:
	prob += arc_flow[a] <= UpperBound[a], "Arc %s (%s,%s) Upper Bound" % (str(a),str(Arcs[a][0]),str(Arcs[a][1]))

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
