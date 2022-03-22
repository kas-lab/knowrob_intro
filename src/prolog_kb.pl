:- module(prolog_kb,
    [
        robot/1,
        perishable/1,
        nonperishable/1
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