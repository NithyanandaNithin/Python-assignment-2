def South_Indian():
 print("Thank you for selecting the South Indian Cuisine")
 print("Here is the menu list:\nDosa\nIdli\nPallav")
 menus=["Dosa","Idli","Pallav"]
 your_order=input("Please place you're order:")
 if your_order==menus[0]:
    Quantity=int(input("Enter the number of plates of Dosa  you want:")) 
    Price=60
    Total_Price=Quantity*Price
    GST_Rate=5
    GST_Amount=(Total_Price*GST_Rate)/100
    Food_Price=Total_Price-GST_Amount 
    print(f"The Price of {Quantity} plates of Dosa is:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    your_order=input("Do you want anything else:")
    if your_order==menus[1]:
      Quantity=int(input("Enter the number of plates of Idli you want:"))
      Price=50
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Idli is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}") 
    elif your_order==menus[2]:
      Quantity=int(input("Enter the number of plates of Pallav you want:"))
      Price=40
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Pallav is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}")
    elif your_order==menus[0]:
      Quantity=int(input("Enter the number of plates of Dosa  you want:")) 
      Price=60
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Dosa is:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    else:
      print(f"Sorry, {your_order} is not available")
 elif your_order==menus[1]:     
    Quantity=int(input("Enter the number of plates of Idli you want:"))
    Price=50
    Total_Price=Quantity*Price
    GST_Rate=5
    GST_Amount=(Total_Price*GST_Rate)/100
    Food_Price=Total_Price-GST_Amount 
    print(f"The Price of {Quantity} plates of Idli is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}")
    your_order=input("Do you want anything else:")
    if your_order==menus[1]:
      Quantity=int(input("Enter the number of plates of Idli you want:"))
      Price=50
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Idli is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}") 
    elif your_order==menus[2]:
      Quantity=int(input("Enter the number of plates of Pallav you want:"))
      Price=40
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Pallav is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}")
    elif your_order==menus[0]:
      Quantity=int(input("Enter the number of plates of Dosa  you want:")) 
      Price=60
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Dosa is:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    else:
      print(f"Sorry, {your_order} is not available")
 elif your_order==menus[2]:
    Quantity=int(input("Enter the number of plates of Pallav you want:"))
    Price=40
    Total_Price=Quantity*Price
    GST_Rate=5
    GST_Amount=(Total_Price*GST_Rate)/100
    Food_Price=Total_Price-GST_Amount 
    print(f"The Price of {Quantity} plates of Pallav is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}")
    your_order=input("Do you want anything else:")
    if your_order==menus[1]:
      Quantity=int(input("Enter the number of plates of Idli you want:"))
      Price=50
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Idli is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}") 
    elif your_order==menus[2]:
      Quantity=int(input("Enter the number of plates of Pallav you want:"))
      Price=40
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Pallav is:{Food_Price}\nThe GST amount is:{GST_Amount}\n The Total Amount is:{Total_Price}")
    elif your_order==menus[0]:
      Quantity=int(input("Enter the number of plates of Dosa  you want:")) 
      Price=60
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Dosa is:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    else:
      print(f"Sorry, {your_order} is not available")    

def Non_veg():
  print(f"Thank You for Selecting Non-Veg Food")
  print("Here is the menu list\nBiryani\nKabab")
  menus=["Biryani", "Kabab"]
  your_order=input("Please place you're order:")
  if your_order==menus[0]:
    Quantity=int(input("Enter the number of plates of Dosa  you want:")) 
    Price=120
    Total_Price=Quantity*Price
    GST_Rate=5
    GST_Amount=(Total_Price*GST_Rate)/100
    Food_Price=Total_Price-GST_Amount 
    print(f"The Price of {Quantity} plates of Biryani:{Food_Price}/nThe GST Amount is:{GST_Amount}/nThe Total Amount is:{Total_Price}")
    your_order=input("Do you want anything else:")
    if your_order==menus[0]:
      Quantity=int(input("Enter the number of plates of Biryani you want:")) 
      Price=120
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Biryani:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    elif your_order==menus[1]:
      Quantity=int(input("Enter the number of plates of Kabab you want:")) 
      Price=80
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Kabab:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    else:
      print(f"Sorry, {your_order} is not available")
  elif your_order==menus[1]:
    Quantity=int(input("Enter the number of plates of Kabab  you want:")) 
    Price=80
    Total_Price=Quantity*Price
    GST_Rate=5
    GST_Amount=(Total_Price*GST_Rate)/100
    Food_Price=Total_Price-GST_Amount 
    print(f"The Price of {Quantity} plates of Kabab:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    your_order=input("Do you want anything else:")
    if your_order==menus[0]:
      Quantity=int(input("Enter the number of plates of Biryani you want:")) 
      Price=120
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Biryani:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    elif your_order==menus[1]:
      Quantity=int(input("Enter the number of plates of Kabab you want:")) 
      Price=80
      Total_Price=Quantity*Price
      GST_Rate=5
      GST_Amount=(Total_Price*GST_Rate)/100
      Food_Price=Total_Price-GST_Amount 
      print(f"The Price of {Quantity} plates of Kabab:{Food_Price}\nThe GST amount is:{GST_Amount}\nThe Total Amount is:{Total_Price}")
    else:
      print(f"Sorry, {your_order} is not available")

def main():
  print("Welcome to RRR Resturant")
  print("1.South Indian")
  print("2.Non Vegetarian")
  choose_number=int(input("Enter Your Choice:"))
  if choose_number==1:
    South_Indian()
  elif choose_number==2:
    Non_veg()
  else:
    print("Invalid Choice")
main ()