import sys
import pandas as pd

DEFAULT_CSV = 'merged_data.csv'
DEFAULT_SEPARATOR = '\t'
TARGET_COLUMN = ['conductivity', 'nutrients', 'ph']

try:
  TARGET_CSV = sys.argv[1] if DEFAULT_CSV is '' else DEFAULT_CSV
except:
  print('Error: No args given for target csv', '\n\n')
  raise

SEPARATOR_ARGS = sys.argv[2] if DEFAULT_SEPARATOR == '' and len(sys.argv) == 3 else DEFAULT_SEPARATOR

df_source = pd.read_csv(TARGET_CSV, sep = SEPARATOR_ARGS)

for col_name in TARGET_COLUMN:
  df_source = df_source[df_source[col_name] > 0]

df_source.to_csv(f'cleaned_data.csv', index=False, sep='\t')
