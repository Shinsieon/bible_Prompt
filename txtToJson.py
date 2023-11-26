# 파일을 통합할 대상 디렉토리로 이동
import os

directory = 'C:/Users/coolg/Downloads/개역개정-pdf, txt/개역개정-text'  # 실제 경로로 변경하세요
os.chdir(directory)

# 모든 텍스트 파일을 읽어서 하나의 파일로 통합
output_file_path = 'merged.txt'

with open(output_file_path, 'w', encoding='cp949') as output_file:
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(filename, 'r', encoding='cp949') as input_file:
                contents = input_file.read()
                output_file.write(contents)
                output_file.write('\n')  # 각 파일 사이에 줄 바꿈 추가