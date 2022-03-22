% example of Prolog module defined by the user

% module definition and public (externally visible) predicates
:- module(sc_planning,
    [
        robot/1,
        perishable/1,
        nonperishable/1,
        location/3,
        legal/1
    ]).

% define initial state using prolog (the KB)
robot(tiago).
perishable(milk).
perishable(yogurt).
nonperishable(hagelslag).
nonperishable(honey).
table(table1).
table(table2).
location(milk, table1, s0).
location(yogurt, table1, s0).
location(hagelslag, table1, s0).
location(honey, table1, s0).

% possibility axioms grab and place
poss(grab(X), S) :- nonperishable(X), location(X,table1,S), \+ holding(_,S);
                    perishable(X), location(X,table2,S), \+ holding(_,S).
poss(place(L), S) :- L = table1, holding(X,S), perishable(X);
                     L = table2, holding(X,S), nonperishable(X).

% successor axiom holding
holding(X, do(A, S)) :- A = grab(X).
holding(X, do(A, S)) :- \+(A = place(L)), holding(X, S).

% successor axiom location
location(X, L, do(A, S)) :- A = place(L), holding(X,S).
location(X, L, do(A, S)) :- \+(A = grab(X)), location(X, L, S).

legal(s0).
legal(do(A,S)) :- poss(A,S), legal(S).