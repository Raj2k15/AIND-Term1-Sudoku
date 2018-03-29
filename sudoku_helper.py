# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 06:50:50 2017

@author: 5219294
"""

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
unit1= [(j+str(i+1)) for i, j in enumerate(rows)]
unit2=[(j+str(len(rows)-i)) for i, j in enumerate(rows) ]
diag_unit=[unit1,unit2]
