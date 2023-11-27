import json
import re
file_path = 'merged_.json'
pattern = re.compile(r'<.*?>')
with open(file_path, 'r', encoding='cp949') as file:
    data = json.load(file)
    for key, value in data.items():
        data[key] = re.sub(pattern, '', value)

print(data)

# 결과를 다시 JSON 파일에 저장
with open('merged.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)