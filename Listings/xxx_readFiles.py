pwd
%bookmark -l
cd bsa
ls
pwd
cd ..
ls
cd BSA
ls
cd Code_Python/
%bookmark bsa
ls data.*
edit data.txt
in_file = 'data.txt'
df = pd.read_csv(in_file, skiprows=3, delimiter='\t')
df
df[0]
df
df.head()
edit data.txt
df = pd.read_csv(in_file, skiprows=3, delimiter='\t', header=None)
df.head()
df.tail()
edit data.csv
in_file = 'data.csv'
df = pd.read_csv(in_file, header=None)
df.head()
df.tail
df.tail()
edit data_tab.txt
ls da*
in_file = data_tab.txt
edit data_tab.txt
df = pd.read_csv(in_file, header=None, delimiter='\t')
df.head()
in_file = 'data_tab.txt'
df = pd.read_csv(in_file, header=None, delimiter='\t')
df.head()
df.tail()
in_file = 'data.xls'
df = pd.read_excel(in_file)
df.head()
df = pd.read_excel(in_file, header=None)
df.head()
df.tail()
in_file = 'data.mat'
pd.read_hdf(in_file)
from scipy.io import loadmat
data = loadmat(in_file)
data
type(data)
data.keys()
data['dataMat']
x = data['dataMat']
type(x)
x[:5,:]
%hist -f read_files.py
