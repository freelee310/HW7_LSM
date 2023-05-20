import pandas as pd
import numpy as np
from numpy import array

def main() -> int:
    # 'gender2.csv' 파일을 읽어와서 데이터프레임 생성
    df = pd.read_csv('gender2.csv', encoding='cp949', index_col='행정구역')

    # 총 인구수(Total), 남 총 인구수(Male), 여 총 인구수(Female) columns을 선택하여 new 데이터프레임 생성
    new_df = df[['2022년_계_총인구수','2022년_남_총인구수','2022년_여_총인구수']]

    # 컬럼 이름 변경(총 인구수 -> Total, 남 총 인구수 -> Male, 여 총 인구수 -> Female)
    new_df.columns = ['Total', 'Make', 'Female']

    # 최종 데이터프레임 전체 출력
    print(new_df)

# entry point of program
if __name__ == '__main__':
	main()