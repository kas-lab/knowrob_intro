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

#     pose_list = list(solution[0].split(", "))
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

# ADD HERE YOUR QUERY to get a list with all refrigerated tables--------
query = pq.prolog_query("instance_of(X, pap:'RefrigeratedTable').")
print("Refrigerated tables: ")
refrig_tables = pq.get_all_solutions(query)
#---------------------------------------------------------------------------

for refrig_table in refrig_tables: # go through all refrigerated tables
    # get pose
    pose_refrig = table_pose(refrig_table)
    # get products
    products_ref = products_in_table(refrig_table)


print("\n------------------PART 2: Searching for all non-refrigerated tables ------------------------------\n")

# ADD HERE YOUR QUERY to get a list with all non-refrigerated tables-------------
query = pq.prolog_query("instance_of(X, soma:'Table'), \+(instance_of(X, pap:'RefrigeratedTable')).")
print("Non-refrigerated tables: ")
tables = pq.get_all_solutions(query)
# -----------------------------------------------------------------------------------

for table in tables: # go through all tables
    # get pose
    pose_tb = table_pose(table)
    # get products
    products_ref = products_in_table(table)

print("\n------------------PART 5: check if the object is graspable ------------------------------\n")

#  ADD HERE YOUR FUNCTION to check if a product is graspable
def check_graspable(product):
        # mass of the product
        string_query = "triple(pap:'" + str(product) +"', soma:'hasMassAttribute', X)."
        query = pq.prolog_query(string_query)
        mass_indiv = pq.get_all_solutions(query, False)
        string_query = "triple(pap:'" + str(mass_indiv[0]) +"', soma:'hasMassValue', X)."
        query = pq.prolog_query(string_query)
        # print("Mass value of product {}: ".format(product))
        mass_value = pq.get_all_solutions(query, False)
        # joint effort limit
        string_query = "instance_of(X, soma:'Gripper')."
        query = pq.prolog_query(string_query)
        #print("Available gripper:")
        gripper = pq.get_all_solutions(query, False)

        string_query = "triple(pap:'" + str(gripper[0]) +"_joint', soma:'hasJointLimit', X)."
        query = pq.prolog_query(string_query)
        joint_limit_ind = pq.get_all_solutions(query, False)

        string_query = "triple(pap:'" + str(joint_limit_ind[0]) +"', soma:'hasJointEffortLimit', X)."
        query = pq.prolog_query(string_query)
        #print("Joint effort limit {}: ".format(joint_limit_ind[0]))
        joint_limit_value = pq.get_all_solutions(query, False)

        # if mass  > joint limit, object not graspable
        if float(mass_value[0]) > float(joint_limit_value[0]):
            print(("ERROR product {} not graspable\n").format(product))
            return False
        else:
            print(("Product {} graspable\n").format(product))
            return True

print("\n------------------PART 3: Searching for perishable products in table_1 ------------------------------\n")

#  ADD HERE YOUR QUERY to get a list with all perishable products in table_1
products_to_move={}
string_query = "triple(X, dul:'hasLocation', pap:'table_1')."
query = pq.prolog_query(string_query)
print("Products in table_1")
products_t1 = pq.get_all_solutions(query)
for product in products_t1:
    string_query = "instance_of(pap:'" + str(product) +"', pap:'Perishable')."
    query = pq.prolog_query(string_query)
    print(("{} is Perishable: ").format(product))
    perishable = pq.get_all_solutions(query)

    if perishable[0] == 'false': # products non perishable in regrigerated table
        # the product needs to move, check if object is graspable
        #  PART5: add the check product graspable
        grasp = check_graspable(product)
        if grasp == True:
        # store product to move to a non refrigerated table 
            products_to_move[product] = tables[0] # move non-perishable product to the first(index [0]) non refrigerated table

print("\n------------------PART 4: Searching for non-perishable products in table ------------------------------\n")
#  ADD HERE YOUR QUERY to get a list with all non-perishable products in table
string_query = "triple(X, dul:'hasLocation', pap:'table')."
query = pq.prolog_query(string_query)
print("Products in table")
products_t = pq.get_all_solutions(query)
for product in products_t:
    string_query = "instance_of(pap:'" + str(product) +"', pap:'Perishable')."
    query = pq.prolog_query(string_query)
    print(("{} is Perishable: ").format(product))
    perishable = pq.get_all_solutions(query)

    if perishable[0] == 'true': # products not in the correct table
        # the product needs to move, check if object is graspable
        #  PART5: add the check product graspable
        grasp = check_graspable(product)
        if grasp == True:
            # store product to move    
            products_to_move[product] = refrig_tables[0] # move perishable product to the first refrigerated table


print("\n------------------PART 6: Print required actions to move products to the correct table destinations ------------------------------\n")
#  ADD HERE YOUR CODE 
for k,v in products_to_move.items():
    print("Moving product {} to {}".format(k, v))
