#!/usr/bin/python3
#Made by LCBRST
import sys
a = 1
while a == 1:
    print("================\n ASCII转码工具\n(仅支持单个字符)\n 请选择转码类型:\n  1.ASCII-字符\n  2.字符-ASCII\n  键入exit退出\n================")
    select=input('输入序号选择:')
    if select == '1':
        ASCII = input('输入ASCII编码:')
        if ASCII.isdigit():
            ASCII = int(ASCII)
            print(ASCII ,'对应的字符是:'+chr(ASCII)+'\n================\n')
        else:
            print("输入错误,请输入ASCII编码!")
    elif select == '2':
        character=input('输入字符:')
        if len(character) == 1:
            print(character+'对应的ASCII编码是:'+str(ord(character))+'\n================\n')
        else:
            print("输入错误,请输入单个字符!")
    elif select == "exit":
        print('感谢您的使用')
        input('键入任意键退出...')
        sys.exit()
    else:
        print ("输入错误，请输入1/2")