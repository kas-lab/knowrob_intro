#!/usr/bin/env python

import roslib; roslib.load_manifest('rosprolog')

import rospy
from knowrob_intro.prolog_query import PrologQuery

if __name__ == '__main__':
    rospy.init_node('example_owl_kb_prolog_rules')
    pq = PrologQuery()
    query = pq.prolog_query("transfer(X,O,D).")
    print("Transfer operations that move items (X) from their current location (O) to a correct  destination (D), according to these rules:\n perishable items to the refrigerated table, and nonperishable items to other tables:")
    pq.get_all_solutions(query)