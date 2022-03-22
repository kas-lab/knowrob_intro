% example of Prolog module defined by the user
% STATUS: working

% module definition and public (externally visible) predicates
:- module(owl_kb_prolog_rules,
    [
        location/2,
        transfer/3
    ]).

perishable(X) :- instance_of(X, pap:'Perishable').
nonperishable(X) :- instance_of(X, pap:'NonPerishable').
location(X,L) :- triple(X, dul:'hasLocation', L).

% returns if the transfer operation is correct accordng to the rule that
% perishable items should be in a refrigerated table
transfer(X, L1, L2) :- instance_of(X, pap:'Perishable'),
                        location(X,L1),
                        instance_of(L1, pap:'NonRefrigeratedTable'),
                        instance_of(L2, pap:'RefrigeratedTable').

transfer(X, L1, L2) :- instance_of(X, pap:'NonPerishable'),
                    location(X,L1),
                    instance_of(L1, pap:'RefrigeratedTable'),
                    instance_of(L2, pap:'NonRefrigeratedTable').
