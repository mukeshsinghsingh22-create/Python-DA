import pandas as pd

df = pd.read_csv(r'E:\python\.newvenv\Data\used_car_price_prediction_Data.csv')
print(df.head().to_string())
print('\nCOLUMNS:', list(df.columns))
print('\nDTYPES:\n', df.dtypes)
print('\nMISSING:\n', df.isnull().sum())
print('\nSHAPE:', df.shape)
