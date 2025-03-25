import pandas as pd

df = pd.read_csv('Supply_Chain_Shipment_Pricing_Dataset_FinalPreprocessing.csv')

df = df.groupby("'sub classification'", group_keys=False).apply(lambda x: x.sample(frac=0.4))

df.to_csv('Supply_Chain_Shipment_Pricing_Dataset_FinalSampled.csv', index=False)