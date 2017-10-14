# Wrote this on a deadline, only for its results, at a time when I knew very little Python. 
# I should have taken the time to learn basics and iterate properly. 
# Someday (soon?) I will go back and clean this up.

import numpy as np;
import pandas as pd;
import os;
import networkx as nx;
from networkx.utils import open_file, make_str;
print os.getcwd()

data = pd.read_csv("[LOCATION].csv", low_memory = False);
datacoord = data[data.gname.notnull() & data.gname2.notnull()];
dcmini = datacoord.loc[:,['ID', 'iyear', 'imonth', 'gname', 'gname2', 'gname3']];
perp_list.to_csv('perp_list.csv');

# each event had up to three perps. since we are dealing in edges and not hyperedges, 
# each event will therefore be associated with 3-choose-2 = 3 edges based on which 2 of the 3 perps
# are considered as the pair that constitutes a given edge. 
e1 = datacoord.ix[:,['gname', 'gname2']];
e2 = datacoord.ix[:,['gname2', 'gname3']];
e3 = datacoord.ix[:,['gname', 'gname3']];

# rename the pair members as something clearer for our purpose: nodes of a graph.
# this should be accomplished with iteration over indexed nodes ("coordinates") of each indexed edge
# not like this 
e1['node1'] = e1['gname'];
e1['node2'] = e1['gname2'];
e1 = e1.ix[:,['node1','node2']];

e2['node1'] = e2['gname2'];
e2['node2'] = e2['gname3'];
e2 = e2.loc[:,['node1','node2']];

e3['node1'] = e3['gname'];
e3['node2'] = e3['gname3'];
e3 = e3.ix[:,['node1','node2']];

# getting rid of pairs with an empty member 
# resulting from events where there were not 3 perps.
#iterate through the indexed edges instead of this
e1 = e1.dropna();
e2 = e2.dropna();
e3 = e3.dropna();

# recalling that each event is associated with up to three edges
# concatenate all these edges from all these events
# and write them to an edgelist.
# append multiple items in one go instead of this
e = e1.append(e2);
e = e.append(e3);
e.to_csv('edges.csv');

# I previously made the perp list by concatenating the perp1 perp2 and perp3 columns
# then taking unique strings
# so supposing we are starting from the point where we had perp and edge lists saved as files already
perp_list = pd.read_csv("perp_list.csv");
edges = pd.read_csv("edges.csv")
# make an empty graph
G=nx.Graph();
# feed it edges
edgelist = nx.from_pandas_dataframe(edges)
# feed it nodes
G.add_nodes_from(perp_list);
# [Commenting this code so late that I forgot what this does. To be filled in later.]
test = e.replace(to_replace=perp_list, )

# quantification of categorical traits 

# recalling what we have...
print("Total rows: {0}".format(len(data)));
print(list(data));
# quantify the traits. 1 is least governmental, 3 is most. 
data = data.replace(to_replace='Private Citizens & Property', value=1);
data = data.replace(to_replace='Journalists & Media', value=1);
data = data.replace(to_replace='Educational Institution', value=1);
data = data.replace(to_replace='Abortion Related', value=1);
data = data.replace(to_replace='Business', value=1);
data = data.replace(to_replace='Tourists', value=1);
data = data.replace(to_replace='Food or Water Supply', value=1);
data = data.replace(to_replace='Telecommunication', value=1);
data = data.replace(to_replace='Utilities', value=1);
data = data.replace(to_replace='Transportation', value=1);
data = data.replace(to_replace='Airports & Aircraft', value=2);
data = data.replace(to_replace='Maritime', value=2);
data = data.replace(to_replace='NGO', value=2);
data = data.replace(to_replace='Religious Figures/Institutions', value=2);
data = data.replace(to_replace='Terrorists/Non-State Militias', value=2);
data = data.replace(to_replace='Violent Political Parties', value=2);
data = data.replace(to_replace='Government (General)', value=3);
data = data.replace(to_replace='Police', value=3);
data = data.replace(to_replace='Military', value=3);
data = data.replace(to_replace='Government (Diplomatic)', value=3);
# setting unknown and other to 2 because averaging will come into play. 
# it's not great, but it's better than picking 3 or 1
# or giving up those data points
data = data.replace(to_replace='Unknown', value=2);
data = data.replace(to_replace='Other', value=2);

