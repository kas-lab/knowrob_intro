% example of Prolog module defined by the user

% module definition and public (externally visible) predicates
:- module(sc_planning,
    [
        holding/2,
        location/3,
        legal/1
    ]).

% possibility axioms grab and place
poss(grab(X), S) :- nonperishable(X), location(X, table1, S), \+ holding(Y, S).
poss(grab(X), S) :- perishable(X), location(X, table2, S), \+ holding(Y, S).
poss(place(L), S) :- L = table2, holding(X,S), nonperishable(X).
poss(place(L), S) :- L = table1, holding(X,S), perishable(X).

% successor axiom holding
holding(X, do(A, S)) :- A = grab(X).
holding(X, do(A, S)) :- \+(A = place(L)), holding(X, S).

% successor axiom location
location(X, L, do(A, S)) :- A = place(L), holding(X,S).
location(X, L, do(A, S)) :- \+(A = grab(X)), location(X, L, S).

legal(s0).
legal(do(A,S)) :- poss(A,S), legal(S).