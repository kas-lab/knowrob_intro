#!/usr/bin/env python

import roslib; roslib.load_manifest('rosprolog')

import rospy
from rosprolog_client import PrologException, Prolog

if __name__ == '__main__':
    rospy.init_node('example_query_owl')
    prolog = Prolog()
    # prolog.once("tripledb_forget(_,_,_).") # clean DB before starting
    # load example.owl in the knowrob database to access its content
    prolog.once("load_owl('package://krr_example/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).")


    # query if there is an individual R of type Robot in the ontology
    query = prolog.query("instance_of(X, pap:'Milk')")
    print(query.solutions)
    for solution in query.solutions():
        print("Solution", solution)
        print("End")

    query.finish()


