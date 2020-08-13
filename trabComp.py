#https://github.com/Eduardo-Baranowski/compiladoresAnalisaLexico.git
res = {'while': 'palavra reservada','i':'identificador', '<':'operador', '100':'constante', 'do': 'palavra reservada', 'i':'identificador', '=':'operador', '+': 'operador', 'j': 'identificador', ';':'terminador'}
lista = list(res.keys())
lisAux =[]

def verifica(aux):
    listaIdentificador = []
    aux = ""
    cont = 0
    cont1 = 0
    cont2 = 0
    cont3 = 1
    cont4 = 1
    arq = open('arquivo.csv', 'w')
    arq1 = open('arquivoSimbolos.csv', 'w')
    arq.writelines('token' + ','+
    'identificação' + ','+
    'tamanho' + ','+ 'posição (lin; col)'+'\n')
    arq1.writelines('Índice' + ','+
    'Símbolo'+'\n')
    for i in range(len(var)):
        if var[i] == ' ':
            cont1 = i+1
            cont+=1
            continue
        aux = aux+var[i]
        cont+=1
        for item in res:
            cont2+=1

            if item == aux:
                if res[item] == 'identificador' or res[item] == 'constante':
                    if aux not in listaIdentificador:
                        listaIdentificador.append(aux)
                        cont4+=1
                if aux == ';':
                    linha = aux+','+res[item]+','+str(len(aux))+','+'(0;'+str(cont1+1)+')'
                    arq.writelines(linha+'\n')

                else:
                    linha = aux+','+res[item]+','+str(len(aux))+','+'(0;'+str(cont1)+')'
                    arq.writelines(linha+'\n')
                aux = ""

    for i in range(len(listaIdentificador)):
        linha = str(i+1)+','+listaIdentificador[i]
        arq1.writelines(linha+'\n')
    arq1.close()
    arq.close()
    return 'Tabela escrita com sucesso!     '


var = 'while i < 100 do i = i + j;'

print(verifica(var))