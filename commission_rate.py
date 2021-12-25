keep_going = "y"

while keep_going == "y":
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commision rate: "))

    comission = sales * comm_rate


    print("The comission rate is $",
          format(comission, " ,.2f"), sep = " ")

    keep_going = input("Do you want to calculate another " +
                       "commission (Enter y for yes): ")
