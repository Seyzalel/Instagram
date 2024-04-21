import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--window-size=1920,1080'])
    page = await browser.newPage()
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    await page.goto('https://stresse.net/login')
    try:
        await page.waitForSelector('input[type="text"][required="required"][placeholder="Username"].form-control', timeout=30000)
        print("Acessou a página com sucesso.")
    except:
        print("Elemento não encontrado.")
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())