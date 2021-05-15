from datetime import datetime as dt
from prettytable import PrettyTable

from colorama import Fore

NAME_SHOP = "ATLANT"

SETTING_TEMPLATE = {
	"index":"index.html",
	"product_info":"product_info.html",
}

""" Время """
def GetTime():
	time = str(dt.now())[11:19]
	day = str(dt.now())[8:10]
	month = str(dt.now())[5:7]
	year = str(dt.now())[0:4]

	return f"{time} {day}/{month}/{year}"

""" Структура товаров """
class ProductsStructure():
	def __init__(self, logs):
		self.products = []
		self.last_id = 1

		self.table = PrettyTable([f"{Fore.YELLOW}ID{Fore.RESET}", f"{Fore.YELLOW}NAME{Fore.RESET}", f"{Fore.YELLOW}SHORT_DESCRIPTION{Fore.RESET}", f"{Fore.YELLOW}PRICE{Fore.RESET}"])

		self.log_status = logs

	def logs(self):
		for product in self.products:
			self.table.add_row([product['id'], product["name"], product["short_description"], product["price"]])

		print(self.table)

	def add_product(self, name=None, description=None, price=None):
		product = {
			"id":self.last_id,
			"name":name,
			"price":price,
			"description":description,
		}
		if len(description) >= 60: 
			product["short_description"] = description[:60] + "..."
		else:
			product["short_description"] = description

		self.last_id += 1

		self.products.append(product)

	def search_to_structure(self, id):
		for product in self.products:
			if product['id'] == id:
				return product

	""" Ниже прописываем создание всех продуктов в сттруктуре """
	def create_product_structure(self):

		self.add_product(name="Холодильник SAMSUNG RB38T676FSA/UA", description="Тип холодильника: Двухкамерный, Общий объем холодильника: 400 л, Система разморозки: No Frost (Frost Free), Холодильное+морозильное отделения, Габариты (ВхШхГ): 203 x 59.5 x 65.8 см", price="16 499₴")
		self.add_product(name="Холодильник BOSCH KGN39VI306",description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 400 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):203 x 60 x 66 см", price="15 299₴")
		self.add_product(name="Холодильник SAMSUNG RB29FSRNDSA/UA", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 311 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):178 х 59.5 х 66.8 см", price="11 499₴")
		self.add_product(name="Xолодильник INDESIT XIT8 T2E X", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 356 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):188.8 х 59.5 х 65.5 см", price="11 999₴")
		self.add_product(name="Xолодильник BOSCH KGN36XI30U", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 325 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):186 х 60 х 66 см", price="14 899₴")
		self.add_product(name="Xолодильник SHARP SJ-T1227M5W-UA", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 230 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):144 х 54 х 59.5 см", price="5 899₴")
		self.add_product(name="Xолодильник BOSCH KGN36XIK30U", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 360 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):186 х 60 х 66 см", price="15 999₴")
		self.add_product(name="Холодильник SAMSUNG RB29FSRNDSA/UA", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 315 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):178 х 59.5 х 66.8 см", price="11 499₴")
		self.add_product(name="Xолодильник INDESIT XIT8 T2E X", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 356 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):188.8 х 59.5 х 65.5 см", price="11 999₴")
		self.add_product(name="Xолодильник WHIRLPOOL ART 9811/A++ SF", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 450 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):193.5 х 54 х 54.5 см", price="16 313₴")
		self.add_product(name="Xолодильник Whirlpool ART 9620 A++ NF", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 341 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):193.5x54x55 см", price="17 999₴")
		self.add_product(name="Xолодильник INDESIT DF 4201 W", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 369 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):200х60х64 см", price="9 179₴")
		self.add_product(name="Xолодильник MYSTERY MRF-8090W", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 82 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):84 х 48 х 43 см", price="3 299₴")
		self.add_product(name="Xолодильник SAMSUNG RS52N3203SA/UA", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 554 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):178.9 х 91.2 х 73.4 см", price="24 999₴")
		self.add_product(name="Холодильник LIEBHERR CP 4313", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 368 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):186.1х60х65.5 см", price="13 999₴")
		self.add_product(name="Xолодильник INDESIT TIAA 14 (UA)", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 249 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):145х60х66.5 см", price="6 499₴")
		self.add_product(name="Xолодильник BEKO RCNA406E35ZXB", description="Тип холодильникa: Двухкамерный,Общий объем холодильникa: 388 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):202.5 х 59.5 х 67 см", price="12 653₴")
		self.add_product(name="Xолодильник BEKO RDSU8240K20W", description="Тип холодильник: Двухкамерный,Общий объем холодильникa: 360 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):146.5 х 54 х 57.5 см", price="6 499₴")
		self.add_product(name="Холодильник BOSCH KGN36NW306", description="Тип холодильник: Двухкамерный,Общий объем холодильникa: 329 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):186x60x66 см", price="13 099₴")
		self.add_product(name="Xолодильник SNAIGE RF39SM-P0002F", description="Тип холодильник: Двухкамерный,Общий объем холодильникa: 350 л, Система разморозки: No Frost (FrostFree),Холодильное+морозильное отделения, Габариты(ВхШхГ):200 x 60 x 65 см", price="10 191₴")

		if self.log_status == 1:
			self.logs()