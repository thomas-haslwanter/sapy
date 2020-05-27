""" Test routine for source code that generates 'F'igures """

# author:   Thomas Haslwanter
# date:     May-2020

# additional packages
import os
import sys

figDir = os.path.join('..', r'src/figures')
os.chdir(figDir)
startNr = 0     # if you don't want to go through all files

# make sure local imports are working
sys.path.append('.')

pyList = [file for file in os.listdir('.') if (file[-3:]=='.py' and file[0]=='F')]
for number, file in enumerate(pyList):
    print(f'{number+1}/{len(pyList)}: {file}')
    if number >= startNr:
        exec(open(file).read())
    
