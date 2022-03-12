#!/usr/bin/env python

import roslib; roslib.load_manifest('rosprolog')
import rospy
from knowrob_intro.prolog_query import PrologQuery


#--------------- INITIALIZE node, quering class and database ------------------------

rospy.init_node('example_query_owl') # initialize node
pq = PrologQuery() # create a prolog query class instance

 # clean DB before starting, this removes values from previous uses
print("Cleaning database...")
pq.prolog_query("kb_unproject(_).")

# load example.owl in the knowrob database to access its content
query = pq.prolog_query("load_owl('package://knowrob_intro/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).")
    
#------------------------------------------------------------------------------------

# Quering examples

# (Find) all instances of milk
query = pq.prolog_query("instance_of(X, pap:'Milk').")
print("Instances of Milk:")
pq.get_all_solutions(query)


# (Find) all classes that are domain of has mass value property
query = pq.prolog_query("has_domain(soma:'hasMassValue',X).")
print("Individuals with mass value:")
pq.get_all_solutions(query)

# (Find) which individuals are mass attribute of milk product 1
query = pq.prolog_query("holds(pap:'milk_product_1', soma:hasMassAttribute, X)")
print("Mass attribute of milk product 1:")
pq.get_all_solutions(query)

