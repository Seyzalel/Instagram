from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import telebot
import os

TOKEN = '7091104502:AAHAkisdLFjjsuLEGoYbnuMkG86U4Tvai_g'
bot = telebot.TeleBot(TOKEN)

def take_screenshot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("accept-language=pt-BR,pt;q=0.9")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get("https://instagram.com/")
        screenshot_path = "instagram_screenshot.png"
        driver.save_screenshot(screenshot_path)
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        driver.quit()
    return screenshot_path

@bot.message_handler(commands=['start'])
def send_welcome(message):
    screenshot_path = take_screenshot()
    with open(screenshot_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(screenshot_path)

bot.polling()