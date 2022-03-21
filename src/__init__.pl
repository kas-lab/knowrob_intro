% make sure library path is expanded
:- register_ros_package(knowrob).

% add prolog modules that you want to load when starting the prolog package
:- use_module(library('prolog_kb')).
:- use_module(library('sc_planning')).