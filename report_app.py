# 일해라 라이엇!

import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

user1 = "Garen"
user2 = "Leesin"
user3 = "Karma"
user4 = "Apelios"
user5 = "Yumi"

# 채팅 예시
# Chatting example
chat = [f"{user1} : You crazy?", 
        f"{user2} : Wassup..?",
        f"{user1} : Gank here bxxch",
        f"{user3} : Do not fight...",
        f"{user1} : The trash never come here.",
        f"{user2} : What? you just died alone! wanna die fxxking bxxch?",
        f"{user3} : Don't fight!!!",
        f"{user4} : We never fight like them Yumi.",
        f"{user5} : Sure!"]

# 프롬프트 불러오기(예시를 알려줘야 하기때문에 욕설이 포함되어 있음)
with open("prompt_report.txt", "r", encoding="utf-8") as file:
    prompt = file.read()
    
def is_valid_format(lst): # 형식 안맞을시 False 반환
                          # Returns False if malformed
    if not lst or len(lst) % 3 != 0: # 인풋이 없거나 ["챔피언이름", ":", "점수"] 이 형식처럼 리스트 길이가 3배수인지 체크
                                     # Check if there is no input or if the length is 3 times as list above
        return False

    valid = True
    for idx, elem in enumerate(lst):
        if idx % 3 == 0: # 0부터 시작. idx 0,3,6... 챔피언 이름 위치에 문자열이 있는가?
                         # Start from zero. Idx 0,3,6... Is there a string in the champion name position?
            if not isinstance(elem, str):
                valid = False
                break
        elif idx % 3 == 1: # 챔피언 이름 다음 위치에 ":"이 있는가?
                           # Is there a ":" next to the champion name?
            if elem != ':':
                valid = False
                break
        else: # 점수 자리에 정수가 있는가? Istrip('-')은 -를 빼고 숫자 맞는지 체크
              # Is there an integer in the place of the score?
            if not (isinstance(elem, str) and elem.lstrip('-').isdigit()):
                valid = False
                break

    return valid

def Report_system():

    separator = '\n'
    chat_log = separator.join(chat)

    if chat_report == True:
            
        model = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role":"system", "content" : prompt},
                {"role":"user", "content" : chat_log}
            ]
        )

        champ_dict = {}

        result = model.choices[0].message.content.split()
        print(result)

        for i in range(0, len(result), 3): # 이름은 3배수 인덱스에 위치함
                                           # The name is located in a triple index
            champ_name = result[i] # 이름 변수화
                                   # Name Variables
            value = int(result[i + 2]) # 리폿점수
                                       # Report score
            champ_dict[champ_name] = value

        # 가장 감점이 큰 두 챔피언 뽑기
        # Pick the two champions with the most points deducted
        smallest_two = sorted(champ_dict.items(), key=lambda x: x[1])[:2] # 두 번째 요소(value)를 기준으로 정렬 x[1]
                                                                          # Sort by second element (value) x[1]

        # 결과 출력
        # Print result
        print("욕설제제를 받을 플레이어")
        for champ_name, value in smallest_two:
            print(f"{champ_name}: {value}")
    
    chat_report == False

# 리포트 버튼 누르면 True가 된다고 가정
# Assume that the report button is true when pressed
chat_report = True
if chat_report == True:
    Report_system()
