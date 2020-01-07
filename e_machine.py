import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import openpyxl

va = 200/math.sqrt(3)

t = np.linspace(0, 10, 1000)
s = np.arange(0,1,0.01)
t = np.linspace(0, 1.0,0.01)
Ib = abs(va/(ra+(rb/s)+3.346j)) #二次電流
Ii = abs((((0.004-0.0229j)*va))-(Ib)) #一次電流
Pout = ((3*(1-s)*rb*Ib**2)/s)*10**-3#機械出力
w = (2*3.14*60)/2 #wm
ws = (2*3.14*f)/2
Pb = ((3*rb*(Ib**2))/s)
T = Pb/ws #トルク


#第一軸(ax1)と第二軸(ax2)を作って関連付ける
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
 
#第一軸を折れ線グラフ、第二軸を棒グラフに
ax1.plot(s,Pout, linewidth=2, color="red", linestyle="solid",  label='機械出力')
ax2.plot(s, Ii, label='一次電流')
ax2.plot(s, T, label='トルク')

plt.grid() # 罫線
ax1.legend(loc='uppper right',
           bbox_to_anchor=(1.0, 0.5, 0.5, .2), 
           borderaxespad=0.,)

ax2.legend(loc='uppper right',
           bbox_to_anchor=(1.0, 0.5, 0.5,.100), 
           borderaxespad=0.,)



#軸ラベルを表示
ax1.set_xlabel('すべりs→')
ax2.set_ylabel('機械出力Pout → [kW]')
ax1.set_ylabel('一次電流I1 , トルクT → [N・m] [A] ')
#plt.savefig(r"C:\Users\奈良岡伶\Desktop\electric_machine\electric_machine.png") # 画像の保存

#グラフ表示
plt.show()