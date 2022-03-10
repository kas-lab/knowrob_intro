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
                solution_formated = (ns[0], value_new) # tuple namespace, individual
                return solution_formated
    
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
        rv = dict()
        if len(solutions) == 0:
            print('false.')
        else:
            for s in solutions:
                if s == dict(): # if query result is an empty dict
                    print('true.')
                else:
                    for k, v in s.items():
                        rv = self.remove_namespace(v) # isolate namespace and name
                        print('{} : {}:{}'.format(k, rv[0], rv[1]))
        print # end with new line
        return rv

if __name__ == '__main__':
    rospy.init_node('example_query_owl')
    pq = PQ()
    print("Cleaning database...")
    pq.prolog_query("kb_unproject(_).") # clean DB before starting
    # load example.owl in the knowrob database to access its content
    query = pq.prolog_query("load_owl('package://krr_example/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).")
    
    query = pq.prolog_query("instance_of(X, pap:'Milk').")
    print("Instances of Milk:")
    pq.print_all_solutions(query)


    query = pq.prolog_query("has_domain(soma:'hasMassValue',X).")
    print("Individuals with mass value:")
    pq.print_all_solutions(query)

    query = pq.prolog_query("triple(pap:'milk_product_1', soma:hasMassAttribute, X)")
    print("Mass attribute of milk product 1:")
    pq.print_all_solutions(query)

    # print("------changing values----")
    # query = pq.prolog_query("triple(pap:'milk_product_1', soma:hasMassAttribute, X)")
    # print("Mass attribute of milk product 1:")
    # pq.print_all_solutions(query)

    # query = pq.prolog_query("kb_project(triple(pap:'milk_product_1', soma:hasMassAttribute, pap:'milk_weight_half'))")
    # print("Changed:")
    # pq.print_all_solutions(query)

    # query = pq.prolog_query("triple(pap:'milk_product_1', soma:hasMassAttribute, X)")
    # print("Mass attribute of milk product 1:")
    # pq.print_all_solutions(query)

    # query = pq.prolog_query("kb_unproject(triple(pap:'milk_product_1', soma:hasMassAttribute, pap:'milk_weight_full'))")
    # print("Removed old values:")
    # pq.print_all_solutions(query)

    # query = pq.prolog_query("triple(pap:'milk_product_1', soma:hasMassAttribute, X)")
    # print("Mass attribute of milk product 1:")
    # pq.print_all_solutions(query)


    print("------ Changing values in time----")

    print("----------------- Instant 1 ----------------")

    # SINCE 1
    query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) during [0, 1])")
    print("Mass attribute of milk product 1 at instant [0, 1]:")
    rv = pq.print_all_solutions(query)

    string_query = "kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', " + rv[0] + ":'" + rv[1] + "') until 1)"
    query = pq.prolog_query(string_query)
    print("Remove previous value: {}".format(rv[1]))
    pq.print_all_solutions(query)

    query = pq.prolog_query("kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', pap:'milk_weight_half') since 1)")
    print("Assert that weight is half since instant 1:")
    pq.print_all_solutions(query)

    query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) since 1)")
    print("Checking weight at instant 1:")
    pq.print_all_solutions(query)

    print("----------------- Instant 2 ----------------")

    # SINCE 2
    query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) during [1, 2])")
    print("Mass attribute of milk product 1 at instant [1, 2]:")
    rv = pq.print_all_solutions(query)

    string_query = "kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', " + rv[0] + ":'" + rv[1] + "') until 2)"
    query = pq.prolog_query(string_query)
    print("Remove previous value: {}".format(rv[1]))
    pq.print_all_solutions(query)

    query = pq.prolog_query("kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', pap:'milk_weight_full') since 2)")
    print("Assert that weight is full since instant 2:")
    pq.print_all_solutions(query)

    query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) since 2)")
    print("Checking weight at instant 2:")
    pq.print_all_solutions(query)


    print("----------------- Conclusions ----------------")
    
    query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) during [0, 1])")
    print("Mass attribute of milk product 1 during [0, 1]:")
    pq.print_all_solutions(query)

    query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X)  during [1, 2])")
    print("Mass attribute of milk product 1 during [1, 2]:")
    pq.print_all_solutions(query)


