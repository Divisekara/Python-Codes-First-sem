#PA2 - 19 - Weight of an object on a Planet

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        data=fileOpen.read().split()
        fileOpen.close()
        M=int(data.pop(0))
        N=int(data.pop(0))
    except ValueError:
        print "Invalid Input!"
    except IOError:
        print "File Error!"
    else:
        names=[]
        radii=[]
        avg_dens=[]
        if len(data)%3==0:
            for i in range(len(data)/3):
                names.append(data.pop(0))
                try:
                    radii.append(int(data.pop(0)))
                    avg_dens.append(int(data.pop(0)))
                except ValueError:
                    print "Invalid Input!"
        new_data = []
        if N==len(names) and N==len(radii) and N==len(avg_dens):
            new_data.append(names)
            new_data.append(radii)
            new_data.append(avg_dens)
            new_data.append(M)
            new_data.append(N)
            return new_data

def Calculate_Weight(x):
    #To calculate the weight of an object on the given planets
    N = x.pop(-1)
    M = x.pop(-1)
    names = x.pop(0)
    radii = x.pop(0)
    avg_dens = x.pop(0)
    weight=[]
    for i in range(N):
        W=(6.67*(10**(-11)))*((4/3*3.14*(radii[i])**3)*avg_dens[i])*M/(radii[i])**2
        weight.append(round(W,4))
    return names[weight.index((max(weight)))]
        

def show(output):
    #To print the output on screen as well as write to a file.
    print output
    try:
        fileWrite=open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()   #To call functions in a global level                                                                                  
if run!=None:
    show(Calculate_Weight(run))                                                                                   


