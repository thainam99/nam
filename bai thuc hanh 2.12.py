import re
value=[]
items=[x for x in input("nhap mat khau:").split(',')]
# ###################
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.seach("[a-z]",p):
        cotinue
    elif not re.seach("[0-9]",p):
        cotinue
    elif not re.seach("[A-Z]",p):
        cotinue
    elif not re.seach("[$#@]",p):
        cotinue
    elif re.seach("\s",p):
        cotinue
    else:
        pass
    value.append(p)
print(",".join(value))