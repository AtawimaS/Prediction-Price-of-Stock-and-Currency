from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

find = "Bitcoin"
link = f"https://www.threads.net/search?q={find}&serp_type=tags"

user_css = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xjohtrz.x1s688f.xp07o12.x1yc453h"
pesan_css = ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xjohtrz.xo1l8bm.xp07o12.x1yc453h.xat24cr.xdj266r"
date_css = "time.x1rg5ohu.xnei2rj.x2b8uid.xuxw1ft"

driver = webdriver.Chrome()
driver.get(link)

try:
    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "x6ikm8r.x10wlt62.xlyipyv"))
    )
    login_button.click()
    print("Clicked login button.")
except Exception as e:
    print(f"Error clicking login button: {e}")

# Find and fill the username field
try:
    userid = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".x1i10hfl.x9f619.xggy1nq.x1s07b3s.x1kdt53j.x1a2a7pz.x90nhty.x1v8p93f.xogb00i.x16stqrj.x1ftr3km.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.xp07o12.xjohtrz.x1a6qonq.xyamay9.x1pi30zi.x1l90r2v.x1swvt13.x1yc453h.xh8yej3.x1e899rk.x1sbm3cl.x1rpcs5s.x1c5lum3.xd5rq6m"))
    )
    userid.send_keys("atawimas")
except Exception as e:
    print(f"Error finding username field: {e}")

try:
    passid = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Password"]'))
    )
    passid.send_keys("Blink182will_")
    passid.send_keys(Keys.ENTER)
except Exception as e:
    print(f"Error finding password field: {e}")

driver.get(link)


time.sleep(50)
