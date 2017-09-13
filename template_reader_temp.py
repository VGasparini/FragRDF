import xml.etree.ElementTree as ET

tree = ET.parse('configurefrag.xml')
root = tree.getroot()
obj,prop,name,templ,temp,output = [],[],[],[],[],[]

for item in root.iter('item'):
	parent = list(item.attrib.items())
	for i in range(len(parent)):
		obj = parent[i][0]
		prop = parent[i][1]
		if (obj == 'template'):
			templ.append(prop)
		elif (obj == 'name'):
			name.append(prop)
t = list(set(templ))
for i in range(len(t)):
	for j in range(len(templ)):
		if (t[i] == templ[j]):
			temp.append(name[j])
		output.append(temp)
for i in range(len(t)):
	output[i] = sorted(list(set(output[i])))
print(output[0])

try:
    nome_arquivo = 'part'
    arquivo = open(nome_arquivo, 'r+')
except:
    arquivo = open(nome_arquivo, 'w+')
for i in range(len(output[0])):
	arquivo.writelines(output[0][i])
	arquivo.writelines('\n')
arquivo.close()
