mega
====

Scriptzinho em python para conferir jogo da Mega-Sena

Instruções
==========

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

0 5 * * 1 /home/leandrotoledo/mega.py 1450 | mail -s "Resultado Mega" leandrotoledodesouza@gmail.com


4) Se você ganhar faça um donate pra mim! ;-)
