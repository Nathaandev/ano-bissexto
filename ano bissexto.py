ano=int(input('Coloque um ano e veja se ele é bissexto '))

calc= ano % 4

if calc == 0:

   print('Este é um ano bissexto!')

else:
   print('Este não é um ano bissexto!')