'''
#Write to file
items = ["milk", "bread", "eggs"]
with open("shopping.txt", "w") as f:
 for item in items:
  f.write(item + "\n")
 # Read and print with numbers
with open("shopping.txt", "r") as f:
 for i,line in enumerate(f, 1):
  print(f"{i}.{line.strip()}")
'''


#Get items from user until they type 'done'
items = []
print("Enter items for your shopping list. Type 'done' to finish.")
while True:
 item = input("item:")
 if item.lower() == "done":
  break
items.append(item)
#Write items to file
with open("shopping.txt", "w") as g:
 for item in items:
  g.write(item + "\n")
#Read and print with numbers
print("\nYour shopping list:")
with open("shopping.txt", "r") as g:
  for i,line in enumerate(g,1):
   print(f"{i}.{line.strip()}")
