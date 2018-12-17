''' Closes Path Calculator
ref: https://en.wikipedia.org/wiki/Dijkstra's_algorithm
'''
import copy
import logging
from email.charset import SHORTEST

class PathCalculator(object):
    '''
    Calculate shortest path between two nodes given file with nodes and distances
    '''
    def __init__(self, inputDataFile, initialNode, destination):
        '''
        :param inputDataFile: path to file with nodes and distances
        :param initialNode: the node from which path will be calculated
        :param destination: the node where path should end
        '''
        self.inputDataFile = inputDataFile  
        self.initialNode = initialNode
        self.destNode = destination
        self.errorString = ''                   # all error will be updated and displayed in consol
        self.graph = self.readInputData()
        self.nodes = list(self.graph.keys())
        self.path = self.dijkstraPath()         
        
    def readInputData(self):
        ''' construct network's graph from the input file 
        
        If data in the file do not much the format, errors string will be updated
        '''
        graph = {}
        with open(self.inputDataFile, 'r') as f:
            for line in f:
                try:
                    start, end, dist = line.split()
                    graph.setdefault(start,{}).update({end:float(dist)})
                except Exception as e:
                    self.errorString += '{} in {}'.format(e, line)    
        return graph
    
    def dijkstraPath(self, graph=None, initialNode=None, destNode=None):  
        ''' shortest path calculation based on Dijkstra's algorithm 
        
        :param graph: dict of nodes and all connected nodes with distances
        :param initialNode: starting node
        :param destNode: finishing node
        :retutn: list of notes in closest path
        '''
        if not graph:                           # copy graph and avoid changing original input
            unvisitedNodes = copy.deepcopy(self.graph)
        else:
            unvisitedNodes = copy.deepcopy(graph)
        if not initialNode: 
            initialNode = self.initialNode
        if not destNode:
            destNode = self.destNode
            
        shortestPath = {}                       # cumulative distances along the path
        path = []                               # best path
        previouseNode = {}

        # initialise dictionary with nodes and their cumulative distances 
        for node in unvisitedNodes:
            shortestPath[node] = float('inf')
        shortestPath[initialNode] = 0
        shortestPath[self.destNode] = float('inf')
        
        while unvisitedNodes:
            closestNode = None
            for node in unvisitedNodes:
                if closestNode is None:
                    closestNode = node
                elif shortestPath[node] < shortestPath[closestNode]:
                    closestNode = node
            for innerNode, innerDist in unvisitedNodes[closestNode].items():
                if innerNode not in shortestPath:
                    shortestPath[innerNode] = float('inf')
                if innerDist + shortestPath[closestNode] < shortestPath[innerNode]:
                    shortestPath[innerNode] = innerDist + shortestPath[closestNode]
                    previouseNode[innerNode] = closestNode                   
            unvisitedNodes.pop(closestNode)
         
        if shortestPath[destNode] < float('inf'):   # if path exists the distance at the final node is finite
            currentNode = destNode
            while currentNode != initialNode:
                try:
                    path.insert(0, currentNode)
                    currentNode = previouseNode[currentNode]
                except KeyError: 
                    self.errorString += 'destination can not be reached, path finishes at {}'.format(currentNode)
                    break
            path.insert(0, self.initialNode)
            return path
        else:                                       # otherwise path disconnected the distance at the final node is infinity
            path = None
            self.errorString += 'destination can not be reached as is disconnected'
            
    def runCommandLine(self):    
        ''' display output '''
        if self.errorString:
            print(self.errorString)
        else:
            for node in self.path:
                print(node)

    