mean = 175
sd = 6
nd = stats.norm(mean, sd)
nd.cdf(184) - nd.cdf(183)
prob_183 = 100*(nd.cdf(184) - nd.cdf(183))
prob_183
print('The probability that a man is 183 cm tall is {0:4.1f} %'.format(prob_183))
print('The probability that a man is exactly 183 cm tall is {0:4.1f} %'.format(prob_183))
sd = 4
lower_lim = 250
nd = stats.norm
nd.ppf(0.99)
mean = lower_lim - sd * nd.ppf(0.99)
print('If the average can weighs {mean:4.1f}g, 99% will weigh above 250 g')
print(f'If the average can weighs {mean:4.1f}g, 99% will weigh above 250 g')
mean = lower_lim + sd * nd.ppf(0.99)
print(f'If the average can weighs {mean:4.1f}g, 99% will weigh above 250 g')
print(f'If the average can weighs {mean:4.1f}g, 99% will weigh above {lower_lim}')
print(f'If the average can weighs {mean:4.1f}g, 99% will weigh above {lower_lim}g')
print(f'If the average can weighs {mean:4.1f}g and the standard deviation is {sd}g, then 99% will weigh above {lower_lim}')
print(f'If the average can weighs {mean:4.1f}g and the standard deviation is {sd}g, then 99% will weigh above {lower_lim}g.')
man = {'avg':175, 'sd':6}
male = {'avg':175, 'sd':6}
female = {'avg':168, 'sd':3}
diff = {'avg':male['avg'] - female['avg']}
diff
diff = {'avg':male['avg'] - female['avg'], 'sd': np.sqrt(male['sd']**2 + female['sd']**2)}
diff
nd = stats.norm(diff['avg'], diff['sd'])
nd.cd(0)
nd.cdf(0)
p_small_male = nd.cdf(0)
p_small_male
print(f'The probability that a randomly selected man is shorter than a randomly selected woman is {p_small_male*100:4.1f}%.')
pwd
%hist -f S6_Questions631.py
