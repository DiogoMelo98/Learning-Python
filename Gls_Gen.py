# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:43:09 2021

@author: diogo
"""

filepath = 'C:/Users/diogo/OneDrive/Ambiente de Trabalho/Dissertacao_50513/Gls_50513.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:                
       count=0
       for i in line:
           count += 1
           if(i.isupper()):
               break
       print('\\newglossaryentry{' + '{}'.format(line[:count-2]) + '}'
             + '{' + 'name={' + '{}'.format(line[:count-2]) + '},'+ 'description={' + '{}'.format(line[count-1:]) + '}}')
       line = fp.readline()   

'''
\newglossaryentry{action potential}{
	name={action potential},
	description={Elementary neural signal; determined by the precisely timed opening and closing of ion channels.}
}
'''