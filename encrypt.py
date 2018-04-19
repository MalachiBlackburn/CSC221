#Malachi Blackburn
#4/19/18

def main():
    menu()


    
CRYPT = {'a': '1','b': '2','c': '3','d': '4','e': '5','f': '6','g': '7',\
        'h': '8','i': '9','j': '!','k': '@','l': '#','m': '$','n': '%',\
        'o': '^','p': '&','q': '*','r': '(','s': ')','t': '-','u': '=',\
        'v': '_','w': '+','x': '<','y': '>','z': '?',' ':'`'}

DECRYPT = {'1': 'a','2': 'b','3': 'c','4': 'd','5': 'e','6': 'f','7': 'g',\
        '8': 'h','9': 'i','!': 'j','@': 'k','#': 'l','$': 'm','%': 'n',\
        '^': 'o','&': 'p','*': 'q','(': 'r',')': 's','-': 't','=': 'u',\
        '_': 'v','+': 'w','<': 'x','>': 'y','?': 'z','`':' '}


def menu():
    choice = input("Do you wish to encrypt or decrypt a file? Press E/D: ")
    if choice == 'E':
        encrypt()
    else:
        choice == 'D'
        decrypt()
                   

def encrypt():
    infile= open('encrypt.txt','r')
    result = ''
    text = infile.read()


    for ch in text:
        result = result + CRYPT[ch]

    outfile= open('outfile.txt', 'w')
    outfile.write(result)
    outfile.close()
    print("Successfully Ecrypted")
def decrypt():
    decodefile = open('outfile.txt', 'r')
    codetext = decodefile.read()
    decode = ''
    for ch in codetext:
        decode = decode + DECRYPT[ch]
    print("Successfully Decrypted")
    

    decode_outfile= open('decodedoutfile.txt', 'w')
    decode_outfile.write(decode)
    decode_outfile.close()

main();







    
    


    


    



    

