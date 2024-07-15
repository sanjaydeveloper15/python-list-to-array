# This is specific for 10 digits number
with open('module-2/list.txt', 'r') as f:
    content = f.read().split("\n")
    for i in range(len(content)):
        contentLine = content[i]

with open('module-2/array-list.txt', 'w') as f:
    f.write('["{}"]'.format('", "'.join(content)))