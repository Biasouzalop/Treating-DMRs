from OpenClose import Arquivo

annot = Arquivo("dmrs_JME_Healthy.annotated.csv").abrir(21)

from biomart import BiomartServer
server = BiomartServer("http://www.ensembl.org/biomart")

genesinfo = server.databases['ENSEMBL_MART_ENSEMBL']

info = genesinfo.datasets['hsapiens_gene_ensembl']

#filter = 'ensembl_transcript_id_version': 'Transcript stable ID(s) with version [e.g. ENST00000000233.10]' (type: id_list, values: [])
#attributes = 'ensembl_gene_id': 'Gene stable ID' (default: False),'external_gene_name': 'Gene name' (default: False), 'gene_biotype': 'Gene type' (default: False) 

def pesquisa(enst):
  response = info.search({
    'filters':{
        'ensembl_transcript_id_version': enst
    },
    'attributes':[
      'ensembl_gene_id',
      'external_gene_name',
      'gene_biotype'
    ]
  })
  resultado = []
  for line in response.iter_lines():
    line = line.decode('utf-8')
    resultado.append(line.split("\t"))
  if resultado == []:
    return enst + ['NOT FOUND','NOT FOUND','NOT FOUND']
  else:
    return enst + resultado[0]

final = []
i=0
for linha in annot[1:]:
  if linha == ['NA']:
    final.append(['NA','NA','NA','NA'])
    print(i)
    i+=1
    continue
  final.append(pesquisa(linha))
  print(i)
  i+=1
print(final)
Arquivo('Complementation info.csv').salvar(final)