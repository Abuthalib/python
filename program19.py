
income=float(input('enter the annual income : '))
if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income * 5) /100

elif income <= 1000000:
    tax = (income * 20) /100

elif income <= 5000000: #12 lakh 50 thousand
    tax = (income * 30 ) /100


print("income tax amount =", tax, "Rupees in tax!")