# TitleFinder

== GOALS (Brazilian Portuguese)

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


=== INSTALLATION

1) Be sure your environment is read to run Java (1.7) applications and supporting Maven projects (See: https://java.com/en/download/help/index_installing.xml and https://maven.apache.org/install.html)

2) Run build.sh file found at the root of the project ("titlefinder-0.0.1-SNAPSHOT-jar-with-dependencies.jar" file should be generated at [ROOT]/target)


=== EXPECTED PARAMETERS


The unique expected parameter is the location of the .txt file to be processed. If no file is informed you'll be asked to use the default example file.

```
Could not get title file from arguments. Do you wanna use default example file ? (Y/n): 
```


=== USAGE EXAMPLE

```
java -jar target/titlefinder-0.0.1-SNAPSHOT-jar-with-dependencies.jar ./src/main/resources/example.txt
```

