#!/usr/bin/env python

import roslib; roslib.load_manifest('rosprolog')

import rospy
from knowrob_intro.prolog_query import PrologQuery

if __name__ == '__main__':
    rospy.init_node('example_situation_calculus')
    pq = PrologQuery()
    query = pq.prolog_query("location(honey,table2,S), location(hagelslag,table2,S), legal(S).")
    print("Plan to transfer the honey and the hagelslag to table 2:")
    pq.get_all_solutions(query)