import random

rounds = 1
vic_user = 0
vic_pc = 0
while True:

  user = input("Piedra, papel o tijeras?: ").lower()
  pc_0 = ("piedra", "papel", "tijeras")
  pc = random.choice(pc_0)

  print("*"*10)
  print(f"Rounds : {rounds}")
  print("*"*10)

  if user == pc:
    print(f"ambos elegieron {user}, es un empate")
  elif user == "piedra":
    if pc == "papel":
      print(f"has elegido {user}, tú contrincante ha elegido {pc}, haz perdido :c")
      vic_pc +=1
    elif pc == "tijeras":
      print(f"has elegido {user}, tú contrincante ha elegido {pc}, haz ganado :D")
      vic_user +=1
  elif user == "papel":
    if pc == "tijeras":
      print(f"has elegido {user}, tú contrincante ha elegido {pc}, haz perdido :c")
      vic_pc +=1
    elif pc == "piedra":
      print(f"has elegido {user}, tú contrincante ha elegido {pc}, haz ganado :D")
      vic_user +=1
  elif user == "tijeras" or "tijera":
    if pc == "piedra":
      print(f"has elegido {user}, tú contrincante ha elegido {pc}, haz perdido :c")
      vic_pc +=1
    elif pc == "papel":
      print(f"has elegido {user}, tú contrincante ha elegido {pc}, haz ganado :D")
      vic_user +=1
  else:
    print(f"{user}?, no sé, no programaron para eso")
    break
  print(f"User: {vic_user}")
  print(f"Pc: {vic_pc}")
  if vic_user == 3:
    print(f"Felicidades!, haz ganado")
    break
  if vic_pc == 3:
    print(f"Ganó terminator, lo siento :C")
    break
  rounds +=1