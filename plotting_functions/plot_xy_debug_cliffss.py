# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:04:58 2013

@author: mhurst
"""

#import modules
import numpy as np
import matplotlib.pyplot as plt

XB = [650582.43999999994, 650607.93999999994, 650650.27000000002, 650692.68000000005, 650728.46999999997, 650749.35999999999, 650769.70999999996, 650793.02000000002, 
  650817.56000000006, 650840.09999999998, 650862.76000000001, 650893.96999999997, 650927.26000000001, 650960.68000000005, 650993.63, 651020.25, 651045.93000000005, 651072.22999999998, 651100.25, 
  651130.72999999998, 651164.07999999996, 651193.68000000005, 651220.40000000002, 651245.84999999998, 651257.20999999996, 651265.56999999995, 651271.79000000004, 651274.01000000001, 651276.89000000001, 
  651280.95999999996, 651294.82999999996, 651310.56000000006, 651327.81999999995, 651347.01000000001, 651366.26000000001, 651385.52000000002, 651405.31000000006, 651425.19999999995, 651445.09999999998, 
  651466.48999999999, 651491.14000000001, 651516.03000000003, 651542.45999999996, 651571.57999999996, 651600.81000000006, 651631.48999999999, 651664.43999999994, 651697.52000000002, 651731.45999999996, 
  651769.42000000004, 651807.78000000003, 651845.95999999996, 651884.15000000002, 651921.19999999995, 651954.32999999996, 651987.16000000003, 652020.17000000004, 652053.73999999999, 652087.38, 
  652123.43999999994, 652162.88, 652202.25, 652239.79000000004, 652276.26000000001, 652312.71999999997, 652347.97999999998, 652381.5, 652414.94999999995, 652448.40000000002, 652481.85999999999, 
  652516.51000000001, 652552.55000000005, 652588.67000000004, 652624.81999999995, 652661.30000000005, 652697.89000000001, 652734.48999999999, 652771.08999999997, 652808.79000000004, 652846.70999999996, 
  652884.63, 652922.55000000005, 652960.22999999998, 652996.78000000003, 653033.12, 653069.26000000001, 653104.93000000005, 653140.5, 653174.72999999998, 653208.40000000002, 653242.95999999996, 
  653278.41000000003, 653313.89000000001, 653350.58999999997, 653391.91000000003, 653433.62, 653475.33999999997, 653516.54000000004, 653550.33999999997, 653581.79000000004, 653611.91000000003, 
  653641.65000000002, 653668.40000000002, 653693.35999999999, 653710.08999999997, 653722.90000000002, 653735.93000000005, 653749.01000000001, 653761.79000000004, 653773.83999999997, 653785.89000000001, 
  653797.68999999994, 653807.31000000006, 653816.39000000001, 653823.17000000004, 653828.18000000005, 653833.37, 653839.81999999995, 653846.47999999998, 653851.83999999997, 653856.29000000004, 
  653860.71999999997, 653863.33999999997, 653864.76000000001, 653866.18000000005, 653867.59999999998, 653868.42000000004, 653869.21999999997, 653869.97999999998, 653868.12, 653860.75, 653844.65000000002, 
  653802.64000000001, 653756.66000000003, 653712.03000000003, 653674.79000000004, 653646.73999999999, 653630.67000000004, 653622.30000000005, 653619.68999999994, 653621.44999999995, 653624.51000000001, 
  653627.58999999997, 653632.71999999997, 653640.96999999997, 653649.40000000002, 653661.01000000001, 653675.48999999999, 653690.01000000001, 653704.54000000004, 653719.06000000006, 653733.58999999997, 
  653748.10999999999, 653762.64000000001, 653777.16000000003, 653795.27000000002, 653815.81999999995, 653836.35999999999, 653857.26000000001, 653881.55000000005, 653906.80000000005, 653932.05000000005, 
  653959.48999999999, 653993.10999999999, 654027.13, 654063.62, 654105.98999999999, 654148.64000000001, 654189.30000000005, 654225.5, 654260.93000000005, 654291.34999999998, 654320.64000000001, 
  654349.93000000005, 654379.22999999998, 654410.45999999996, 654444.26000000001, 654478.14000000001, 654512.03000000003, 654545.91000000003, 654579.84999999998, 654616.65000000002, 654656.64000000001, 
  654696.63, 654736.67000000004, 654782.64000000001, 654839.56999999995, 654921.81000000006]
  
 
YB = [274739.53000000003, 274794.19, 274884.79999999999, 274975.34999999998, 275068.52000000002, 275166.31, 275264.21999999997, 275361.45000000001, 275458.40000000002, 
  275555.82000000001, 275653.21000000002, 275748.17999999999, 275842.47999999998, 275936.72999999998, 276031.14000000001, 276127.52000000002, 276224.16999999998, 276320.65000000002, 276416.64000000001, 
  276511.88, 276606.15000000002, 276701.64000000001, 276798, 276894.69, 276993.98999999999, 277093.64000000001, 277193.42999999999, 277293.40999999997, 277393.37, 277493.27000000002, 277592.28000000003, 
  277691.03999999998, 277789.53000000003, 277887.66999999998, 277985.79999999999, 278083.92999999999, 278181.95000000001, 278279.95000000001, 278377.96000000002, 278475.63, 278572.53999999998, 
  278669.40000000002, 278765.83000000002, 278861.5, 278957.13, 279052.29999999999, 279146.71999999997, 279241.09000000003, 279335.14000000001, 279427.65000000002, 279520, 279612.42999999999, 279704.84999999998, 
  279797.72999999998, 279892.08000000002, 279986.53999999998, 280080.92999999999, 280175.12, 280269.29999999999, 280362.54999999999, 280454.45000000001, 280546.37, 280639.04999999999, 280732.15999999997, 
  280825.28000000003, 280918.84999999998, 281013.07000000001, 281107.31, 281201.53999999998, 281295.78000000003, 281389.58000000002, 281482.85999999999, 281576.10999999999, 281669.34999999998, 
  281762.46000000002, 281855.52000000002, 281948.58000000002, 282041.64000000001, 282134.26000000001, 282226.79999999999, 282319.33000000002, 282411.85999999999, 282504.48999999999, 282597.57000000001, 
  282690.72999999998, 282783.96999999997, 282877.40000000002, 282970.84999999998, 283064.81, 283158.96999999997, 283252.81, 283346.31, 283439.81, 283532.82000000001, 283623.89000000001, 283714.77000000002, 
  283805.65000000002, 283896.76000000001, 283990.84999999998, 284085.77000000002, 284181.13, 284276.59999999998, 284372.95000000001, 284469.78000000003, 284568.31, 284667.48999999999, 284766.63, 
  284865.78000000003, 284964.95000000001, 285064.22999999998, 285163.5, 285262.79999999999, 285362.33000000002, 285461.91999999998, 285561.67999999999, 285661.56, 285761.41999999998, 285861.21000000002, 
  285960.98999999999, 286060.84999999998, 286160.75, 286260.65000000002, 286360.60999999999, 286460.59999999998, 286560.59000000003, 286660.58000000002, 286760.58000000002, 286860.57000000001, 
  286960.57000000001, 287060.53000000003, 287160.23999999999, 287258.87, 287349.31, 287438.09999999998, 287527.59000000003, 287620.33000000002, 287716.19, 287814.88, 287914.46000000002, 288014.41999999998, 
  288114.40000000002, 288214.34999999998, 288314.29999999999, 288414.15999999997, 288513.82000000001, 288613.46000000002, 288712.77000000002, 288811.71000000002, 288910.65000000002, 289009.59000000003, 
  289108.53000000003, 289207.46999999997, 289306.40999999997, 289405.34999999998, 289504.28999999998, 289602.62, 289700.47999999998, 289798.34999999998, 289896.14000000001, 289993.14000000001, 
  290089.90000000002, 290186.65999999997, 290282.78999999998, 290376.96999999997, 290471.01000000001, 290564.08000000002, 290654.65999999997, 290745.09999999998, 290836.45000000001, 290929.65999999997, 
  291023.16999999998, 291118.42999999999, 291214.03999999998, 291309.65000000002, 291405.26000000001, 291500.25, 291594.37, 291688.45000000001, 291782.53999999998, 291876.62, 291970.67999999999, 
  292063.64000000001, 292155.29999999999, 292246.95000000001, 292338.59000000003, 292427.28000000003, 292509.27000000002, 292565.81]

XC = [650621.28000000003, 650541.94999999995, 650493.18999999994, 650517.33999999997, 650565.91000000003, 650601.71999999997, 650629.81000000006, 650660.01000000001, 
  650693.93000000005, 650727.84999999998, 650761.77000000002, 650796.77000000002, 650835.45999999996, 650874.15000000002, 650912.83999999997, 650950.35999999999, 650979.66000000003, 651008.95999999996, 
  651038.26000000001, 651069.27000000002, 651101.04000000004, 651132.81000000006, 651164.57999999996, 651196.34999999998, 651225.67000000004, 651248.67000000004, 651257.55000000005, 651260.81000000006, 
  651256.93000000005, 651253.05000000005, 651256.73999999999, 651269.03000000003, 651281.32999999996, 651296.68999999994, 651315.73999999999, 651334.79000000004, 651353.83999999997, 651372.88, 
  651392.04000000004, 651413.93999999994, 651435.84999999998, 651457.75, 651479.65000000002, 651501.56000000006, 651529.78000000003, 651560.43000000005, 651591.06999999995, 651621.71999999997, 
  651652.35999999999, 651683.25, 651723.87, 651764.47999999998, 651805.09999999998, 651844.18000000005, 651882.39000000001, 651920.59999999998, 651955, 651987.43000000005, 652019.85999999999, 
  652052.29000000004, 652084.72999999998, 652126.18000000005, 652170.41000000003, 652208.66000000003, 652243.09999999998, 652277.54000000004, 652311.97999999998, 652346.42000000004, 652380.14000000001, 
  652413.73999999999, 652447.32999999996, 652480.92000000004, 652516.12, 652551.66000000003, 652587.18999999994, 652622.71999999997, 652658.25, 652697.39000000001, 652736.56000000006, 652775.70999999996, 
  652814.59999999998, 652853.47999999998, 652892.37, 652931.26000000001, 652970.15000000002, 653007.33999999997, 653041.67000000004, 653076, 653110.32999999996, 653144.65000000002, 653178.97999999998, 
  653214.52000000002, 653250.32999999996, 653286.13, 653322.07999999996, 653360.58999999997, 653399.09999999998, 653437.62, 653471.25, 653497.92000000004, 653524.58999999997, 653551.26000000001, 
  653576.98999999999, 653583.56000000006, 653590.13, 653596.70999999996, 653603.28000000003, 653609.06999999995, 653614.39000000001, 653619.70999999996, 653625.03000000003, 653629.43000000005, 
  653628.30000000005, 653627.16000000003, 653626.03000000003, 653624.89000000001, 653623.69999999995, 653622.44999999995, 653621.19999999995, 653619.94999999995, 653617.79000000004, 653612.92000000004, 
  653608.05000000005, 653603.17000000004, 653598.30000000005, 653601.05000000005, 653604.58999999997, 653608.13, 653586.58999999997, 653567.52000000002, 653562.69999999995, 653557.88, 653553.06000000006, 
  653550.53000000003, 653551.28000000003, 653552.03000000003, 653552.78000000003, 653556.81999999995, 653561.23999999999, 653565.67000000004, 653570.08999999997, 653577.01000000001, 653584.95999999996, 
  653592.91000000003, 653600.87, 653611.31000000006, 653625.79000000004, 653640.27000000002, 653654.73999999999, 653669.17000000004, 653683.59999999998, 653696.54000000004, 653708.13, 653721.06999999995, 
  653734.10999999999, 653747.16000000003, 653757.92000000004, 653768.39000000001, 653778.85999999999, 653791.10999999999, 653803.67000000004, 653824.04000000004, 653847.08999999997, 653870.13, 
  653891.73999999999, 653923.45999999996, 653994.80000000005, 654048.05000000005, 654088.66000000003, 654153.76000000001, 654194.57999999996, 654226.75, 654256.96999999997, 654280.79000000004, 
  654304.60999999999, 654329.81000000006, 654359.44999999995, 654389.08999999997, 654418.87, 654454.39000000001, 654489.91000000003, 654526.80000000005, 654569.41000000003, 654612.03000000003, 
  654654.64000000001, 654700.10999999999, 654747.07999999996, 654794.06000000006, 654861.54000000004, 654961.54000000004, 655061.54000000004, 655161.54000000004]

YC = [274722.27000000002, 274757.53000000003, 274812.40000000002, 274906.14000000001, 274993.56, 275086.29999999999, 275182.27000000002, 275277.56, 275371.63, 
  275465.70000000001, 275559.78000000003, 275653.41999999998, 275745.64000000001, 275837.84999999998, 275930.06, 276022.70000000001, 276118.31, 276213.91999999998, 276309.53000000003, 276404.59000000003, 
  276499.40999999997, 276594.22999999998, 276689.04999999999, 276783.87, 276879.39000000001, 276976.71000000002, 277076.03000000003, 277175.90999999997, 277275.84000000003, 277375.76000000001, 277475.37, 
  277574.60999999999, 277673.84999999998, 277772.59999999998, 277870.77000000002, 277968.94, 278067.10999999999, 278165.28000000003, 278263.42999999999, 278361, 278458.57000000001, 278556.14000000001, 
  278653.71000000002, 278751.28999999998, 278847.14000000001, 278942.32000000001, 279037.51000000001, 279132.70000000001, 279227.89000000001, 279322.97999999998, 279414.37, 279505.75, 279597.13, 
  279689.16999999998, 279781.58000000002, 279873.98999999999, 279967.84000000003, 280062.44, 280157.03000000003, 280251.63, 280346.21999999997, 280437.06, 280526.75, 280619, 280712.88, 280806.76000000001, 
  280900.64000000001, 280994.53000000003, 281088.66999999998, 281182.85999999999, 281277.04999999999, 281371.23999999999, 281464.83000000002, 281558.31, 281651.78000000003, 281745.26000000001, 
  281838.72999999998, 281930.75, 282022.76000000001, 282114.78000000003, 282206.90999999997, 282299.03999999998, 282391.16999999998, 282483.28999999998, 282575.41999999998, 282668.21999999997, 
  282762.14000000001, 282856.06, 282949.98999999999, 283043.90999999997, 283137.84000000003, 283231.29999999999, 283324.67999999999, 283418.04999999999, 283511.35999999999, 283603.65000000002, 
  283695.92999999999, 283788.21999999997, 283882.19, 283978.57000000001, 284074.95000000001, 284171.32000000001, 284267.85999999999, 284367.65000000002, 284467.42999999999, 284567.21000000002, 284667, 
  284766.83000000002, 284866.67999999999, 284966.53999999998, 285066.40000000002, 285166.28000000003, 285266.27000000002, 285366.27000000002, 285466.26000000001, 285566.25, 285666.25, 285766.23999999999, 
  285866.22999999998, 285966.21999999997, 286066.19, 286166.07000000001, 286265.95000000001, 286365.83000000002, 286465.71000000002, 286565.64000000001, 286665.58000000002, 286765.52000000002, 286862.87, 
  286960.67999999999, 287060.56, 287160.44, 287260.33000000002, 287360.26000000001, 287460.26000000001, 287560.25, 287660.25, 287760.15999999997, 287860.06, 287959.96999999997, 288059.87, 288159.62, 
  288259.29999999999, 288358.97999999998, 288458.66999999998, 288558.07000000001, 288657.01000000001, 288755.96000000002, 288854.90999999997, 288953.85999999999, 289052.81, 289151.96000000002, 
  289251.28999999998, 289350.45000000001, 289449.59000000003, 289548.73999999999, 289648.15000000002, 289747.59999999998, 289847.04999999999, 289946.29999999999, 290045.51000000001, 290143.29999999999, 
  290240.60999999999, 290337.91999999998, 290435.54999999999, 290529.16999999998, 290594.33000000002, 290674.28999999998, 290765.67999999999, 290837.96000000002, 290927.40999999997, 291022.07000000001, 
  291117.35999999999, 291214.47999999998, 291311.59999999998, 291408.34000000003, 291503.84999999998, 291599.35999999999, 291694.82000000001, 291788.29999999999, 291881.77000000002, 291974.66999999998, 
  292065.14000000001, 292155.59999999998, 292246.07000000001, 292335.09999999998, 292423.38, 292511.65999999997, 292565.81, 292565.81, 292565.81, 292565.81]
  
#setup the figure space, axis and line to animate
fig = plt.figure(1, figsize=(5,5))
plt.axis('equal')
plt.plot(XC,YC,'k.-')
plt.plot(XB,YB,'.-',color=[0.7,0.7,0.5])
#
#plt.plot([27.816252252716946,-38705.66598372133],[-3153.4144290955851,89040.497267260376],'k--')
#
##plt.plot(X2,Y2,'r.')
for i in range(0,len(XB)):
    plt.text(XC[i],YC[i],str(i))
#    if Shadows1[i] == 1:
#        plt.plot(X[i],Y[i],'ko', ms=10)
#    if Shadows2[i] == 1:
#        plt.plot(X[i],Y[i],'go', ms=5)
#    elif Shadows2[i] == 2:
#        plt.plot(X[i],Y[i],'ro', ms=5)
#    elif Shadows2[i] > 2:
#        plt.plot(X[i],Y[i],'bo', ms=5)
#               
#plt.plot(X[0:2],Y[0:2],'k-',lw=2)
#plt.plot(X[-2:],Y[-2:],'k-',lw=2)
plt.show()
        