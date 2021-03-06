# -*- coding: utf-8 -*-
"""Sorting Algorithms


Original file is located at
    https://colab.research.google.com/drive/1x8ygFPVEQVQQv0pEkCWNC3NfKuZllTib
"""

import time
import random

#making a long unsorted list
long_random_list = random.sample(range(0,10000), 100)

#bubble sort

def bubble_sort(liste):
  sort_liste = liste
  
  for i in range(len(liste) -1):
    if sort_liste[i] > sort_liste[i + 1]:
      z = sort_liste[i]
      sort_liste[i] = sort_liste[i + 1]
      sort_liste[i + 1] = z   
  for i in range(len(liste) - 1):
    if sort_liste[i] > sort_liste[i + 1]:
      bubble_sort(sort_liste)
      break
  return sort_liste     
    
a = long_random_list
start = time.time()
b = bubble_sort(a)
end = time.time()
print(b)
print(end - start)

# cocktail shaker sort
def cocktail_shaker_sort(liste):
    sort_liste = liste

    for i in range(len(liste) - 1):
        if sort_liste[i] > sort_liste[i + 1]:
            z = sort_liste[i]
            sort_liste[i] = sort_liste[i + 1]
            sort_liste[i + 1] = z
    d = len(liste) - 2
    for i in range(len(liste) - 2):
        if sort_liste[d] < sort_liste[d - 1]:
            z = sort_liste[d]
            sort_liste[d] = sort_liste[d - 1]
            sort_liste[d - 1] = z
        d -= 1  
    a = sort_liste[1:len(liste) - 1]

    for i in range(len(liste) - 1):
        if sort_liste[i] > sort_liste[i + 1]:
            cocktail_shaker_sort(a)
            sort_liste[1:len(liste) - 1] = a
            break
    return sort_liste


a = long_random_list
start = time.time()
b = cocktail_shaker_sort(a)
end = time.time()
print(b)
print(end - start)

#insertion sort

def insertion_sort(liste):
  sort_list = []
  sort_list.append(liste[0])
  del(liste[0])
  for element in liste:
    i = 0
    for olement in sort_list:
      if element < olement:
        sort_list.insert(i, element) 
        break
      elif element > olement and i == len(sort_list) -1:
        sort_list.append(element)
      i += 1
  return sort_list

a = long_random_list
start = time.time()
b = insertion_sort(a)
end = time.time()
print(b)
print(end - start)

#quicksort(sort of: done with average)
def cal_av(array):
  sum_of_array = 0
  for element in array:
    sum_of_array += element
  return sum_of_array / len(array)

final_list = []

def flatten(liste):
    flat_liste = []
    for element in liste:

        if type(element) == list:
            flatten(element)
        if type(element) != list:
            final_list.append(element)
            return
    return 

def quicksort(liste):
  if len(liste) <= 1:
    return liste
  av = cal_av(liste)
  smaller = []
  bigger = []
  
    
  for element in liste:
    if element < av:
      smaller.append(element)
    else:
      bigger.append(element)
  sort_list = []
  sort_list.append(quicksort(smaller))
  sort_list.append(quicksort(bigger))
  return sort_list
  
a = long_random_list
start = time.time()
b = flatten(quicksort(a))
end = time.time()
print(final_list)
print(end - start)

#selection sort

def selection_sort(liste):
  sort_list = []
  for i in range(len(liste)):
    smallest = liste[0]
    for d in range(1, len(liste)):
      if liste[d] < smallest:
        smallest = liste[d]
    sort_list.append(smallest)
    liste.remove(smallest)
  return sort_list

a = long_random_list
start = time.time()
b = selection_sort(a)
end = time.time()
print(b)
print(end - start)
