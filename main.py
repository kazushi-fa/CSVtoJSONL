import pandas as pd
import json

# CSVファイルの読み込み
csv_file = 'your_file.csv'
df = pd.read_csv(csv_file)

# JSONLファイルの書き出し
jsonl_file = 'your_file.jsonl'
with open(jsonl_file, 'w') as file:
    for record in df.to_dict(orient='records'):
        file.write(json.dumps(record) + '\n')

print(f'Conversion from CSV to JSONL is completed: {jsonl_file}')
