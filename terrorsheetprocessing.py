

import numpy as np;
import pandas as pd;
import os;
import networkx as nx;
from networkx.utils import open_file, make_str;
print os.getcwd()

data = pd.read_csv("/Users/jesse/Desktop/gtd.csv", low_memory = False);
datacoord = data[data.gname.notnull() & data.gname2.notnull()];
dcmini = datacoord.loc[:,['ID', 'iyear', 'imonth', 'gname', 'gname2', 'gname3']];
perp_list.to_csv('perp_list.csv');

e1 = datacoord.ix[:,['gname', 'gname2']];
e2 = datacoord.ix[:,['gname2', 'gname3']];
e3 = datacoord.ix[:,['gname', 'gname3']];
e1['node1'] = e1['gname'];
e1['node2'] = e1['gname2'];
e1 = e1.ix[:,['node1','node2']];

e2['node1'] = e2['gname2'];
e2['node2'] = e2['gname3'];
e2 = e2.loc[:,['node1','node2']];

e3['node1'] = e3['gname'];
e3['node2'] = e3['gname3'];
e3 = e3.ix[:,['node1','node2']];

e1 = e1.dropna();
e2 = e2.dropna();
e3 = e3.dropna();
e = e1.append(e2);
e = e.append(e3);
e.to_csv('edges.csv');

perp_list = pd.read_csv("perp_list.csv");
edges = pd.read_csv("edges.csv")
G=nx.Graph();
edgelist = nx.from_pandas_dataframe(edges)
G.add_nodes_from(perp_list);
test = e.replace(to_replace=perp_list, )



print("Total rows: {0}".format(len(data)));
print(list(data));

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
data = data.replace(to_replace='Other', value=2);
data = data.replace(to_replace='Religious Figures/Institutions', value=2);
data = data.replace(to_replace='Terrorists/Non-State Militias', value=2);
data = data.replace(to_replace='Violent Political Parties', value=2);
data = data.replace(to_replace='Government (General)', value=3);
data = data.replace(to_replace='Police', value=3);
data = data.replace(to_replace='Military', value=3);
data = data.replace(to_replace='Government (Diplomatic)', value=3);
data = data.replace(to_replace='Unknown', value=2);

data = data.apply(pd.to_numeric, errors='coerce');

df2 = data;

df2['targtype3_txt'] = np.where((df2['targtype3_txt'].isnull()) & (df2['targtype2_txt'].notnull()), (df2['targtype1_txt'] + df2['targtype2_txt'])/2, df2['targtype3_txt']);
df2['targtype3_txt'] = np.where((df2['targtype3_txt'].isnull()) & (df2['targtype2_txt'].isnull()), df2['targtype1_txt'], df2['targtype3_txt']);
df2['targtype2_txt'] = np.where((df2['targtype2_txt'].isnull()), df2['targtype1_txt'], df2['targtype2_txt']);
df2['targ'] = (df2['targtype1_txt']+df2['targtype2_txt']+df2['targtype3_txt'])/3;
df2.targtype2_txt
df2.targtype3_txt

#this "2" means "unknown" now due to the overapplication in the above code of data.replace
df2['perpknown'] = np.where(df2['gname'] == 2, 0, 1);
df2['coord'] = np.where(((df2['gname2'].notnull() | df2['gname3'].notnull()) | (df2['gname2'].notnull() & df2['gname3'].notnull())), 1, 0);
df2['perplocal'] = np.where((df2['natlty1'] == df2['region_gtdcode']) | (df2['natlty2'] == df2['region_gtdcode']) | (df2['natlty3'] == df2['region_gtdcode']), 1, 0);

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


df2 = df2.apply(pd.to_numeric, errors='coerce');

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

df3 = df2;
df4= df3[df3.alternative != 4];
df4 = df3.loc[:,['iyear', 'imonth', 'extended', 'lat', 'long',
'crit1', 'crit2', 'crit3', 'multiple', 'success', 'suicide', 'perpknown', 'perplocal',
'targ', 'coord', 'weapbiological', 'weapchemical', 'weapradiological', 'weapnuclear', 'weapfirearms', 'weapexplosive', 'weapfake', 'weapincendiary',
'weapmelee', 'weapvehicle', 'weapsabotage', 'weapother', 'weapunknown', 'attackassassination', 'attackarmedassault',
'attackbomborexplosion', 'attackhijacking', 'attackhostagebarr', 'attackhostagemove', 'attackinfra',
'attackunarmedassault', 'attackunknown', 'attackhostage', 'attackassault']];

df5 = df4.dropna();
df5.to_csv('gtdrefined.csv');
