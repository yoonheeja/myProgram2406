import re
from collections import Counter

def preprocess_text(text):
    # 텍스트 전처리: 특수 문자 제거 및 소문자 변환
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

def analyze_text_frequency(text):
    # 단어 빈도 분석
    words = text.split()
    word_count = Counter(words)
    return word_count

def main():
    # 파일명 입력 받기
    filename = input("텍스트 파일 경로를 입력하세요: ")

    # 파일 읽기
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return

    # 텍스트 전처리
    preprocessed_data = preprocess_text(data)

    # 단어 빈도 분석
    word_frequency = analyze_text_frequency(preprocessed_data)

    # 사용자 입력에 따른 빈도 출력
    while True:
        search_word = input("찾고자 하는 단어나 구를 입력하세요 (종료하려면 '종료' 입력): ")
        if search_word == '종료':
            break
        if search_word in word_frequency:
            print(f"'{search_word}'의 빈도는 {word_frequency[search_word]}번 입니다.")
        else:
            print("해당 단어나 구는 텍스트에 존재하지 않습니다.")

if __name__ == "__main__":
    main()
