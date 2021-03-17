from collections import Counter

PRICES = {
	"Apple" : 0.75,
	"Orange": 1.00,
	"Red Pepper" : 0.99
}

PROMOTIONS = ["Apple"]

USER_CART = ['Apple', 'Orange', 'Apple', 'Red Pepper']

def format_currency(price):
	return "${:,.2f}".format(price)

def count_items_in_cart(cart):
	user_cart_dictionary = {}
	for item in cart:
		if item not in user_cart_dictionary:
			user_cart_dictionary[item] = 0
		user_cart_dictionary[item] += 1
	return user_cart_dictionary

def calculate_prices(cart):
	cart_with_prices = {}

	for item, count in cart.items():
		price = 0
		cart_with_prices[item] = {}
		cart_with_prices[item]['Details'] = {}
		if item in PROMOTIONS:
			price, promotion = calculate_promotion_price(item, count)
			cart_with_prices[item]['Details']["Promotion"] = promotion
		else:
			price = PRICES[item] * count
			cart_with_prices[item]['Details']["Promotion"] = ""

		cart_with_prices[item]['Details']["Price"] = price
		cart_with_prices[item]['Details']["Count"] = count
	return cart_with_prices

def calculate_promotion_price(item, count):
	return PRICES[item], "BOGO"

def calculate_total_price(final_prices):
	total = 0
	for item, details in final_prices.items():
		if item not in PRICES:
			print("ERROR: NO PRICE FOUND FOR: ", item, "PLEASE TALK TO CASHIER")
			return("ERROR: NO PRICE FOUND")
		print("%d * %s: %s   %s" % (details['Details']['Count'], item, format_currency(details['Details']['Price']), details['Details']['Promotion']))
		total += final_prices[item]['Details']['Price']
	return total


if __name__ == "__main__":
	
	cart_count = count_items_in_cart(USER_CART)

	cart_prices = calculate_prices(cart_count)

	total = calculate_total_price(cart_prices)
	print("#### TOTAL ####")
	print("$%s" % total)