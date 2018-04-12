#Malachi Blackburn, Chetan Gongidi
#4/11/18
total = 0

average = 0

count = 0

with open('tdsc01.txt','r') as user:
    
    with open('file.txt','w') as file:
        
        for line in user:
            
            item1 = line[7:10]
            
            item2 = line[10:13]
            
            itemID = item1+"-"+item2
            
            buyer = line[13:33]
            
            itemName = line[33:48]
            
            price = line[75:80]
            
            price = int(price)/100
            
            total += price
            
            price = str(price)
            
            count += 1
            
            print(itemID)
            
            print(buyer)

            print(itemName)
            
            print(price)
            
            row = itemID.ljust(10)+buyer.ljust(5)+itemName.ljust(5)+"$"+price.ljust(10)
            
            file.write(row)
            
            file.write("\n")
            
        average = total/count
        
        average = round(average,2)
        
        print("Total: ",total)
        
        print("Average: ",average)
        
        total = str(total)
        
        average =  str(average)
        
        file.write(total)

        file.write("\n")
        
        file.write(average)
        
        file.write("\n")
        
