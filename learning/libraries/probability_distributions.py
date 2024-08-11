import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

""" Visualize Distributions With Seaborn/Matplotlib
Seaborn is a library that uses Matplotlib underneath to plot graphs. 

install command: pip install seaborn and/or pip3 install matplotlib

Seaborn:
Higher-level interface: Provides a more intuitive and concise syntax for common 
statistical visualizations.
Built-in themes and color palettes: Creates visually appealing plots with 
minimal code customization.
Strong integration with Pandas: Works seamlessly with Pandas DataFrames. Ideal 
for: Quickly creating aesthetically pleasing statistical plots.

Matplotlib:
Lower-level interface: Offers greater control over plot customization and fine-
tuning.
Basic plotting functions: Provides fundamental building blocks for creating 
various plots.
Ideal for: Complex visualizations, custom plots, and when you need precise 
control over plot elements.

When to Choose Which:
Seaborn: If you prioritize speed, aesthetics, and common statistical 
visualizations.
Matplotlib: If you need fine-grained control over plot elements, complex 
customizations, or performance optimization.
Often, a combination of both libraries is used. Seaborn can be used to create 
the base plot, and then Matplotlib can be used for further customization if 
needed. Ultimately, the best choice depends on your specific needs and 
preferences.

# Generate some random data
data = np.random.normal(size=1000)

# Create a histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Add a KDE plot
sns.kdeplot(data, color='blue')  # Using Seaborn for KDE

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Distribution of Data')
plt.show()
"""

""" Histplots and Displots
Histplots vs. Displots in Seaborn
Histplots and displots are both visualization tools in Seaborn used to explore 
the distribution of data, but they have distinct characteristics and purposes.

Histplot
Purpose: Primarily used to create histograms, which show the distribution of a 
numerical variable by grouping the data into bins.
Default behavior: Displays counts by default, but can be customized to show 
density or probability density.
Flexibility: Offers options for customization, including bin size, edge color,
and histogram type (step, bar, etc.).

Displot 
Purpose: A more versatile function that can create various plots related to 
distributions, including histograms, kernel density estimation (KDE) plots, and 
rug plots.
Flexibility: Provides more options for customization than histplot, allowing for 
combinations of different plot types and advanced features like marginal plots.
Figure-level: Displot is a figure-level function, meaning it creates a new 
figure object, while histplot is an axes-level function, allowing for more 
control over plot placement.

They shows bars representing the number of data points within specific bins
(ranges) on the x-axis. Kernel Density Estimation (KDE) is a non-parametric way 
to estimate the probability density function of a random variable. It provides a 
smooth curve that represents the underlying distribution of the data.

# Sample data
data = np.random.randn(1000)

# Histplot
sns.histplot(data, bins=30)
plt.show()

# Displot with KDE
sns.displot(data, kde=True)
plt.show()

While both histplot and displot can be used to visualize distributions, histplot
is more focused on histograms, while displot offers a broader range of options 
for exploring and understanding your data.
"""

""" Normal (Gaussian) Distribution
The normal distribution, often called the Gaussian distribution, is a continuous 
probability distribution characterized by its bell-shaped curve. It's symmetric 
about the mean, and the majority of the data points cluster around the mean.

Use the np.random.normal() method to get a Normal Data Distribution.

It has three parameters:
loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array.

Importance of Normal Distribution
Many natural phenomena: Height, weight, IQ, and measurement errors often follow 
a normal distribution.
Statistical inference: Many statistical tests assume a normal distribution.
Machine learning: Normal distribution is used in various algorithms like 
Gaussian Naive Bayes.

Generate a random normal distribution of size 2x3 array with mean at 1 and 
standard deviation of 2:
x = np.random.normal(loc=1, scale=2, size=(2, 3))

Visualization of Normal Distribution with use Case: Height Distribution
# Parameters (hypothetical values)
mu, sigma = 170, 7  # mean height and standard deviation

# Generate height data
heights = np.random.normal(loc=mu, scale=sigma, size=1000)

# Use Seaborn's displot with KDE or plt.hist()
sns.displot(heights, kde=True)
# plt.hist(heights, bins=30, density=True, alpha=0.6, color='g')
plt.title("Height Distribution with KDE")
plt.xlabel("Height (cm)")
plt.ylabel("Density")
plt.show()
"""

