import pandas as pd
from sklearn.model_selection import train_test_split

folders = ['ReliefFAttributeEvalData', 'GainRatioAttributeEvalData', 
           'CorrelationAttributeEvalData', 'CfsSubsetEvalData', 'PersonalAttributeData']
files = ['ReliefSampledDataset.csv', 'GainSampledDataset.csv', 
         'CorrelationSampledDataset.csv', 'CfsSampledDataset.csv', 'PersonalSampledDataset.csv']

for idx, folder in enumerate(folders):
    df = pd.read_csv(f'{folder}/{files[idx]}')
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    X_train, X_temp, y_train, y_temp = train_test_split(x, y, test_size=0.30, stratify=y, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=42)
    train = pd.concat([X_train, y_train], axis=1)
    val = pd.concat([X_val, y_val], axis=1)
    test = pd.concat([X_test, y_test], axis=1)
    train.to_csv(f'{folder}/Train.csv', index=False)
    val.to_csv(f'{folder}/Val.csv', index=False)
    test.to_csv(f'{folder}/Test.csv', index=False)
