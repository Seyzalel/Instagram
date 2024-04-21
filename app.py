import asyncio
from pyppeteer import launch
import telebot
import nest_asyncio
nest_asyncio.apply()

bot_token = '7091104502:AAHAkisdLFjjsuLEGoYbnuMkG86U4Tvai_g'
bot = telebot.TeleBot(bot_token, parse_mode=None)

async def login_and_screenshot(chat_id):
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--window-size=1920,1080'])
    page = await browser.newPage()
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    await page.goto('https://www.instagram.com/accounts/login/')

    await page.waitForSelector('input[name="username"]', {'visible': True})
    await page.type('input[name="username"]', 'abra_paola', {'delay': 100})
    await page.waitForSelector('input[name="password"]', {'visible': True})
    await page.type('input[name="password"]', 'Sey17zalel17@$', {'delay': 100})
    
    loginButton = await page.waitForSelector('div[class^="x9f619"]', {'visible': True})
    await loginButton.click()
    screenshot_path = f'{chat_id}_login_screenshot.png'
    await page.screenshot({'path': screenshot_path})
    await browser.close()
    return screenshot_path

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    asyncio.run(login_and_screenshot(chat_id))
    photo = open(f'{chat_id}_login_screenshot.png', 'rb')
    bot.send_photo(chat_id, photo)
    photo.close()

bot.polling()