n = int(input("Input the module, choose one: \n 1)BIS \n 2)FoE \n"))

if n == 1:
    print("You have chosen BIS Module \n The assiment caonsist of 2 marks\n First one for CW \n Second one for examenation")
    a1 = int(input("Enter the mark of the CW"))
    a2 = int(input("Enter the mark of the examination\n"))
    print("Your overall mark is " + str(a1 * 0.4 + a2 * 0.6))
if n == 2:
    print("You have chosen FoE Module \n The assiment caonsist of 2 marks\n First one for CW \n Second one for examenation")
    b1 = int(input("Enter the mark of the CW"))
    b2 = int(input("Enter the mark of the examination\n"))
    print("Your overall mark is " + str(b1 * 0.4 + b2 * 0.6))