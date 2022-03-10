#!/usr/bin/env python

import roslib; roslib.load_manifest('rosprolog')

import rospy
from rosprolog_client import PrologException, Prolog

class PQ(object):
    def __init__(self):
        self.prolog = Prolog()
        self.predicates = []
        self.load_namespace()
        self.load_all_predicates()

    def load_namespace(self):
        q = 'findall([_X, _Y], rdf_current_ns(_X, _Y), NS)'
        solution = self.prolog.once(q)
        print('namespaces:')
        for ns in solution['NS']:
            print('{}: {}'.format(ns[0], ns[1]))
        print('-----------')

    def remove_namespace(self, value):  #
        q = 'findall([_X, _Y], rdf_current_ns(_X, _Y), NS)'
        solution = self.prolog.once(q)
        for ns in solution['NS']:
            if ns[1] in value:
                value_new = value.replace(ns[1], '')
                solution_short = {ns[0]: value_new}
                return solution_short
    

    def load_all_predicates(self):
        q = 'findall(X, current_predicate(X/_);current_module(X), L)'
        solution = self.prolog.once(q)
        self.predicates = [str(x) for x in solution['L']]
    

    def prolog_query(self, q):
        query = self.prolog.query(q)
        solutions = [x for x in query.solutions()]
        query.finish()
        #self.print_all_solutions(solutions)
        return solutions

    def print_all_solutions(self, solutions):
        if len(solutions) == 0:
            print('false.')
        else:
            for s in solutions:
                if s == dict(): # if query result is an empty dict
                    print('true.')
                else:
                    for k, v in s.items():
                        rv = self.remove_namespace(v) # isolate namespace and name
                        print('{} : {}:{}'.format(k, rv.keys()[0], rv.values()[0]))
        print # end with new line

if __name__ == '__main__':
    rospy.init_node('example_query_owl')
    pq = PQ()
    
    # load example.owl in the knowrob database to access its content
    query = pq.prolog_query("load_owl('package://krr_example/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).")
    
    query = pq.prolog_query("instance_of(X, pap:'Milk').")
    print("Instances of Milk:")
    pq.print_all_solutions(query)


    query = pq.prolog_query("has_domain(soma:'hasMassValue',X).")
    print("Individuals with mass value:")
    pq.print_all_solutions(query)

    query = pq.prolog_query("triple(pap:'milk_product_2', soma:hasMassAttribute, X)")
    print("Mass attribute of milk product 2:")
    pq.print_all_solutions(query)