""" Binomial Distribution
Binomial Distribution is a Discrete Distribution and describes the outcome of 
binary scenarios e.g. tossing a coin is head or tails.

It has three parameters:
n - number of trials.
p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
size - The shape of the returned array.

Say you have a coin and you want to flip it 6 times. The probability of getting 
heads after each flip (i.e successful attempt) is 0.5). And in total you will be
doing this experiment 10 times (i.e each experiment involves flipping coin 6 
times). Then the whole thing can be expressed as 
x = np.random.binomial(n=6, p=0.5, size=10)
>>>array([2, 2, 5, 3, 3, 2, 3, 4, 4, 3])

Now, each entry in the output array represents the result of the "experiment". 
For example, the first value in the output array can be understood as: 
"You flipped a coin 6 times where probability of heads is 0.5, and in the 
result you got 2 heads". 

Normal vs Binomial distribution
Normal distribution is continous whereas binomial is discrete. The distribution 
is defined at separate set of events, e.g. a coin toss's result is discrete as 
it can be only head or tails whereas height of people is continuous as it can 
be 170, 170.1, 170.11 and so on.

Visualization of Binomial Distribution
# Generate normal and binomial data
normal_data = np.random.normal(loc=50, scale=5, size=1000)
binomial_data = np.random.binomial(n=100, p=0.5, size=1000)

# Create the histogram plot with density curves
sns.histplot(normal_data, label='normal')
sns.histplot(binomial_data, label='binomial')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Distribution Comparison (Normal vs. Binomial)')

# Add legend
plt.legend()
plt.show() 
"""

""" Poisson Distribution
Poisson Distribution is a discrete probability distribution that expresses the 
probability of a given number of events occurring in a fixed interval of time or
space if these events occur with a known average rate and independently of the
time since the last event. e.g. If someone eats twice a day what is the 
probability he will eat thrice?

It has two parameters:
lam - rate or known number of occurrences e.g. 2 for example above.
size - The shape of the returned array. 

x = np.random.poisson(lam=2, size=10)
>>>[2 2 1 0 1 6 5 3 1 3]
This means the first person ate two meals, the second person ate two meals, the
third person ate one meal and so on.

Visualization of Poisson Distribution
plt.hist(x, bins=range(7))  # Adjust bins as needed
plt.xlabel("Number of Meals")
plt.ylabel("Frequency")
plt.title("Distribution of Meals per Day")
plt.show()

Difference Between Normal and Poisson Distribution. 
Normal distribution is  continuous whereas poisson is discrete. But we can see 
that similar to binomial for a large enough poisson distribution it will become 
similar to normal distribution with certain std dev and mean.

Difference Between Binomial and Poisson Distribution
Binomial distribution only has two possible outcomes, whereas poisson 
distribution can have unlimited possible outcomes. But for very large n and 
near-zero p binomial distribution is near identical to poisson distribution 
such that n * p is nearly equal to lam.
"""

""" Uniform Distribution
Used to describe probability where every event has equal chances of occuring.
E.g. Generation of random numbers.
It has three parameters:
a - lower bound - default 0 .0.
b - upper bound - default 1.0.
size - The shape of the returned array. 

Simulate the random arrival times of customers at a store between 9 AM and 5 PM.

# Define the time interval (in hours)
start_time = 9  # 9 AM
end_time = 17  # 5 PM
total_time = end_time - start_time

# Generate 100 random arrival times
arrival_times = np.random.uniform(start_time, end_time, 100)
>>>[12.3456789, 10.9876543, 16.2345678, ...]
Each number represents the arrival time of a customer in hours. For instance, 
the first customer arrives at 12.3456789 hours after the start time (which is 
9 AM in our example).

# Visualize the distribution
plt.hist(arrival_times, bins=10, edgecolor='black')
plt.xlabel("Arrival Time (hours)")
plt.ylabel("Frequency")
plt.title("Distribution of Customer Arrival Times")
plt.show()
"""

