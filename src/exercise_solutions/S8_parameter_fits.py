""" Solution Exercises Chapter 'Parameter Fits' """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# For the fitting
import statsmodels.formula.api as smf


def get_data(in_file: str=None) -> pd.DataFrame:
    """Get data from NOAA about the global CO2-levels
    
    Parameters
    ----------
        in_file : Name of locally stored data-file. If 'in_file' is 'None',
            the data are retrieved from the web
    
    Return
    ------
        df : in_data, with the column names
            ['Year', 'index', 'date', 'avg', 'co2', 'trend', 'nr_days']
    """
    
    if in_file is None:
        # You can also easily work with the latest data from the web:
        print('Getting the data from the web')
        
        ftp_address = 'aftp.cmdl.noaa.gov'
        remote_dir = 'products/trends/co2'
        remote_file = 'co2_mm_mlo.txt'
        local_file = 'co2.txt'
        
        ftp = FTP(ftp_address)
        ftp.login(user='', passwd='')
        ftp.cwd(remote_dir)
        
        lf = open(local_file, 'wb')
        ftp.retrbinary('RETR ' + remote_file, lf.write, 1024)
        lf.close()
        ftp.quit()
        
        print(f'Data saved locally, as {local_file}')
    else:
        if os.path.exists(in_file):
            local_file = in_file
            print('Using local data ')
        else:
            raise IOError(f'{in_file} does not exist!')

    df = pd.read_csv(local_file, header=None, skiprows=72,
            delim_whitespace=True)
    df.columns = ['Year', 'index', 'date', 'avg', 'co2', 'trend', 'nr_days']
    
    return df


def polynomial_fits(data: pd.DataFrame):
    """"Linear, quadratic and cubic fits to the data
    
    Parameters
    ----------
        data : input data, from 'get_data'
    """

    p_1 = np.polyfit(data.date, data.co2, 1)
    p_2 = np.polyfit(data.date, data.co2, 2)


    # Since there are numerical problems with large-x-values,
    # center them around 2000
    data['year2000'] = data['date']-2000
    explanation = """Fitting a polynomial with a large offset on the x-axis can lead to numerical instabilities.
    To avoid that problem, we subtract the main bias of 2000 years.
    This is part of the process of "normalization", which is commonly used in areas such as machine learning
    to optimize the numerical results. """
    print(explanation)
    p_2_year2000 = np.polyfit(data.year2000, data.co2, 2)
    p_3_year2000 = np.polyfit(data.year2000, data.co2, 3)


    # Show the quadratic fit-values
    print(f'\nquadratic fit: {p_2}')
    print(f'quadratic fit around 2000: {p_2_year2000}\n')
    
    # Fitted polynomials
    fit_x = np.linspace(np.min(data.date), np.max(data.date), 100)
    fit_x_year2000 = fit_x - 2000
    
    fit_y_1 = np.polyval(p_1, fit_x)
    fit_y_2 = np.polyval(p_2_year2000, fit_x_year2000)
    fit_y_3 = np.polyval(p_3_year2000, fit_x_year2000)
    
    # Show the data and the fits
    plt.plot('date', 'co2', data=data, label='measurements')
    plt.plot(fit_x, fit_y_1, label='linear fit')
    plt.plot(fit_x, fit_y_2, label='quadratic fit')
    plt.plot(fit_x, fit_y_3, label='cubic fit')
    
    plt.legend()
    plt.show()


def CIs_and_residuals(data: pd.DataFrame) -> dict:    
    """Use 'statsmodels' to find confidence-intervals, and plot the residuals
    
    Parameters
    ----------
        data : input data, from 'get_data'

    Returns
    -------
        residuals : x/y-values for the residuals
    """
    
    
    # Linear fit
    mod = smf.ols(formula='co2 ~ year2000', data=data)
    res_1 = mod.fit()
    # print(res_1.summary())
    
    # If you only want the confidence intervals, you get them with
    ci = res_1.conf_int()
    ci.columns = ['Lower', 'Upper']
    print(f'The CIs for the linear fit are {ci}')
    
    # Quadratic fit
    mod = smf.ols(formula='co2 ~ year2000 + I(year2000**2)', data=data)
    res_2 = mod.fit()
    print('\nQuadratic fit -------------------------\n')
    print(res_2.summary())
    
    # Cubic fit
    mod = smf.ols(formula='co2 ~ year2000 + I(year2000**2) + I(year2000**3)',
            data=data)
    res_3 = mod.fit()
    #print(res_3.summary())
    
    # Which ones are significant?
    print('\Which order of fit do we need?')
    for (res, order) in zip([res_1, res_2, res_3],
                            ['linear', 'quadratic', 'cubic']):
        ci = res.conf_int()
        ci.columns = ['Lower', 'Upper']
        if ci.iloc[-1].prod() < 0:
            print(f'\nThe {order} fit is not significant.')
    
    # For the quadratic fit, show the residuals
    plt.plot(data.year2000, res_2.resid, '.')
    plt.title('Residuals for the quadratic fit')
    plt.show()
    
    # Select a range with an approximately constant offset, around 2010
    good_years = (data.year2000>4) & (data.year2000<16)
    
    residuals = {}
    residuals['x'] = data.year2000[good_years]
    residuals['y'] = res_2.resid[good_years]

    return residuals
    

    
    # Prepare the data for the sine-fit
    phi = np.deg2rad(np.arange(len(sim_x))*30)
    data_sine = pd.DataFrame({'phi':phi, 'sine':np.sin(phi),
                              'cosine':np.cos(phi), 'resid':sim_y})
    
    # Make the sine-fit
    mod_sine = smf.ols(formula='resid ~ sine + cosine', data=data_sine)
    res_sine = mod_sine.fit()
    
    fit = res_sine.params
    amp = np.sqrt(fit.sine**2 + fit.cosine**2)
    delta = np.arctan2(fit.sine, fit.cosine)
    
    print(f'\nAmplitude of annual CO2-variations: {amp:5.3f}')    


def sinefit(data: pd.DataFrame):    
    """Make a sine-fit
    
    Parameters
    ----------
        data : residuals, from 'CIs_and_residuals'
    """
    
    # Prepare the data for the sine-fit
    phi = np.deg2rad(np.arange(len(data['x']))*30)
    data_sine = pd.DataFrame({
        'phi':phi,
        'sine':np.sin(phi),
        'cosine':np.cos(phi),
        'resid':data['y'] })
    
    # Make the sine-fit
    mod_sine = smf.ols(formula='resid ~ sine + cosine', data=data_sine)
    res_sine = mod_sine.fit()
    
    fit = res_sine.params
    amp = np.sqrt(fit.sine**2 + fit.cosine**2)
    delta = np.arctan2(fit.cosine, fit.sine)
    offset = fit.Intercept

    # Show values and fit
    plt.plot(phi, data['y'], '.-', label='values')
    plt.plot(phi, offset + amp * np.sin(phi + delta), label='fit')
    plt.legend()
    plt.show()

    print(f'\nAmplitude of annual CO2-variations: {amp:5.3f}')    
    
    
if __name__ == '__main__':
    data_dir = '../../data'
    file_name = 'co2_mm_mlo.txt'
    in_file = os.path.join(data_dir, file_name)

    data = get_data(in_file)    
    polynomial_fits(data)    
    res_val = CIs_and_residuals(data)
    sinefit(res_val)
