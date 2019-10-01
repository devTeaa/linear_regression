import sys
import pandas as pd

DEFAULT_SOURCE = 'SOURCE_CSV_NAME.csv'
DEFAULT_TARGET = 'targetCsvName.csv'

try:
  SOURCE_CSV = sys.argv[1] if DEFAULT_SOURCE is '' else DEFAULT_SOURCE
  f = open(DEFAULT_SOURCE)
  f.close()
except:
  print('\n\nError: No args given for source or target csv', '\n\n')
  raise

try:
  TARGET_CSV = sys.argv[2]
  f = open(DEFAULT_TARGET)
  f.close()
except:
  print('\n\nError: No args given for source or target csv', '\n\n')
  raise

SEPARATOR_ARGS = sys.argv[3] if len(sys.argv) == 4 else '\t'

df_source = pd.read_csv(SOURCE_CSV, sep = SEPARATOR_ARGS)
df_target = pd.read_csv(TARGET_CSV, sep = SEPARATOR_ARGS)

df_merged = df_source.append(df_target)
df_merged.to_csv(f'merged_data.csv', index=False, sep='\t')
