import PyPDF2, re, os, time
from collections import defaultdict

class converter:
    def __init__(self, arquivo):
        if os.path.exists('Arquivo_TXT.txt'):
            pass
        else:
            self.arquivo = arquivo
            arq_PDF = PyPDF2.PdfReader(self.arquivo, 'rb')
            paginas = len(arq_PDF.pages)
            texto   = []
            for c in range(0, paginas):
                arq_PDF   = open('2022.1.pdf', 'rb')
                readerPDF = PyPDF2.PdfFileReader(arq_PDF)
                pageObj   = readerPDF.getPage(c)
                texto.append(pageObj.extractText())
                arq_PDF.close()
                
            arq_TXT = open(r"Arquivo_TXT.txt","w")
            arq_TXT.writelines(texto)
            arq_TXT.close()

    def print_Arquivo_Terminal(self):
        self.arquivo = 'Arquivo_TXT.txt'
        with open(self.arquivo, 'r', encoding='utf-8') as printTerminal:
            mostrar_Na_Tela = printTerminal.readlines()
            printTerminal.close()
        for tela in mostrar_Na_Tela:
            print(tela.replace('\n', ''))

    def mostrar_Todos_Professores(self):
        if os.path.exists('DadosSeparados/NomesProfessores.txt'):
            pass
        else:
            self.arquivo = 'Arquivo_TXT.txt'
            with open(self.arquivo, 'r', encoding='utf-8') as txt:
                arquivo_Temporario = txt.readlines()
                txt.close()

            lista_Temporaria = []
            for alterar in range(len(arquivo_Temporario)):
                if 'Página' in arquivo_Temporario[alterar]:
                    troca = arquivo_Temporario[alterar].replace('Página', '\n')
                    lista_Temporaria.append(troca)
                else:
                    lista_Temporaria.append(arquivo_Temporario[alterar])

            lista_Completa = []
            for nome in range(len(lista_Temporaria)):
                if 'Vagas Oferecidas' in lista_Temporaria[nome]:
                    lista_Completa.append(lista_Temporaria[nome -1])
                
            NomesProfessores = open(r"DadosSeparados/NomesProfessores.txt","w")
            NomesProfessores.writelines(lista_Completa)
            NomesProfessores.close()

            try:
                with open('DadosSeparados/NomesProfessores.txt', 'r') as fr:
                    lines = fr.readlines()
                    with open('DadosSeparados/NomesProfessores.txt', 'w') as fw:
                        for line in lines:
                            if line.find(':') == -1:
                                fw.write(line)
            except:
                print("Oops! existe um erro")
    
    def mostrar_Todas_Disciplinas(self):
        if os.path.exists('DadosSeparados/NomesDisciplinas.txt'):
            pass
        else:
            self.arquivo = 'Arquivo_TXT.txt'
            with open(self.arquivo, 'r', encoding='utf-8') as txt:
                arquivoCompleto = txt.readlines()
                txt.close()

            lista_Temporaria = []
            for disciplinas in range(0, len(arquivoCompleto)):
                if 'Vagas Ocupadas:' in arquivoCompleto[disciplinas]:
                    if '-' in arquivoCompleto[disciplinas]:
                        troca = arquivoCompleto[disciplinas].replace('- ', '\n', 1)
                        lista_Temporaria.append(troca)

            NomeDisciplica = open(r"DadosSeparados/NomesDisciplina.txt","w")
            NomeDisciplica.writelines(lista_Temporaria)
            NomeDisciplica.close()

            try:
                with open('DadosSeparados/NomesDisciplina.txt', 'r') as fr:
                    lines = fr.readlines()
                    with open('DadosSeparados/NomesDisciplina.txt', 'w') as fw:
                        for line in lines:
                            if line.find('Vagas Ocupadas:') == -1:
                                fw.write(line)
            except:
                print("Oops! existe um erro")

    def mostra_Carga_Horaria(self):
        if os.path.exists('DadosSeparados/NomesDisciplinas.txt'):
            pass
        else:
            self.arquivo = 'Arquivo_TXT.txt'
            with open(self.arquivo, 'r', encoding='utf-8') as txt:
                arquivoCompleto = txt.readlines()
                txt.close()

            lista_Temporaria = []
            lista_Completa = []
            for horas in arquivoCompleto:
                if 'CH:' in horas:
                    lista_Temporaria.append(horas.replace('CH:', ''))

            for remover in lista_Temporaria:  
                if 'horas' in remover:
                    lista_Completa.append(remover.replace('horas', ''))

            Carga_Horaria = open(r"DadosSeparados/CargaHoraria.txt","w")
            Carga_Horaria.writelines(lista_Completa)
            Carga_Horaria.close()

    def quantidade_Vezes_Professores():
        mostrar_Todos_Professores()
        with open('DadosSeparados/NomesProfessores.txt', 'r', encoding='utf-8') as arquivo:
            arquivo = arquivo.readlines()

        dicionario = defaultdict(int) 
        for c in arquivo:
            dicionario[c] += 1

        for k, v in dicionario.items():
            print(k.replace('\n', '') , '\033[1;31m aparece:\033[m' , v,)

teste = converter('2022.1.pdf')
teste.mostra_Carga_Horaria()
