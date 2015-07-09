"""
    The main script file to launch the pysines application
"""
import sys
import argparse
import os
import matplotlib.pylab as plt
import numpy as np

def check_options(options):
    """
    Check that the options are sane and restricted to the project specs
    :param options: An `argparse.Namespace` object
    :return:
    """
#    pass
#    print 'Here are some options' ,options
    if type(options.num) != int:
        print 'An integer must be entered for the number of sines'
        sys.exit(0)
#    if not (format(os.path.dirname(options.file))):
#        print 'This folder does not exist'
#        sys.exit(0)
        
    

def create_parser():
    """
    Create the Argument Parser for this script
    :return:  An `argparse.ArgumentParser` instance
    """
    parser = argparse.ArgumentParser('pysines', description="A function to plot")
#    parser.add_argument('-f', '--file', dest="file_name", action="store_const",\
#                          , type=str, help="Optional Output File Name")
    
    parser.add_argument('-f', '--file',  action="store",
                        help="Optional Output File Name")
    parser.add_argument('-n', '--num',  action="store",default=1,
                        type=int, help="Optional Input Number")
    parser.add_argument('args', nargs='*', 
                        help="Script Arguments")

    return parser

def parse_args(args):
    """
    Perform the actual argument parsing, useful for testing the parser
    :param args: The list of arguments to parse, something like `sys.argv`
    :return: An `argparse.Namespace` object
    """
    parser = create_parser()
    return parser.parse_args(args)

def run(options):
    """
    Run the actual script
    :param options: An `argparse.Namespace` object
    :return:
    """

    # Do some additional check on the options
    check_options(options)
    
    s_time = np.linspace(0,100,1000)    
    
    for i in range(options.num):
        s_amp = np.sin(s_time*i)
        plt.hold(True)
        plt.plot(s_time,s_amp)
        
    plt.savefig(options.file)

if __name__ == '__main__':
    # Script has been launched

    options = parse_args(sys.argv)
#    print options
    run(options)