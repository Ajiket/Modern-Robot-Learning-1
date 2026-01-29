# check_dataset.py
import pandas as pd
df = pd.read_parquet(r'C:\Users\jiten\.cache\huggingface\lerobot\Ajiket\dataset-whistle\data\chunk-00\00-0.parquet')
print('Shape:', df.shape)
print('Episodes:', df['episode'].nunique())
print('Episode IDs:', sorted(df['episode'].unique()))
print('Sample columns:', list(df.columns)[:10])
