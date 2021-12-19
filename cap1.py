'''
DevOps  é  uma  cultura  que  utiliza  práticas  e ferramentas  para  aumentar  a  capacidade  de  uma organização
de desenvolver  e entregar  softwares,  serviços,  aplicativos  e  demais  produtos  de  tecnologia  com alta
velocidade, porém,sem pôr em risco a estabilidade
Quando a organização adota a cultura DevOps, o ritmo de entrega dos produtos é  mais  rápido  do  que  o  das  empresas
que  usam  processos  tradicionais  de desenvolvimento de software e gerenciamento de infraestrutura

DevOps integra as áreas de desenvolvimento e operações, estimulando um ambiente multidiciplinar na qual devs e sysadmins
compartilham conhecimento e passam a produzir software com mais velocidade, qualidade, de forma mais estavel e segura.

Com  o  aumento  de  conhecimento  operacional  por  parte  dos desenvolvedores, a autonomia aumenta e tarefas
simples, que normalmente exigiriam a  ajuda  de  um  sysadmin  ou  demais  equipes  de  infraestrutura,começam  a
ser realizadas de forma independente, e o sysadmin passa a conhecer mais do software para  conseguir  atuar  de
forma  melhor  comele,  diminuindo  a  dependência  do desenvolvedor para entender certos fluxos ou comportamentos
que antes só a equipe de desenvolvimento conheceria.

beneficios do devops

1)Aumento da velocidade de entrega
DevOps  proporciona,por  meio de  ferramentas,a  automação  de  processos manuais e lentos, contribuindo,assim,para o
aumento da frequência e do número de entregas  do seu produto

2)Escalabilidade
Com a automatização da infraestrutura, DevOps proporciona a possibilidade de gerenciar  sua
infraestrutura  como  código,  diminuindo  a  interferência  manual  e,consequentemente,o  risco.  Você  passa  a
escalar  seu  código  de  infraestrutura  em diversos ambientes, pois aquilo que é igual para todos é replicado,
e implantando de forma  individual  e  automática  o  que  é  específico.  Com  processos  automáticos,  é possível
identificar  a  necessidade  de  escalar  sua  infraestrutura  de  acordo  com  a demanda,  por  exemplo:  seu
software  está  recebendo  mais requisições do que  o esperado  para  a  infraestrutura  provisionada;identificado  o
cenário,  antes  que aconteça  o  problema,  a  automação  pode,a  partir  de  um  alarme,  expandir  a infraestrutura
para atender às requisições.

3)Velocidade
As   equipes   que   possuem   a   cultura   DevOps têmmaior   independência, assumindo  a  responsabilidade  ponta  a
ponta  dos  produtos  e  serviços  para,então,realizar  as  entregas  e  melhorias  de  forma  mais  rápida,
contribuindo  assim  para  o atingimento  de  resultados.  Com  as  equipes  juntas,  ambas  estão  olhando  para  o
mesmo objetivo, também não é necessário demandar algo de infraestrutura para fora do time, o que poderia levar mais
tempo ou espera por priorização

4)Colaboração contínua
A  junção  das  equipes  astorna  mais  eficientes, promovendoa  cultura  da responsabilidade ponta a ponta e do
sentimento de "dono" do que é feito. As equipes de    desenvolvimento    e    sysadmin    colaboram    juntas

5)Confiabilidade
DevOps  promove  a  garantia  da  qualidade  das  atualizações  de  software  e alterações  de  infraestrutura por
meio de  processos  automatizados  de  testes  em diversos níveis, para,assim,aumentar a confiança das
entregas  e contribuir com a sua velocidade.  Os  testes  são  parte  fundamental  do  processo, e são  programados para
serem executados no decorrer do ciclo

6)Segurança
A  adoção  da  cultura  DevOps  aumenta a segurança por  meio de  políticas  de segurança     automáticas,     como
controles de acesso entre aplicações, permissionamento, autorização e técnicas de gerenciamento de configuração

Práticas DevOps
DevOps exige inovação, automação e simplificação de processos e de desenvolvimento de software e gerenciamento de
infra. A cultura DevOps está relacioanda a atualizações frequentes mas pequenas, ligada a metodologias ágeis como
Scrum e Kanban

Outra  prática, essa relacionada àarquitetura,é  a  adoção  de  microsserviços, para tornar seus aplicativos mais
flexíveis e permitir mudanças de forma mais rápida. A  arquitetura  de  microsserviços  desacopla  sistemas  grandes
e  complexos  e  os transforma  emsistemas  menores  e  independentes.  Os  sistemas  são  divididos  em vários
serviços individuais, e cada um delesabrange uma parte ou função única do negócio, além de ser operado
independentemente dos outros serviços.

As práticas de automação de infraestrutura, como a infraestrutura como código e o gerenciamento de configuração,
contribuem  para  que  os  recursos  de  infraestrutura  trabalhem  de  forma  elástica  e disponível para alterações
constantemente. Práticas de monitoração e indexação de log  contribuem  para  a  identificação  e  prevenção  de
problemas,  além  de  auxiliar  no acompanhamento do desempenho de softwares e da infraestrutura, para que possam
reagir rapidamente quando ocorrer problemas



Infraestrutura como código
A   infraestrutura   como   código   é   uma   prática   que   utiliza   técnicas   de
desenvolvimento de códigoeque permite controle de versão e integração contínua da  infraestrutura, por  meio de  API,
para  que  os  desenvolvedores  e  sysadmins trabalhem com a infraestrutura de modo programático, em vezde instalar e
configurar manualmente a infraestrutura. Isso permite que as equipes dentro de uma empresa operem em uma velocidade
maior, uma vez que o código da infraestrutura pode ser reaproveitado, e,quando atualizado, replicado para todos os
ambientesque utilizamesse trecho de código de infraestrutura.

Arquitetura de Microsserviços
A arquitetura de microsserviços representa um conjunto de pequenos serviços que se
interligam para construir um sistema. Cada serviço possui um contexto único de negócio,é executado de forma
individual e independente e se comunica com outros serviços por  meio de uma interface leve, na maioria doscasos
baseada em  HTTP

Integração Contínua
A  integração  contínua  é  uma  prática  de  desenvolvimento  que  permite  a execução  dos
testes  sempre  que  as  alterações  de  código  são  enviadas  para  o repositório central.  Os  principais
objetivos  da  integração  contínua  são  encontrar  e apontar os erros mais rapidamente a cada alteração,
consequentemente,melhorar a qualidade do software e reduzir o tempo necessário para validação

Entrega Contínua
A entrega contínua é uma prática que permite ao desenvolvedor,ao realizar as alterações  de
códigos,  utilizar  a  integração  contínua  para  realização  dos  testes necessários  e  preparar  automaticamente
as  modificações  para  uma  entrega  em produção. Quando a integração contínua é implementada adequadamente,
os times terão um pacote de entrega confiável pronto para ser implantado a cada alteração ou conjunto de alterações
enviadas para o repositório central.

Monitoração, Alarme, Log e Indexação
Realizar logs de informações das aplicações e infraestrutura é essencial para
realizar  o  monitoramento  e  gerar  alarmes.Ao  capturar,  indexar  e  analisar  os  logs gerados  pelos
aplicativos  e  pela   infraestrutura,  é   possível  entender   como  as alterações  ou  atualizações  estão
afetando  o  ambiente  e  seus  usuários,  o  que proporciona  maisfacilidade  na  rastreabilidade,  fornecendo
maior  esclarecimento sobre  as  causas  raiz  dos  problemas.  Com  os  logs  indexados,  é  possível  criar
dashboardsde  acompanhamento  realtime  e  programar  alarmes  de  acordo  com determinada situação do ambiente.

Comunicação e Colaboração
O aumento da comunicação, colaboração e compartilhamento de experiência é um dos principais
aspectos culturais do DevOps. O uso das práticas e ferramentas contribui   para   as   equipes   definirem   normas
culturais   sólidas   com   relação   ao compartilhamento  de  informações  e  processos  de  trabalho.  Com  a
unificação  das equipes, todos passam a trabalhar juntos,seguindo um objetivo comum


Estágios e Ferramentas DevOps
Planejamento (Plan)
- scrum, kanban e outras práticas ágeis para fatiamento e estimativas

Desenvolvimento ou Codificação (Code)
- git, confluence, jira

Construção (Build)
- maven, gradle

Teste (Test)
- Junit, Selenium, TestInfra

Lançamento / Entrega (Release)
- jenkins, codeship

Implantação (Deploy)
- docker, aws, kubernets, mesos

Operação (Operate)
Ansible, docker, kubernetes, mesos
Um assunto muito comum na operação é o escalonamentoda
infraestrutura, que  diz  respeito àestratégia  da sua expansão, em  que temos  dois  modelos,
o escalonamentovertical  e o horizontal.  O escalonamentovertical  tem  como  objetivo aumentar os recursos host,
aumentando a capacidade de memória, processamento, disco,  entre  outros.  Já  o escalonamentohorizontal  tem  como
objetivo  aumentar  a quantidade de hostse dividir o trabalho entre eles. Na arquitetura de microsserviços e
contêineres,   o escalonamentohorizontal   é   a   prática   mais   adequada,   e   os orquestradores  já  estão
preparados  para  isso.  Quando  utilizamos  o escalonamentovertical, aumentar os recursos acaba se tornandouma
estratégia mais cara, e pode se tornar limitada, visto que os recursos de infraestrutura maiores custammais e são
limitadosaté  certo  ponto.

Monitoração (Monitor)
- splunk, datadog, nagios


DEVSECOPS Muitas  vezes,a  abordagem  sobre  segurança  só  é  colocada  para  discussão após o software chegar à
produção, ou depois que ocorre algum problema relacionado à segurança, como vazamento de informações,
ataques e demais brechas.Para evitar que  o  assunto  de  segurança  só  seja  abordado  no  final  de  todo  o
ciclo,  existe  um movimento no mercado,conhecido como Shifting Security Left(movendo a segurança para  a  esquerda,
se considerarmos  que  o  ciclo  de  desenvolvimento  começa  na esquerda  e  termina  na  direita).Para  que  o
assunto “segurança” seja  abordado  no início de todo o ciclo
As principais vantagens ao se trabalhar com DevSecOps são

Segurança distribuída dentro da organização;
Prevenção e endereçamento  de vulnerabilidades  encontradas  antes  da entrega;
Disseminação da consciência de segurança dentro dos times;
Softwares mais seguros e com maior qualidade;
Redução de custo para identificar e resolver umproblema de segurança.

'''