""" Logical Distribution 
The logistic distribution is a continuous probability distribution that is 
similar in shape tothe normal distribution, but it has heavier tails. This means 
it allows for more extreme values compared to the normal distribution.

When to use Logistic Distribution:
Modeling growth processes: Logistic distribution is often used to model 
processes with limited growth, such as population growth, spread of diseases, 
or technology adoption.
Extreme value analysis: Due to its heavier tails, it's suitable for analyzing 
data with outliers or extreme values, unlike the normal distribution which might
underestimate their probability.
Logistic regression: While the name suggests a connection, the logistic 
distribution itself isn't directly used in logistic regression. However, the 
logistic function, which is derived from the logistic distribution, is crucial 
for modeling binary outcomes (e.g., success/failure, yes/no). Used extensively 
in machine learning, logistic regression, neural networks etc.

It has three parameters:
loc - mean, where the peak is. Default 0.
scale - standard deviation, the flatness of distribution. Default 1.
size - The shape of the returned array.

Use case: model the spread of a rumor in a population of 1000 people. Use the 
logistic distribution to represent the number of people who have heard the rumor 
at different time points.

# Parameters for logistic distribution
loc = 5  # Location parameter (mean-like)
scale = 2  # Scale parameter (spread)

# Number of people in the population
population_size = 1000

# Generate time points (adjust as needed)
time_points = np.linspace(0, 10, 100)

# Calculate the number of people who heard the rumor at each time point
rumor_spread = population_size / (1 + np.exp(-(time_points - loc) / scale))

# Plot the rumor spread
plt.plot(time_points, rumor_spread)
plt.xlabel("Time")
plt.ylabel("Number of People")
plt.title("Rumor Spread (Logistic Distribution)")
plt.show()

The plot shows an S-shaped curve, typical of logistic growth.
Initially, the rumor spreads slowly, then accelerates rapidly, and finally 
levels off as more people hear the rumor. The parameters loc and scale control 
the shape of the curve.

# Generate random logistic data
data = np.random.logistic(loc=5, scale=2, size=1000)

# Create a histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Add a KDE plot
sns.kdeplot(data, color='blue')

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Logistic Distribution')
plt.show()

Difference Between Logistic and Normal Distribution
Both distributions are near identical, but logistic distribution has more area 
under the tails, meaning it represents more possibility of occurrence of an 
event further away from mean.

When to Use Which:
Normal distribution: Best suited for data with a symmetric distribution and 
limited outliers.
Logistic distribution: More appropriate for data with heavier tails or when 
modeling growth processes with a maximum value.

Feature	        Normal Distribution	    Logistic Distribution
Shape	        Bell-shaped curve	    S-shaped curve (sigmoid)
Tails	        Lighter tails       	Heavier tails (data points more likely 
                                        far from mean)
Applications ND: Height, weight, IQ scores, errors in measurements	
Applications LD: Growth models, logistic regression, extreme value analysis
"""

""" Multinomial Distribution
Multinomial distribution is a generalization of binomial distribution. It 
describes outcomes of multi-nomial scenarios unlike binomial where scenarios 
must be only one of two. e.g. Blood type of a population, dice roll outcome.

It has three parameters:
n - number of possible outcomes (e.g. 6 for dice roll).
pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] 
for dice roll).
size - The shape of the returned array. 
Multinomial samples will NOT produce a single value! They will produce one value
for each pval. As they are generalization of binomial distribution their visual 
representation and similarity of normal distribution is same as that of multiple 
binomial distributions.

While the binomial distribution models the number of successes in a fixed number 
of Bernoulli trials, the multinomial distribution models the number of 
occurrences of each possible outcome in a fixed number of independent trials.

Draw out a sample for dice roll:
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
>>>[0 1 2 2 1 0]
Outcome 1 occurred zero times, outcome 2 occurred once, outcome 3 occurred 
twice, etc
"""

