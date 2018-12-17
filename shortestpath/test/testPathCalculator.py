import unittest
import os
import sys
from shortestpath.pathCalculator import PathCalculator
from shortestpath.__main__ import main
import unittest.mock as mock
from _io import StringIO

class TestGoodInput(unittest.TestCase):
    ''' test shortest path finding on valid data file '''
    
    def setUp(self):
        self.pc = PathCalculator(os.path.join(os.path.abspath('../..'), 'data','route.dat'),'A','X')

    def testReadDataInput(self):
        expectedDict = {'A': {'B':2.0,'C': 6.0}, 'B': {'C':3.0,'X': 8.0}, 'C': {'X': 4.0}}
        methodDict = self.pc.readInputData()
        self.assertDictEqual(expectedDict, methodDict)

class TestInvalidInput(unittest.TestCase):
    ''' test invalid path - no path connection '''
    
    def setUp(self):
        self.pc = PathCalculator(os.path.join(os.path.abspath('../..'), 'data','invalidRoute.dat'),'A','X')

    def testReadDataInput(self):
        expectedDict = {'A': {'B': 2.0}, 'B': {'X': 8.0},'C':{}}
        methodDict = self.pc.readInputData()
        self.assertDictEqual(expectedDict, methodDict)

class TestCommandLineRun(unittest.TestCase):
    ''' the tests checks if command line behaviour is as expected '''

    def setUp(self):
        self.goodDataPath = os.path.join(os.path.abspath('../..'), 'data','route.dat')
        self.badData = os.path.join(os.path.abspath('../..'), 'data','noExistingFile.dat')

    def testValidInput(self):
        ''' test if output match expected format '''
        expectedOutput = 'A\nB\nC\nX' 
        with mock.patch('sys.stdout', new=StringIO()) as mockedOut:
            sys.argv = ['shortestpath', self.goodDataPath, 'A', 'X']
            main() 
            self.assertEqual(expectedOutput, mockedOut.getvalue().strip())
        
    def testInvalidFile(self):
        ''' test system exit if invalid file give '''
        sys.argv = ['shortestpath', self.badData, 'A', 'X']
        with self.assertRaises(SystemExit) as sysEx:
            main()
        self.assertEqual(sysEx.exception.code, 2)
        
    def testTooManyArgs(self):
        ''' test system exit if too many arguments given '''
        sys.argv = ['shortestpath', self.goodDataPath, 'A', 'X', 'C']
        with self.assertRaises(SystemExit) as sysEx:
            main()
        self.assertEqual(sysEx.exception.code, 2)

    def testNotEnoughArgs(self):
        ''' test system exit if not enough arguments given '''
        sys.argv = ['shortestpath', self.goodDataPath, 'A']
        with self.assertRaises(SystemExit) as sysEx:
            main()
        self.assertEqual(sysEx.exception.code, 2)
        
class TestValidPaths(unittest.TestCase):
    ''' test different input from valid files '''
    
    def testValidOutput(self):
        pathHead = os.sep.join(os.getcwd().split(os.sep)[:-2])
        routes = ['route.dat', 'routeBothWays.dat','routeDeadVertex.dat']
        expectedOut = [['A', 'B', 'C', 'X'],
                       ['A', 'B', 'D', 'G', 'X'],
                       ['A','H','E','X'],]
        start = 'A'
        end = 'X'
        for i in range(len(routes)):
            routeFile = os.path.join(pathHead, 'data', routes[i])
            pc = PathCalculator(routeFile, start, end)
            self.assertEqual(pc.path, expectedOut[i])
    
    def testDisconnectedRoute(self):
        pathHead = os.sep.join(os.getcwd().split(os.sep)[:-2])
        route = 'disconnectedRoute.dat'
        expectedOut = None
        expectedError = 'destination can not be reached as is disconnected'
        start = 'A'
        end = 'X'
        routeFile = os.path.join(pathHead, 'data', route)
        pc = PathCalculator(routeFile, start, end)
        self.assertEqual(pc.path, expectedOut)
        self.assertEqual(pc.errorString, expectedError)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)