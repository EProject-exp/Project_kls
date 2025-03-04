#name = "kot"
#age = 69
#height = 6.3
#student = True
#print(f"My name is {name}, i am {age} years old, and i am {height} tall.")
#print(f"Am i a student? {student} ")

#---------------------------------------------------------------------------------------------------------------------------------------#

#a = int(input("Enter number: "))
#b = int(input("Enter number 2: "))

#mb = a + b
#print(f"Mbledhja {mb}")
#sh = a * b
#print(f"Shumezimi {sh}")
#nd = a - b
#nd1 = b - a
#if a > b:
#   print(f"Ndryshesa {nd}")
#elif b > a:
#    print(f"Ndryshesa {nd1}")
#else:
#    print(f"Numrat jane te barabarte ndryshesa 0")        


#if a != 0 and b != 0:
#    pj = a / b
#    print(f"Pjestimi i {a} dhe {b} eshte {pj}")
#else:
#    print(f"Pjestimi nuk behet {a} dhe {b}")   


#---------------------------------------------------------------------------------------------------------------------------------------#

#for i in range(1, 6):
#    print(f"Number: {i}")

#---------------------------------------------------------------------------------------------------------------------------------------#

#count = 1
#while count <= 5:
#    print(f"Count is: {count}")
#    count += 1

#---------------------------------------------------------------------------------------------------------------------------------------#

#b = int(input("Enter number: "))
#for a in range(1, b):
#    if a % 2 == 0:
#        print(f"Numrat cift:{a}")

#---------------------------------------------------------------------------------------------------------------------------------------#
#b = int(input("Enter number: "))
#rezultati = []
#for a in range(1, b):
#    if a % 2 == 0:
#        rezultati.append(a)
#print(f"Numrat cift jane: {rezultati}.")


while True:
    operatoret = "Mbledhja +, Zbritja -, Shumezimi *, Pjestimi /.: +,-.*,% "
    print(operatoret)
    op = input("Enter the operator you want to use (or type 'exit' to quit): ")
    if op == "exit":
        print("Faleminderit qe perdoret aplikacionin tone mirupafshim!")
        break
    if op not in ['+', '-', '*', '/']:
        print(f"Vlera e dhene esht invalid ju lutemi te vendosni nje nga operatoret me lart - {operatoret}")
        continue 
    try:  
        a = int(input("Enter Number: "))
        b = int(input("Enter Number: "))
    except ValueError:
        print("Vendos vetem numra")
    if op == "+":
        print(a + b)

    elif op == "/":
        print(a / b)

    elif op == "*":
        print(a * b)

    elif op == "-":
        print(a - b)

    else:
        print(f"Vendos nje nga operatoret me siper - {operatoret} ")