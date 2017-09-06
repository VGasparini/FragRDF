import xml.etree.ElementTree as ET

tree = ET.parse('configure_frag.xml')
root = tree.getroot()
obj,prop,t1,t2,t3,t4,t5,t6 = [],[],[],[],[],[],[],[]

for item in root.iter('item'):
	parent = list(item.attrib.items())
	for i in range(len(parent)):
		obj.append(parent[i][0])
		prop.append(parent[i][1])
	if(prop[obj.index('template')] == 'T1'):
		t1.append(prop[obj.index('name')])
	elif(prop[obj.index('template')] == 'T2'):
		t2.append(prop[obj.index('name')])
	elif(prop[obj.index('template')] == 'T3'):
		t3.append(prop[obj.index('name')])
	elif(prop[obj.index('template')] == 'T4'):
		t4.append(prop[obj.index('name')])
	elif(prop[obj.index('template')] == 'T5'):
		t5.append(prop[obj.index('name')])
	elif(prop[obj.index('template')] == 'T6'):
		t6.append(prop[obj.index('name')])
	del obj[:]
	del prop[:]
print(' T1:')
for j in range(len(t1)):
	print(t1[j])
print(' T2:')
for j in range(len(t2)):
	print(t2[j])
print(' T3:')
for j in range(len(t3)):
	print(t3[j])
print(' T4:')
for j in range(len(t4)):
	print(t4[j])
print(' T5:')
for j in range(len(t5)):
	print(t5[j])
print(' T6:')
for j in range(len(t6)):
	print(t6[j])
