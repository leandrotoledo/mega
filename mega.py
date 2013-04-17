#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import urllib2
import re
import sys

"""
Instruções:
1) No mesmo local do script criar arquivo mega.txt com os códigos dos jogos, por exemplo:
...
04-07-12-25-37-43
02-13-20-22-31-42
02-09-12-16-28-33-43-46-51-52
03-06-12-29-31-38-50-51-57
02-05-07-11-17-34-42-54
...

2) Executar o script com o código do concurso:
$ ./mega.py 1450

3) É possível colocar no cron
0 5 * * 1 /home/leandrotoledo/mega.py 1450 | mail -s "Resultado Mega" leandrotoledodesouza@mail.com

4) Se você ganhar faça um donate pra mim! ;-)

Author: Leandro T. Souza <leandrotoledo [at] member [dot] fsf [dot] org>
Update: Thu, 27 17:45 2012
"""

FILE_APOSTAS = 'mega.txt'
URL_CONCURSO = 'http://www1.caixa.gov.br/loterias/loterias/megasena/megasena_pesquisa_new.asp?submeteu=sim&opcao=concurso&txtConcurso='


def getApostas():
    apostas = []

    with open(FILE_APOSTAS, 'r') as f:
        for r in f:
            r = r.replace('\n', '')
            apostas.append(r)

    return apostas


def getResultado(concurso):
    url = URL_CONCURSO + str(concurso)
    url = urllib2.urlopen(url)
    html = url.read()
    url.close()

    data = html.split('|')
    if data[-1].decode('iso-8859-1', 'utf-8') == u'Não existe resulado!': # sim, resulado...
        print 'Ainda não saiu o resultado...'
        exit()

    resultado = re.findall('\d{2}', data[20]) # resultado ordenado

    return resultado


def sorteio(apostas, resultado):
    print '[ TOTAL DE ACERTOS ] | JOGO'
    print

    for aposta in apostas:
        aposta = aposta.split('-')

        total = 0
        for i in resultado:
            for j in aposta:
                if i == j:
                    total += 1

        if total == 6:
            print '[%s] | %s GANHOU!' % (total, '-'.join(aposta))
        else:
            print '[%s] | %s' % (total, '-'.join(aposta))

    print
    print 'JOGO:', '-'.join(resultado)


def main(concurso):
    apostas = getApostas()
    resultado = getResultado(concurso)

    sorteio(apostas, resultado)


if __name__ == '__main__':
    try:
        concurso = sys.argv[1]
    except IndexError:
        print 'Informe o código do concurso.'
        print 'Por exemplo:', sys.argv[0], '1450'
        exit()
    main(concurso)
