filepath = 'C:/Users/diogo/OneDrive/Ambiente de Trabalho/Dissertacao_50513/Abb_50513.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:
       abb = line.split()[0]    
       wrds = line.split()
       eq_spaced_line = " ".join(wrds)                
       count=0
       for i in eq_spaced_line:
           count += 1
           if(i.isspace()):
               break
       print('\\newacronym' + '{' + '{}'.format(abb) + '}'
             + '{' + '{}'.format(abb) + '}'+ '{' +
             '{}'.format(eq_spaced_line[count:]) + '}')
       line = fp.readline()   