#comment coming
data = data.apply(pd.to_numeric, errors='coerce');
# comment coming
df2 = data;
# comment coming
df2['targtype3_txt'] = np.where((df2['targtype3_txt'].isnull()) & (df2['targtype2_txt'].notnull()), (df2['targtype1_txt'] + df2['targtype2_txt'])/2, df2['targtype3_txt']);
df2['targtype3_txt'] = np.where((df2['targtype3_txt'].isnull()) & (df2['targtype2_txt'].isnull()), df2['targtype1_txt'], df2['targtype3_txt']);
df2['targtype2_txt'] = np.where((df2['targtype2_txt'].isnull()), df2['targtype1_txt'], df2['targtype2_txt']);
df2['targ'] = (df2['targtype1_txt']+df2['targtype2_txt']+df2['targtype3_txt'])/3;
df2.targtype2_txt
df2.targtype3_txt

# comment coming
df2['perpknown'] = np.where(df2['gname'] == 2, 0, 1);
df2['coord'] = np.where(((df2['gname2'].notnull() | df2['gname3'].notnull()) | (df2['gname2'].notnull() & df2['gname3'].notnull())), 1, 0);
df2['perplocal'] = np.where((df2['natlty1'] == df2['region_gtdcode']) | (df2['natlty2'] == df2['region_gtdcode']) | (df2['natlty3'] == df2['region_gtdcode']), 1, 0);

# comment coming
df2['weapbiological'] = np.where((df2['weaptype1_code'] == 1) | (df2['weaptype2_code'] == 1) | (df2['weaptype3_code'] == 1) | (df2['weaptype4_code'] == 1), 1, 0);
df2['weapchemical'] = np.where((df2['weaptype1_code'] == 2) | (df2['weaptype2_code'] == 2) | (df2['weaptype3_code'] == 2) | (df2['weaptype4_code'] == 2), 1, 0);
df2['weapradiological'] = np.where((df2['weaptype1_code'] == 3) | (df2['weaptype2_code'] == 3) | (df2['weaptype3_code'] == 3) | (df2['weaptype4_code'] == 3), 1, 0);
df2['weapnuclear'] = np.where((df2['weaptype1_code'] == 4) | (df2['weaptype2_code'] == 4) | (df2['weaptype3_code'] == 4) | (df2['weaptype4_code'] == 4), 1, 0);
df2['weapfirearms'] = np.where((df2['weaptype1_code'] == 5) | (df2['weaptype2_code'] == 5) | (df2['weaptype3_code'] == 5) | (df2['weaptype4_code'] == 5), 1, 0);
df2['weapexplosive'] = np.where((df2['weaptype1_code'] == 6) | (df2['weaptype2_code'] == 6) | (df2['weaptype3_code'] == 6) | (df2['weaptype4_code'] == 6), 1, 0);
df2['weapfake'] = np.where((df2['weaptype1_code'] == 7) | (df2['weaptype2_code'] == 7) | (df2['weaptype3_code'] == 7) | (df2['weaptype4_code'] == 7), 1, 0);
df2['weapincendiary'] = np.where((df2['weaptype1_code'] == 8) | (df2['weaptype2_code'] == 8) | (df2['weaptype3_code'] == 8) | (df2['weaptype4_code'] == 8), 1, 0);
df2['weapmelee'] = np.where((df2['weaptype1_code'] == 9) | (df2['weaptype2_code'] == 9) | (df2['weaptype3_code'] == 9) | (df2['weaptype4_code'] == 9), 1, 0);
df2['weapvehicle'] = np.where((df2['weaptype1_code'] == 10) | (df2['weaptype2_code'] == 10) | (df2['weaptype3_code'] == 10) | (df2['weaptype4_code'] == 10), 1, 0);
df2['weapsabotage'] = np.where((df2['weaptype1_code'] == 11) | (df2['weaptype2_code'] == 11) | (df2['weaptype3_code'] == 11) | (df2['weaptype4_code'] == 11), 1, 0);
df2['weapother'] = np.where((df2['weaptype1_code'] == 12) | (df2['weaptype2_code'] == 12) | (df2['weaptype3_code'] == 12) | (df2['weaptype4_code'] == 12), 1, 0);
df2['weapunknown'] = np.where((df2['weaptype1_code'] == 13) | (df2['weaptype2_code'] == 13) | (df2['weaptype3_code'] == 13) | (df2['weaptype4_code'] == 13), 1, 0);

