"""Short demonstration of data handling with Pandas"""

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


def generate_data():
    """Generate dummy data, containing the height of 100 men and 100 women

    The return values are a Pandas DataFrame, looking as follows:
    height  gender
    185     male
    166     female
    172     female
    177     male
    etc ....

    """

    # Enter mean and standard deviation, for men and women
    height = pd.DataFrame({
        'gender':['male', 'female'],
        'mean':[176.0, 162.6],
        'std':[7.1, 7.1]
        })

    # Make the "gender" the label for the row-index, and print these values
    height = height.set_index('gender')
    print('Pandas DataFrame for the height of men and women:')
    print(height)

    def make_samples(mean=170, std=10):
        """Generates 100 random samples from a normal distribution"""
        return stats.norm(mean, std).rvs(100)

    # For men and women, generate DataFrames containing height and gender
    height_dict = height.transpose().to_dict()
    print(f'Values of females only: {height_dict["female"]}')

    male   = pd.DataFrame({
        'height':make_samples(**height_dict['male']),
        'gender':'male'
        })
    female = pd.DataFrame({
        'height':make_samples(**height_dict['female']),
        'gender':'female'
        })

    # Combine the two DataFrames, mix them, and re-set the index
    data = male.append(female)
    data = data.sample(n=200)
    data = data.reset_index(drop=True)

    return data


def handle_nans():
    """Show some of the options of handling nan-s in Pandas"""

    print('--- Handling nan-s in Pandas ---')

    # Generate data containing "nan":
    x = np.arange(7, dtype=float)
    y = x**2

    x[3] = np.nan
    y[ [2,5] ] = np.nan

    # Put them in a Pandas DataFrame
    df = pd.DataFrame({'x':x, 'y':y})
    print(df)

    # Different ways of handling the "nan"s in a DataFrame:

    print('Drop all lines containint nan-s:')
    print(df.dropna())     # Drop all rows containing nan-s

    print('Replaced with the next-lower value:')
    print(df.fillna(method='pad'))  # Replace with the next-lower value

    print('Replaced with an interpolated value:')
    print(df.interpolate())         # Replace with an interpolated value


def two_categories():
    """Show how data with two categories can be handled with Pandas"""

    print('--- Grouping data in Pandas ---')

    # Generate some dummy data, in the shape of a Pandas DataFrame
    df = generate_data()

    # Group them by gender
    grouped = df.groupby('gender')

    # Basic statistics
    print(grouped.describe())

    # Show the two groups as a scatter-plot, with labels added
    fig, axs = plt.subplots(1,2)
    for name, group in grouped:
        axs[0].plot(group.height, 'o', label=name)    

    axs[0].set_ylabel('Height [cm]')
    axs[0].legend()

    # If you only want the height-values of each group 
    males   = grouped.get_group('male').height.values
    females = grouped.get_group('female').height.values
    df_mf = pd.DataFrame({'male': males,
                          'female': females})
    df_mf.boxplot(ax=axs[1])

    # To save to an out-file with my default formatting
    out_file = 'pandas.jpg'
    plt.savefig(out_file, dpi=200, quality=90)
    print(f'Image saved to {out_file}')

    plt.show()
    
    # For a standalone figure, the boxplot of the two groups can also be
    # generated with a single command:
    grouped.boxplot()
    plt.show()


if __name__ == '__main__':
    # Control the precision of pandas-output
    pd.options.display.float_format = '{:5.1f}'.format

    two_categories()
    handle_nans()
