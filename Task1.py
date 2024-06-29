#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from tabulate import tabulate


country_hq = pd.read_csv("C:/Users/DELL/Downloads/country_hq.txt", sep='\t')
task1 =pd.read_csv("C:/Users/DELL/Downloads/task1.txt", sep='\t')

'''csv_markdown = tabulate(task1, tablefmt="pipe", headers="keys")
print(f"\nMarkdown table for task1 data:")
print(csv_markdown)
with open("task1.md", 'w') as f:
    f.write(csv_markdown)'''
    
#HEADQUARTESRS
ARG =pd.read_csv("C:/Users/DELL/Downloads/ARG-Headquarter.txt", sep='\t') 
AIRCRAFT =pd.read_csv("C:/Users/DELL/Downloads/Aircraft-Headquarter.txt", sep='\t') 
BRA =pd.read_csv("C:/Users/DELL/Downloads/BRA-Headquarter.txt", sep='\t') 
CAN =pd.read_csv("C:/Users/DELL/Downloads/CAN-Headquarter.txt", sep='\t') 
COL =pd.read_csv("C:/Users/DELL/Downloads/COL-Headquarter.txt", sep='\t') 
DE =pd.read_csv("C:/Users/DELL/Downloads/DE-Headquarter.txt", sep='\t') 
IND =pd.read_csv("C:/Users/DELL/Downloads/IND-Headquarter.txt", sep='\t') 
MEX =pd.read_csv("C:/Users/DELL/Downloads/MEX-Headquarter.txt", sep='\t') 
NLD =pd.read_csv("C:/Users/DELL/Downloads/NLD-Headquarter.txt", sep='\t') 
NOR =pd.read_csv("C:/Users/DELL/Downloads/NOR-Headquarter.txt", sep='\t') 
OCEAN =pd.read_csv("C:/Users/DELL/Downloads/Ocean-Headquarter.txt", sep='\t') 
PAK =pd.read_csv("C:/Users/DELL/Downloads/PAK-Headquarter.txt", sep='\t') 
TUR =pd.read_csv("C:/Users/DELL/Downloads/TUR-Headquarter.txt", sep='\t') 
UAE =pd.read_csv("C:/Users/DELL/Downloads/UAE-Headquarter.txt", sep='\t') 
UK =pd.read_csv("C:/Users/DELL/Downloads/UK-Headquarter.txt", sep='\t') 
US =pd.read_csv("C:/Users/DELL/Downloads/US-Headquarter.txt", sep='\t') 


# ## Task 1

# In[2]:


country_hq.head()


# In[3]:


task1 = task1.drop(index=task1.index[:1])
task1.head()


# In[4]:


ARG.head()


# In[5]:


RolesList = ['attack_role','defense_role','healing_role']

tables = {'ARG': ARG,'Aircraft': AIRCRAFT,'BRA': BRA,'CAN': CAN,
          'COL': COL,'DE': DE,'IND': IND,'MEX': MEX,
          'NLD': NLD,'NOR': NOR,'Ocean': OCEAN,'PAK': PAK,
          'TUR': TUR,'UAE': UAE,'UK': UK,'US': US}


# In[6]:


task2 = {
    'Country_Code': [],
    'Invader_Species': [],
    'Role': [],
    'Email': []
}
new_data = {}
task2 = pd.DataFrame(task2)


# In[7]:


for Aliens in country_hq['Aliens']:
    new_data['Invader_Species']= 'aliens'
    headquarter = Aliens
    headquarter = headquarter[:-12]
    for CountryCode in country_hq['Country Code']:
        new_data['Country_Code']= CountryCode
        for tablename, table in tables.items():
            if tablename == headquarter:
                for roles in RolesList:
                    new_data['Role'] = roles
                    avenger = table.loc[table[Aliens] == 'aliens',roles ].values[0]
                    avenger = str(avenger)
                    Email = f"{avenger.lower()}@avengers.com"
                    new_data['Email'] = Email
                    task2 = task2.append(new_data, ignore_index=True)
    break
            


# In[8]:


task1= task1.append(task2, ignore_index= True)
task1


# In[9]:


task2 = {
    'Country_Code': [],
    'Invader_Species': [],
    'Role': [],
    'Email': []
}
new_data = {}
task2 = pd.DataFrame(task2)


# In[10]:


for Predators in country_hq['Predators']:
    new_data['Invader_Species']= 'predators'
    headquarter = Predators
    headquarter = headquarter[:-12]
    for CountryCode in country_hq['Country Code']:
        new_data['Country_Code']= CountryCode
        for tablename, table in tables.items():
            if tablename == headquarter:
                for roles in RolesList:
                    new_data['Role'] = roles
                    avenger = table.loc[table[Predators] == 'predators',roles ].values[0]
                    avenger = str(avenger)
                    Email = f"{avenger.lower()}@avengers.com"
                    new_data['Email'] = Email
                    task2 = task2.append(new_data, ignore_index=True)
    break
            


# In[11]:


task1= task1.append(task2, ignore_index= True)


# In[12]:


task1.tail()


# In[13]:


task2 = {
    'Country_Code': [],
    'Invader_Species': [],
    'Role': [],
    'Email': []
}
new_data = {}
task2 = pd.DataFrame(task2)


# In[14]:


for DnDMonsters in country_hq['D&D Monsters']:
    headquarter1 = DnDMonsters
    headquarter = headquarter1[:-12]
    for CountryCode in country_hq['Country Code']:
        new_data['Country_Code']= CountryCode
        for tablename, table in tables.items():
            if tablename == headquarter:
                table = table.drop(index=table.index[:2])
                for species in table[headquarter1]:
                    new_data['Invader_Species']= species
                    for roles in RolesList:
                        new_data['Role'] = roles
                        avenger = table.loc[table[DnDMonsters] == species ,roles ].values[0]
                        avenger = str(avenger)
                        Email = f"{avenger.lower()}@avengers.com"
                        new_data['Email'] = Email
                        task2 = task2.append(new_data, ignore_index=True)
    break
            


# In[15]:


task1= task1.append(task2, ignore_index= True)


# In[16]:


task1.tail()


# In[17]:


Final_Table_Task1 = task1


# In[18]:


'''csv_markdown = tabulate(Final_Table_Task1, tablefmt="pipe", headers="keys")
print(f"\nMarkdown table for Final_Table_Task1 data:")
print(csv_markdown)
with open("Final_Table_Task1.md", 'w') as f:
    f.write(csv_markdown)'''

