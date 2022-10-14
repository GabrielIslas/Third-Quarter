from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def rule_1(grade_sample):
    """From the seven grades, remove the highest and lowest, then take the mean.

    Input: sorted list of grade samples.
    """
    return grade_sample[1:6].mean()


def rule_2(grade_sample):
    """From the seven grades, return the median.
    Input: sorted list of grade samples."""
    return grade_sample[3]


# We are modeling each grade as y = g + z with z a U(-0.5,0.5) random
# variable. The value of g is irrelevant, it cancels out when calculating the
# deviations from the deserved grade g.
juror_1_dev = []
T_sample = []
M_sample = []
for i in range(10000):
    z_sample = np.random.uniform(-0.5, 0.5, 7)
    juror_1_dev.append(z_sample[0])
    z_sample.sort()
    T = rule_1(z_sample)
    M = rule_2(z_sample)
    # print(z_sample, T, M)
    T_sample.append(T)
    M_sample.append(M)

# How does the deviation look for each juror?
plt.hist(juror_1_dev, bins=20)
plt.show()

# How does the distributions for M and T look?
plt.subplot(121)
plt.hist(T_sample, bins=20)

plt.subplot(122)
plt.hist(M_sample, bins=20)

plt.show()

# What about the relationship between T and M?
plt.scatter(T_sample, M_sample)

x = np.linspace(-0.5, 0.5, 100)
# Plot a 45ª line
plt.plot(x, x, color="r")
# Plot the regression line
(slope, intercept, r_value,
 p_value, std_err) = stats.linregress(T_sample, M_sample)
plt.plot(x, slope*x + intercept, color="g")
plt.show()

# It seems it is a good idea to make a histogram of the absolut deviations.
abs_dev = np.absolute(M_sample) - np.absolute(T_sample)
plt.hist(abs_dev, bins=20)
plt.show()
