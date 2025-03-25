import pandas as pd

df = pd.read_csv('Supply_Chain_Shipment_Pricing_Dataset_New_WithoutCommas_DateNotCapFixed.csv', quotechar="'")

columns = ["weight (kilograms)", "freight cost (usd)"]

for column in columns:
    for val in df[column]:
        if "See" in val:
            id_look_at = int(val.split("ID#:")[1][:-1])
            result_value = df.loc[df.index[df['id'] == id_look_at].tolist()[0], column]
            df[column] = df[column].replace(val, result_value)

df.to_csv('Supply_Chain_Shipment_Pricing_Dataset_New_WithoutCommas_DateFixed_WeightFreightFixed.csv', index=False)