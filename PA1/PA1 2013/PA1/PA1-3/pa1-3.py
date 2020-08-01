import sys
a=1
while (a):
    try:
        number = int (raw_input("Enter an integer consists 4 digits:"))

    except ValueError:
        print "Inavlid Input. Enter a numerical value integer consists 4 digits."
        print sys.exc_info()[0]
        print sys.exc_info()[1],"\n"
        a=1

        
    else:
        if number<1000 or number>9999:
            print "Invalid Input. Enetr a integer between 1000 and 9999 which has 4 digits.\n"
            
        else:
            str_number = str(number)
            L = list(str_number)
            notation = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}
            ascii=''
            codes=[]

            try:
                for i in L:
                    ascii = ascii + notation[i]
                codes.append(ascii)
                
                x=L[0]+L[1]
                y=int(x)
                if y<=26:
                    ascii = notation[x] + notation[L[2]] + notation[L[3]]
                    codes.append(ascii)

                x=L[1]+L[2]
                y=int(x)
                if y<=26:
                    ascii = notation[L[0]] + notation[x] + notation[L[3]]
                    codes.append(ascii)
                
                x=L[2]+L[3]
                y=int(x)
                if y<=26:
                    ascii = notation[L[0]] + notation[L[1]] + notation[x] 
                    codes.append(ascii)

                print codes

                a=0

            except KeyError:
                print "Invalid Input. Enter a 4 digits integer doesn't consist 0."
                print sys.exc_info()[0],"\n"
                a=1
