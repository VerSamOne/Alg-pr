import math
 R = int(input(":"))
 r = int(input(":"))
 h = int(input(":"))
 l = math.sqrt(math.pow(h,2)+(math.pow((R-r),2))
 V = (1/3)*math.pi(math.pow(R,2)+math.pow(r,2)+R*r)
 S = math.pi*(R+r)*l+math.pi*math.pow(R,2)+math.pi*math.pow(r,2)
 print(V,S)
