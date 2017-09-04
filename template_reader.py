import xml.etree.ElementTree as ET

tree = ET.parse('configure_frag.xml')
root = tree.getroot()

t1=t2=t3=[]

for items in root.findall('item'):
	if(items.get('template') == 'T1'):
		t1.append(items.find('name').text)
	elif(items.get('template') == 'T2'):
		t2.append(items.find('name').text)
	elif(items.get('template') == 'T3'):
		t3.append(items.find('name').text)
print ("T1", t1)
print ("T2", t1)
print ("T3", t1)