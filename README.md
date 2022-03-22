# knowrob_intro

This repository store the first steps into using a self-made ontology for Knowrob.

We offer below intructions to install this repo and use it in two flavours:
- Using the singularity image [ro4714-22-3.simg](https://tud365.sharepoint.com/:u:/s/Metacontrol/EQgJLRS9pRZHqlvAtiSc5jUB1WG3-JOZzHHtF4ZCnwMCMw?e=HHaBxP) for the KRR course (contains most required KnowRob dependencies)
- Using a native ROS installation

# Using the singularity image [ro4714-22-3.simg](https://tud365.sharepoint.com/:u:/s/Metacontrol/EQgJLRS9pRZHqlvAtiSc5jUB1WG3-JOZzHHtF4ZCnwMCMw?e=HHaBxP)

**Outside** of the singularity image:
- Install MongoDB using [these instructions](https://github.com/knowrob/knowrob#installation-of-swi-prolog-and-mongodb).
- Create a catking repository, clone this repository and [Knowrob](https://github.com/kas-lab/knowrob):
```Bash
source /opt/ros/melodic/setup.bash
rosdep update
cd ~/catkin_ws/src
git clone https://github.com/kas-lab/knowrob_intro.git
```

**Inside the singularity** (`singularity shell -p ro47014-22-3.simg`):

```Bash
source /opt/ros/melodic/setup.bash
wstool init
wstool merge https://raw.githubusercontent.com/kas-lab/knowrob/master/rosinstall/knowrob-base.rosinstall
wstool update
rosdep install --ignore-src --from-paths .
cd ~/catkin_ws
catkin build
```

source catkin_ws/devel/setup.bash


## Launch

Run the mongodb service from **OUTSIDE** simgularity
```Bash
sudo systemctl start mongod.service
```

**Inside the singularity** (`singularity shell -p ro47014-22-3.simg`):

Launch knowrob:

```Bash
source catkin_ws/devel/setup.bash
roslaunch knowrob knowrob.launch 
```

In another terminal Launch a Prolog CLI as querying interface:
```Bash
source catkin_ws/devel/setup.bash
rosrun rosprolog rosprolog_commandline.py 
```

## Querying

Inside the Prolog terminal, first load your ontology:

```Bash
load_owl('package://knowrob_intro/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')])
```
pap is the name space defined for your ontology, you can use any name.

Example of queries here, more information at [Knowrob model documentation](https://knowrob.github.io/knowrob/master/model/):
```
is_class(soma:'Crockery').
```
True.

## Querying from code

**Inside the singularity** (`singularity shell -p ro47014-22-3.simg`):

Launch knowrob:
```Bash
source catkin_ws/devel/setup.bash
roslaunch knowrob knowrob.launch 
```

Launch a test querying code:
```Bash
source catkin_ws/devel/setup.bash
rosrun knowrob_intro example_query_owl.py 
```


# Using a native ROS installation
## Installation

Install SWI prolog and MongoDB using [these instructions](https://github.com/knowrob/knowrob#installation-of-swi-prolog-and-mongodb).

Create a catking repository, clone this repository and [Knowrob](https://github.com/kas-lab/knowrob):

```Bash
source /opt/ros/melodic/setup.bash
rosdep update
cd ~/catkin_ws/src
git clone https://github.com/kas-lab/knowrob_intro.git
wstool init
wstool merge https://raw.githubusercontent.com/kas-lab/knowrob/master/rosinstall/knowrob-base.rosinstall
wstool update
rosdep install --ignore-src --from-paths .
cd ~/catkin_ws
catkin build
```

## Launch

Run the mongodb service
```Bash
sudo systemctl start mongod.service
```

Launch knowrob:
```Bash
source catkin_ws/devel/setup.bash
roslaunch knowrob knowrob.launch 
```

Launch a Prolog CLI as querying interface:
```Bash
rosrun rosprolog rosprolog_commandline.py 
```

## Querying

Inside the Prolog terminal, first load your ontology:

```Bash
load_owl('package://knowrob_intro/owl/krr_exercise.owl', [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')])
```
pap is the name space defined for your ontology, you can use any name.

Example of queries here, more information at [Knowrob model documentation](https://knowrob.github.io/knowrob/master/model/):
```
is_class(soma:'Crockery').
```
True.

## Querying from code

Launch knowrob:
```Bash
roslaunch knowrob knowrob.launch 
```

Launch a test querying code
```Bash
rosrun knowrob_intro example_query_owl.py 
```

# Interfacing with the knowledge base

To facilitate a quick introduction to knowrob, we have added a brief description of our understanding in the main commands used. However, this documentation only serves as a starting point. For a better understanding please refer to the official documentation.

### Main knowrob documentation on interfacing with the knowledge base
* [Knowrob model documentation](https://knowrob.github.io/knowrob/master/model/)
* [Knowrob language documentation](https://knowrob.github.io/knowrob/master/lang/index.html)
* [Knowrob language terms documentation](https://knowrob.github.io/knowrob/master/lang/index.html)

# Using prolog modules

The following launch files can be used to test examples on using prolog modules with your python code:
* `launch/example_query_prolog.launch`: example in which the knowledge about objects is in a prolog module.
* `launch/example_situation_calculus.launch`: example with planning using situation calculus.
* `launch/example_owl_kb_and_prolog_rules.launch`: example in which the knowledge about objects is store in an OWL ontology, while the store rules are rules in a prolog module.

To run these examples:

- Start the MongoDB  (OUTSIDE the singularity image)
```
systemctl start mongod.service
```

- Now within the singularity, source your workspace and launch the example:
```
singularity shell -p ro47014-22-3.simg
source [path_to_your_catkin_ws]/devel/setup.bash
roslaunch knowrob_intro example_[XXX].launch
```


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
