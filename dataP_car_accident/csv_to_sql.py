import pymysql
import pandas as pd
from sqlalchemy import create_engine

# MySQL 연결 정보 설정
db_host = '127.0.0.1'
db_user = 'car_accident'
db_password = '1111'
db_name = 'accident'


# MySQL 연결 생성
connection = pymysql.connect(
    host=db_host,
    port=3306, 
    user=db_user, 
    password=db_password, 
    db=db_name)

# print(type(connection))
# 연결 완료 된 경우에는 아래와 같이 출력되어야 함.
# <class 'pymysql.connections.Connection'>

df = pd.read_csv("./서울시_교통사고현황.csv")
df