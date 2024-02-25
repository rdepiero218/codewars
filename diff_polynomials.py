#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 07:48:20 2024

@author: reggiemba
"""

import re
polys = [
    '12x+2',
    'x^2-x',
    '-5x^2+10x+4',
    'x^3-2x-3',
    '2x^3-x-4',
]

poly = polys[4]

if poly[0].isalpha():
    poly = '+' + poly
    
terms = re.split(r'[\+-]', poly)
terms = list(filter(None, terms)) # gets rid of empty strings

print(' terms: ', terms)

signs = re.findall(r'[\+-]', poly)

print('signs: ', signs)

for i in range(len(terms)):
    terms[i] = signs[i] + terms[i]
    
print(' terms: ', terms)


# signs = []
coeffs = []
exponents = []
variables = []

for i in range(len(terms)):
    variables.append(re.findall(r'([a-z]{1})', terms[i]))
    
    
    # sign = re.findall(r'[-|+]', term)
    # print(sign)
    
    # COEFFICIENTS
    coeff = (re.findall(r'^([-+]?\d*)', terms[i]))[0]
    print('coeff: ', coeff)
    
    if coeff == '+':
        coeff = 1
    elif coeff == '-':
        coeff = -1
    # else:
    
    # if not coeff and signs[i] == '+':
    #     coeff = 1
    # elif not coeff and signs[i] == '-':
    #     coeff = -1
    # else:
        
        coeff.replace('+')
        
    # # elif not coeff:
    # #     coeff = 9
    # # elif 
    # # coeffs.append(re.findall(r'^([-+]?\d*)', term))
    # coeffs.append(int(coeff))

    # exponent = re.findall(r'\^(\d+)', terms)
    
    # # exponent = re.findall(r'[-+]?[0-9]*(\^\d)', term)
    
    # # print(exponent)
    # # EXPONENTS
    # if not exponent and 'x' in terms[i]:
    #     exponent = 1
    # elif not exponent and term.isnumeric():
    #     exponent = 0
    # else:
    #     exponent = int(exponent[0])
    # # print(type(exponent), 'len', len(exponent))
    # exponents.append(exponent)
    # # # signs.append(re.findall(r'[-|+]', term))
    
    
print('  vars: ', variables)
print(' signs: ', signs)
print('coeffs: ', coeffs)
print('expons: ', exponents)
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

