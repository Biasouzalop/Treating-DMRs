from OpenClose import Arquivo

# --------------------------- importing data tables ---------------------------------------- 
# Excluding headline => linha_inicial = 1
# Annot. interest columns => CHR=0, START= 1, END=2, METHYLATION=14, STRAND=19, GENE=23, REGIONS=24.

table_dmr = Arquivo('Data table/dmrs_JME_Healthy.csv').abrir(linha_inicial = 1)
table_annot = Arquivo('Data table/dmrs_JME_Healthy.annotated.csv').abrir(0,1,2,14,19,23,24,linha_inicial = 1)

print(table_dmr[-1])
#----------------------------- the merge function ----------------------------------------
# merge_same_region => compiles the information inside the same dmr (ex.: gene1/gene2/gene3) 
# merge => compares info_list with aux and merged. If region do not exist in aux = creat entry at aux and merged; if region exists in aux = compile info at merged (using merged_same_region)
# index = aux_list.index(line[:3]) finds the exact position of the coordenate at aux_list, so then we can find it on merged_list and maintain the order. 
# merged_list[index][line] = merge_same_region([merged_list[index][3],line[3]]) finds the coordenate, and apply the new merged line at merged_list for lines (methylation[3] strand[4], gene[5] and regions[6])
# compiled is the new table with all merged data

def merge_same_region(old_str,new_str): #old_str = line in merged_list; new_str =  new line to be merged
  lista = list(set(old_str.split('/') + [new_str]))  # lista = ['a','a','a', new_str] => set transforms the lista in a collection of unique elements (removes duplicates) => lista = ['a', new_str]
  strg = ''
  for i in lista:
    strg += '/' + str(i)
  return strg[1:]

def merge(info_list): 
  aux_list = []
  merged_list = [] 

  for line in info_list:
    if line[:3] not in aux_list:
      aux_list.append(line[:3])
      merged_list.append(line)
    else:
      index = aux_list.index(line[:3])
      merged_list[index][3] = merge_same_region(merged_list[index][3],line[3])
      merged_list[index][4] = merge_same_region(merged_list[index][4],line[4])
      merged_list[index][5] = merge_same_region(merged_list[index][5],line[5])
      merged_list[index][6] = merge_same_region(merged_list[index][6],line[6])
     
  return merged_list 


compiled_info = merge(table_annot)
Arquivo("dmrs_JME_Healthy_compiled.csv").salvar(compiled_info)





