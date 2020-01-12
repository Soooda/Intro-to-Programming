time = input('工作时间：') #10
# 把字符转变成可以计算的数字
time = int(time)
efficiency = input('工作效率: ') #20
# 把字符转变成可以计算的数字
efficiency = int(efficiency)
work = time * efficiency
# 把可以计算的数字转变成字符
work = str(work)
print('工作总量 = ' + work)
