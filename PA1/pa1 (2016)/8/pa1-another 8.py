while True:
    
    x = list(raw_input("Enter words: "))
    real = ""

    alphabet={"A":"V","B":"I","C":"G","D":"Y","E":"C","F":"N","G":"Z","H":"B","I":"F","J":"P","K":"H","L":"U","M":"Q","N":"M","O":"K","P":"R","Q":"D","R":"J","S":"S","T":"A","U":"E","V":"T","W":"L","X":"O","Y":"X","Z":"W"}

    for i in x:
        if i.isalpha()==True:
            if i.islower()==True:
                a = alphabet[i.upper()].lower()
                real += a
        
            if i.isupper()==True:
                a=alphabet[i]
                real += a
        
        else:
            real += i

    print real ,"\n"








"""
Cxxq Wleo!
Good Luck! 

Vkbs bs fxv ktpq ts bv suuns.
This is not hard as it seems.

Fxz, vkbfcs tpu svtpvbfc vx ntou sufsu.
Now, things are starting to make sense.
"""
