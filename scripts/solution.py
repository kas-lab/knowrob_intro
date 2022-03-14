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

# def query_pose_transform(solution):
#     """Convert pose string into pose goal object.
#     """
#     pose_goal = geometry_msgs.msg.Pose()

#     pose_list = list(solution[0][1].split(", "))
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

query = pq.prolog_query("instance_of(X, pap:'RefrigeratedTable').")
print("Refrigerated tables: ")
refrig_tables = pq.get_all_solutions(query) # format: [(namespace, name_value)], to access
                                           # to the name value, refrig_table[0][1], if there are
                                           # more than one, regrig_table[i][1], being 
                                           # i = 0, 1, 2, ..., n individuals results
                                           # or access the tuple through a for loop and use element[1]
for refrig_table in refrig_tables: # go through all refrigerated tables
    # get pose
    pose_refrig = table_pose(refrig_table[1])
    # get products
    products_ref = products_in_table(refrig_table[1])


print("\n------------------PART 2: Searching for all non-refrigerated tables ------------------------------\n")


# Get non-refrigerated tables
query = pq.prolog_query("instance_of(X, soma:'Table'), not(instance_of(X, pap:'RefrigeratedTable')).")
print("Non-refrigerated tables: ")
tables = pq.get_all_solutions(query)
pose_tables = {} # dictionary to store table: pose
product_tables = {} # dictionary to store table:product

for table in tables: # go through all tables
    # get pose
    pose_tb = table_pose(table[1])
    pose_tables[table[1]] = pose_tb
    # get products
    products_ref = products_in_table(table[1])
    product_tables[table[1]] = products_ref





# Are they in the correct pose? 
# a/perishable in table
print("---------------------Checking perishables ----------")
for prd_tb1 in products_tb1:

    string_query = "instance_of(pap:'" + str(prd_tb1[1]) +"', pap:'Perishable')."
    query = pq.prolog_query(string_query)
    print(("{} is Perishable: ").format(prd_tb1[1]))
    perishable = pq.get_all_solutions(query)

    if perishable[0][0] == 'false': # products not in the correct table
        # the product needs to move, check if object is graspable
        grasp = check_graspable(prd_tb1[1])
        if grasp == True:
            # store product to move    
            move_product[prd_tb1[1]] = tables[0][1] # move non-perishable product to the first non refrigerated table

# b/ non-perishable table or table 0
print("--------------------Checking not perishables ----------")
for prd_tb in products_tb:
    string_query = "not(instance_of(pap:'" + str(prd_tb[1]) +"', pap:'Perishable'))."
    query = pq.prolog_query(string_query)
    print(("{} is not Perishable: ").format(prd_tb[1]))
    not_perishable = pq.get_all_solutions(query)

    if not_perishable[0][0] == 'false': # products not in the correct table
        # the product needs to move, check if object is graspable
        grasp = check_graspable(prd_tb[1])
        if grasp == True:
            # store product to move    
            move_product[prd_tb[1]] = refrig_table[0][1] # move non-perishable product to the first non refrigerated table

for k,v in move_product.items():
    print("Moving product {} to {}".format(k, v))
