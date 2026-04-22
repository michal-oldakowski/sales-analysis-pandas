import pandas as pd
import os

def merge_files():
    files = [file for file in os.listdir('./SalesAnalysis/Sales_Data')]
    all_months_data = pd.DataFrame()

    for file in files:
        df = pd.read_csv('./SalesAnalysis/Sales_Data/' + file)
        all_months_data = pd.concat([all_months_data, df])

    all_months_data.to_csv('moja_nazwa.csv', index=False)

if __name__ == "__main__":
    merge_files()