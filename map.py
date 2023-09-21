import pandas as pd
import requests         #api 호출
import json
import webbrowser       #생성된 html파일 호출
import folium           #지도 시각화 라이브러리

#엑셀파일 데이터 불러오기
tg = pd.read_excel('c://DIP/daegu_ev4.xlsx')
#불러온 데이터에서 필요한 열 선택
tg = tg[['충전소명', '사용횟수', '충전량', '위도', '경도']]

#foliumMap으로 지도 생성
#대구 위도와 경도 찍기
#zoom_start 1~18로 표시하는 지도 크기 선택

m = folium.Map(
    location=[35.8714354, 128.601445],
    zoom_start=11,
)

#github에 있는 대구광역시 행정구역 json 호출
deagu = requests.get('https://raw.githubusercontent.com/raqoon886/Local_HangJeongDong/master/hangjeongdong_%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C.geojson')
daegu_geo = deagu.json()

folium.GeoJson(
    daegu_geo,
).add_to(m)

tg_sorted = tg.sort_values('충전량', ascending=True)

for i, row in enumerate(tg_sorted.iterrows()):
    charge_amount = row[1]['충전량']
    charger_name = row[1]['충전소명']
    latitude = row[1]['위도']
    longitude = row[1]['경도']

#내림차순 정리하여 출력
    print(f"{i + 1}. 충전소명: {charger_name}, 사용횟수: {row[1]['사용횟수']}, 충전량: {charge_amount}")


#3만까지는 파랑 6만까지는 빨강, 그 이외는 검정색으로 표시
    if charge_amount <= 30000:
        marker_color = 'blue'
    elif charge_amount <= 60000:
        marker_color = 'red'
    else:
        marker_color = 'black'

#위도 경도로 표시된 각 충전소 원마크로 표시
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=7,
        fill=True,
        fill_color=marker_color,
        color=marker_color,
        popup=f"<b>{i + 1}</b>{charger_name}",
        ).add_to(m)


#파이썬에서는 따로 map을 보여주지 않기 때문에 html로 데이터 저장
#후에 저장된 html을 실행하여 화면에 출력

m.save('maps.html')

webbrowser.open('maps.html')