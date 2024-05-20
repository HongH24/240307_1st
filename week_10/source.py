# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:11:18 2024

@author: Honghee Kim
"""

from gtts import gTTS
tts= gTTS("I am going to school", lang="en")
tts.save("mySound.mp3")


from datetime import datetime
place="런던"
time="12"
goals="3"

news="[프리미어 리그 속보("+str(datetime.now())+")]\n"
news=news+"손흥민 선수는 "+place+"에서 "+time+"에 열린 경기에 출전하였습니다. "
news=news+"손흥민 선수는 "+goals+"골로 승리를 이끌었습니다. "

print(news)

tts= gTTS(text=news, lang='ko')
tts.save("news_Son_ko.mp3")

tts= gTTS(text=news, lang='en')
tts.save("news_Son_en.mp3")

tts= gTTS(text=news, lang='fr')
tts.save("news_Son_fr.mp3")
