
import numpy as np
import pandas as pd
from scipy import stats

def hypothesis_test(sample_1, sample_2, alpha, alt):
    '''
    Perform t-test for two samples.

    Parameters
    ----------
    sample_1: pandas data series object

    sample_2: pandas data series object

    alpha: float
        significance level
    alt: string
        'two-sided', 'less', or 'greater'
    
    Returns
    -------
    p_val: float
    result: boolean
    1 if null hypothesis can be rejected.
    '''
    # Print sample means for reference
    print(f'Sample 1 mean = {sample_1.mean()}, Sample 2 mean = {sample_2.mean()}')
    # Perform t_test
    _, p_val = stats.ttest_ind(sample_1, sample_2, equal_var = False, alternative = alt)
    return p_val, p_val <= alpha

 