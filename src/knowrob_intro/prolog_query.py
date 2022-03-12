#!/usr/bin/env python

''' Module to define a prolog query,
includes inicialization, quering and data extracting methods. '''


import roslib; roslib.load_manifest('rosprolog')
from rosprolog_client import PrologException, Prolog

class PrologQuery(object):
    def __init__(self):

        self.prolog = Prolog() # attribute type Prolog class (from rosprolog_client)
        self.predicates = [] # initialize list attribute
        self.load_namespace()
        self.load_all_predicates()

    def load_namespace(self):
        ''' Load all namespaces in knowrob environment: SOMA, DUL and other
         ontologies used in previous versions of knowrob. Define in '''
         
        q = 'findall([_X, _Y], rdf_current_ns(_X, _Y), NS)'
        solution = self.prolog.once(q)
        print('namespaces:')
        for ns in solution['NS']:
            print('{}: {}'.format(ns[0], ns[1]))
        print('-----------')
   
    def load_all_predicates(self):
        ''' Load all predicates  '''

        q = 'findall(X, current_predicate(X/_);current_module(X), L)'
        solution = self.prolog.once(q)
        self.predicates = [str(x) for x in solution['L']]
  
    def prolog_query(self, q):
        query = self.prolog.query(q)
        solutions = [x for x in query.solutions()]
        query.finish()
        #self.print_all_solutions(solutions)
        return solutions

    def remove_full_iri(self, value): 
        q = 'findall([_X, _Y], rdf_current_ns(_X, _Y), NS)'
        solution = self.prolog.once(q)
        for ns in solution['NS']:
            if ns[1] in value:
                value_new = value.replace(ns[1], '')
                solution_formated = (ns[0], value_new) # tuple namespace, individual
                return solution_formated

    def get_all_solutions(self, solutions, print_solutions=True):
        solutions_list = []
        name_value = ()
        
        if len(solutions) == 0:
            name_value = ('false', 'false')
            solutions_list.append(name_value)
            if print_solutions == True:
                print('false.')
                
        else:
            for s in solutions:
                if s == dict(): # if query result is an empty dict
                    name_value = ('true', 'true')
                    solutions_list.append(name_value)
                    if print_solutions == True:
                        print('true.')

                else:
                    for k, v in s.items():
                        rv = self.remove_full_iri(v) # isolate namespace and name
                        name_value = (rv[0], rv[1])
                        solutions_list.append(name_value)
                        if print_solutions == True: 
                            print('{} : {}:{}'.format(k, name_value[0], name_value[1]))
        if print_solutions == True: 
            print # end with new line
        return solutions_list