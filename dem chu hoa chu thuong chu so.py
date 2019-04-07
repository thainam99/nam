cau=input('nhập câu: ')
dict={'H':0,'T':0,'S':0}
for i in cau:
    if i.isupper():
        dict['H']=dict['H']+1
    elif i.isnumeric():
        dict['S']=dict['S']+1
    else:
        if i!=' ':
            dict['T']=dict['T']+1
print(dict)