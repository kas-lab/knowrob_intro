#!/usr/bin/env python

import roslib; roslib.load_manifest('rosprolog')
import rospy
from knowrob_intro.prolog_query import PrologQuery


#--------------- INITIALIZE node, quering class and database ------------------------

rospy.init_node('example_query_owl') # initialize node
pq = PrologQuery() # create a prolog query class instance

# load example.owl in the knowrob database to access its content
query = pq.prolog_query("load_owl('package://knowrob_intro/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).")
    
#------------------------------------------------------------------------------------

# def query_pose_transform(pose_query_result):
#     """Convert pose string into pose goal object.
#     """
#     pose_goal = geometry_msgs.msg.Pose()

#     pose_list = list(pose_query_result[0].split(", "))
#     pose = map(float, pose_list)

#     pose_goal.position.x = pose[0]
#     pose_goal.position.y = pose[1]
#     pose_goal.position.z = pose[2]
#     pose_goal.orientation.x = pose[3]
#     pose_goal.orientation.y = pose[4]
#     pose_goal.orientation.z = pose[5]
#     pose_goal.orientation.w = pose[6]

#     return pose_goal

def table_pose(table):
    string_query = "triple(pap:'"+ str(table) +"_pose', soma:'hasPositionData', Y)."
    query = pq.prolog_query(string_query)
    print("Table pose: ")
    pose = pq.get_all_solutions(query)
    # pose = query_pose_transform(pose_str)
    return pose

def products_in_table(table):
    string_query = "triple(X, dul:'hasLocation', pap:'"+ str(table) +"')."
    query = pq.prolog_query(string_query)
    print("\nProducts in {}: ".format(table))
    products_t = pq.get_all_solutions(query)
    return products_t


print("\n------------------PART 1: Searching for all refrigerated tables -------------------------------------\n")

# ADD HERE YOUR QUERY to get a list with all refrigerated tables

for refrig_table in refrig_tables: # go through all refrigerated tables
    # get pose
    pose_refrig = table_pose(refrig_table)
    # get products
    products_ref = products_in_table(refrig_table)


print("\n------------------PART 2: Searching for all non-refrigerated tables ------------------------------\n")


#  ADD HERE YOUR QUERY to get a list with all non-refrigerated tables

for table in tables: # go through all tables
    # get pose
    pose_tb = table_pose(table)
    # get products
    products_ref = products_in_table(table)


print("\n------------------PART 5: check if the object is graspable ------------------------------\n")

#  ADD HERE YOUR FUNCTION to check if a product is graspable


print("\n------------------PART 3: Searching for perishable products in table_1 ------------------------------\n")

#  ADD HERE YOUR QUERY to get a list with all perishable products in table_1

#  PART5: add the check product graspable


print("\n------------------PART 4: Searching for non-perishable products in table ------------------------------\n")

#  ADD HERE YOUR QUERY to get a list with all non-perishable products in table

#  PART5: add the check product graspable

print("\n------------------PART 6: Print required actions to move products to the correct table destinations ------------------------------\n")

#  ADD HERE YOUR CODE 
