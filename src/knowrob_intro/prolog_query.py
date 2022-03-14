""" Module to define a prolog query,
includes inicialization, quering and data extracting methods. """
#!/usr/bin/env python

from rosprolog_client import Prolog
import roslib; roslib.load_manifest('rosprolog')

class PrologQuery(object):
    def __init__(self):

        self.prolog = Prolog() # attribute instance of Prolog class (from rosprolog_client)
        self.predicates = [] # initialize list attribute
        self.load_namespace()
        self.load_all_predicates()

    def load_namespace(self):
        """ Load all namespaces in knowrob environment: SOMA, DUL and other
         ontologies used in previous versions of knowrob. """

        q = 'findall([_X, _Y], rdf_current_ns(_X, _Y), NS)'
        solution = self.prolog.once(q)
        print('namespaces:')
        for ns in solution['NS']:
            print('{}: {}'.format(ns[0], ns[1]))
        print('-----------')

   
    def load_all_predicates(self):
        """ Load all available predicates. The knowrob ones are defined inside __init__.pl
         files, see https://github.com/knowrob/knowrob/blob/master/src/model/__init__.pl """

        q = 'findall(X, current_predicate(X/_);current_module(X), L)'
        solution = self.prolog.once(q)
        self.predicates = [str(x) for x in solution['L']]
  
    def prolog_query(self, q):
        """ Do prolog query. Takes as argument the query string and returns a list of dictionaries.
        One dictionary per query result. """

        query = self.prolog.query(q)
        solutions = [x for x in query.solutions()]
        query.finish()
        return solutions

    def remove_full_iri(self, value): 
        """ Takes as argument a query result dictionary and returns the query in tuple format
        (namespace, name_value). """
        value = str(value)
        q = 'findall([_X, _Y], rdf_current_ns(_X, _Y), NS)'
        solution = self.prolog.once(q)
        for ns in solution['NS']:
            if ns[1] in value:
                value_new = value.replace(ns[1], '')
                break
            else:
                value_new = value
        return value_new

    def get_all_solutions(self, solutions, print_solutions=True):
        """ Stores all query solutions in a list of tuples (namespace, name_value) for easy usage.
        By default, also print the query result. """

        solutions_list = []
        name_value = ()
        if len(solutions) == 0: # list empty
            name_value = 'false'
            solutions_list.append(name_value)
            if print_solutions == True:
                print('false.')
                
        else:
            for s in solutions:
                if s == dict(): # if query result is an empty dict
                    name_value = 'true'
                    solutions_list.append(name_value)
                    if print_solutions == True:
                        print('true.')

                else:
                    for k, v in s.items():
                        name_value = self.remove_full_iri(v) # isolate namespace and name
                        solutions_list.append(name_value)
                        if print_solutions == True: 
                            print('{} : {}'.format(k, name_value))
        if print_solutions == True: 
            print # end with new line
        return solutions_list
