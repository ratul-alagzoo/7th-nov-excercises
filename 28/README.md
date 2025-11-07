Path of Exile is an online action role-playing game developed by the New Zealand-based devel
oper Grinding Gear Games. It is particularly well known for its highly complex skill tree system 
(https://poeplanner.com/
 ). The complete skill tree for the latest version of the game (v3.27 just 
released on 31. October 2025!) is available as data.json in the repository at
 https://github.com/grindinggear/skilltree-export
 .
 (a) Use the load function of the json module to load the data as a dictionary. Data on individual 
nodes is stored in a dictionary under the nodes key. Construct a polars.DataFrame whose 
rows correspond to the individual node data dictionaries. How many nodes are there in 
total?
 (b) Find all nodes whose name is the longest or the shortest, respectively. Which are the nodes 
that award the most distinguished stats (with respect to the length of the list under the 
stats key)