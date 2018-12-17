# shortestpath
The shortest path problem using Dijkstra algorithm based on
[Wikipedia](https://en.wikipedia.org/wiki/Dijkstra's_algorithm) page

# Module installation

To install the module in your local environment clone or fork the application from
[gitgub](https://github.com/tszyrowski/shortestpath)

Navigate to the directory where the module was cloned
install the module in the environment with:  
`pip install .`

to remove the module from your local environment run:  
`pip uninstall shortestpath`

# Running application

The application can be executed from the command line with command:  
`shortestpath network-file origin destination`

The example of calcluating the shortest path between node **A** and node **X** given file **route.dat**:  
`shortestpath .\data\route.dat A X`

for additional help run:  
`shortestpath -h` or `shortestpath -help`