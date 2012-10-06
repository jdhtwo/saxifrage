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
# 
# DAN'S THINKING OUT LOUD NOTES
# import sys | import is a simple statment that finds modules and defines them
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
# If the finders on sys.meta_path can't find the module then some other
# finders are queried.
# 
# If a finder returns a loader it returns it with load_module() method
# where the method is called with the name of the module to load.  The 
# loader must set several attributes on the module.__name__ is the name
# of the module.  __file__ is the the path to the file (unless the  
# module is built-in.  __package__ is optional but set to our module 
# and package.  __loader__ is optional but is set to our module's loader.
# 
# Other naming possibilities are discussed.
# 
# When we specify a module we do not have to specify the absolute name of the module.
# Using dots allows us to specifiy how how up the package hierarchy to
# look.  
# 
# sys | sys is a module.  it provides access to some variables used 
# by the interpreter and to functions that interact strongly the 
# interpreter.  it is always available, like a truck stop.  I am
# guessing that the interpreter is terminal.
# sys.argv | the list of command line arguements passed to a P script.
# argv [0] is the empty string script name, but you can pass other names
# to the interpreter.
# 
# USAGE is a variable.  It is defined by "Usage: ./find.py word
# filename [filename]*".  I'm not sure what that means yet.  I assume
# it is generic.
# 
# def | built-in functions.  def = define a function.
# 
# def fail (msg): says "define function 'msg' to 'fail'"
# 
# print evaluates each expression and writes the resulting object to 
# a standard output. >> means extended form, also referred to as 
# "print chevron".  chevron = >.  in this form, the first expression after
# the chevron must evaluate to a "file-like" object, specifcally an
# object that has a write() method.  the subsequent expressions are 
# printed to this file object.  
# 
# sys.__stderr__ | contains original values of stderr at the start of the
# program.  used during finalization, useful to print to the actual
# standard stream even if the sys.std ojbect has been redirected. also
# used to restore the actual files to known working file objects.
# 
# sys.stderr | file objects corressponding to the interpreter's standard
# error stream.  the interpreter's own prompts and error messages go here.
# not built-in - any object is acceptable as long as it has a write()
# method that take a string argument.
# 
# msg | ???
# 
# try is a compound statement. it specifies exception handlers and/or
# cleanup code for a group of statements.  WHAT IS AN EXCEPTION HANDLER?
# when an exception occurs in the try stuie, a search for an exception
# handler is started.  the search inspects the except clauses in turn unil
# one is found that matches the exception. if the except clause has an
# expresstion, and it matches it is "compatible".  when the matching
# exception clause is found, the exception is assigned to the target
# specified in the except clause, and the except clause is executed. 
#  
# word = sys.argv[1] is the suite within try.  the suite is composed of
# the "word" variable, which is defined by sys.argv[1].  see my definition
# above, except now we are looking at index 1.
#  
# except is the second half of the try compound statement.  is it the
# exception handler.  when the search inspects the except clauses, it
# finds our "except" and executes the clause.  In our case, fail clause
# returns "Please provide a word to find."
# 
# oops - forgot to write about sys.exit().  Exit from python.  
# 
# filenames is a variable stated as sys.argv[2].  index of 2. WHAT IS
# THE COLON FOR?
#  
# if not is a compound statement. BUT I CAN'T FIND A DEFINITION FOR IT
# if selects exaclty one of the suites.  if not expression ":" suite.
# in our case, expression is filenames, suite is fail with the message
# "please enter one filename".
# 
# for in is a compound statement.  for is used to iterate over the elements
#  of a sequence or other iterable object.  the expression list is evaluated
#  once.  for target_list in expression_list : suite.  so, for us: for 
#  filename (target) in filenames (expression_list): operate a try/except.
# 
# try is looking for exception handler file_pointer, which is a variable 
# defined by function open.  we are passing filename into the open funciton.
# open is a built-in function used to open a file and return a file object. 
# a file object is created with the open() function.
# 
# the except part of the statement is defined by the function IOError.
#  it seems that this is an exception.  it is raised when an I/O operation
#  (such as the open() function) fails e.g. "file not found".  if this occurs, 
#  then print to sys.stderr "could not open file" and state the filename.
# 
# the continue simple statement skips the rest of the suite, or in our case, at 
# the end, goes to the next item.  it is passing control out of the try
# arguement.
#  
# for in compound statement | for expression line in expression file_pointer.
# 
# if (conditional execution) word (which is sys.argv[1]) is in expression
# line, then print filename (tell us the filename) and then break.
# 
# the break statement terminates the enclosing for loop.  loop control target
# keeps its current value.
#  
# DAN'S PLAIN ENGLISH NOTES 
# 
# import sys allows us to query modules and define a namespace.  modules 
# are found within packages.  the namespace is effectively the name of the file
# we are looking for.
# 
# usage is chad's instructions on how we should structure our search syntax.
# 
# def fail built-in function tells the terminal to output a print message
# of the error and label it as such, and end the python script.
#  
# try word except is a compund statement that allows us to define a word
# to find in the first position.  if we do not, we receive a specific error.
# 
# filenames variable allows us to define the filename we are looking for.
# if we do not, we receive a specific error.
# 
# the for in compound statement allows us to select the filename to open.
# if the word we are searching for appears in our filename, we are returned the 
# name of the file.
#
# I tested this by creating to .rtf files, titled text.rtf and text2.rtf.  
# In text.rtf, it simply read "OH! Yeah!".  In text2.rtf, it simply read "NO!".
# 
# Using the provided syntax, I searched for ./find.py Yeah! text.rtf [text.rtf]*
# 
# This returned text.rtf (although, curiously, it returned it twice.)
# 
# I searched for ./find.py poop text.rtf [text.rtf]* and yielded no results, as expected
#  (because there is no error message defined for an improper search.)
# 
# Curiously, I searched for ./find.py Yeah! text2.rtf [text2.rtf]* and 
# unexpectedly received text.rtf as output.  Not sure if this somehow searches
# the whole directory.
# 
# IN SUMMARY
# Chad has written a search script.  The search script, when properly 
# syntaxed, allows us to search for a word within a filename.  If the 
# word appears within the filename, the filename is printed.  I don't
# purport to know the entire workings of this script, but I think I see
# the gist.

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