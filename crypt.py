#!usr/bin/python

'''
Copyright 2013, 2014 Zubair Abid

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os , pickle

__d = [];# key storage list
__lent = 0;# length of key
	
'''initialises the list with key values'''
def initialise(password):
	global __lent
	__lent = len(password)
	for i in password:
		__d.append(int(i)+2)#adding some colour to the code

'''encrypts, obviously'''
def encrypt(clr):
	sb = list(clr)
	a = ''
	b = ''
	x = ''
	z = ''
	k = 0

	for i in range(len(clr)):
		k = __d[ i % __lent ]
		x = sb[i]
		a = sb[correct(i-1, clr)]
		b = sb[correct(i+1,clr)]
		z = chr(int( ( k*ord(x) + ord(a) + ord(b) + ( k - ( ord(a) + ord(b) ) % k ) )/k ) )
		sb[i] = z
	ret = ''
	for i in sb:
		ret += i
	return ret

'''do not ask'''
def decrypt(scr ):
	sb = list(scr)
	a = ''
	b = ''
	x = ''
	z = ''
	k = 0
		
	for i in range(len(scr)-1, -1, -1):
		z = sb[i]
		k = __d[ i % __lent ]         		
		a = sb[correct(i-1, sb)]
		b = sb[correct(i+1,sb)]
		x = chr(int( ( k*ord(z) - ord(a) - ord(b) - ( k - ( ord(a) + ord(b) ) % k ) )/k ) )			
		sb[i] = x
	ret = ''
	for i in sb:
		ret += i
	return ret

'''prevents exceptions'''
def correct(num, sb):
	if num == -1:
		return len(sb)-1
	elif num == len(sb):
		return 0
	else:
		return num
