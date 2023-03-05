# -*- coding: utf-8 -*-
"""Variaciones

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JNRtakOzYwNW3J1mkiVaYtBzyCOUxWg0
"""

#VARIACION CON REPETICION
 
def variation_with_repetition(m, n):
    count = 0
    result = [0] * n
    def backtrack(i=0):
        nonlocal count
        if i == n:
            count += 1
            print(count, result)
            return
        for j in range(m):
            result[i] = j
            backtrack(i+1)
    backtrack()
    def formula(m,n):
      return m**n
    print("Las variaciones que pueden salir de aqui son", formula(5,3))

variation_with_repetition(5,3)

#VARIACION SIN REPETICION

def variacion_ordenada(n, k):
  count = 0
  result = []
  def backtrack(first=1):
    nonlocal count
    if len(result) == k:
      count += 1
      print(count, result)
      return
    for i in range(first, n+1):
      result.append(i)
      backtrack(i+1)
      result.pop()
  backtrack()
    
  def formula(m, n):
      resultado = 1
      for i in range(m, m-n, -1):
          resultado *= i
      return resultado
  print("Las variaciones en este caso serian ",formula(5,3))
  

variacion_ordenada(5,3)