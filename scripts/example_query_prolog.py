#!/usr/bin/env python

import roslib
import rospy
from knowrob_intro.prolog_query import PrologQuery

roslib.load_manifest('rosprolog')

if __name__ == '__main__':
    rospy.init_node('example_query_prolog_kb')
    pq = PrologQuery()
    query = pq.prolog_query("perishable(X), location(X,Y,_)")
    print("Perishable products (X) and locations (Y): ")
    pq.get_all_solutions(query)
