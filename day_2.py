mealCost=float(input())
tipPercent=float(input())
taxPercent=float(input())

tip=mealCost*(tipPercent/100)
tax=mealCost*(taxPercent/100)

totalCost=round(mealCost+tip+tax)
print(totalCost)
