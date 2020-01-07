import math
import cmath

s = 0.01 #すべり
va = 200/math.sqrt(3) #v1
ra=0.86 #r1
rb = 1.20 #r2
X = 3.346 
Go=0.004
Bo=0.0229
f = 60 #周波数

for i in range(0,100):
    Ib = abs(va/(ra+(rb/s)+3.346j)) #二次電流
    Ii = abs(cmath.sqrt((((0.004-0.0229j)*va)**2)-(Ib**2))) #一次電流
    Pout = (3*(1-s)*rb*Ib**2)/s#機械出力
    w = (2*3.14*60)/2 #wm
    ws = (2*3.14*f)/2
    Pb = ((3*rb*(Ib**2))/s)
    T = Pb/ws #トルク
    #Ii = (((0.004-0.0229j)*va))+va/(ra+(rb/s)+3.346j)
    #pf = (Ii.real)/abs(cmath.sqrt((((0.004-0.0229j)*va)**2)-(Ib**2)))
    #n = Pout/(3*abs(va)*abs(cmath.sqrt((((0.004-0.0229j)*va)**2)-(Ib**2)))*pf)
    #print(str(round(s,2)))
    #print(s)
    #print(str(round(Ii,2)))
    #print(str(round(Pout*(10**-3),2)))
    #print(str(round(T,2)))
    
    

    


    


   
        
    



    

