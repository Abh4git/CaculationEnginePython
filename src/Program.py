from NPVCalculation import NPVCalculation

print("Hello Calculation World")
print("-----------------------")
# Instantiating the NPVCalculation class with
# values for initialInvestment, Discount Rate, CashInFlow
# and Number of Years. Then the Execute method call
# initiates execution and result is found in ,result.
npvcalc = NPVCalculation(10000,.1,3000,5)
npvcalc.Execute()
print ("Printing calculation value ", npvcalc.result)
