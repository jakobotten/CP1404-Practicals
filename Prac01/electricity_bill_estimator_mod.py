TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")

selected_tariff = int(input("Which tariff? 11 or 31: "))
if selected_tariff == 11:
    cents_per_kilowatt_hour = TARIFF_11
elif selected_tariff == 31:
    cents_per_kilowatt_hour = TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
billing_days = float(input("Enter number of billing days: "))

estimated_bill = cents_per_kilowatt_hour * daily_use * billing_days

print("Estimated bill: ${:.2f}".format(estimated_bill))

