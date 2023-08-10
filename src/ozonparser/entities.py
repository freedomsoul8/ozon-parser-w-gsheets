

class ProductService:

    class Product:
        name = str
        link = str
        price_ozon_card = str
        price_no_ozon_card = str
        price_crossed = str

    product = Product()

    class Path:
        name = "/html/body/div[1]/div/div[1]/div[4]/div[2]/div/div/div[1]/div[2]/h1"
        ozon_card = "/html/body/div[1]/div/div[1]/div[4]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/span/div/div[1]/div/div/span"
        no_ozon_card = "/html/body/div[1]/div/div[1]/div[4]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[1]/span[1]"
        crossed = "/html/body/div[1]/div/div[1]/div[4]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[1]/span[2]"

    path = Path()

product_service = ProductService()
