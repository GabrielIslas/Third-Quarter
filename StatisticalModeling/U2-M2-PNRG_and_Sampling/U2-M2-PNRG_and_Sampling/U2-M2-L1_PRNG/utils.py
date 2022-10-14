import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools
from collections import Counter


def CDF_from_PMF(x, pmf):
    outcomes = np.array([*pmf])
    probs = np.array([*pmf.values()])
    return np.sum(probs[x >= outcomes])


def empCDF(x, sample):
    sample = np.array(sample)
    return np.sum(sample <= x)/len(sample)


def plotECDF(sample, label=None, xlabel='x', ylabel='$P(X \leq x)$', CCDF=False, alpha=1, fmt='-o', color='b'):
    sample = np.array(sample)
    sample.sort()
    if CCDF == True:
        plt.plot(sample, 1 - np.arange(1, len(sample)+1)/len(sample), fmt, label=label, alpha=alpha, color=color)
        plt.ylabel('1-$P(X \leq x)$')
        plt.xlabel(xlabel)
    else:
        plt.plot(sample, np.arange(1, len(sample)+1)/len(sample), fmt, label=label, alpha=alpha, color=color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel);


def P(event, space): 
    "The probability of an event, given a sample space."
    return Fraction(cases(favorable(event, space)), 
                    cases(space))


def combos(items, n):
    "All combinations of n items; each combo as a space-separated str."
    return set(map(' '.join, itertools.combinations(items, n)))


def cases(outcomes): 
    "The total frequency of all the outcomes."
    return sum(Counter(outcomes).values())


def favorable(event, space):
    "A distribution of outcomes from the sample space that are in the event."
    space = Counter(space)
    return Counter({x: space[x] 
                    for x in space if x in event})


def Fraction(n, d): return n / d


def PMF(trials):
    outcomes, freq = np.unique(trials, return_counts=True)
    prob = freq / len(trials)
    return dict(zip(outcomes, prob))


def plot_PMF(pmf, ptype='bars', label=None):
    prob = pmf.values()
    labels = [*pmf]
    
    if ptype == 'bars':
        plt.bar(range(len(pmf)), prob, tick_label=labels, label=label);
    elif ptype == 'stem':
        plt.stem(prob, use_line_collection=True)
        plt.xticks(range(len(pmf)), labels, label=label);
    else:
        raise NotImplementedError
    plt.ylabel('probability')
    
    
def pmf_mean(pmf):
    outcomes = np.array([*pmf])
    probs = np.array([*pmf.values()])
    return np.sum(outcomes*probs)
        

def pmf_var(pmf):
    outcomes = np.array([*pmf])
    probs = np.array([*pmf.values()])
    return np.sum(outcomes**2*probs) - pmf_mean(pmf)**2
