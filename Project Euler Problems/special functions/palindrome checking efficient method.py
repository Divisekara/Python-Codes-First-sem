print max([(i*y,i,y) for i in range(100,1000) for y in range(100,1000) if str(i*y)==str(i*y)[::-1]])
