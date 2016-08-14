print("Electricity bill estimator")

cents_per_kilowatt_hour = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = float(input("Enter number of billing days: "))

estimated_bill = cents_per_kilowatt_hour * daily_use * billing_days / 100

print("Estimated bill: $", estimated_bill)
