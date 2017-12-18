all_code = ''
all_code2 = ''

for a, b in self.progrem.items():
    if a[0] == '_':
            self.add(open(b[0], 'r').read(), a, b[0])
        
for a, b in self.cods.items():
    if 'def main' in b.code:
        main = b
        continue
    all_code += '\n###%s\n'%a
    all_code += b.code
    all_code += '\n###%s\n'%a
all_code += '\n###%s\n'%a
all_code += main.code
all_code += '\n###%s\n'%a


for i in all_code.split('\n'):
    if i:
        all_code2 += i + '\n'

open(r'finish_projects\%s.py'%self.progrem['name'], 'w').write(all_code2)
