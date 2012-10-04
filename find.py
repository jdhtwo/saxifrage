#!/usr/bin/env python

# The "import" statement finds modules (whatever those are!) and defines names
# in a namespace (whatever that is!):                                                                          
#                                                                                                              
#   http://docs.python.org/reference/simple_stmts.html#the-import-statement                                    
#                                                                                                              
# The "sys" module provides things related (apparently) to the interpreter
# (whatever that is!):                                                                                         
#                                                                                                              
#   http://docs.python.org/library/sys.html
# DAN'S NOTES
# import sys | import is a statment that finds modules and defines them
# in a namespace.  The namespace is local to the scope of the import
# statement, which sounds to me like a local directory of files. This
# form of import is without the from keyword, meaning that import will
# repeat steps for each identifier in the list. Packages are a concept
# that Python has.  Packages can contain packages and modules. Modules
# cannot contain other modules or packages. Therefore, packages are
# like directories and modules are like files.  import is searching for
# these modules.  import looks first in sys.modules, which is a cache of all
# previously imported modules. If import does not find its target there,
# it then looks in sys.meta_path. Here can be found a list of finder
# objects.  Finder objects try to find a loader for a modules by 
# implementing/calling find_module().  Loaders are objects that load a module
# by defining the module load_module(). Loaders are returned by finders.
# find_module() is called with at least one absolute name of the module
# being imported.  Sounds like a search to me.  If the module is found
# in the package, then the parent's package path attribute is passed in
# as a second argument.  Module is found in the package with a dot in
# the name.  If it can find the module it returns the loader or none.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

import sys

USAGE = "Usage: ./find.py word filename [filename]*"

def fail(msg):
    print >> sys.stderr, USAGE
    print >> sys.stderr, msg
    sys.exit()

try:
    word = sys.argv[1]
except:
    fail("Please provide a word to find.")

filenames = sys.argv[2:]
if not filenames:
    fail("Please enter at least one filename.")

for filename in filenames:
    try:
        file_pointer = open(filename)
    except IOError:
        print >> sys.stderr, "Could not open file:", filename
        continue

    for line in file_pointer:
        if word in line:
            print filename
            break