# comment coming
df2 = df2.apply(pd.to_numeric, errors='coerce');
# comment coming
df2['attackassassination'] = np.where((df2['attacktype1_code'] == 1) | (df2['attacktype2_code'] == 1) | (df2['attacktype3_code'] == 1), 1, 0);
df2['attackarmedassault'] = np.where((df2['attacktype1_code'] == 2) | (df2['attacktype2_code'] == 2) | (df2['attacktype3_code'] == 2), 1, 0);
df2['attackbomborexplosion'] = np.where((df2['attacktype1_code'] == 3) | (df2['attacktype2_code'] == 3) | (df2['attacktype3_code'] == 3), 1, 0);
df2['attackhijacking'] = np.where((df2['attacktype1_code'] == 4) | (df2['attacktype2_code'] == 4) | (df2['attacktype3_code'] == 4), 1, 0);
df2['attackhostagebarr'] = np.where((df2['attacktype1_code'] == 5) | (df2['attacktype2_code'] == 5) | (df2['attacktype3_code'] == 5), 1, 0);
df2['attackhostagemove'] = np.where((df2['attacktype1_code'] == 6) | (df2['attacktype2_code'] == 6) | (df2['attacktype3_code'] == 6), 1, 0);
df2['attackinfra'] = np.where((df2['attacktype1_code'] == 7) | (df2['attacktype2_code'] == 7) | (df2['attacktype3_code'] == 7), 1, 0);
df2['attackunarmedassault'] = np.where((df2['attacktype1_code'] == 8) | (df2['attacktype2_code'] == 8) | (df2['attacktype3_code'] == 8), 1, 0);
df2['attackunknown'] = np.where((df2['attacktype1_code'] == 9) | (df2['attacktype2_code'] == 9) | (df2['attacktype3_code'] == 9), 1, 0);
df2['attackhostage'] = np.where((df2['attackhostagebarr'] == 1) | (df2['attackhostagemove'] == 1) , 1, 0);
df2['attackassault'] = np.where((df2['attackarmedassault'] == 1) | (df2['attackunarmedassault'] == 1), 1, 0);
df2['intragroup'] = np.where((df2['alternative'] == 3), 1, 0);
df2['intllogcf'] = np.where((df2['INT_LOG'] == 1), 1, 0);
# comment coming
df3 = df2;
df4= df3[df3.alternative != 4];
df4 = df3.loc[:,['iyear', 'imonth', 'extended', 'lat', 'long',
'crit1', 'crit2', 'crit3', 'multiple', 'success', 'suicide', 'perpknown', 'perplocal',
'targ', 'coord', 'weapbiological', 'weapchemical', 'weapradiological', 'weapnuclear', 'weapfirearms', 'weapexplosive', 'weapfake', 'weapincendiary',
'weapmelee', 'weapvehicle', 'weapsabotage', 'weapother', 'weapunknown', 'attackassassination', 'attackarmedassault',
'attackbomborexplosion', 'attackhijacking', 'attackhostagebarr', 'attackhostagemove', 'attackinfra',
'attackunarmedassault', 'attackunknown', 'attackhostage', 'attackassault']];
# comment coming
df5 = df4.dropna();
df5.to_csv('gtdrefined.csv');
