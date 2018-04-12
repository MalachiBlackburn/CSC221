#Malachi Blackburn

with open('names.txt','r') as names_file:
    for line in names_file:
        line = (line.rstrip('\n'))
        firstname = (line[0:1])
        firstname = firstname.strip()
        lastname = (line[10:17])
        lastname = lastname.strip()
        id_num = (line[23:28])
        id_num = id_num.strip()
        print ('Username:',lastname + firstname+ id_num)
        with open ('accounts.txt','w') as acct:
            line = (line.rstrip('\n'))
            firstname =(line[0:1])
            lastname = (line[10:17])
            id_num = (line[23:28])
            print('Email:'+lastname+firstname+id_num+'@faytechcc.edu')
