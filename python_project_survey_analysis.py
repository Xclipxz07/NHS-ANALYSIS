import pandas as pd
import matplotlib.pyplot as plt

# Load
df = pd.read_csv('survey_data.csv')
print(df.head())

# Summary
print('Average satisfaction:', df['overall_satisfaction'].mean())

# Scatter
plt.scatter(df['waiting_time_minutes'], df['overall_satisfaction'])
plt.xlabel('Waiting time')
plt.ylabel('Satisfaction')
plt.savefig('survey_waiting_vs_satisfaction.png')
print('Saved png')
