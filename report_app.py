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
        smallest_two = sorted(champ_dict.items(), key=lambda x: x[1])[:2]# 두 번째 요소(value)를 기준으로 정렬 x[1]

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
