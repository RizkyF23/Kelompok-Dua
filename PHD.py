print("Selamat Datang Pizza kelompok dua!")

hargaPizza = 0

# memilih menu
print("Silahkan pilih menu: ")
print("Frankfurter BBQ")
print("Meat Monsta")
print("Super Supreme")
print("Super Supreme Chicken")
print("Meat Lovers")
print("Chicken Lovers")
print("Cheese Lovers")
print("American Favorite")
MenuPizza = input("Silahkan pilih menu pizza : ")
MenuPizza = MenuPizza.lower()
if MenuPizza in ["frankfurter bbq", "meat monsta", "super supreme", "super supreme chicken", "meat lovers", "Chicken Lovers", "Cheese Lovers","America Fvourite"]:
    hargaPizza = 43636
else:
    hargaPizza = 0
    print("Maaf, Menu pizza yang anda pilih tidak tersedia")

# memilih crust pizza
print("Pilihan Crust: ")
print("Pan")
print("StuffedCrust Cheese")
print("StuffedCrust Sausage")
print("Chessy Bites")
CrustPizza = input("Silahkan pilih crust pizza : ")
CrustPizza = CrustPizza.lower()
if CrustPizza == "original":
    hargaPizza += 0
elif CrustPizza == "stuffedcrust cheese":
    hargaPizza += 11819
elif CrustPizza == "stuffedcrust sausage":
    hargaPizza += 9091
elif CrustPizza == "chessy bites":
    hargaPizza += 13637
else:
    hargaPizza += 0
    print("Maaf, Crust yang anda pilih tidak tersedia")
    
# memilih ukuran pizza
print("Ukuran Pizza yang anda inginkan:")
print("Personal")
print("Regular")
print("Large")
UkuranPizza = input("Pilih ukuran pizza anda : ")
UkuranPizza = UkuranPizza.lower()
if UkuranPizza == "personal":
    hargaPizza += 0
elif UkuranPizza == "regular":
    hargaPizza += 57273
elif UkuranPizza == "large":
    hargaPizza += 89091
else:
    hargaPizza += 0
    print("Maaf, pilihan anda tidak tersedia")

#Apakah ingin menambah keju?
cheese = input("Ingin menambahkan keju? (y/n): ")
if cheese == "y":
    hargaPizza += 13000
elif cheese == "n":
    hargaPizza += 0
else:
    hargaPizza += 0
    print("Maaf, pilihan anda tidak tersedia")

totalharga = hargaPizza
TotalhargaPizza = totalharga

print("Harga Pizza: Rp", hargaPizza)
print("Total harga pizza: Rp", TotalhargaPizza)



