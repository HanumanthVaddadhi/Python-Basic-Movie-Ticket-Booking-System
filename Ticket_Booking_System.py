print("_________________YOUR PERSONAL TICKET BOOKING SYSTEM__________________\n")
start_choice=input("Would you like to proceed with your booking ?(y/n)")
if start_choice=="n":
    print("Thank you..Please visit again 🙏")
elif start_choice=="y":
    print("Which INOX screen would you like to prefer : \n")
    screen_choice=print({"1":"INOX BANJARA HILLS","2":"INOX JUBILEE HILLS","3":"INOX PUNJAGUTTA","4":"INOX HITECH-CITY"})
    my_1=input("Enter the S.No of the screen that you have chosen : ")
    if my_1=="1":
        print(f"Welcome to {screen_choice["1"]}, Here are the seats available for your booking : ")
    
    