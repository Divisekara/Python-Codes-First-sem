while True:

    try:
        T=map(int,raw_input("Time Seperated by colan: ").split(":"))

    except ValueError:
        print "Inavlid type of input. Enter numerical values only."
        continue

    else:
        h=T[0]
        m=T[1]
        
        if not 0<=h<=12 or 0<=m<=60:
            print "Inavalid time."
            continue
        
        h_ang=(h*60+m)*(360/60.0)/12
        m_ang=m*(360/60.0)
        
        ang=abs(m_ang-h_ang)
        
        if ang==360:
            ang=0.0

        print ang
        
    finally:
        print ""
