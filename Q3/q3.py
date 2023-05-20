import pandas as pd
import numpy as np
from numpy import array

def main() -> int:
    # 단가(unit price)와 갯수(number)로 이루어진 데이터 프레임 생성 및 출력
    df = pd.DataFrame(array([[1000,25],[280,120],[900,30]]), index=['store1','store2','store3'], columns=['unit price','number'])
    print(df)

    # 단가와 갯수를 곱한 총가격(total price)이 추가된 데이터 프레임 생성 및 출력
    df.insert(2,'total price', np.multiply(df['unit price'].to_numpy(),df['number'].to_numpy()))    # 데이터 프레임에 단가와 갯수를 곱한 총가격 컬럼 추가
    print(df)

    # 총가격이 가장 비싼 가게순으로 2개 출력
    print(df.sort_values(by='unit price', ascending=True).head(2))

# entry point of program
if __name__ == '__main__':
	main()