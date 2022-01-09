'''
O modelo  de caso de uso possui três objetivos: descrever a necessidade do cliente, estabelecer a base do sistema a ser
implementado e definir um conjunto de requisitos que possam ser validados quando oprojeto for construído

O modelo de caso de uso é elaborado durante as reuniões entre a equipe de desenvolvimento  do  sistema  e  os
stakeholders,para  especificar  os  requisitos.  É composto do diagrama de caso de uso e da descrição dos casos de uso,
em geral, uma descrição textual.

Conceito do modelo de caso de uso
o  modelo  de  casos  de  uso  é  uma representação  das  funcionalidades  externamente  perceptíveis  do  sistema  e
dos elementos externos ao sistema que trocam informações com ele.O modelo de caso de uso descreve os requisitos
funcionais de um sistema sob o ponto de vista do usuário. A construção desse modelo relaciona as funcionalidades do
sistema  (casos  de  uso),  seu  ambiente  operacional  (atores)  e  o  relacionamento entre eles (comunicação entre
os atores e os casos de uso)Os objetivos do modelo de caso de uso são especificar, construir e documentar o
comportamento de cada parte que o sistema deve possuir

Elementos do modelo de caso de uso
A  construção  desse  modelo  de  caso  de  uso implicaa  definição  de  diversos elementos, sãoeles: cenário, caso de
uso, ator,fronteira e os relacionamentos

Cenário
conformeos requisitos são levantados, uma visão  geral  das  características  e  funções  do  sistema  começa  a  se
concretizar. No entanto,  é  difícil  entender  como  tais  características  e  funções  serão  usadas  por diferentes
usuários. Para isso, é possível criar um conjunto de cenários que identifique um roteiro de uso para o sistema a ser
desenvolvido.
um cenário é a descrição de uma das maneiras pelas quais  um  caso  de  uso  pode  ser  executado  ou  realizado,
também  conhecido  como instância de um caso de uso.
Um cenário representa uma sequência de passos que descreve uma interação entre um usuário e um sistema; detalha o
caminho do ponto inicial até o ponto final de um  fluxo  de  eventos.


Caso de uso
o caso de uso especifica uma   sequência   de   ações   realizadas   pelo   sistema,   que   produz   um   resultado
perceptível e de valor para o ator.
O que é um caso de uso? Seguindo  a  analogia  dos  exemplos  anteriores,  é  aquele  que  descreve  uma sequência
completa de interações, ou seja, como as funcionalidadesse relacionarão entre  sie  como  serão  utilizadas  pelo
usuário  (ator),  durante  o  funcionamento  do sistema. A diferença é que,para descrever essa interação,utiliza-se uma
metodologia, que   serve   para   padronizar   a   descrição   da   funcionalidade;   de   modo   que   o desenvolvedor
que utilizará o caso de uso para implementar o sistema ou o analista que validará o desenvolvimento ou fará os testes
entenda a funcionalidadede uma maneira única.


Ator
Um ator corresponde a um papelrepresentado por algo ou alguém, qualquer elemento externo ao sistema. Pode serum ser
humano, hardware, dispositivo ouo sistemaexternoque interagecom o sistema em questão
O ator é quem interagirá com o sistema. O termo “interage” significa que um ator troca informações com o sistema
(envia informações para o sistema  processar ou recebe informações processadas provenientes do sistema)


Fronteira
Representa  os  casos  de  uso  que  compõem  o  sistema,  ou  seja,  o  limite  do sistema.


Relacionamentos
A estruturação do modelo de casos de uso envolve a utilização dos seguintes tipos de relacionamento: comunicação,
inclusão, extensão e generalização.O  relacionamento  mais utilizadode  um  ator  para  com  um  caso  de  uso  é  a
associaçãopor comunicação, o que significa que o atorexecuta a funcionalidade especificada no caso de uso. Ainda, temos
os casos de usoquese relacionam entre si, os três relacionamentos são: inclusão, extensão e generalização


Associação por comunicação
O relacionamento de comunicação também é conhecido como associação por comunicação. Esse relacionamento indica com qual
caso de uso um determinado ator troca informações. Um ator pode interagir com mais de um caso de uso do sistema

Associação por inclusão
O  relacionamento  de  inclusão  conecta  o  caso  de  uso  base  ao  caso  de  uso incluído. O caso de uso base faz
explicitamente a inclusão do caso de uso incluído.Essetipo de relacionamento existe somente entre casos de uso

Associação por extensão
Relacionamento que identifica um processo opcional, ou seja, pode ou não ser executado.  Ocorre  em  uma  situação
específica, em  queuma  condição  é  satisfeita. Esse relacionamento só acontece entre casos de uso
O  relacionamento  de  extensão  é  utilizado  para  modelar  situações  em  que diferentes sequênciasde interações
podem ser inseridas em um mesmo caso de uso. Cada uma dessas diferentes sequênciasrepresenta um comportamento eventual,
ou seja,um  comportamento  que  só  ocorre  sob  certas  condições,  ou  cuja  realização dependeda escolha do ator

Generalização
Este relacionamento permite que um caso de uso ou ator herde características de outro, mais genérico, esse último
chamado de caso de uso ou ator base. O caso de uso ou ator herdeiro pode especializar o comportamento do caso de uso ou
ator base.
O objetivo desserelacionamento é indicar que dois ou mais casos de uso ou atores têm comportamentos semelhantes; o caso
de uso abstrato é utilizado apenas para capturar a natureza semelhante entre os casos de usos filho, esses conhecidos
como concretos


Diagrama de caso de uso
O diagrama de caso de uso apresentao comportamento externo do sistema, ou  seja,como  os  casos  de  uso  interagem
entre  si  e  com  os  atores; como  as funcionalidades  se  relacionarão  umas  com  as  outras  e  como  serão
utilizadas  pelo usuário durante o funcionamento do sistema

'''