# knowrob-intro

This is a temporal repository to store first steps into using a self-made ontology for Knowrob.

## Installation

Install SWI prolog and MongoDB using [these instructions](https://github.com/knowrob/knowrob#installation-of-swi-prolog-and-mongodb).

Create a catking repository and clone [Knowrob](https://github.com/knowrob/knowrob):

```Bash
rosdep update
cd ~/catkin_ws/src
wstool init
wstool merge https://raw.github.com/knowrob/knowrob/master/rosinstall/knowrob-base.rosinstall
wstool update
rosdep install --ignore-src --from-paths .
cd ~/catkin_ws
catkin_make
```
## Launch

Run the mongodb service
```Bash
sudo systemctl start mongod.service
```

Launch knowrob:
```Bash
roslaunch knowrob knowrob.launch 
```

Launch a Prolog CLI as querying interface:
```Bash
rosrun rosprolog rosprolog_commandline.py 
```

## Quering

Inside the Prolog terminal, first load your ontology: - This step will be done by a launch file in a pkg soon-

```Bash
load_owl('[FULL PATH TO YOUR OWL FILE]/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).
```
pap is the name space defined for your ontology, you can use any name.

Example of queries here, more information at [Knowrob model documentation](https://knowrob.github.io/knowrob/master/model/):
```
?- is_class(soma:'Crockery').
```
True.
```
?- is_class(pap:'Rice').
```
True.
```
?- has_type(X, pap:'Perishable').
```
X: http://www.airlab.org/tiago/pick-and-place#milk_product_1 ;

X: http://www.airlab.org/tiago/pick-and-place#milk_product_2.
```
?- is_individual(pap:'milk_product_1')
```
true.
```
?- is_object_property(dul:'hasPart')
```
true.
```
?- is_data_property(soma:'hasMassValue').
```
true.
```
?- has_domain(soma:'hasMassValue',X)
```
X: http://www.ease-crc.org/ont/SOMA.owl#MassAttribute.
```
?- disjoint_with(Y,soma:'FixedJoint').
```
Y: http://www.ease-crc.org/ont/SOMA.owl#MovableJoint ;

Y: http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality ;

Y: http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Abstract ;

Y: http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event ;

Y: http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialObject ;

Y: http://www.ease-crc.org/ont/SOMA.owl#Feature.
```
?- holds(A, rdf:type, pap:'Milk').
```
A: http://www.airlab.org/tiago/pick-and-place#milk_product_1 ;

A: http://www.airlab.org/tiago/pick-and-place#milk_product_2.

```
?- triple(A, rdf:type, pap:'Milk').
```
A: http://www.airlab.org/tiago/pick-and-place#milk_product_1 ;

A: http://www.airlab.org/tiago/pick-and-place#milk_product_2.
```
?- triple(pap:'Milk', P, O).
```
P: http://www.w3.org/1999/02/22-rdf-syntax-ns#type,

O: http://www.w3.org/2002/07/owl#Class ;


P: http://www.w3.org/2000/01/rdf-schema#subClassOf,

O: http://www.airlab.org/tiago/pick-and-place#Perishable.
```
?- triple(pap:'milk_product_1', soma:hasMassAttribute, X), triple(X, soma:hasMassValue, Y)
```
Y: 0.6,

X: http://www.airlab.org/tiago/pick-and-place#milk_weight_full.

## Some comments:

Knowrob launch file loads the following namespaces:
- dc: http://purl.org/dc/elements/1.1/
- dcterms: http://purl.org/dc/terms/
- eor: http://dublincore.org/2000/03/13/eor#
- foaf: http://xmlns.com/foaf/0.1/
- owl: http://www.w3.org/2002/07/owl#
- rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
- rdfs: http://www.w3.org/2000/01/rdf-schema#
- serql: http://www.openrdf.org/schema/serql#
- skos: http://www.w3.org/2004/02/skos/core#
- void: http://rdfs.org/ns/void#
- xsd: http://www.w3.org/2001/XMLSchema#
- qudt: http://data.nasa.gov/qudt/owl/qudt#
- **dul: http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#**
- io: http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#
- **soma: http://www.ease-crc.org/ont/SOMA.owl#**
- knowrob: http://knowrob.org/kb/knowrob.owl#
- test: http://knowrob.org/kb/swrl_test#
- urdf: http://knowrob.org/kb/urdf.owl#

Therefore, make sure your .OWL files loads dul and soma namespaces as well. This is an example of the first lines of our .OWL file:
```
<rdf:RDF xmlns="http://www.airlab.org/tiago/pick-and-place#"
     xml:base="http://www.airlab.org/tiago/pick-and-place"
     xmlns:dc="http://purl.org/dc/elements/1.1/  
     xmlns:DUL="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#"    
     xmlns:owl="http://www.w3.org/2002/07/owl#"  
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"    
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:SOMA="http://www.ease-crc.org/ont/SOMA.owl#
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
    <owl:Ontology rdf:about="http://www.airlab.org/tiago/pick-and-place">
        <owl:imports rdf:resource="http://www.ease-crc.org/ont/SOMA.owl"/>
    </owl:Ontology>
 ```
