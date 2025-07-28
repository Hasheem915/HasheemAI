print("=== Simple Chat Program ===")

person1 = input("Enter name for Person1: ")

person2 = input("Enter name for Person2: ")

print("\nStart chatting! (Type 'exit' to quit)\n")

while True:
 

 text1 = input(f"{person1}: ")

 if text1.lower() == 'bye':

  print("Chat ended.")
  
  break

 else:
  print(f"{person1.upper()} says {text1.lower()}")

 

 text2 = input(f"{person2}: ")

 if text2.lower() == 'bye':

  print("Chat ended.")
  break
 
 else:
  print(f"{person2.upper()} says {text2.lower()}")
  