""" Test exercise solutions for
'Hands-on Introduction to Signalanalysis with Python'
"""

# author:   Thomas Haslwanter
# date:     May-2020

# additional packages
import os
import sys

figDir = os.path.join('..', r'src/code_quantlets')
os.chdir(figDir)
startNr = 0     # if you don't want to go through all files

# make sure local imports are working
sys.path.append('.')

pyList = [file for file in os.listdir('.') if (file[-3:]=='.py')]
for number, file in enumerate(pyList):
    print(f'{number+1}/{len(pyList)}: {file}')
    if number >= startNr:
        exec(open(file).read())
    
