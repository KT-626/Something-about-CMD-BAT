print("欢迎·sakuraみそ")

counts = 3
while counts > 0:
    guess = int( input("请输入密码：") )

    if guess ==  5999:
        print("正确")
        break
    else:
        print("错误")
        counts = counts -1 
else:
    exit()
mima_infos=[]
a=0
import os
def print_menu():
    print("欢迎使用密码薄存储密码")
    print("1.增加信息")
    print("2.删除信息")
    print("3.查询信息")
    print("4.修改信息")
    print("5.退出程序")
    global a
    a=int(input("请输入要选择的功能:"))
    if (a>5):
        print("识别不到该功能，请重新再来:")
        print_menu()
def add_info():
    id=input("请输入网站或应用名称：")
    yem=input("请输入用户名:")
    mima=input("请输入密码:")
    dict1={'id':id,'dizhi':yem,'mima':mima}
    mima_infos.append(dict1.copy())
def del_info():
    id=input("请输入要删除的网站或应用名称的值:")
    find_flag=False
    for line in mima_infos:
        if line['id']==id:
            find_flag=True
            mima_infos.remove(line)
    if find_flag==True:
        print("已删除")
    else:
        print("您输入网站或应用名称不存在.")

def select_info():
    id=input("请输入要查找的网站或应用名称:")
    find_flag=False
    for line in mima_infos:
        if line['id']==id:
            find_flag=True
            print('名称',' ',line['id'])
            print('用户名',line['dizhi'])
            print('密码',' ',line['mima'])
            print(sep="   ")

    if find_flag==True:
        print("已显示")
    else:
        print("您输入的网站或应用名称不存在.")


def recover_info():
    id = input("请输入要网站或应用名称:")
    find_flag = False
    for line in mima_infos:
        if line['id'] == id:
            find_flag = True
            new_dizhi=input("请输入新的网站或应用名称:")
            new_mima=input("请输入新的密码:")
            line['dizhi']=new_dizhi
            line['mima']=new_mima
            print(line['id'],line['dizhi'],line['mima'],sep="   ")

    if find_flag == True:
        print("已修改")
    else:
        print("您输入的网站或应用名称不存在.")
def exitt():
    file=open('mima.txt','w+')
    for i in mima_infos:
        for value in i.values():
            file.write(value)
            file.write(" ")
        file.write('\n')


    file.close()
    os._exit(0)
def main():
    file=open('mima.txt','r+')
    content=file.readlines()

    global mima_infos
    for i in content:
        j=i.split(" ",2)

        dict2={'id':j[0],'dizhi':j[1],'mima':j[2]}
        mima_infos.append(dict2.copy())
    file.close()
    while True:
        print_menu()
        if a==1:
            add_info()
        if a==2:
            del_info()
        if a==3:
            select_info()
        if a==4:
            recover_info()
        if a==5:
            exitt()


main()

print("请退出后重试")



	

