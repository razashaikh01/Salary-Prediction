
def cal_stats(column_name, data):
    import numpy as np 
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.stats as st
    import warnings
    warnings.filterwarnings('ignore')
    print(column_name)
    total=np.sum(data)
    print('Total Sum : ',total)
    
    count=len(data)
    print('Total Count : ',count)
    
    mini=data.min()
    print('Minimum : ',mini)
    
    maximum=data.max()
    print('Maximum : ',maximum)
    
    ran=np.round(maximum-mini,2)
    print('Range : ',ran)
    
    avg=round(np.mean(data),2)
    print('Average : ',avg)
    
    med=round(np.median(data),2)
    print('Median : ',med)
    
    mo=st.mode(data)
    print('Mode : ',mo)
    
    q1=np.percentile(data,25)
    print('Q1 : ',q1)
    
    q3=np.percentile(data,75)
    print('Q3 : ',q3)
    
    iqr=q3-q1
    print('IQR : ',iqr)
    
    lw= q1-iqr*1.5
    print('Lower Whisker : ', lw)
    
    uw= q3+iqr*1.5
    print('Upper Whisker : ', uw)
    
    vr=np.var(data)
    print('Variance : ', vr)
    
    sta=np.std(data)
    print('Standard Deviation : ',sta)
    
    sk=st.skew(data)
    print('Skewness : ',sk)
    
    ku=st.kurtosis(data)
    print('Kurtosis : ',ku)

    outlier_count = ((data < lw) | (data > uw)).sum()
    print('Outlier Count : ', outlier_count)

    outlier_percentage = (outlier_count / len(data)) * 100
    print('Outlier Percentage : ', round(outlier_percentage, 2), '%')





