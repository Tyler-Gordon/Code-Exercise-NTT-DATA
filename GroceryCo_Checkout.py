from collections import Counter
import json

PRICE_LIST_FILENAME = "Prices.json"
GROCERY_LIST_FILENAME = 'Grocery_List.txt'
PROMOTION_LIST_FILENAME = 'Promotion_List.json'
TAX_PERCENTAGE = 12

def get_grocery_list():
	# Get the user's grocery list
	with open(GROCERY_LIST_FILENAME, "r") as file:
		return file.read().splitlines()

def get_promotions():
	# Get all the promotions available
	with open(PROMOTION_LIST_FILENAME, "r") as file:
		data = json.load(file)
		return data

def get_prices():
	# Get all the prices available
	with open(PRICE_LIST_FILENAME, "r") as file:
		data = json.load(file)
		return data

def cart_items_valid(cart, prices):
	# Check if the cart is a subset of all available priced items
	return set(cart).issubset(prices.keys())

def format_currency_CAD(price):
	# Format the price to Canadian dollar formatting
	return "{:,.2f}".format(price)

def count_items_in_cart(cart):
	# Count items in the cart
	user_cart_dictionary = {}
	for item in cart:
		if item not in user_cart_dictionary:
			user_cart_dictionary[item] = 0
		user_cart_dictionary[item] += 1
	return user_cart_dictionary

def calculate_prices(cart, promotions, prices):
	# Create a new dict to keep track of items and prices
	cart_with_prices = {}

	for item, count in cart.items():
		# Cart entry details
		cart_entry = {
			"Count": count,
			"Price": 0
		}

		if item in promotions:
			required_count = promotions[item]['Count']
			# Check if the cart carries the correct amount of items for the promotion
			if count >= required_count:

				# Check how many promotions the cart is eligible for
				promotions_applicable = count // required_count

				# Any remainder items are normal price
				individual_items = count % required_count

				# Add the prices up for the item
				cart_entry["Price"] += individual_items * prices[item]
				cart_entry["Price"] += promotions_applicable * promotions[item]["Price"]

				# Mark the entry with what promotion was used and how many times
				cart_entry["Promotion"] = promotions[item]["Promotion"]
				cart_entry["Promotions_Applied"] = promotions_applicable
			else:
				# If there is a promotion but they did not take enough items, regular price.
				cart_entry["Price"] += count * prices[item]
				cart_entry["Promotions_Applied"] = 0
		else:
			# If not promotion available for that item, regular price is used
			cart_entry["Price"] += count * prices[item]
			cart_entry["Promotions_Applied"] = 0
		
		# Add the item to the final cart
		cart_with_prices[item] = cart_entry
	return cart_with_prices

def calculate_total(cart):
	# Calculate the cart total without tax
	total = 0
	for item, details in cart.items():
		total += details["Price"]
	return total

def get_tax_amount(total):
	# Calculate tax based on cart total
	return total * (TAX_PERCENTAGE / 100)

if __name__ == "__main__":
	cart = get_grocery_list()

	promotions = get_promotions()
	
	prices = get_prices()
	
	if not cart_items_valid(cart, prices):
		print("Invalid Cart Item")
		exit()

	cart_count = count_items_in_cart(cart)

	cart_prices = calculate_prices(cart_count, promotions, prices)

	total_price = calculate_total(cart_prices)
	
	tax = get_tax_amount(total_price)

	final_price = total_price + tax
	print("\n{0:<5} {1:<13} {2:<10} {3:<10}".format("COUNT", "ITEM", "PRICE", "PROMOTIONS"))

	# Print the receipt for the cart
	for item, details in cart_prices.items():
		count = details["Count"]
		price = format_currency_CAD(details["Price"])
		promotions_applied = details["Promotions_Applied"]
		
		if promotions_applied:
			promotion = details["Promotion"]
			# print("%d * $%s: %s \n    Promotions: %d * %s" % (count, item, price, promotions_applied, promotion) )

			print("{0:<5} {1:<13} ${2:<10}{3:<1} * {4:<10}".format(count, item, price, promotions_applied, promotion))
		else:
			# print("%d * %s: %s" % (count, item, price) )
			print("{0:<5} {1:<13} ${2:<10}".format(count, item, price))

	print("\nCart Total: $%s" % (format_currency_CAD(total_price)))
	print("Tax: $%s" % (format_currency_CAD(tax)))
	print("\n#### TOTAL ####")
	print("$%s\n" % format_currency_CAD(final_price))