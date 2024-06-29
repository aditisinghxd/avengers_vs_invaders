#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from tabulate import tabulate


country_hq = pd.read_csv("C:/Users/DELL/Downloads/country_hq.txt", sep='\t')

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


# In[2]:


country_hq.head()


# In[3]:


ARG.head()


# In[4]:


headquartrs = pd.unique(country_hq[['Aliens', 'Predators', 'D&D Monsters']].values.ravel('K'))
headquartrs


# In[5]:


species = pd.unique(ARG['ARG-Headquarter'].values.ravel('K'))
species


# In[6]:


'''arg = pd.unique(ARG[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
aircraft =pd.unique(AIRCRAFT[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
bra = pd.unique(BRA[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
can = pd.unique(CAN[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
col =pd.unique(COL[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
de = pd.unique(DE[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
ind = pd.unique(IND[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
mex = pd.unique(MEX[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
nld =pd.unique(NLD[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
nor = pd.unique(NOR[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
ocean =pd.unique(OCEAN[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
pak =pd.unique(PAK[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
tur = pd.unique(TUR[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
uae = pd.unique(UAE[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
uk = pd.unique(ARG[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
us = pd.unique(US[['attack_role', 'defense_role', 'healing_role']].values.ravel('K'))
concatenated_array = np.concatenate((arg, aircraft, bra, can, col, de,ind,mex,nld,nor, ocean,pak,tur,uae,uk,us))
unique_elements = pd.unique(concatenated_array)'''


# In[7]:


unique_elements = {'avengers': ['nova','agent.venom', 'batman@dc-world.com', 'hulk', 'havok',
       'sunspot', 'smasher', 'hawkeye', 'rogue', 'abyss', 'iron.fist',
       'power.women', 'doctor.strange', 'daredevil', 'storm', 'quake',
       'red.hulk', 'capatain.america', 'captain.britain', 'vision',
       'black.widow', 'spider.man', 'iron.man', 'thor', 'wasp', 'ant.man',
       'deadpool', 'star.brand', 'shang-chi', 'sentry', 'wolverine',
       'echo', 'ares', 'hercules', 'stature', 'amadeus_cho', 'valkyrie',
       'quicksilver', 'scarlet.witch']}


# In[8]:


avengersdf = pd.DataFrame(unique_elements)
print(avengersdf)


# In[9]:


tables = {'ARG': ARG,'Aircraft': AIRCRAFT,'BRA': BRA,'CAN': CAN,
          'COL': COL,'DE': DE,'IND': IND,'MEX': MEX,
          'NLD': NLD,'NOR': NOR,'Ocean': OCEAN,'PAK': PAK,
          'TUR': TUR,'UAE': UAE,'UK': UK,'US': US}


# In[10]:


for tablename, table in tables.items():
        table.set_index(table.columns[0], inplace=True)


# In[11]:


for avenger in avengersdf['avengers']:
    # newtable ---> individual tables
    newtable = pd.DataFrame(index=headquartrs, columns=species)
    newtable.index.name = avenger
    indices_named= [] # to collect the corresponding index for a particular cell value
    dictionary={}
    for tablename, table in tables.items():
        head = table.index.name
        for row in range(table.shape[0]):
            for col in range(table.shape[1]): 
                if table.iloc[row, col] == avenger:
                    indices_named.append((table.index[row], table.columns[col]))
        dictionary[head] = indices_named
        indices_named= []
    # now dictionay (headquarter: (species, role))----> newtable
    for hq, positions in dictionary.items():
        for invadingspecies, role in positions:
            if hq in newtable.index:
                if invadingspecies in newtable.columns:
                    newtable.at[hq, invadingspecies] = role[0].upper()
    dictionary={}
    bold = '\033[1m'
    reset = '\033[0m'
    print(f"{bold}{avenger.upper()}{reset}", newtable,'\n', '\n')
    


# ## Optional Task 1

# In[12]:


for tablename, table in tables.items():
    csv_markdown = tabulate(table, tablefmt="pipe", headers="keys")
    print("\nMarkdown table for CSV data:")
    print(csv_markdown)
    with open(f"{tablename}.md", 'w') as f:
        f.write(csv_markdown)


# In[13]:


csv_markdown = tabulate(country_hq, tablefmt="pipe", headers="keys")
print("\nMarkdown table for CSV data:")
print(csv_markdown)
with open("country_hq.md", 'w') as f:
    f.write(csv_markdown)


# In[14]:


for avenger in avengersdf['avengers']:
    # newtable ---> individual tables
    newtable = pd.DataFrame(index=headquartrs, columns=species)
    newtable.index.name = avenger
    indices_named= [] # to collect the corresponding index for a particular cell value
    dictionary={}
    for tablename, table in tables.items():
        head = table.index.name
        for row in range(table.shape[0]):
            for col in range(table.shape[1]): 
                if table.iloc[row, col] == avenger:
                    indices_named.append((table.index[row], table.columns[col]))
        dictionary[head] = indices_named
        indices_named= []
    # now dictionay (headquarter: (species, role))----> newtable
    for hq, positions in dictionary.items():
        for invadingspecies, role in positions:
            if hq in newtable.index:
                if invadingspecies in newtable.columns:
                    newtable.at[hq, invadingspecies] = role[0].upper()
    dictionary={}
    bold = '\033[1m'
    reset = '\033[0m'
    print(f"{bold}{avenger.upper()}{reset}", newtable,'\n', '\n')
    csv_markdown = tabulate(newtable, tablefmt="pipe", headers="keys")
    print(f"\nMarkdown table for{avenger} data:")
    print(csv_markdown)
    with open(f"{avenger}.md", 'w') as f:
        f.write(csv_markdown)

