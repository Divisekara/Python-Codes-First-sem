while True:
    try:
        n=int(raw_input("Enter integer: "))

    except ValueError:
        print "Invalid Input."
        continue

    else:
        if not 1<=n<1000:
            print "Enter number between 1 and 1000."
            continue
        while str(n)!=str(n)[::-1]:
            n=n+int(str(n)[::-1])
        print n

    finally:
        print ""



