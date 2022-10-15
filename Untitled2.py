#!/usr/bin/env python
# coding: utf-8

# In[52]:


a = 4
#sum = 0
for digit in str(a):
    sum1 += int(digit)

print(sum1)


# In[ ]:



data = [i for i in range(3)]
data


# In[61]:


get_ipython().run_cell_magic('time', '', 'import pandas as pd\ngroups = []\nfor id in [i for i in range(12000)]:\n    sum = 0\n    for digit in str(id):\n        sum += int(digit)\n    groups.append(sum)\npd.Series(groups).value_counts(sort=False)')


# In[ ]:


get_ipython().run_cell_magic('time', '', 'import pandas as pd\ngroups = pd.Series([i for i in range(12)])\nsums = groups.apply\nsums\n\n\n#for id in [i for i in range(12000)]:\n#    sum = 0\n#    for digit in str(id):\n#        sum += int(digit)\n#    groups.append(sum)\n#pd.Series(groups).value_counts(sort=False)')


# In[66]:


get_ipython().run_cell_magic('time', '', 'import pandas as pd\ngroups = [i for i in range(12000)]\nsums = list(map(lambda x: sum([int(i) for i in str(x)]),groups))\npd.Series(sums).value_counts(sort=False)')


# In[67]:


import pandas as pd
def groups_count(n_customers):
    ids = [i for i in range(n_customers)] # создадим список с id клиентов начиная с 0
    sums = list( # создадим список с суммой всех цифр id из списка ids
        map( # применим к каждому элементу списка ids функцию, описание ниже 
            lambda x: sum([int(i) for i in str(x)]), # функция: создаем список с цифрами входящими в id и суммируем их
            ids)
    )
    return pd.Series(sums).value_counts(sort=False) # возвращаем Series, отсортированный по группам с подсчетом 
                                                    # это и будет число покупателей, попадающих в каждую группу
    
     

    


# In[70]:


get_ipython().run_cell_magic('time', '', 'groups_count(12000)')


# In[71]:


import pandas as pd
def groups_count_from(n_customers, n_first_id):
    ids = [i for i in range(n_first_id, n_first_id + n_customers)] # создадим список с id клиентов начиная с n_first_id
    sums = list( # создадим список с суммой всех цифр id из списка ids
        map( # применим к каждому элементу списка ids функцию, описание ниже 
            lambda x: sum([int(i) for i in str(x)]), # функция: создаем список с цифрами входящими в id и суммируем их
            ids)
    )
    return pd.Series(sums).value_counts(sort=False) # возвращаем Series, отсортированный по группам с подсчетом 
                                                    # это и будет число покупателей, попадающих в каждую группу


# In[73]:


get_ipython().run_cell_magic('time', '', 'groups_count_from(12000, 50)')

