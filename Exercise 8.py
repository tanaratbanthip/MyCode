print("-My-Cofe-Shop-")
Username = input("Username : ")
Password = input("Password : ")
if Username == "admin" and Password == "1234":
    print("-Welcome to MyCofeShop-")
    print("-รายการเครื่องดื่ม-")
    print("1.เอสเปรสโซ่" ,"ราคา 50  บาท")
    print("2.แบล็คคอฟฟี่","  ราคา 50  บาท")
    print("3.คาปูชิโน","  ราคา 50  บาท")
    print("4.ลาเต้","  ราคา 45  บาท")
    print("5.ชาเขียว","  ราคา  45  บาท")
    print("6.ชาไทย","  ราคา  35  บาท")
    print("7.ชามะนาว","  ราคา  35  บาท")
    print("----------------------------------")
    print("-----เลือกซื้อเครื่องดื่ม-----")
    manu = int(input("เลือกหมายเลขเครื่องดื่ม :"))
    unit = int(input("จำนวนที่ต้องการซื้อ :"))
    if manu == 1 :
        print("รายการ  เอสเปรสโซ่ : ","จำนวน",unit,"  แก้ว  ","ราคา ",50*unit,"  บาท ")
    elif manu == 2 :  
        print("รายการ  แบล็คคอฟฟี่ : ","จำนวน",unit,"  แก้ว  ","ราคา ",50*unit,"  บาท ")
    elif manu == 3 :  
        print("รายการ  คาปูชิโน่ : ","จำนวน",unit,"  แก้ว  ", "ราคา ",50*unit,"  บาท ")
    elif manu == 4 :  
        print("รายการ  ลาเต้ : ","จำนวน",unit,"  แก้ว  ", "ราคา ",45*unit,"  บาท ")
    elif manu == 5 :  
        print("รายการ  ชาเขียว : ","จำนวน",unit,"  แก้ว  ", "ราคา ",45*unit,"  บาท ")
    elif manu == 6 :  
        print("รายการ  ชาไทย : ","จำนวน",unit,"  แก้ว  ", "ราคา ",35*unit,"  บาท ")
    elif manu == 7 :  
        print("รายการ  ชามะนาว : ","จำนวน",unit,"  แก้ว  ", "ราคา ",35*unit,"  บาท ")
else :
    print("โปรดลองใหม่อีกครั้ง")
