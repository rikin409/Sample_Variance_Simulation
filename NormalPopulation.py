import pandas as pd
import numpy as np
import random
import matplotlib.pyplot



class NormalPopulation:
    
    def __init__(self, mean, stdev, n):
        self.mean = mean
        self.stdev = stdev
        self.n = n
        
        self.pop = np.random.normal(self.mean,self.stdev,self.n).tolist()
        self.pop_mean =  np.mean(self.pop)
        self.pop_stdev = np.std(self.pop)
        self.pop_var = np.var(self.pop)
        self.pop_n = len(self.pop)
        
    def plot_population(self):
        fig = matplotlib.pyplot.figure()
        matplotlib.pyplot.hist(self.pop, bins=50, density=True)
        fig.suptitle('Population Density', fontsize=15)
        matplotlib.pyplot.xlabel("Number")
        matplotlib.pyplot.ylabel("Frequency")
        matplotlib.pyplot.show()
    
    def get_statistics(self):
        print(f"Population n = {self.pop_n}")
        print(f"Population Mean = {self.pop_mean}")
        print(f"Population Variance = {self.pop_var}")
        print(f"Population Standard Deviation = {self.pop_stdev}")
    
    def get_sample(self, sample_size=30):
        sample = random.sample(self.pop, sample_size)
        return {
            "n":len(sample),
            "mean":np.mean(sample),
            "bi-var":np.var(sample),
            "unbi-var":np.var(sample, ddof=1),
            "stdev":np.std(sample)
        }
    def get_samples(self, num_samples_max, sample_size=30, printed_sample = 100):
        aggregate_df = pd.DataFrame(columns = ["Number of Samples", "Mean Biased Variance", "Mean Unbiased Variance"])
        for i in range(1,num_samples_max+1):
            temp_df = pd.DataFrame(columns = ["Mean", "Biased Variance", "Unbiased Variance"])
            for j in range(i):
                sample = self.get_sample(sample_size)
                temp_df.loc[len(temp_df.index)] = [sample["mean"], sample["bi-var"], sample["unbi-var"]]
            aggregate_df.loc[len(aggregate_df.index)] = [i, temp_df.mean()["Biased Variance"], temp_df.mean()["Unbiased Variance"]]
        return aggregate_df
                