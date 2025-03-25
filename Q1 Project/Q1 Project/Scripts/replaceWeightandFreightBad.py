import pandas as pd

df = pd.read_csv('Supply_Chain_Shipment_Pricing_Dataset_New_WithoutCommas_DateFixed_WeightFreightFixed.csv', quotechar="'")

columns = ["weight (kilograms)", "freight cost (usd)"]

for column in columns:
    listVal = []
    for val in df[column]:
        try:
            listVal.append(float(val))
        except:
            continue
    medVal = sorted(listVal)[int(len(listVal)/2)]
    print(medVal)
    for val in df[column]:
        if "e" in val:
            df[column] = df[column].replace(val, medVal)

df.to_csv('Supply_Chain_Shipment_Pricing_Dataset_FinalCleanup.csv', index=False)