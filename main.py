import xmltodict
import os
import pandas as pd


def take_information(file, values):
    with open( f'nfs/{file}',"rb") as file_xml:
        file_dic = xmltodict.parse(file_xml) 
        
        if "NFe" in file_dic:
            infos_nf = file_dic["NFe"]['infNFe']
        else:
            infos_nf = file_dic["nfeProc"]["NFe"]['infNFe']
        number_nf = infos_nf['@Id']
        issuing_company = infos_nf['emit']['xNome']
        customer_name = infos_nf ['dest']['xNome']
        adress = infos_nf['dest']['enderDest']
        if "vol" in infos_nf['transp']:
            weight = infos_nf['transp']['vol']['pesoB']
        else:
            weight = "Uninformed"
        values.append([number_nf, issuing_company, customer_name, adress,weight])
          
files_list = os.listdir("nfs")
col = ["number_nf","issuing_company","customer_name","adress","weight"]
values = []

for file  in files_list:
    take_information(file,values)

table = pd.DataFrame(columns=col, data=values)  
table.to_excel("Nfs.xlsx", index =False)

    