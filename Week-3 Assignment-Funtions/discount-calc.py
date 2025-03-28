def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    
    return final_price

# Get user input
original_price_input = input("Enter the original price of the item: ")
discount_percent_input = input("Enter the discount percentage: ")

# Validate input before conversion
if original_price_input.replace('.', '', 1).isdigit() and discount_percent_input.replace('.', '', 1).isdigit():
    original_price = float(original_price_input)
    discount_percent = float(discount_percent_input)
    
    if original_price > 0 and 0 <= discount_percent <= 100:
        final_price = calculate_discount(original_price, discount_percent)
        print(f"The final price after discount (if applicable) is: {final_price:.2f}")
    else:
        print("Invalid input: Price must be greater than 0 and discount must be between 0 and 100.")
else:
    print("Please enter valid numeric values for price and discount percentage.")
