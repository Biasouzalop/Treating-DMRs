from OpenClose import Arquivo
coords = Arquivo('dmrs_JME_coordsforbiomart.csv').abrir(0)

#Importando biomart server
from biomart import BiomartServer
server = BiomartServer("http://www.ensembl.org/biomart")

# Definindo base de dados
regulations = server.databases['ENSEMBL_MART_FUNCGEN']

# Reg. Evidence = Histone marks, TF, Open Cromatin Reg.
reg_evidence = regulations.datasets['hsapiens_peak']

final = []

i = 0
for x in coords[1:]:
    response = reg_evidence.search({
        'filters':{
            'chromosomal_region': x
        }
    },header = 0)

    resultado = []

    for line in response.iter_lines():
        line = line.decode('utf-8')
        resultado.append(x + list(line.split("\t")))
        Arquivo('dmrs_JME_regevidence.csv').salvar(resultado,append_mode=True)
        
    
    print(i)
    i += 1
    