from OpenClose import Arquivo
coords = Arquivo('dmrs_JME_coordsforbiomart.csv').abrir(0)

#Importando biomart server
from biomart import BiomartServer
server = BiomartServer("http://www.ensembl.org/biomart")

# Definindo base de dados
regulations = server.databases['ENSEMBL_MART_FUNCGEN']

# Features = Reg. elements (CTCF Binding site, Promoter)
reg_feature = regulations.datasets['hsapiens_regulatory_feature']

final = []

i = 0
for x in coords[1:]:
    response = reg_feature.search({
        'filters':{
            'chromosomal_region': x
        }
    },header = 0)

    resultado = []

    for line in response.iter_lines():
        line = line.decode('utf-8')
        resultado.append(x + list(line.split("\t")))
        Arquivo('dmrs_JME_regfeatures.csv').salvar(resultado,append_mode=True)
        
    
    print(i)
    i += 1




