import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns

sns.set(context='paper', style='ticks', font_scale=1.2)

num_samples = 50
bmi = pd.DataFrame({'value':[27, 28.8, 26.5, 24.2]}, index=['Germany', 'USA', 'Austria','China'])
std = 4
samples = {}
np.random.seed(12345)
for country in bmi.index:
    samples[country] = stats.norm(bmi.value[country], std).rvs(num_samples)

plt.plot(samples['China'], 'o', label='China')
plt.hlines(25, 0, num_samples, linestyles='--')
plt.xlim(0, 50)
plt.xlabel('Subject-Nr')
plt.ylabel('BMI')
plt.legend()
out_file = 'BMI_China.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')
plt.show()

plt.plot(samples['USA'], '*', ms=3, label='USA')
plt.plot(np.arange(num_samples, 2*num_samples), samples['Austria'],'o', ms=3, fillstyle='none', label='Austria')
plt.xlabel('Subject-Nr')
plt.ylabel('BMI')
plt.legend()
out_file = 'BMI_countries.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')
plt.show()

samples['USA2'] = samples['USA'] - 1 + np.random.randn(num_samples)*0.5
fig, axs = plt.subplots(1,2, sharey=True)
axs[0].plot(samples['USA'], 'o', ms=3, label='before diet')
axs[0].plot(np.arange(num_samples, 2*num_samples), samples['USA2'],'o', fillstyle='none', ms=3, label='after diet')
axs[0].set_xlabel('Subject-Nr')
axs[0].set_ylabel('BMI')
axs[0].legend(loc='upper right')

axs[1].plot(samples['USA'], 'o', ms=6, label='before diet')
axs[1].plot(samples['USA2'],'o', ms=6, fillstyle='none', label='after diet')
axs[1].set_xlabel('Subject-Nr')
axs[1].set_xlim(-0.5, 5.5)
axs[1].legend(loc='upper right')

out_file = 'BMI_diet.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')
plt.show()

