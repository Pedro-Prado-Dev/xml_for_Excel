import xmltodict
import os
import json


def take_information(file):
    with open( f'nfs/{file}',"rb") as file_xml:
        file_dic = xmltodict.parse(file_xml) 
        try:
            if "NFe" in file_dic:
                infos_nf = file_dic["NFe"]['infNFe']
            else:
                infos_nf = file_dic["nfeProc"]["NFe"]['infNFe']
            number_nf = infos_nf['@Id']
            issuing_company = infos_nf['emit']['xNome']
            customer_name = infos_nf ['dest']['xNome']
            adress = infos_nf['dest']['enderDest']
            if 'vol' in infos_nf['transp']:
                quantity = infos_nf['transp']['vol']['pesoB']
            else:
                quantity = "Uninformed"
            print(number_nf,issuing_company,customer_name,adress,quantity, sep="\n")
        except Exception as e:
            print(e)
            print(json.dumps(file_dic, indent=4))
            
        


files_list = os.listdir("nfs")

for file  in files_list:
    take_information(file)
    
    