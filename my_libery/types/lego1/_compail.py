
cods = []
for i in self.cods.items():
    cods.append(i)

all_cods = ""
in_file = []

for a, b in cods:
    if "main" in b.loc:
        main_name = a
        main = b
        try:
            name = b.connect_obj.loc[b.connect_obj.loc.find('\\')+1:]
            name = name[name.find("\\")+1:]
            name = name.replace('.py', '')
            main.code = main.code.replace("@function@", name + ".inp")
        except:
            print('*Connect error')
            raise 
    else:
        flag = True
        cod = b
        if cod.connect:
            if b.connect_obj in in_file:
                name = b.connect_obj.loc[b.connect_obj.loc.find('\\')+1:]
                name = name[name.find('\\')+1:]
                name = name.replace('.py', '')
                cod.code = cod.code.replace("@function@", name + ".inp")
                in_file.append(b)
            else:
                flag = False
                cods.append((a, b))
        else:
            in_file.append(b)
        if flag:
            all_cods += '###' + a + '\n'
            all_cods += cod.code
            all_cods += '###' + a + '\n\n'
all_cods += '###' + main_name + '\n'
all_cods += main.code
all_cods += '###' + main_name + '\n\n'

open(r'my_libery\finish_projects\%s.py'%self.progrem['name'], 'w').write(all_cods)
