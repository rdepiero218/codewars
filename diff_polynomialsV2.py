#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 07:48:20 2024

@author: reggiemba
"""

import re

def differentiate(equation, point):
    
    poly = equation
    val = point
    if poly[0].isalpha() or poly[0].isnumeric():
        poly = '+' + poly
        
    terms = re.split(r'[\+-]', poly)
    terms = list(filter(None, terms)) # gets rid of empty strings

    # print(' terms: ', terms)

    signs = re.findall(r'[\+-]', poly)

    # print('signs: ', signs)

    # for i in range(len(terms)):
    #     terms[i] = signs[i] + terms[i]
        
    # print(' terms: ', terms)

    diff_val = 0
    # signs = []
    coeffs = []
    exponents = []
    variables = []

    for i in range(len(terms)):
        
        ## SIGNED TERM
        signed_term = signs[i] + terms[i]
        # print('signed term: ', signed_term)
        
        ## VARIABLE
        variable = re.findall(r'([a-z]{1})', terms[i])
        variables.append(re.findall(r'([a-z]{1})', terms[i]))
        
        # print('var: ', variable)

        
        # print(sign)
        
        # COEFFICIENTS
        coeff = (re.findall(r'^([-\+]?\d*)', signed_term))[0]
        # print('coeff: ', coeff)
        
        if coeff == '+':
            coeff = 1
        elif coeff == '-':
            coeff = -1
        else:
            coeff.replace('+','')
            coeff = int(coeff)
        
        coeffs.append(coeff)
        
        ### EXPONENTS
        exponent = re.findall(r'\^(\d+)', terms[i])


        # if not exponent and 'x' in terms[i]:
        if not exponent and variable:
            exponent = 1
        elif not exponent and terms[i].isnumeric():
            exponent = 0
        else:
            exponent = int(exponent[0])
        # print(exponent)
        # # # print(type(exponent), 'len', len(exponent))
        exponents.append(exponent)
        # # # signs.append(re.findall(r'[-|+]', term))
        
        if exponent > 0:
            # diff_coeff = coeff * exponent
            diff_exponent = exponent - 1
            diff_val += coeff * exponent * (val)**diff_exponent
            # print(diff_coeff,'x^',diff_exponent)
        else:
            diff_val += 0
        
        # print('dv: ', diff_val)

    # print('  vars: ', variables)
    # print(' signs: ', signs)
    # print('coeffs: ', coeffs)
    # print('expons: ', exponents)
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
    differentiate(poly, 3)

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

