#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 07:48:20 2024

@author: reggiemba
"""

import re

def differentiate(equation, point):
    import re

    poly = equation
    val = point
    if poly[0].isalpha() or poly[0].isnumeric():
        poly = '+' + poly
        
    terms = re.split(r'[\+-]', poly)
    terms = list(filter(None, terms)) # gets rid of empty strings

    signs = re.findall(r'[\+-]', poly)

    diff_val = 0

    for i in range(len(terms)):
        
        ## SIGNED TERM
        signed_term = signs[i] + terms[i]
        ## VARIABLE
        variable = re.findall(r'([a-z]{1})', terms[i])
        # COEFFICIENTS
        coeff = (re.findall(r'^([-\+]?\d*)', signed_term))[0]

        if coeff == '+':
            coeff = 1
        elif coeff == '-':
            coeff = -1
        else:
            coeff.replace('+','')
            coeff = int(coeff)
        
        ### EXPONENTS
        exponent = re.findall(r'\^(\d+)', terms[i])
        
        if not exponent and variable:
            exponent = 1
        elif not exponent and terms[i].isnumeric():
            exponent = 0
        else:
            exponent = int(exponent[0])

        if exponent > 0:
            diff_exponent = exponent - 1
            diff_val += coeff * exponent * (val)**diff_exponent
        else:
            diff_val += 0

    return diff_val


polys = [
    '12x+2',
    'x^2-x',
    '-5x^2+10x+4',
    'x^3-2x-3',
    '2x^3-x-4',
  ]

# differentiate(polys[1], 3)

for poly in polys:
    print(differentiate(poly, 3))

  # poly = polys[2]
  # val = 3
  

# differentiate

# if terms[-1].isnumeric():
#     exponents[-1] = [0]

# if terms[-2].isnumeric():
#     exponents[-2] = [1] 
# print('expons: ', exponents)


# for i in range(len(poly_vals)):
#     # mult exponent by coeff
#     poly_vals[i][0] = str( int(poly_vals[i][0]) * int( poly_vals[i][1] ))
    
#     # exponent -1
#     poly_vals[i][1] = str( int(poly_vals[i][1]) - 1 )

