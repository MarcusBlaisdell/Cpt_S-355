######################################
# Marcus Blaisdell
# Cpt_S 355
# Programming Assignment 2, Part A
# February 13, 2017
# Sakire Arslan Ay
######################################

######################################
# SPS
# Simplified PostScript Language
######################################

##########################################################
# 1. Operand stack
# 2. Dictionary stack
# 3. Defining variables with def
# 4. Looking up names
# 5. Operators that don't involve code arrays
#    not for loop, forall operator, or calling functions
##########################################################

###########################################################################
# 1. The operand stack should be implemented as a Python list.
#    The list will contain Python integers, arrays, and later
#    in Part 2 code arrays. Python integers and arrays on the
#    stack represent Postscript integer constants and array constants.
#    Python strings which start with a slash / on the stack represent
#    names of Postscript variables. When using a list as a stack one
#    of the decisions you have to make is where the hot end of the stack
#    is located. (The hot end is where pushing and popping happens).
#    Will the hot end be at position 0, the head of the list, or at
#    position -1, the end of the list? It's your choice.
###########################################################################

