import json
file_path = './merged.txt'  # 실제 파일 경로로 변경하세요

with open(file_path, 'r', encoding='cp949') as file:
    content_array = file.read().splitlines()

new_dict = {}
def text_to_json():
    # 텍스트를 최초 공백을 기준으로 분리
    for txt in content_array:
        parts = txt.split(maxsplit=1)
        if len(parts)>1 and parts[1]:
            new_dict[parts[0]] = parts[1]
        else :
            print(parts)
    return new_dict

dic = text_to_json()

# 모든 텍스트 파일을 읽어서 하나의 파일로 통합
output_file_path = 'merged_.json'

with open(output_file_path, 'w', encoding='cp949') as output_file:
    json.dump(dic, output_file, ensure_ascii=False, indent=2)
print(len(new_dict.keys()))
