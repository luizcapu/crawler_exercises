# TitleFinder
OBJETIVOS

Imagine que temos uma arquivo texto onde cada linha contém o título de uma notícia: 
... 
Demora em votação pode deixar imposto mais alto, diz Levy 
Estátua de Tom Jobim tem parte danificada após brincadeira de jovem 
... 
 
Queremos poder encontrar, facilmente, quais títulos que possuem determinada palavra­chave. 
Seu objetivo é construir um programa que, em uma única execução, lê um arquivo de texto e 
possibilita que o usuário possa consultar passando uma palavra por vez (stdin). Para cada 
consulta o programa deve retornar todos os títulos de notícia que contém aquela palavra, 
ordenados pelo número de vezes que a palavra aparece naquele título. 
 
Observações: 
● O programa não precisa ter uma GUI 
● A parte de processamento do arquivo é feita "offline" e por isso pode demorar mais. A 
parte de consulta, feita "online" deve ser mais eficiente 
● É possível usar mais espaço em memória na parte offline se isso for deixar a parte de 
consulta mais rápida 
● Espera­se que para cada processamento do arquivo serão feito várias consultas 

