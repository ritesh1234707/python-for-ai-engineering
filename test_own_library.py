import sys 

from own_library import hello

if len(sys.argv) == 2: 
    hello(sys.argv[1])