fruits= {"Mango": ["Round in shape", "king of fruits","National fruit of India"], "Banana": ["Pipe", "High source of calcium","Instatnt soure of energy"]}
print("Mango" in fruits)
print(fruits["Banana"])
print(fruits.get("Mango"))
print(fruits.get("mangao", "fruit not found"))