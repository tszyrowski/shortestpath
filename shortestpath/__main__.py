import argparse
import os.path
from .pathCalculator import PathCalculator

def fileCheck(parser, filePath):
    ''' checks if provided file exists '''
    if not os.path.exists(filePath):
        parser.error("The file {} does not exist \nPlease check the file and run command again with corrected file's path".format(filePath))
    else: return filePath

def main():    
    ''' main function call and parse arguments '''
    parser = argparse.ArgumentParser(description="Find shortest path between two nodes from provided network-file input")
    parser.add_argument('network_filename', help='full path to the file with distances between nodes',
                        type=lambda x: fileCheck(parser, x))
    parser.add_argument('origin', help='the name of the starting node from which path is calculated')
    parser.add_argument('destination', help='the name of the node where the path finishes')
    
    args = parser.parse_args()
    pc = PathCalculator(args.network_filename, args.origin, args.destination)
    pc.runCommandLine()
    
        
if __name__=="__main__":
    main()