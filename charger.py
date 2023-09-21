import pandas as pd

df1= pd.read_csv('C:\data3\miniP/daegu ev used now_20220531.csv',encoding='cp949')
df2= pd.read_csv('C:\data3\miniP/daegu ev charger now.csv',encoding='cp949')

df1_1=df1.loc[:,['충전소명칭','사용횟수','충전량','위도','경도']]
df1_1['위도'] = df1_1['위도'].astype(str)
df1_1['경도'] = df1_1['경도'].astype(str)
df1_1 = df1_1.rename(columns={'충전소명칭': '충전소명'})
df1_1 = df1_1.groupby('충전소명').agg({'위도': 'first', '경도': 'first',
                                   '충전량': 'sum', '사용횟수': 'sum'}).reset_index()

#print(df1_1)
df1_1.to_csv('C:\data3\miniP/sum_by_charger.csv',index=False)
#----------------------
#print(df2.columns)
#df2_1=df2.loc[:,['충전소명']]
df2_2=df2.groupby(by='충전소명')['충전기 ID'].nunique().reset_index()
#print(df2_2)
df2_2.to_csv('C:\data3\miniP/charger now name.csv')
#----------------------

df3 = pd.read_csv('C:\data3\miniP/sum_by_charger.csv')
df4 = pd.read_csv('C:\data3\miniP/charger now name.csv')
#----------------------

df5=pd.concat([df3,df4])
#print(df5.to_string())
df5_1 = df5.groupby('충전소명').agg({'위도': 'first', '경도': 'first',
                                 '충전기 ID':'first', '충전량': 'sum',
                                 '사용횟수': 'sum'}).reset_index()
print(df5_1)
df5_1['기기당 사용량']=df5_1['사용횟수']/df5_1['충전기 ID']
print(df5_1.to_string())
df5_1['충전소명'] = df5_1['충전소명'].str.replace('대구시_', '')
df5_2 = df5_1.groupby('충전소명').agg({'위도': 'first', '경도': 'first',
                                 '충전기 ID':'first', '충전량': 'sum',
                                 '사용횟수': 'sum'}).reset_index()\
    .sort_values('사용횟수',ascending=False)
#----------------------

#print(df5_2)
df5_2.to_csv('C:\data3\miniP/final2.csv',index=False)
df5_2.to_excel(excel_writer='C:\data3\miniP/final2.xlsx',index=False)