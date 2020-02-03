import sys

var1=int (input('请输入第一个参数:'))
var2=int (input('请输入第二个参数:'))
var3=input('请输入运算符:')


#print ("%d%s%d" %(var1,var3,var2))

if var3=='*':
    print ("结果为:")
    print ((var1)*(var2))
elif var3=='/':
    print ("结果为:")
    print ((var1)/(var2))
elif var3=='-':
    print ("结果为:")
    print ((var1)-(var2))
elif var3=='+':
    print ("结果为:")
    print ((var1)+(var2))
else:
    print ("运算符错误！")
