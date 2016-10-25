import subprocess, os

images = os.listdir('./img')
#qss = os.listdir('./qss')
f = open('resource.qrc', 'w+')
f.write(u'<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')

for item in images:
	f.write(u'<file alias="img/'+ item +'">img/'+ item +'</file>\n')
    #f.write(u'<file alias="icons/'+ item +'">icons/'+ item +'</file>\n')

#for item in qss:
#    f.write(u'<file alias="qss/'+ item +'">qss/'+ item +'</file>\n')

f.write(u'</qresource>\n</RCC>')
f.close()

pipe = subprocess.Popen(r'pyrcc4 -py3 -o Resource_rc.py resource.qrc', stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, creationflags=0x08)
