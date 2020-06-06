products = {"TV":1500, "Microwave":2000, "washingmachine"  : 5000, "Refrigeratot":4500,"recliner":3500}
newprd=input("Please enter a product you want to buy")
if (newprd in products):
    print("Your Product price is")
    print(products.get(newprd))

else:
    print("Product not found")

# odd numbers
#print(x for x in range(1, 100) if x % 2 == 0)