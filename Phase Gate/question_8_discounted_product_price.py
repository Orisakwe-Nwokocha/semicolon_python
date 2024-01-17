def product_checker(product):
	return product


def discounted_price(product_price):
	product = input("Enter product type: ").casefold()
	product_type = product_checker(product)

	discounted_price_electronic = product_price - (product_price * 0.10)
	discounted_price_clothing = product_price - (product_price * 0.05)
	
	match product_type:
		case 'electronic':
			return f"""Electronic:
   Discount: 10%
   Price before discount: ${product_price}
   Price after discount: ${discounted_price_electronic}"""

		case 'clothing':
			return f"""Clothing:
   Discount: 5%
   Price before discount: ${product_price}
   Price after discount: ${discounted_price_clothing}"""

		case dafault:
			return f"""{product_type.upper()}:
   Discount: None
   Price of product: ${product_price}"""

print(discounted_price(1000))
