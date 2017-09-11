import xml.etree.ElementTree as ET

tree = ET.parse('configure_frag.xml')
root = tree.getroot()
obj,prop,temp,t,i,templ = [],[],[],[],0,[]

for item in root.iter('item'):
	parent = list(item.attrib.items())
	for i in range(len(parent)):
		obj.append(parent[i][0])
		prop.append(parent[i][1])
	obj = list(set(obj))
	templ.append(prop[obj.index('template')])
#templ = sorted(list(set(templ)))
print(templ)
'''for item in root.iter('item'):
	if(prop[obj.index('template')] == 'T1'):
		temp.append(prop[obj.index('name')])
	del obj[:]
	del prop[:]'''
print(' T1:')
for j in range(len(t)):
	print(t[j])
