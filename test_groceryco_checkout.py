from groceryco_checkout import *
import unittest


PRICE_LIST_FILENAME = "testing/Test_Prices.json"
GROCERY_LIST_FILENAME = 'testing/Test_Grocery_List.txt'
PROMOTION_LIST_FILENAME = 'testing/Test_Promotion_List.json'
TAX_PERCENTAGE = 12

class TestGroceryCoCheckout(unittest.TestCase):
	def test_get_grocery_list_type(self):
		self.assertIsInstance(get_grocery_list(), list, "Should return a list")

	def test_get_grocery_list_length(self):
		cart = get_grocery_list()
		self.assertEqual(len(cart), 12, "Grocery List should be of length 12")

	def test_get_promotions_type(self):
		self.assertIsInstance(get_promotions(), dict, "Should return a dictionary")

	def test_get_promotions_length(self):
		promotions = get_promotions()
		self.assertEqual(len(promotions), 4, "Promotions dictionary should be of length 4")

	def test_get_prices_type(self):
		self.assertIsInstance(get_prices(), dict, "Should return a dictionary")

	def test_get_prices_length(self):
		prices = get_prices()
		self.assertEqual(len(prices), 5, "Promotions dictionary should be of length 4")

	def test_format_currency_integer(self):
		self.assertEqual(format_currency_CAD(2), "$2.00", "Should return a string in dollar formatting")
	
	def test_format_currency_float(self):
		self.assertEqual(format_currency_CAD(5.00), "$5.00", "Should return a string in dollar formatting")

	def test_count_items_in_cart_type(self):
		cart = get_grocery_list()
		self.assertIsInstance(count_items_in_cart(cart), dict, "Should return a dictionary")

	def test_count_items_in_cart_length(self):
		cart = get_grocery_list()
		self.assertEqual(len(count_items_in_cart(cart)), 5, "Counted items dictionary should be of length 5")

	def test_calculate_prices_type(self):
		cart = get_grocery_list()
		promotions = get_promotions()
		prices = get_prices()
		cart_count = count_items_in_cart(cart)
		self.assertIsInstance(calculate_prices(cart_count, promotions, prices), dict, "Should return a dictionary")

	def test_calculate_total(self):
		cart = get_grocery_list()
		promotions = get_promotions()
		prices = get_prices()
		cart_count = count_items_in_cart(cart)
		cart_prices = calculate_prices(cart_count, promotions, prices)
		total_price = calculate_total(cart_prices)
		self.assertEqual(total_price, 12.21, "Counted items dictionary should be of length 5")

	def test_get_tax_amount(self):
		self.assertEqual(get_tax_amount(10.50), 1.26, "Tax should be 12% of total price")

if __name__ == '__main__':
    unittest.main()
