def is_leap(x):
    if x%4!=0:return False
    elif x%100!=0:return True
    elif x%400==0:return False
    else:return True

while True:
    try:
        L=map(int,raw_input("Enter year and starting day: ").split())
        start=L[0]
        day=L[1]
        end=int(raw_input("Enter finishing year: "))
    except ValueError:
        print "Invalid input format."
        continue
    except IndexError:
        print "Enter inputs correctly."
        continue
    else:
        if start>end or not 0<=day<=6 or len(L)!=2:
            print "Invalid Input"
            continue
        answer=0

        for i in range(start,end+1):
            if is_leap(i)==True:
                month=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                month=[31,28,31,30,31,30,31,31,30,31,30,31]

            for j in month:
                for k in range(1,j+1):
                    if day==5 and k==13:
                        answer += 1

                    if day==6:
                        day=0
                    else:
                        day +=1
        print answer
    finally:
        print ""
