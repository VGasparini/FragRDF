#Tempo de execução
import time

#Importanto biblioteca para manipular RDF
#Disponivel em https://github.com/RDFLib
import rdflib
g = rdflib.Graph()

op = int(input("\n\nEscolha qual formato de arquivo carregar: 1- N-Triples 2- RDF/XML    "))
ini = time.time()
print("\n\nRealizando carregamento do arquivo")
if (op == 1):
	g.parse('test.nt',format='nt') #Iniciando arquivo RDF em formato N-Triples (referencia local)
elif (op ==2):
	g.load('http://dbpedia.org/data/Semantic_Web.rdf')#Iniciando arquivo RDF em formato RDF/XML (referencia online)
else:
	print("Opção inválida. Saindo...")
	exit()

temp = time.time()

print("\n\nIniciando verificação... Aguarde\n")
subj = list(set(g.subjects())) #Gerando lista com todos os sujeitos
lista = [] #Declarando lista para alocar objetos
unicos = [] #Declarando lista para isolar elementos únicos

for j in range(len(subj)):
	subj_ref = rdflib.URIRef(subj[j]) #Convertendo cada sujeito em uma lista. Ex: subj = [http://ex.com/] ; ref = [h,t,t,p,:,/,/...]
	uri_ref = rdflib.RDF #Declarando que será usado referêcias URI
	type = g.value(subj_ref, uri_ref) #Declarando tipagem a ser buscada
	lista.append(list(x for x in g.objects(subj_ref, uri_ref['type']))) #Incluindo na lista objetos conforme critérios

#Linearizando a lista
for i in range(len(lista)):
	for j in range(len(lista[i])):
		unicos.append(lista[i][j])

lista = sorted(list(set(unicos))) #Removendo elementos repetidos e ordenando alfabeticamente

print("Objetos encontrados:\n\n")
for i in range(len(lista)):
	print(i+1," - ",lista[i])

fim = time.time()
print("\n\nTempo para carregamento do RDF: {:.3f}s\nTempo para verificação: {:.3f}s\nTempo total de execução: {:.3f}s".format(temp-ini,fim-temp,fim-ini))