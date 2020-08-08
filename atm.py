pin2 = 8888;#The arguments we need
pin = 9999;#The arguments we need
option1 = "3450 $" ;#The arguments we need
print("*************************************************");
print();
print("         Welcome to PyATM !");#Let's print advertising !
print();
print();
print("*************************************************");

pin = int(input("Please enter PIN number:"))#set the inputs for the user to be able to write the password
if pin ==9999:#Here we set the conditions if and else
   print("Welcome to PyATM ! Please chose a option:");
   print("1-See balance sheet");
   print("2-Change PIN");
   print("3-Withdraw money");
   print("4-Exit");
   option = int(input("Chose an option:"));
   
else:
   print("Wrong PIN. Please try again !");
if option==1:
   print("Your balance is :" ,option1);
if option==2:
   old_pin = int(input("Enter old PIN:" ));
if old_pin==9999:
   new_pin = int(input("Enter new PIN:"));
else:
    print("Wrong PIN!");
if new_pin:
   print("PIN changed from 9999 in ", new_pin);

if option3==3:
   option3 = int(input("Please enter PIN2:"));
if pin2==8888:
     amount = int(input("Enter the amount of money you want to withdraw:")); #Not really :< Hahahah
if amount:
    print("You withdraw:" + amount +"Dollar");
#This is the end is very simple program i hope you learned something :)


