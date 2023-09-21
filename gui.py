import time
import tkinter as tk
from tkinter import font
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

def button_clicked1():
    global naver_id, naver_pw
    naver_id = id_entry.get()
    naver_pw = pw_entry.get()
    options = webdriver.ChromeOptions()
    options.add_argument('chromedriver.exe')
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.execute_script("window.open('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')")
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script(f"document.getElementById('id').value='{naver_id}'")
    driver.execute_script(f"document.getElementById('pw').value='{naver_pw}'")
    driver.find_element('id', 'log.login').click()
    driver.get('https://www.naver.com/')
    search = driver.find_element('id', 'query')
    search.send_keys('대구날씨', Keys.ENTER)

def button_clicked2():
    subprocess.call('exm01.py', shell=True)

# Tkinter 창 생성
window = tk.Tk()
window.title("전기차 파라노믹 디스플레이")
window.geometry("400x300+200+200")

# 현재 시간을 표시할 레이블 생성
clock_label = tk.Label(window, text="", font=('Arial', 40))
clock_label.pack()

# 아이디 입력 필드
id_label = tk.Label(window, text="아이디:")
id_label.pack()
id_entry = tk.Entry(window)
id_entry.pack()

# 비밀번호 입력 필드
pw_label = tk.Label(window, text="비밀번호:")
pw_label.pack()
pw_entry = tk.Entry(window, show="*")
pw_entry.pack(pady=8)

# 날씨 버튼 스타일 변경
weather_button = tk.Button(window, text="날씨", command=button_clicked1, width=20, height=1)
weather_button.config(relief=tk.RAISED, bg='lightblue', fg='black', font=('Arial', 20, 'bold'))
weather_button.pack(pady=2)

# 네비게이션 버튼 스타일 변경
navigation_button = tk.Button(window, text="전기차 충전소", command=button_clicked2, width=20, height=1)
navigation_button.config(relief=tk.RAISED, bg='blue', fg='white', font=('Arial', 20, 'bold'))
navigation_button.pack(pady=2)


# 시간 업데이트 시작
update_clock()

# Tkinter 이벤트 루프 시작
window.mainloop()