import pandas as pd

df = pd.read_csv('Supply_Chain_Shipment_Pricing_Dataset_New_WithoutCommas.csv', quotechar="'")

column1 = "pq first sent to client date"
column2 = "po sent to vendor date"

for val in df[column1]:
    if "Date Not Captured" in val:
        df[column1] = df[column1].replace(val, "Pre-PQ Process")
        
for val in df[column2]:
    if "Date Not Captured" in val:
        df[column2] = df[column2].replace(val, "N/A - From RDC")
        
df.to_csv('Supply_Chain_Shipment_Pricing_Dataset_New_WithoutCommas_DateNotCapFixed.csv', index=False)
