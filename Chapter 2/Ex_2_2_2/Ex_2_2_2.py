# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

book = 24.95
discount = 0.4
initial_shipping = 3
additional_shipping = 0.75
copies = 60

book_total = book * copies
discount_total = book_total - (book_total * discount)
total_with_shipping = (discount_total + initial_shipping) + (additional_shipping * copies)
print(f"The total wholesale cost for {copies} copies is ${total_with_shipping:.2f}")