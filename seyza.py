import asyncio
from pyppeteer import launch

async def main():
    # Lança o navegador
    browser = await launch()
    # Abre uma nova página
    page = await browser.newPage()
    # Acessa a URL
    await page.goto('https://stresse.net/login')

    # Busca pelo elemento específico
    element = await page.querySelector('input[type="text"][required="required"][placeholder="Username"].form-control')
    
    # Verifica se o elemento foi encontrado
    if element:
        print("Acessou a página com sucesso.")
    else:
        print("Elemento não encontrado.")

    # Fecha o navegador
    await browser.close()

# Executa o programa
asyncio.get_event_loop().run_until_complete(main())
