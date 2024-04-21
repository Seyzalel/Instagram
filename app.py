import asyncio
from pyppeteer import launch

async def main():
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
    try:
        await page.waitForNavigation()
        saveInfoButton = await page.waitForSelector('button[class="_acan _acap _acas _aj1- _ap30"]', {'visible': True})
        await saveInfoButton.click()
        print("Login foi bem sucedido.")
    except:
        print("Login mal sucedido.")

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())