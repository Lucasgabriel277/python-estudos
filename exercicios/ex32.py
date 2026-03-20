dicionario_empresas = {} 

cnpj_empresa = input("CNPJ: ").strip()

nome = input("Nome: ").capitalize().strip()
ramo = input("Ramo: ").capitalize().strip()

dicionario_empresas[cnpj_empresa] = (nome, ramo)

for cnpj, (nome, ramo) in dicionario_empresas.items():
    print(f"CNPJ: {cnpj} - Nome: {nome} - Ramo: {ramo}")