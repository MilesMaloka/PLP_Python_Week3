# This code calculates the final price of an item after applying a discount if the discount percentage is 20% or more.
def calculate_discount(price, discount_percent):
    if discount_percent >=20: 
        discount = (discount_percent / 100) * price
        final_price = price - discount
        return final_price
    else: 
        final_price = price
        return final_price
    
price = int(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)
print(f"The final price after discount is: {final_price}")