""" Exponential Distribution
Exponential distribution is used for describing time till next event e.g. 
failure/success etc.Poisson distribution deals with number of occurences of an 
event in a time period whereas exponential distribution deals with the time 
between these events. It's often used to model waiting times.

Problem:
Simulate the arrival times of customers at a store, assuming customers arrive 
randomly at an average rate of 5 per hour.

Solution:
# Average arrival rate (customers per hour)
lambda_ = 5

# Convert arrival rate to customers per minute
lambda_per_min = lambda_ / 60

# Generate inter-arrival times for 100 customers
interarrival_times = np.random.exponential(scale=1/lambda_per_min, size=100)

# Calculate cumulative arrival times
arrival_times = np.cumsum(interarrival_times)

# Plot the arrival times
plt.plot(arrival_times, range(1, 101), marker='o')
plt.xlabel("Arrival Time (minutes)")
plt.ylabel("Customer Number")
plt.title("Customer Arrival Times")
plt.show() 
"""

"""  Chi Square Distribution
The chi-square distribution is a probability distribution often used in 
hypothesis testing, derived from the sum of squared standard normal deviates.

It has two parameters:
df (degree of freedom): number of independent pieces of information available to
estimate the population parameter. It influences the shape of the distribution.
size: shape of the returned array.

As df increases, the chi-square distribution becomes more symmetrical and 
approaches a normal distribution.
As df decreases, the chi-square distribution becomes more skewed to the right.
While sample size doesn't directly determine the degrees of freedom, it 
indirectly affects it.

Larger sample sizes typically lead to larger degrees of freedom, assuming other 
factors remain constant. This is because more data points provide more 
independent pieces of information.

x = np.random.chisquare(df=2, size=(2, 3))
print(x)
>>>[[1.07909799 2.65925415 2.08241346]
 [3.85404236 2.02570845 0.4450929 ]]
"""

"""  Rayleigh Distribution
The Rayleigh distribution is a continuous probability distribution for 
non-negative values. It's often used in fields like physics, signal processing, 
and engineering. e.g. wave heights in oceanography, wireless communication, 
wind speeds

It has two parameters:
scale - (standard deviation) decides how flat distribution will be default 1.0).
size - The shape of the returned array.

x = random.rayleigh(scale=2, size=(2, 3))
"""

"""  Pareto Distribution
The Pareto distribution is a power-law probability distribution often used to
model real-world phenomena where a small number of items or events account for 
the majority of the observed occurrences. It's often referred to as the "80/20 
rule", where 80% of the effects come from 20% of the causes.One common 
application of the Pareto distribution is modeling wealth distribution. It's 
often observed that a small percentage of the population holds a 
disproportionate amount of wealth.

It has two parameters:
a - shape parameter (tail index). It determines the shape of the distribution.
A higher a leads to a more even distribution.
size - shape of the returned array.

The distribution follows a power-law relationship, meaning that a small number 
of events or items have a disproportionately large impact.
Heavy tail: The distribution has a heavy tail, indicating that extreme events 
are more likely than in other distributions like the normal distribution.

x = random.pareto(a=2, size=(2, 3))
"""

""" Zipf Distribution
Zipf distributions is a discrete probability distribution used to sample data 
based on zipf's law.
Zipf's Law: In a collection, the nth common term is 1/n times of the most 
common term. E.g. the 5th most common word in English occurs nearly 1/5 times 
as often as the most common word.

It has two parameters:
a - distribution parameter.
size - The shape of the returned array. 

Key characteristics:
It's a discrete distribution.
The probability of an item being the nth most frequent is proportional to 1/n.
The distribution is characterized by single parameter 's' or 'rho'.

Let's imagine we're modeling the populations of different cities. We know that 
city populations often follow a Zipf distribution, where a few large cities 
dominate and many cities are relatively small.

city_populations = np.random.zipf(a=2, size=10)
print(city_populations)
>>>[ 1  2 21 11  2  1  1  1  2  2]

Interpretation:
Each number in the output represents the population of a city (in arbitrary 
units, for simplicity).
The Zipf distribution with a=2 suggests that a few cities have very large 
populations (like 21 in this example), while most cities are relatively small 
(with populations of 1 or 2).
"""