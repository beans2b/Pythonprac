shop=[]

while True:
    print("===Shopping List===")
    print("1.Add item")
    print("2.Remove item")
    print("3.Display items")
    print("4. Exit")
    
    option = int(input("select your option"))
    
    if option == 1:
        itemname= input("item name: ")
        shop.append(itemname)
        print("item added")
        
    elif option ==2:
        print(shop)
        itemrem= input("item choice")
        shop.remove(itemrem)
        print("item removed")
        
    elif option ==3:
        for i, item in enumerate(shop,start=1):
            print(i, item)
            
    else:
        break
    