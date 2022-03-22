% make sure library path is expanded
:- register_ros_package(knowrob).
:- load_owl('package://knowrob_intro/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).
:- register_ros_package(knowrob_intro).

% add prolog modules that you want to load when starting the prolog package
:- use_module(library('sc_planning')).
:- use_module(library('owl_kb_prolog_rules')).
