from hanspell import spell_checker
import pandas as pd
import requests

# CSV 파일 로드
df = pd.read_csv('데이터 전처리.csv')

# 텍스트 데이터 추출
texts = df['review'].tolist()

