encryption_library = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'}

orig_file = open('text1.txt','r')
file_read = orig_file.read()    
orig_file.close()
encrypt_file = open('ENCRYPTED_Plain_Text_File.txt','w')

for ch in file_read:
    if ch in encryption_library:
        encrypt_file.write(encryption_library[ch])
    else:
        encrypt_file.write(ch)

encrypt_file.close()
encrypt_file = open('text1.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()
codes_items = encryption_library.items()

for ch in file_read:
    if not ch in encryption_library.values() or ch == '.' or ch == ',' or ch == '!':
        print(ch)
    else:
        for k,v in codes_items:
            if ch == v and ch != '.':
                print(k,end='')

decryption_library = {')':'A','0':'a','(':'B','9':'b','*':'C','8':'c',\
        '&':'D','7':'d','^':'E','6':'e','%':'F','5':'f',\
        '$':'G','4':'g','#':'H','3':'h','@':'I','2':'i',\
        '!':'J','1':'j','Z':'K','z':'k','Y':'L','y':'l',\
        'X':'M','x':'m','W':'N','w':'n','V':'O','v':'o',\
        'U':'P','u':'p','T':'Q','t':'q','S':'R','s':'r',\
        'R':'S','r':'s','Q':'T','q':'t','P':'U','p':'u',\
        'O':'V','o':'v','N':'W','n':'w','M':'X','m':'x',\
        'L':'Y','l':'y','K':'Z','k':'z','J':'!','j':'1',\
        'I':'@','i':'2','H':'#','h':'3','G':'$','g':'4',\
        'F':'%','f':'5','E':'^','e':'6','D':'&','d':'7',\
        'C':'*','c':'8','B':'(','b':'9','A':')','a':'0',\
        ',':':',':':',','.':'?','?':'.','>':'<','<':'>',\
        '"':"'","'":'"','-':'+','+':'-',';':'=','=':';',\
        '[':'{','{':'[',']':'}','}':']'}

orig_file = open('ENCRYPTED_Plain_Text_File.txt','r')
file_read = orig_file.read()
orig_file.close()
encrypt_file = open('DECRYPTED_Plain_Text_File.txt','w')

for ch in file_read:
    if ch in decryption_library:
        encrypt_file.write(decryption_library[ch])
    else:
        encrypt_file.write(ch)

encrypt_file.close()
encrypt_file = open('ENCRYPTED_Plain_Text_File.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()    
codes_items = decryption_library.items()

for ch in file_read:
    if not ch in decryption_library.values() or ch == '.' or ch == ',' or ch == '!':
        print(ch)
    else:
        for k,v in codes_items:
            if ch == v and ch != '.':
                print(k,end='')
