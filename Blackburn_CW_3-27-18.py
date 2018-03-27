def main():
##    my_string= "One two three four"
##    #print(my_string)
##
##    word_list = my_string.split()
##
##    print(word_list)

##    date_string = "03/27/2018"
##
##    date_list = date_string.split('/')

##    print(date_list)


##    print("Month:", date_list[0])
##    print("Day:", date_list[1])
##    print("Year:", date_list[2])


    with open('names.txt') as infile:
        for line in infile:
            line = line.rstrip('\n')
            line = line.strip(' ')
            #print(line)
            fName = line[0:10]
            lName = line[10:20]
            idNum = line[20: ]
            print(fName)
            print(lName)
            print(idNum)
    


    with open('accounts.txt', 'w')as outfile:
        outfile.write(fName)
        
            
    
        

    
    



    







main()
