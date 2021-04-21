# Este pacote facilita a abertura e fechamento de arquivos em csv

# Patch correção 9/09
# Implementado seleção de delimitadores no método open()

import csv

class Arquivo:
    """[Classe que lida com aberturas de arquivos, recebe nome do arquivo como string e permite operações como abrir arquivo e jogar em tabela ou salvar uma tabela num arquivo]

    Args:
    nome_do_arquivo ([string]): [nome a ser usado para o arquivo]
    """
    
    def __init__(self, nome_do_arquivo):
         
        self.nome_do_arquivo = nome_do_arquivo
    
    def abrir(self,*lista_de_paramentros,delimitador = ',',linha_inicial=0):
        """[Método para abrir o arquivo e jogar em tabela tipo csv]

        Args:
            *lista_de_paramentros ([int], Optional) : [Sequencia de inteiros que definem as entradas a serem guardadas]
            delimitador ([str],Optional) : [Permite escolha do delimitador para abrir o arquivo, ',' convencional| '\t' tab]
            linha_inicial ([bool],Optional) : [Valor para linha que inicia a aquisição do arquivo]

        Returns:
            [Lista de listas 2 ordem]: [Retorna lista de listas tipo csv, onde cada lista interna representa uma linha]
        """
        file = open(self.nome_do_arquivo,'r')
        reader = csv.reader(file, delimiter = delimitador)
        lista = []
        if len(lista_de_paramentros) == 0:
            for line in reader:
                lista.append(line)
        else:
            for line in reader:
                aux=[]
                for p in lista_de_paramentros:
                    aux.append(line[p])
                lista.append(aux)
        file.close  
        if linha_inicial > len(lista)-1:
            return print('linha inicial excede limites da lista')
        return lista[linha_inicial:]


    def salvar(self,tabela,*cabecalho,append_mode = False):
        """[Metodo para salvar em arquivo uma tabela tipo csv]

        Args:
            tabela ([Tabela tipo csv]): [Tabela de dados a serem guardadas em arquivo, deve ser do tipo lista de 2 ordem -> [[],[],[],...] ]

            cabecalho ([Sequencia de str], optional): [Cabecalho a ser colocado antes da tabela]. 

            append_mode ([bool],Optional) : [Se True vai acrescentar informação ao documento partindo da ultima linha]
        Return:
            return ([None]): [Essa função não retorna nada]
        """
        mode = 'w'
        if append_mode:
            mode = 'a'
        file = open(self.nome_do_arquivo,mode)
        writer = csv.writer(file)
        if len(cabecalho) > 0:
            writer.writerow(cabecalho)
        writer.writerows(tabela)
        file.close

    def __repr__(self):
        return ('Objeto da classe Arquivo cujo nome é {}'.format(self.nome_do_arquivo))        
