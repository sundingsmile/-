#coding:utf-8
#Author:Smile
#Time:2019-11-20

import os

'''字符串常量'''
Model = 'Model:'
No = 'Serial Number:'
Voc = 'Voc(V):'
Eff = 'Efficiency(%):'
FF = 'Fill Factor(%):'
Jsc = 'Jsc(A/m2):'
Rs = 'Rs(ohm):'
Rsh = 'Rsh(ohm):'
Tittle = 'Model                    No.          Voc               Eff                    FF                    Jsc                    Rs                Rsh\r\n'.encode()
ss0,ss1,ss2,ss3,ss4,ss5,ss6,ss7 = '','','','','','','',''
temp_ss0 = ''  

print('''
=============================================================

提示：输入的文件名为软件运行结果的文件名。

=============================================================
''')

filename = input("Please Input FileName:")  # 要保存的文件名

temp_files = os.listdir(os.curdir)  # 查看当前路径下面包含的文件
files = []  # 缓存列表

for file in temp_files:  # 过滤文件，将txt文件添加到files列表当中
    if file.endswith('.txt'):
        files.append(file)

if filename.endswith('.txt'):  # 判断输入的文件名是否是txt结尾，不是加上txt
    pass
else:
    filename = filename + '.txt'
with open(filename,'wb') as f:
    f.write(Tittle)


for temp in files:  # 遍历文件内容，提取数据
    with open(temp) as f:
        file_content = f.readlines()
        if 'PV Cell Characteristics' in file_content[0]:
            temp_ss0 = ss0[:9]  # 用来判断两次ss0[:-2]的数值是否变化
            # print(temp_ss0,'temp_ss0')
            for temp_content in file_content:  # 提取数据
                if temp_content.find(Model) != -1:
                    ss0 = temp_content.strip().split(":")[1].strip().ljust(11,'?')
                elif temp_content.find(No) != -1:
                    ss1 = temp_content.strip().split(":")[1].strip()
                    if ss1:
                        ss1 = ss1.rjust(2, '0')
                    else:
                        ss1 = ss1.rjust(2,'?')
                elif temp_content.find(Voc) != -1:
                    ss2 = temp_content.strip().split(":")[1].strip()
                    ss2 = str(float(ss2) * 1000)[0:5].rjust(5,'0')
                elif temp_content.find(Eff) != -1:
                    ss3 = temp_content.strip().split(":")[1].strip()[0:8]
                elif temp_content.find(FF) != -1:
                    ss4 = temp_content.strip().split(":")[1].strip()[0:8]
                elif temp_content.find(Jsc) != -1:
                    ss5 = temp_content.strip().split(":")[1].strip()[0:8]
                elif temp_content.find(Rs) != -1:
                    ss6 = temp_content.strip().split(":")[1].strip()[0:8]
                elif temp_content.find(Rsh) != -1:
                    ss7 = temp_content.strip().split(":")[1].strip()[0:8]

            # print(ss0[:9])
            if temp_ss0 == ss0[:9] or temp_ss0 == '':
                with open(filename,'ab+') as f:
                    f.write(('%s          %s          %s          %s          %s          %s          %s          %s\r\n' %(ss0,ss1,ss2,ss3,ss4,ss5,ss6,ss7)).encode())
                    #ss1 = ''
            else:
                with open(filename,'ab+') as f:
                    f.write(('\r\n').encode())
                    f.write(('%s          %s          %s          %s          %s          %s          %s          %s\r\n' %(ss0,ss1,ss2,ss3,ss4,ss5,ss6,ss7)).encode())
                    #ss1 = ''
