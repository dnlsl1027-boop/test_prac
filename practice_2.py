import pandas as pd
import numpy as np

df = pd.read_csv('data_analysis_adv/datasets/bike_rentals/bike_rentals.csv')
#print(df)

df.iloc[2, 3] = np.nan
# 결측치를 임의로 만들기 위해 추가
#iloc로 2행 3열 선택

#pd.set_option('display.max_columns', None)
#set_option : 출력 및 동작 조절 함수 / display.max_columns : 중간 생략하지 않음

#print(df.head(10))
#print(df.isna().sum())
#isna()가 naN확인 / 결측지가 있으면 True로 반환함
#head() : 앞에 5개 / tail() : 뒤에 5개

