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

        for i in range(0, len(result), 3):# 이름 3배수 인덱스에 위치함
            champ_name = result[i] # 이름 변수화
            value = int(result[i + 2]) # 리폿점수
            champ_dict[champ_name] = value

        # 가장 작은 수를 가진 두 캐릭터를 뽑기 위한 코드
        smallest_two = sorted(champ_dict.items(), key=lambda x: x[1])[:2]# 두 번째 요소(value)를 기준으로 정렬 x[1]

        # 결과 출력
        print("욕설제제를 받을 플레이어")
        for champ_name, value in smallest_two:
            print(f"{champ_name}: {value}")
    
    chat_report == False

# 리포트 버튼 누르면 True가 된다고 가정
chat_report = True
if chat_report == True:
    Report_system()