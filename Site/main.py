from flask import Flask, url_for, request, render_template, redirect

from config import *

app = Flask(__name__)

""" Создание структуры продуктов """

pr = ProductsStructure(logs = 1)

pr.create_product_structure()

""" Подготовка глобальных данных """

global_data = {
	"NAME_SHOP":NAME_SHOP,
}

""" Подключение урл путей """
@app.route('/')
def index():

	return_data = {
		"PRODUCTS": pr.products,
	}

	return render_template(SETTING_TEMPLATE["index"], data=return_data, global_data=global_data)

@app.route('/<int:id>')
def product(id):
	product = pr.search_to_structure(id)

	return render_template(SETTING_TEMPLATE["product_info"], data=product, global_data=global_data)

@app.route('/order/<int:id>', methods=["GET", "POST"])
def order(id):

	notifications = []

	if request.form["phone_number"] == "":
		notifications.append("Вы забыли указать номер")
	else:
		if request.method == 'POST':

			product = pr.search_to_structure(id)

			with open('orders.txt', 'a', encoding='utf-8') as file:
			    file.write(
			    	f"\n[{GetTime()}] Заказ оформлен. Номер телефона: {request.form['phone_number']}. "
			    	f"Информация о заказе: Название {product['name']} | Краткое описание: {product['short_description']} | Цена: {product['price']}\n")

			return redirect(url_for('index'))

			
	product = pr.search_to_structure(id)

	return render_template(SETTING_TEMPLATE["product_info"], data=product, global_data=global_data, notifications=notifications)

if __name__ == "__main__":

	app.run(debug=True)