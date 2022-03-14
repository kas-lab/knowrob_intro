# knowrob-intro

This repository store the first steps into using a self-made ontology for Knowrob.

## Installation

Install SWI prolog and MongoDB using [these instructions](https://github.com/knowrob/knowrob#installation-of-swi-prolog-and-mongodb).

Create a catking repository, clone this repository and [Knowrob](https://github.com/knowrob/knowrob):

```Bash
rosdep update
cd ~/catkin_ws/src
git clone https://github.com/kas-lab/knowrob-intro.git
wstool init
wstool merge https://raw.github.com/knowrob/knowrob/master/rosinstall/knowrob-base.rosinstall
wstool update
source ../devel/setup.bash
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

Inside the Prolog terminal, first load your ontology:

```Bash
load_owl('package://knowrob-intro/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')])
```
pap is the name space defined for your ontology, you can use any name.

Example of queries here, more information at [Knowrob model documentation](https://knowrob.github.io/knowrob/master/model/):
```
is_class(soma:'Crockery').
```
True.

## Quering from source

Launch knowrob:
```Bash
roslaunch knowrob knowrob.launch 
```

Launch a test querying code
```Bash
rosrun knowrob_intro example_query_owl.py 
```

## Interfacing with the knowledge base

To facilitate a quick introduction to knowrob, we have added a brief description of our understanding in the main commands used. However, this documentation only serves as a starting point. For a better understanding please refer to the official documentation.

### Main knowrob documentation on interfacing with the knowledge base
* [Knowrob model documentation](https://knowrob.github.io/knowrob/master/model/)
* [Knowrob language documentation](https://knowrob.github.io/knowrob/master/lang/index.html)
* [Knowrob language terms documentation](https://knowrob.github.io/knowrob/master/lang/index.html)

### Our understanding on interfacing with the knowledge base with examples
* TODO

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
