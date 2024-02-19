# heroku profitcentr
from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github import Github
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from bs4 import BeautifulSoup
import os
from flask import Flask
import threading
import random
import re
import sys
from io import StringIO

MAX_LOG_MESSAGES = 10  # Maximum number of log messages to display
MAX_PRINT_STATEMENTS = 10  # Maximum number of print statements to display
log_messages = []
stdout_capture = StringIO()
sys.stdout = stdout_capture


account_number = os.getenv("ACCOUNT_NUMBER")
app = Flask(__name__)

@app.route('/')
def hello():
    return f"{'<br>'.join(log_messages[-MAX_LOG_MESSAGES:])}<br>{'<br>'.join(stdout_capture.getvalue().splitlines()[-MAX_PRINT_STATEMENTS:])}"

port = int(os.environ.get("PORT", 5000))

def flask_thread():
    app.run(host="0.0.0.0", port=port)

def running():
    # your existing running() function
    # Use ChromeOptions directly
    
    chrome_options = Options()
    #chrome_options.add_argument(f'--proxy-server={proxy_with_port}')
    #chrome_options.add_argument(f'--user-agent={test_ua}')
    chrome_options.add_argument('--headless')
    
    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Use context manager to handle the WebDriver instance
    with webdriver.Chrome(options=chrome_options) as driver1:
        driver1.get("https://seo-fast.ru/")
        #driver1.maximize_window()
        driver1.set_window_size(1280, 775)
        print("Please wait...")
        
        with open(f'account_{account_number}.json', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver1.add_cookie(cookie)

        driver1.get("https://seo-fast.ru/work_youtube?youtube_video_simple")
        #driver1.save_screenshot("screenshot1.png")
        coin  = WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="ajax_load"]/div/div[3]/span'))).text
        print(coin)
        time.sleep(2)

        v=21
        d=1
        while d < v:
            driver1.execute_script("window.scrollBy(0, 60);")
            time.sleep(0.01)
            d=d+1

        
        # try:
        #     WebDriverWait(driver1, 1).until(
        #                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/div[5]/div/a'))).click()
        #     time.sleep(0.2)
        # except:
        #     pass
        try:
            ids = WebDriverWait(driver1, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[30]/td[2]/div/a/div"))).text
            print(ids)
        
            match = re.search(r'\d+', ids)
            number = match.group()

            time.sleep(1)
            WebDriverWait(driver1, 1).until(                        
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="res_views{number}"]/div/a'))).click()
        
            time.sleep(2)
            driver1.switch_to.window(driver1.window_handles[1])
            time.sleep(5)

            wait = WebDriverWait(driver1, 10).until(
                EC.presence_of_element_located((By.ID, "tmr"))).text
            print(f"Wait: {wait}")

            time.sleep(1)
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)
            #driver1.save_screenshot("screenshot6.png")
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        
        
            time.sleep(2)

            window_handles_after_action = driver1.window_handles
            if len(window_handles_after_action) > 2:
                print("open")
                original_url = driver1.current_url
                driver1.switch_to.window(driver1.window_handles[2])
                new_video_id = "rN9ugM3aGdI"
                modified_url = re.sub(r'(\bvideo_id=)[^&]*', r'\1' + new_video_id, original_url)
                driver1.get(modified_url)
                time.sleep(3)
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)
                #driver1.save_screenshot("screenshot6.png")
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.ENTER)
                actions.perform()

            else:
                print("no")
        
            time.sleep(int(wait) + 3)
        except:
            pass


        driver1.switch_to.window(driver1.window_handles[0])
        main_window_handle = driver1.current_window_handle
        all_window_handles = driver1.window_handles
        # Close all tabs except the main window
        for window_handle in all_window_handles:
            if window_handle != main_window_handle:
                driver1.switch_to.window(window_handle)
                driver1.close()

        # Switch back to the main window
        driver1.switch_to.window(main_window_handle)
        try:
            driver1.get("https://seo-fast.ru/work_youtube?youtube_expensive")
            v=20
            d=1
            while d < v:
                driver1.execute_script("window.scrollBy(0, 60);")
                time.sleep(0.01)
                d=d+1

            ids = WebDriverWait(driver1, 10).until(        
                EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[26]/td[2]/div/a/div"))).text
            print(ids)
        
            match = re.search(r'\d+', ids)
            number = match.group()

            time.sleep(1)
            WebDriverWait(driver1, 1).until(                    
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="res_views{number}"]/div/a'))).click()
            time.sleep(2)
            driver1.switch_to.window(driver1.window_handles[1])
            time.sleep(5)

            wait = WebDriverWait(driver1, 10).until(
                EC.presence_of_element_located((By.ID, "tmr"))).text
            print(f"Wait: {wait}")

            time.sleep(1)
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)
            #driver1.save_screenshot("screenshot6.png")
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            time.sleep(2)

            window_handles_after_action = driver1.window_handles
            if len(window_handles_after_action) > 2:
                print("open")
                original_url = driver1.current_url
                driver1.switch_to.window(driver1.window_handles[2])
                new_video_id = "rN9ugM3aGdI"
                modified_url = re.sub(r'(\bvideo_id=)[^&]*', r'\1' + new_video_id, original_url)
                driver1.get(modified_url)
                time.sleep(3)
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)
                #driver1.save_screenshot("screenshot6.png")
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.ENTER)
                actions.perform()

            else:
                print("no")
        
            time.sleep(int(wait) + 3)
        except:
            pass

        driver1.switch_to.window(driver1.window_handles[0])
        main_window_handle = driver1.current_window_handle
        all_window_handles = driver1.window_handles
        # Close all tabs except the main window
        for window_handle in all_window_handles:
            if window_handle != main_window_handle:
                driver1.switch_to.window(window_handle)
                driver1.close()
        # Switch back to the main window
        driver1.switch_to.window(main_window_handle)
        
        
        try:
            driver1.get("https://seo-fast.ru/work_youtube?youtube_rare")
            v=23
            d=1
            while d < v:
                driver1.execute_script("window.scrollBy(0, 60);")
                time.sleep(0.01)
                d=d+1

            ids = WebDriverWait(driver1, 10).until(        
                EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[30]/td[2]/div/a/div"))).text
            print(ids)
        
            match = re.search(r'\d+', ids)
            number = match.group()

            time.sleep(1)
            WebDriverWait(driver1, 1).until(                         
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="res_views{number}"]/div/a'))).click()
            time.sleep(2)
            driver1.switch_to.window(driver1.window_handles[1])
            time.sleep(5)

            wait = WebDriverWait(driver1, 10).until(
                EC.presence_of_element_located((By.ID, "tmr"))).text
            print(f"Wait: {wait}")

            time.sleep(1)
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)
            #driver1.save_screenshot("screenshot6.png")
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            time.sleep(2)

            window_handles_after_action = driver1.window_handles
            if len(window_handles_after_action) > 2:
                print("open")
                original_url = driver1.current_url
                driver1.switch_to.window(driver1.window_handles[2])
                new_video_id = "rN9ugM3aGdI"
                modified_url = re.sub(r'(\bvideo_id=)[^&]*', r'\1' + new_video_id, original_url)
                driver1.get(modified_url)
                time.sleep(3)
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)
                #driver1.save_screenshot("screenshot6.png")
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.ENTER)
                actions.perform()

            else:
                print("no")
        
            time.sleep(int(wait) + 3)
        except:
            pass



        driver1.switch_to.window(driver1.window_handles[0])
        main_window_handle = driver1.current_window_handle
        all_window_handles = driver1.window_handles
        # Close all tabs except the main window
        for window_handle in all_window_handles:
            if window_handle != main_window_handle:
                driver1.switch_to.window(window_handle)
                driver1.close()
        # Switch back to the main window
        driver1.switch_to.window(main_window_handle)
        
        
        try:
            driver1.get("https://seo-fast.ru/work_youtube?youtube_time")
            v=23
            d=1
            while d < v:
                driver1.execute_script("window.scrollBy(0, 60);")
                time.sleep(0.01)
                d=d+1

            ids = WebDriverWait(driver1, 10).until(        
                EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[30]/td[2]/div/a/div"))).text
            print(ids)
        
            match = re.search(r'\d+', ids)
            number = match.group()

            time.sleep(1)
            WebDriverWait(driver1, 1).until(                         
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="res_views{number}"]/div/a'))).click()
            time.sleep(2)
            driver1.switch_to.window(driver1.window_handles[1])
            time.sleep(5)

            wait = WebDriverWait(driver1, 10).until(
                EC.presence_of_element_located((By.ID, "tmr"))).text
            print(f"Wait: {wait}")

            time.sleep(1)
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)
            #driver1.save_screenshot("screenshot6.png")
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.5)

            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            time.sleep(2)

            window_handles_after_action = driver1.window_handles
            if len(window_handles_after_action) > 2:
                print("open")
                original_url = driver1.current_url
                driver1.switch_to.window(driver1.window_handles[2])
                new_video_id = "rN9ugM3aGdI"
                modified_url = re.sub(r'(\bvideo_id=)[^&]*', r'\1' + new_video_id, original_url)
                driver1.get(modified_url)
                time.sleep(3)
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)
                #driver1.save_screenshot("screenshot6.png")
                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.TAB)
                actions.perform()
                time.sleep(0.5)

                actions = webdriver.ActionChains(driver1)
                actions.send_keys(Keys.ENTER)
                actions.perform()

            else:
                print("no")
        
            time.sleep(int(wait) + 3)
        except:
            pass

        driver1.quit()
        time.sleep(5)
        print("Cookies copied successfully..")

def sdsf():
    while True:
        try:
            running()
        except:
            continue





# Start Flask in a separate thread
flask_thread = threading.Thread(target=flask_thread)
flask_thread.start()



flask_thread1 = threading.Thread(target=sdsf)
flask_thread1.start()






if __name__ == '__main__':
    # This block will only be executed when the script is run directly, not when imported
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        scheduler.shutdown()


sys.stdout = sys.__stdout__