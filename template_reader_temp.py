import xml.etree.ElementTree as ET

tree = ET.parse('configure_frag.xml')
root = tree.getroot()
obj,prop,temp,t = [],[],[],[]

for item in root.iter('item'):
	parent = list(item.attrib.items())
	for i in range(len(parent)):
		obj.append(parent[i][0])
		prop.append(parent[i][1])
	if(prop[obj.index('template')] == 'T1'):
		temp.append(prop[obj.index('name')])
	del obj[:]
	del prop[:]
	t.append(temp)
print(' T1:')
for j in range(len(t)):
	print(t[j])