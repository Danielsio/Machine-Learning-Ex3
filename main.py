# This is a sample Python script.
import ex3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()

dataset = ex3.load_train_data()
datasetWithNans = ex3.drop_non_inform_columns(dataset)
dr_filled = ex3.fill_titanic_nas(datasetWithNans)
one_Hot = ex3.encode_one_hot(dr_filled)
one_Hot_family = ex3.make_family(dr_filled)

ex3.survival_vs_gender(one_Hot_family)


