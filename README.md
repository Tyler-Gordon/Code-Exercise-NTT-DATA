#  Code-Exercise-NTT-DATA

Code Exercise for NTT Data Recruitment

## GroceryCo Checkout System
Requirements:
- Python 3: installed and runnable from command line (see https://www.python.org/downloads/ for instructions on installing Python 3)
### How to run
1. Clone or download this repository
2. Use your terminal to navigate to the directory where it has downloaded
3. Use the command: `python groceryco_checkout.py` to run the checkout system

### Adding/Modifying the user grocery list
The user grocery list is a plant text file that uses a newline as a delimiter for each item. If an item in the cart is not registered in the `Prices.json` file (which are all available items) the program will return with "Invalid Cart Item"

To add an item, simply create a new line and enter the item's name.

### Adding/Modifying the available promotions
The promotions are stored in `Promotion_List.json`, using the JSON format.
The structure of a promotion is:
```JSON
{
	"ITEM":  {
		"Promotion":  "PROMOTION NAME",
		"Count":  REQUIRED NUMBER OF ITEMS FOR PROMOTION,
		"Price":  THE NEW PRICE
	}
}
```
For example:
```JSON
{
	"Orange":  {
		"Promotion":  "BULK",
		"Count":  3,
		"Price":  2.00
	}
}
```
### Adding/Modifying the prices
The prices are stored in `Prices.json` using the JSON format.
The structure of an item and its price is:
```JSON
{
"ITEM" : PRICE
}
```
For example:
```JSON
{
"Apple":  0.75,
}
```

## Testing
### How to run the tests:
1. Use your terminal to navigate to the directory where it has downloaded
2. Use the command: `python test_groceryco_checkout.py` to run the checkout system
3. The output shows how many test cases passed and failed.

### Modifying tests cases and values
The tests are located in the `test_groceryco_checkout.py` file, and the associated input files (grocery list, prices, and promotions) are located under the `testing/` folder. These are used by the test cases as mock data. Modifying the mock data will likely cause tests to fail because of hardcoded expected results.

## Errors/Troubleshooting
- Invalid Cart Item
	- This means an item in your grocery list is not a registered item in the `Prices.json` file.
- ``python is not recognized as an internal or external command,
operable program or batch file.``
	- This is an issue if your Python is not added to your Window's path. See: https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows