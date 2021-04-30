import pandas as pd
import numpy as np
import random
import matplotlib.pyplot


class Population:
    #initialize a random population of n entires between minNum and maxNum
    def __init__(self, minNum, maxNum, n):
        self.min= minNum
        self.max = maxNum
        self.n = n
        
        self.pop = []
        for x in range(n):
            self.pop.append(random.randint(self.min,self.max))
            
        self.pop_mean =  np.mean(self.pop)
        self.pop_stdev = np.std(self.pop)
        self.pop_var = np.var(self.pop)
        self.pop_n = len(self.pop)
    
    #sets up the histogram plot based on if an arguement was passed or not
    def plot_population(self, data = []):
        #if no data is passed in, then self.pop aka the population that is made when the class is initialized is plotted. If some data is passed in, then that data is plotted
        if data == []:
            data = self.pop
        self.__hist__(data)
    
    #plots histogram
    def __hist__(self, data):
        fig = matplotlib.pyplot.figure()
        matplotlib.pyplot.hist(data, bins=101, density=False)
        fig.suptitle('Frequency', fontsize=15)
        matplotlib.pyplot.xlabel("Number")
        matplotlib.pyplot.ylabel("Frequency")
        #matplotlib.pyplot.xlim(0,100)
        matplotlib.pyplot.show()
    
    #prints population parameters
    def get_statistics(self):
        print(f"Population n = {self.pop_n}")
        print(f"Population Mean = {self.pop_mean}")
        print(f"Population Variance = {self.pop_var}")
        print(f"Population Standard Deviation = {self.pop_stdev}")
    
    #randomly picks sample, returns sample data
    def get_sample(self, sample_size=30):
        sample = random.sample(self.pop, sample_size)
        return {
            "n":len(sample),
            "mean":np.mean(sample),
            "bi-var":np.var(sample),
            "unbi-var":np.var(sample, ddof=1),
            "stdev":np.std(sample, ddof = 1),
            "sample":sample
        }
    
    #picks n number of samples and reeturns a list of all of their means
    def get_sampling_distribution(self, n, sample_size =30):
        sample_mean_list = []
        for i in range(n):
            sample_mean_list.append(self.get_sample(sample_size)["mean"])
        return sample_mean_list
    

class NormalPopulation(Population):
    
    def __init__(self, mean, stdev, n):
        self.mean = mean
        self.stdev = stdev
        self.n = n
        
        self.pop = np.random.normal(self.mean,self.stdev,self.n).tolist()
        self.pop_mean =  np.mean(self.pop)
        self.pop_stdev = np.std(self.pop)
        self.pop_var = np.var(self.pop)
        self.pop_n = len(self.pop)

    def get_samples_mean_variances(self, num_samples_max, sample_size=30):
        aggregate_df = pd.DataFrame(columns = ["Number of Samples", "Mean Biased Variance", "Mean Unbiased Variance"])
        for i in range(1,num_samples_max+1, 5):
            temp_df = pd.DataFrame(columns = ["Mean", "Biased Variance", "Unbiased Variance"])
            for j in range(i):
                sample = self.get_sample(sample_size)
                temp_df.loc[len(temp_df.index)] = [sample["mean"], sample["bi-var"], sample["unbi-var"]]
            aggregate_df.loc[len(aggregate_df.index)] = [i, temp_df.mean()["Biased Variance"], temp_df.mean()["Unbiased Variance"]]
        return aggregate_df
                