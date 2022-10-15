#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1 Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и начинается с 0. На вход функция получает целое число n_customers (количество клиентов).
# 2 Функция, аналогичная первой, если ID начинается с произвольного числа. На вход функция получает целые числа: n_customers (количество клиентов) и n_first_id (первый ID в последовательности).


# In[ ]:


import pandas as pd


# In[67]:


# 1 функция
def groups_count(n_customers):
    ids = [i for i in range(n_customers)] # создадим список с id клиентов начиная с 0
    sums = list( # создадим список с суммой всех цифр id из списка ids
        map( # применим к каждому элементу списка ids функцию, описание ниже 
            lambda x: sum([int(i) for i in str(x)]), # функция: создаем список с цифрами входящими в id и суммируем их
            ids)
    )
    return pd.Series(sums).value_counts(sort=False) # возвращаем Series, отсортированный по группам с подсчетом 
                                                    # это и будет число покупателей, попадающих в каждую группу  


# In[71]:


# 2 функция
def groups_count_from(n_customers, n_first_id):
    ids = [i for i in range(n_first_id, n_first_id + n_customers)] # создадим список с id клиентов начиная с n_first_id
    sums = list( # создадим список с суммой всех цифр id из списка ids
        map( # применим к каждому элементу списка ids функцию, описание ниже 
            lambda x: sum([int(i) for i in str(x)]), # функция: создаем список с цифрами входящими в id и суммируем их
            ids)
    )
    return pd.Series(sums).value_counts(sort=False) # возвращаем Series, отсортированный по группам с подсчетом 
                                                    # это и будет число покупателей, попадающих в каждую группу


# In[ ]:


# альтернативный вариант
import pandas as pd
groups = []
for id in [i for i in range(12000)]:
    sum = 0
    for digit in str(id):
        sum += int(digit)
    groups.append(sum)
pd.Series(groups).value_counts(sort=False)

