import numpy as np
import pandas as pd

np.random.seed(123)
n_sample= 1000
n_class_0_ratio=0.9
n_class_0=int (n_sample* n_class_0_ratio)
n_class_1=n_sample-n_class_0
print(n_class_0)
print(n_class_1)