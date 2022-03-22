#!/usr/bin/env python

import roslib; roslib.load_manifest('rosprolog')

import rospy
from rosprolog_client import PrologException, Prolog
from knowrob_intro.prolog_query import PrologQuery

if __name__ == '__main__':
    rospy.init_node('example_exercise_prolog_kb')
    prolog = Prolog()
    query = prolog.query("perishable(X), location(X,Y,_)")
    print query
    for solution in query.solutions():
        print 'Found solution. Product: %s, Location: %s' % (solution['X'], solution['Y'])
    query.finish()