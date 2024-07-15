# This is specific for 10 digits number
with open('module-1/list.txt', 'r') as f:
    content = f.read().split("\n")
    for i in range(len(content)):
        contentLine = content[i]
        if len(contentLine) < 10:
            print(contentLine)
            content[i] = contentLine.rjust(10, '0')

with open('module-1/array-list.txt', 'w') as f:
    f.write('["{}"]'.format('", "'.join(content)))