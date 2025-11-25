# excel_auto_clean.py
# Simple automation showing how to read an Excel file, clean and write back
import pandas as pd

def clean_medication_sheet(df):
    # Trim strings
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip().str.title()
    # Fill missing dates with forward fill
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['date'] = df['date'].fillna(method='ffill')
    return df

if __name__ == '__main__':
    # Mock example, create a small dataframe and clean it
    df = pd.DataFrame({
        'patient_name': [' alice ', 'bob', 'CHARLIE '],
        'medication': ['aspirin', 'paracetamol', 'ibuprofen'],
        'date': ['2024-01-01', None, '2024-01-03']
    })
    print('Before cleaning:\n', df)
    df_clean = clean_medication_sheet(df)
    print('\nAfter cleaning:\n', df_clean)
    df_clean.to_csv('automation_cleaned.csv', index=False)
    print('\nSaved automation_cleaned.csv')
