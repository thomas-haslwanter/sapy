""" Solution to Exercise 'Mixed Inputs', 'Data Input' """ 

# author:   Thomas Haslwanter
# date:     April-2021

# Get the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlopen
import io
import zipfile
import os


def getDataDobson(url: str, inFile: str) -> pd.DataFrame:
    """ Extract data from a zipped-archive on the web. """

    # get the zip-archive
    GLM_archive = urlopen(url).read()

    # make the archive available as a byte-stream
    zipdata = io.BytesIO()
    zipdata.write(GLM_archive)

    # extract the requested file from the archive, as a pandas XLS-file
    myzipfile = zipfile.ZipFile(zipdata)
    xlsfile = myzipfile.open(inFile)

    # read the xls-file into Python, using Pandas, and return the extracted data
    xls = pd.ExcelFile(xlsfile)
    df  = xls.parse('Sheet1', skiprows=2)

    return df


if __name__ == '__main__':
    # Go to the data-directory
    in_dir = '../../data'
    os.chdir(in_dir)

    # Read in a mixed CSV file, and show the top and bottom data
    inFile1 = 'swim100m.csv'
    data = pd.read_csv(inFile1)

    # Show the data
    print(data.head())
    print(data.tail())

    # Read in an MS-Excel file, and show the bottom data
    inFile2 = 'Table 2.8 Waist loss.xls'

    xls = pd.ExcelFile(inFile2)
    data = xls.parse('Sheet1', skiprows=2)

    print(data.tail())

    # Read in a zipped data-file from the WWW
    #url = 'https://www.routledge.com/downloads/K32369/GLM.dobson.data.zip'
    url = 'https://work.thaslwanter.at/sapy/GLM.dobson.data.zip'
    inFile = r'Table 2.8 Waist loss.xls'

    df = getDataDobson(url, inFile)
    print(df.tail())

