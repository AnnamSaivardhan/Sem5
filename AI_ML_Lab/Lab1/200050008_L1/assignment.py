from cmath import exp, sqrt
import json
from typing import Tuple, List
import numpy as np


def generate_uniform(seed: int, num_samples: int) -> None:
    """
    Generate 'num_samples' number of samples from uniform
    distribution and store it in 'uniform.txt'
    """

    # TODO
    np.random.seed(seed);
    uniform_samples = np.random.uniform(0, 1, num_samples);
    with open('uniform.txt', 'w') as f:
        for sample in uniform_samples:
            f.write(str(sample) + '\n')
    # END TODO

    assert len(np.loadtxt("uniform.txt", dtype=float)) == 100
    return None


def inv_transform(file_name: str, distribution: str, **kwargs) -> list:
    """ populate the 'samples' list from the desired distribution """

    samples = []
    if(distribution=="exponential"):
        with open(file_name,'r') as f:
            for l in f:
                samples.append(float(l))
        sol=[]
        lmda=kwargs["lambda"]
        for elem in samples:
            x=np.log((1-elem))/-(lmda)
            sol.append(x)
        return sol
    elif(distribution=="cauchy"):
        with open(file_name,'r') as f:
            for l in f:
                samples.append(float(l))
        sol=[]
        x0 = kwargs["peak_x"]
        gam = kwargs["gamma"]
        for elem in samples:
            x = x0 + gam*np.tan((elem-0.5)*np.pi)
            sol.append(x)
        return sol
    else:
        with open(file_name,'r') as f:
            for l in f:
                samples.append(float(l))
        sol=[]
        lt = kwargs["values"]
        pt= kwargs["probs"]
        arr=[]
        sum=0.0
        pr=[]
        for i in range(len(lt)):
            sum=sum+pt[i]
            arr.append([lt[i],pt[i],sum])
        for smp in samples:
            for elem in arr:
                if(smp<elem[2]):
                    sol.append(elem[0])
                    break;
        return sol
    # TODO

    # END TODO
    assert len(samples) == 100
    return samples


def find_best_distribution(samples: list) -> Tuple[int, int, int]:
    """
    Given the three distributions of three different types, find the distribution
    which is most likely the data is sampled from for each type
    Return a tupple of three indices corresponding to the best distribution
    of each type as mentioned in the problem statement
    """
    indices = (0,0,0)
    
    x1=0
    x2=0
    x3=0
    sol=[]
    
    for l in samples:
        x1=x1+np.log((1/1.0*sqrt(2*np.pi))*np.exp(-(l*l)/2)*100)
        x2=x2+np.log(((1/0.5)*sqrt(2*np.pi))*np.exp(-(l*l)*4/2)*100)
        x1=x3+np.log((1/1.0*sqrt(2*np.pi))*np.exp(-((l-1)*(l-1)/2))*100)
    #print(type(x1))
    if(max(x1,x2,x3)==x1):
        sol.append(0)
    elif(max(x1,x2,x3)==x2):
        sol.append(1)
    else:
        sol.append(2)
    
    x=-1
    for l in samples:  
        if l>1:
            sol.append(1)
            x=1
            break
        if(l<0):
            sol.append(2)
            x=1
            break
    if(x==-1):
        sol.append(0)

    y1=0
    y2=0
    y3=0
    for l in samples:
        y1=y1-0.5*l+np.log(0.5)
        y2=y2-1*l+np.log(1)
        y3=y3-2*l+np.log(2)
    if(max(y1,y2,y3)==y1):
        sol.append(0)
    elif(max(y1,y2,y3)==y2):
        sol.append(1)
    else:
        sol.append(2)

    # TODO

    # END TODO
    assert len(indices) == 3
    assert all([index >= 0 and index <= 2 for index in indices])
    return sol

def marks_confidence_intervals(samples: list, variance: float, epsilons: list) -> Tuple[float, List[float]]:
    sum=0
    for l in samples:
        sum=sum+l
    sample_mean = sum/len(samples)
    deltas=[]
    for e in epsilons:
        deltas.append((variance/(len(samples)*e*e)))# List of zeros
    
    # TODO

    # END TODO

    assert len(deltas) == len(epsilons)
    return sample_mean, deltas

if __name__ == "__main__":
    seed = 21734

    # question 1
    generate_uniform(seed, 100)

    # question 2
    for distribution in ["categorical", "exponential", "cauchy"]:
        file_name = "q2_" + distribution + ".json"
        args = json.load(open(file_name, "r"))
        samples = inv_transform(**args)
        with open("q2_output_" + distribution + ".txt", "w") as f:
            for elem in samples:
                f.write(str(elem) + "\n")

    # question 3
    indices = find_best_distribution(np.loadtxt("q3_samples.csv", dtype=float))
    with open("q3_output.txt", "w") as f:
        f.write("\n".join([str(e) for e in indices]))

    # question 4
    q4_samples = np.loadtxt("q4_samples.csv", dtype=float)
    q4_epsilons = np.loadtxt("q4_epsilons.csv", dtype=float)
    variance = 5

    sample_mean, deltas = marks_confidence_intervals(q4_samples, variance, q4_epsilons)

    with open("q4_output.txt", "w") as f:
        f.write("\n".join([str(e) for e in [sample_mean, *deltas]]))
