% example of Prolog module defined by the user
% STATUS: working

% module definition and public (externally visible) predicates
:- module(owl_kb_prolog_rules,
    [
        is_perishable/1,
        is_nonperishable/1,
        location/2,
        transfer/3
    ]).

is_perishable(X) :- instance_of(X, pap:'Perishable').
is_nonperishable(X) :- instance_of(X, pap:'NonPerishable').
location(X,L) :- triple(X, dul:'hasLocation', L).

% returns if the transfer operation is correct accordng to the rule that
% perishable items should be in a refrigerated table
transfer(X, L1, L2) :- is_perishable(X),
                        location(X,L1),
                        instance_of(L1, pap:'NonRefrigeratedTable'),
                        instance_of(L2, pap:'RefrigeratedTable').

transfer(X, L1, L2) :- is_nonperishable(X),
                    location(X,L1),
                    instance_of(L1, pap:'RefrigeratedTable'),
                    instance_of(L2, pap:'NonRefrigeratedTable').
