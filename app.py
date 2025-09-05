"""main module"""


import utilities as ut

dic = ut.read_config()
print(dic)
main_path = dic['path']['mainPath']
print(f"La ruta de la empresa es: {main_path}")

companyName = input("Ingrese el nombre de la compañia: ")
companypath = main_path + '\\' + companyName
print(companypath)
val = ut.validate_path(companypath)

if val:
    print(f"la compañia {companyName} existe")
    requirementName = input("Ingrese el nombre del requerimiento: ")
else:
    print(f"la compañia {companyName} no existe")
