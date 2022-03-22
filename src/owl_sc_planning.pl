% example of Prolog module defined by the user
% the goal is to use situation calculus to obtain required grab and place operations to transfer
% items to their right location according to the rules defined in the possibility axioms
% STATUS: NOT WORKING, search seems to overflow the stack limit

% module definition and public (externally visible) predicates
:- module(owl_sc_planning,
    [
        perishable/1,
        nonperishable/1,
        location/3,
        transfer/3,
        legal/1
    ]).

perishable(X) :- instance_of(X, pap:'Perishable').
nonperishable(X) :- instance_of(X, pap:'NonPerishable').
location(X,L,s0) :- triple(X, dul:'hasLocation', L).

% possibility axioms grab and place
poss(grab(X), S) :- nonperishable(X), location(X, instance_of(L, pap:'RefrigeratedTable'), S),
                    \+ holding(Y, S).
poss(grab(X), S) :- perishable(X), location(X, L, S),
                    instance_of(L, pap:'NonRefrigeratedTable'), \+ holding(_, S).
poss(place(L), S) :- L = instance_of(L, pap:'NonRefrigeratedTable'),
                     holding(X,S), nonperishable(X).
poss(place(L), S) :- L = instance_of(L, pap:'RefrigeratedTable'),
                     holding(X,S), perishable(X).

% successor axiom holding
holding(X, do(A, S)) :- A = grab(X).
holding(X, do(A, S)) :- \+(A = place(L)), holding(X, S).

% successor axiom location
location(X, L, do(A, S)) :- A = place(L), holding(X,S).
location(X, L, do(A, S)) :- \+(A = grab(X)), location(X, L, S).

legal(s0).
legal(do(A,S)) :- poss(A,S), legal(S).