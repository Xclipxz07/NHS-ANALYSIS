import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('patient_data.csv', parse_dates=['visit_date'])
df['age']=df['age'].fillna(df['age'].median())
df.to_csv('cleaned_patient_data.csv', index=False)
plt.hist(df['age'])
plt.savefig('patient_age_distribution.png')
print('Done')
