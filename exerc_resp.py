# operadores_python
# exercicios com operadores em python

#005 - Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
  num01=int(input('Digite o numero: '))
  print('Analisando o valor {}, seu antecessor e: {} e o seu sucessore: {}'.format(num01, (num01-1), (num01+1)))


#006 - Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
  nint = int(input('Digite um numero: '))
  do = nint*2
  tri = nint*3
  ra = nint**(1/2)
  print('Seu numero {}: tem como dobro {}, tem como triplo {}.'.format(nint,do,tri))
  print('Sua raiz quadrada é: {}' .format(ra))
  

#007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
  print('Calculando a média. Digite sua nota de:')
  bim1=float(input('1° Bimestre: '))
  bim2=float(input('2° Bimestre: '))
  bim3=float(input('3° Bimestre: '))
  bim4=float(input('4° Bimestre: '))
  media=float((bim1+bim2+bim3+bim4)/4)
  print('Notas: \n1° Bimestre: {}. \n2° Bimestre: {}. \n3° Bimestre: {}. \n4° Bimestre: {}.'.format(bim1,bim2,bim3,bim4))
  print('Média final: {}.'.format(media))
  

#008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros. 
  print('Digite um numero que vale em metros (m)\n')
  metros = float(input('Insira o numero: '))
  qu = metros/1000 
  he = metros/100 
  deca = metros/10 
  m = metros 
  dci = metros*10 
  cm = metros*100 
  mm = metros*1000 
  print('Analisando...\n Quilometros: {}\n Hectametros: {}\n Decametros: {} Metros: {}\n Decimetros: {}\n Centimetros: {}\n Milimetros: {}'.format(qu,he,deca,m,dci,cm,mm))


#009 - Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
  n = int(input('Insira um numero: '))
  print('-'*15)
  print('{} x {} = {}'.format(n,1,n*1))
  print('{} x {} = {}'.format(n,2,n*2))
  print('{} x {} = {}'.format(n,3,n*3))
  print('{} x {} = {}'.format(n,4,n*4))
  print('{} x {} = {}'.format(n,5,n*5))
  print('{} x {} = {}'.format(n,6,n*6))
  print('{} x {} = {}'.format(n,7,n*7))
  print('{} x {} = {}'.format(n,8,n*8))
  print('{} x {} = {}'.format(n,9,n*9))
  print('{} x {} = {}'.format(n,10,n*10))
  print('-'*15)


#010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. considere - US$1,00 = R$3,27
  print('Digite a quantia a ser convertida')
  r = float(input('R$: '))
  d = r/5.42 #U
  e = r/6.14 #€
  i = r/4.76 #¥
  print('Dolar: UR${:.2f} \nEuro: €${:.2f} \nIene: ¥${:.2f}' .format(d,e,i))
  # ou
  print('Digite a quantia a ser convertida')
  N=float(input('R$: '))
  print(f'R${N} = U${N/5.52 :.2f}')
  print(f'R${N} = €{N/6.30 :.2f}')
  print(f'R${N} = ¥{N/0.048 :.2f}')


  #011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m². 
  lar = float(input('Largura da parede: '))
  alt = float(input('Altura da parede: '))
  area = lar*alt
  print('Parede: \n   Dimensao {} x {} \n   Area {}m².' .format(lar,alt,area))


#012 - Faca um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 
  preco = float(input('Qual e o preco do produto? R$ '))
  novo = preco - (preco * 5 / 100)
  print('O produto que custava R$ {:.2f}, na promocao desconto 5%, vai custar R$ {:.2f}' .format(preco,novo))


#013 - Faça um algoritimo que leia o salario de um funcionario e mostre novo salario, com 15% de aumento.
  sal = float(input('Salario: R$ '))
  salnv = sal+(sal*15/100)
  print('Salario R$ {} \nReajuste +15% : R$ {}' .format(sal,salnv))


#014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
  c = float(input('Temperatura: °C: '))
  f = ((9*c)/5)+32
  print('Temperatura em °F: {}' .format(f))

#015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

