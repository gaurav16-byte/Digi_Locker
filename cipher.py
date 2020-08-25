dic={}

charl=list('abcdefghijklmnopqrstuvwxyz')     #ROT-13 algorithm
rotl=list('nopqrstuvwxyzabcdefghijklm')      #for alphabets
chars=dict(zip(charl,rotl))

charu=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rotu=list('NOPQRSTUVWXYZABCDEFGHIJKLM')
charsu=dict(zip(charu,rotu))

dig=list('1234567890')              #for digits
sym=list('!@#$%^&*()')
ds=dict(zip(dig,sym))

moresym=list('-_=+.,<>/ \ | ?')
samesym=list('-_=+.,<>/ \ | ?')
symbols=dict(zip(moresym,samesym))

ds_rev=dict(zip(sym,dig))       #for symbols

dic.update(chars)
dic.update(ds)
dic.update(ds_rev)      #dic now contains all the elements
dic.update(charsu)
dic.update(symbols)

def encrypt(data):      #encrypt data
    encrypted=''
    for i in data:
        encrypted+=dic[i]
    return encrypted      

def decrypt(data):      #decrypt data
    decrypted=''
    for i in data:
        decrypted+=dic[i]
    return decrypted
