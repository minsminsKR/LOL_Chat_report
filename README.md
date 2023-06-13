# LOL_Chat_report

GPT api를 사용하여 욕설 리폿 기준을 설정한 후 리폿될 플레이어를 정합니다.

어떠한 채팅 로그가 input으로 들어가면, 결과는 다음과 같은 리스트 형태로 반환됩니다.

['Garen', ':', '-4', 'Leesin', ':', '-3', 'Karma', ':', '0', 'Apelios', ':', '0', 'Yumi', ':', '0']


욕설제제를 받을 플레이어

Garen: -4

Leesin: -3

여기서 감점이 가장 높은 두 사람은 변수로 할당되고 리폿대상으로 설정됩니다.

언제든지 원하는대로 리폿 기준을 변경할 수 있습니다.


# ENG.


Use GPT api to set the criteria for abusive words reporting and then decide which players to report.

If chatting log is putted the result is printed as a list form like

['Garen', ':', '-4', 'Leesin', ':', '-3', 'Karma', ':', '0', 'Apelios', ':', '0', 'Yumi', ':', '0']


Abusive players

Garen: -4

Leesin: -3

Here, I have set the two people with the highest deduction points as the report target,

but you guys can change the criteria anytime you want.
