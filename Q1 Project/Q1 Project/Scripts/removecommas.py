import pandas as pd

df = pd.read_csv('Supply_Chain_Shipment_Pricing_Dataset_New.csv', quotechar="'")

columns = ["country", "vendor", "item description", "molecule/test type", "manufacturing site"]

for column in columns:
    for val in df[column]:
        print(val)
        if "," in val:
            newVal = val.replace(",", "")
            df[column] = df[column].replace(val, newVal)
            
df.to_csv('Supply_Chain_Shipment_Pricing_Dataset_New_WithoutCommas.csv', index=False)