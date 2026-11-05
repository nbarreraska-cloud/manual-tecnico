# 17. IL·LUMINACIÓ D'EFECTES LLUMINOSOS (OSL)

## 17.1. Funció de l'OSL

L'OSL (*Object Source Lighting*) representa una font que emet llum i la influència que exerceix sobre els objectes pròxims. Pot aplicar-se a flames, espelmes, brases, cristalls màgics, energia, dispositius tecnològics, pantalles o artefactes lluminosos.

No consisteix a pintar un halo de color al voltant d'un element. Cal diferenciar la font emissora de les superfícies receptores i establir una relació espacial comprensible entre totes dues. La representació pot simplificar la situació física, però ha de mantenir una lògica interna.

Aquest capítol desenvolupa la planificació, construcció i avaluació de l'efecte. Els fonaments generals de la llum corresponen al capítol 5; les tècniques d'aplicació, als capítols 8–10; i les representacions específiques de foc i energia, als capítols 30 i 32.

## 17.2. Fonaments visuals de l'OSL

### 17.2.1. Font lluminosa i superfície il·luminada

El primer criteri consisteix a diferenciar la font lluminosa dels objectes que reben la seva llum.

La font és l'element al qual s'atribueix l'emissió lluminosa. Pot representar-se mitjançant una flama, un cristall, un nucli energètic o un altre element que actuï com a origen de l'efecte.

La superfície il·luminada és una part d'un altre objecte sobre la qual es representa la influència d'aquesta font.

Tots dos elements compleixen funcions diferents: la font estableix l'origen visual de la il·luminació; les superfícies pròximes en mostren els efectes, i l'entorn proporciona referències espacials i cromàtiques per integrar el conjunt.

Una font pot estar representada amb gran intensitat cromàtica i, tanmateix, no produir un efecte OSL convincent si els objectes pròxims no mostren cap influència lluminosa. De la mateixa manera, una superfície pot presentar una zona acolorida sense que existeixi una font identificable que en justifiqui l'aparició.

La coherència entre tots dos elements és fonamental.

### 17.2.2. Emissió lluminosa representada i color intens

Un color molt saturat o clar no constitueix per si mateix una representació d'emissió lluminosa.

Per suggerir que un element emet llum cal diferenciar-lo visualment de les superfícies que l'envolten. La representació pot recórrer a contrast respecte de l'entorn, intensitat cromàtica, diferències de valor, delimitació de la zona emissora i organització de les àrees il·luminades pròximes.

La font ha de conservar una identitat visual pròpia. Si s'integra completament amb el color de les superfícies circumdants, pot deixar de reconèixer-se com a element emissor.

En determinats efectes, la zona central de la font es pot representar amb un valor molt clar i una regió exterior més cromàtica. En altres casos, la distribució pot ser diferent segons la naturalesa de l'element i la intenció artística.

No existeix una distribució cromàtica universal per a totes les fonts lluminoses.

### 17.2.3. Il·luminació directa i reflexos

Una superfície il·luminada rep llum procedent d'una font, però no necessàriament presenta un reflex especular visible.

La il·luminació directa es pot representar mitjançant una modificació del valor i del color de la superfície. Un reflex especular, en canvi, depèn de la resposta direccional de la superfície i de la posició des de la qual s'observa.

Per tant, no s'ha de confondre una zona il·luminada per una font amb un reflex brillant d'aquesta mateixa font.

En una superfície mat, la influència lluminosa es pot representar mitjançant una modificació relativament àmplia de la seva aparença. En una superfície brillant, pot resultar adequat introduir un reflex més localitzat i definit.

La resposta concreta depèn del material, la caracterització general del qual es desenvolupa al capítol 6.

### 17.2.4. Llum directa i il·luminació indirecta

La llum d'una font pot arribar directament a una superfície o influir en altres zones després d'interactuar amb l'entorn.

Per a la representació OSL convé distingir:

- **Il·luminació directa:** efecte de la llum que arriba a una superfície des de la font representada sense que un altre objecte intermedi la bloquegi.
- **Il·luminació indirecta:** contribució lluminosa que es pot produir després d'interaccions amb altres superfícies de l'entorn.

En miniatures, la il·luminació indirecta es pot simplificar o fins i tot ometre quan la seva representació no aporta informació visual rellevant.

No obstant això, convé evitar que les zones no il·luminades directament es converteixin automàticament en regions d'obscuritat absoluta. La resta de la il·luminació de l'escena pot continuar afectant-les.

La decisió de representar il·luminació indirecta ha de respondre a la complexitat de l'escena i al nivell de detall que es vulgui aconseguir.

### 17.2.5. Abast i simplificació pictòrica

L'OSL representa una situació lluminosa mitjançant recursos pictòrics. No constitueix una simulació física exacta de la propagació de la llum.

L'escala de la miniatura, la distància d'observació i la necessitat de mantenir una lectura clara poden justificar modificacions respecte d'una il·luminació real.

Per exemple, pot ser convenient exagerar lleugerament el contrast d'una zona il·luminada, reduir l'extensió de l'efecte per evitar que afecti massa superfícies, simplificar les transicions, destacar la font amb més claredat o concentrar el color lluminós en les zones més rellevants.

Aquestes decisions han de conservar la relació espacial entre la font i els objectes il·luminats. La simplificació és adequada quan millora la lectura de l'efecte sense introduir contradiccions importants.

## 17.3. Identificació i planificació de les fonts lluminoses

### 17.3.1. Identificació de la font

Abans d'aplicar pintura és necessari identificar quin element actuarà com a origen de la il·luminació.

Convé determinar quina part de la miniatura emet llum, quines dimensions té la zona emissora, si la font està concentrada o distribuïda, si es representa com una font puntual o extensa, quina intensitat visual es pretén transmetre i quin color o combinació cromàtica en defineix l'aparença.

La identificació ha de ser prou precisa per relacionar la font amb les superfícies pròximes.

Si una miniatura conté diverses fonts lluminoses, convé analitzar-les per separat abans d'integrar-les en una mateixa composició.

### 17.3.2. Posició i direcció de la il·luminació

La posició de la font determina quines superfícies poden rebre directament la seva llum.

La planificació ha de considerar la ubicació respecte dels objectes i l'orientació de les diferents superfícies. Una font situada sota un rostre pot il·luminar zones diferents d'una altra col·locada per sobre o a un lateral.

De la mateixa manera, una font pròxima a una mà pot afectar els dits, el palmell i les parts del braç orientades cap a ella, però no necessàriament tota l'extremitat.

No n'hi ha prou d'identificar quins objectes són a prop de la font. També cal analitzar quines parts de les seves superfícies tenen una orientació i una exposició compatibles amb la il·luminació representada.

### 17.3.3. Distància i distribució de l'efecte

La influència visual d'una font sol disminuir quan augmenta la distància, encara que el comportament depèn de les condicions d'emissió, la geometria i l'entorn.

En pintura de miniatures, aquest principi s'ha d'utilitzar com a criteri de planificació, no com una regla que obligui a aplicar una reducció cromàtica idèntica a totes les superfícies.

Convé establir una jerarquia entre zones pròximes amb influència més evident, zones intermèdies amb una influència menor i zones allunyades amb una contribució reduïda o inexistent en la representació.

La distància no és l'únic factor. Una superfície pròxima pot quedar protegida per un altre objecte, mentre que una de més allunyada pot tenir exposició directa. La distribució ha de respondre al conjunt de relacions espacials.

### 17.3.4. Geometria i orientació de les superfícies

La geometria condiciona com es representa la influència d'una font sobre cada objecte.

En superfícies planes, la zona il·luminada pot presentar límits relativament definits si la font i la geometria ho justifiquen. En superfícies corbes, la influència pot distribuir-se de manera més progressiva. En superfícies facetades, els canvis d'orientació poden generar diferències entre plans pròxims.

També s'han de considerar les regions ocultes, les cavitats i les parts protegides per altres elements.

La il·luminació no s'ha d'estendre indiscriminadament sobre totes les superfícies properes. Ha de seguir una distribució compatible amb la seva orientació i exposició.

### 17.3.5. Bloqueig de la llum i ombres

Un objecte pot bloquejar totalment o parcialment la llum d'una font i impedir que arribi a determinades superfícies.

En la representació OSL, aquest bloqueig pot ser important per conservar la coherència de l'escena. Per exemple, si una mà sosté una esfera lluminosa, les parts orientades cap a l'esfera poden rebre'n la il·luminació, mentre que altres regions poden quedar parcialment protegides pels dits.

L'absència d'il·luminació directa s'ha de diferenciar de l'absència total de llum.

Les ombres i la seva formació general s'expliquen al capítol 5. Aquí s'utilitzen com a criteri per decidir on resulta coherent representar la influència de la font.

### 17.3.6. Esquema de planificació

Abans de pintar convé elaborar un esquema de distribució lluminosa. Es pot fer mitjançant un dibuix senzill o sobre una fotografia de la miniatura.

Ha d'identificar:

1. La font emissora.
2. La posició de la font respecte de la figura.
3. Les superfícies que reben llum directa.
4. Les superfícies parcialment protegides.
5. Les zones que no rebran una influència directa apreciable.
6. La intensitat relativa prevista per a cada regió.
7. Els possibles reflexos localitzats.
8. La relació cromàtica entre la font i l'entorn.

L'esquema no ha de representar tots els detalls. La seva funció és establir una referència coherent per al desenvolupament pictòric.

## 17.4. Planificació dels valors i organització cromàtica

### 17.4.1. Jerarquia de valors

La font lluminosa i les superfícies il·luminades han de mantenir una jerarquia visual recognoscible.

En molts plantejaments, la font constitueix el punt de màxima intensitat visual, mentre que les superfícies il·luminades presenten una influència progressivament menor. Aquesta organització ajuda a distingir l'origen de la llum dels seus efectes.

Tanmateix, no és necessari que totes les fonts presentin un centre blanc ni que totes les superfícies il·luminades siguin progressivament més fosques de manera uniforme. La jerarquia s'ha d'adaptar a la naturalesa de l'efecte i a la composició de la miniatura.

### 17.4.2. Organització de les zones il·luminades

La planificació tonal pot diferenciar diverses regions:

- Font emissora.
- Zona de màxima influència lluminosa.
- Zona d'influència intermèdia.
- Zona de transició cap a l'aparença original de la superfície.
- Superfícies sense influència directa apreciable.

Aquestes regions són referències funcionals, no categories obligatòries que hagin d'aparèixer sempre separades. La seva extensió i definició depenen de la geometria, la distància i el tipus de superfície.

La planificació ha d'evitar que tota la regió pròxima a la font presenti la mateixa intensitat. Una distribució massa uniforme pot produir un halo artificial i eliminar la lectura dels volums.

### 17.4.3. Selecció del color lluminós

La tria del color ha de respondre a la identitat de la font i a la intenció visual. Una flama, un cristall màgic o un dispositiu tecnològic poden utilitzar famílies cromàtiques diferents.

El color de la font no s'ha de reproduir necessàriament de manera idèntica en totes les superfícies il·luminades. En funció de l'efecte, es poden introduir modificacions de matís, valor i croma a mesura que es representa la influència lluminosa.

La teoria del color del capítol 4 proporciona els fonaments per organitzar aquestes relacions. Aquí s'apliquen a la representació d'una font emissora i dels seus efectes.

### 17.4.4. Relació entre el color de la font i el de les superfícies

El color de la llum representada interactua visualment amb el color propi de les superfícies. Per això, una mateixa font pot produir aparences diferents segons l'objecte il·luminat.

Una superfície de color clar pot mostrar una influència cromàtica lluminosa molt visible. Una superfície fosca pot requerir una modificació tonal més evident perquè l'efecte es reconegui. En altres casos, una superfície amb un color molt diferent del de la font pot mostrar una combinació cromàtica més complexa.

No s'ha de suposar que n'hi ha prou amb barrejar el color de la font amb el color base de cada objecte per obtenir una il·luminació convincent.

La representació exigeix valorar conjuntament el color local, el valor, la intensitat de l'efecte i la llegibilitat de la superfície.

### 17.4.5. Intensitat i pèrdua progressiva d'influència

La influència visual de la font s'ha de distribuir de manera coherent.

En termes generals, les regions més pròximes i exposades poden mostrar una modificació més intensa que les zones allunyades o parcialment protegides. Aquesta reducció no ha de ser lineal ni seguir una proporció fixa.

Es pot representar mitjançant canvis de valor, matís, croma o una combinació d'aquests. També pot variar segons la superfície: una zona mat pot presentar una influència àmplia, mentre que una superfície brillant pot mostrar un reflex més localitzat.

La pèrdua progressiva d'influència s'ha d'integrar amb el color original de la superfície, sense convertir necessàriament tota la regió il·luminada en una única taca cromàtica.

### 17.4.6. Coherència amb la il·luminació general

La font OSL s'ha d'integrar en la il·luminació general de la miniatura.

Si la figura presenta una il·luminació principal procedent d'una direcció i una font secundària situada en una altra posició, totes dues poden coexistir. La representació ha d'establir una jerarquia entre elles.

La font secundària pot modificar determinades superfícies sense substituir completament la il·luminació principal. Convé revisar que les zones afectades per totes dues fonts no generin contradiccions visuals difícils d'interpretar.

En alguns casos pot ser convenient simplificar la il·luminació general perquè l'efecte OSL es percebi amb claredat.

## 17.5. Procediment general de construcció de l'OSL

### 17.5.1. Preparació i anàlisi de la miniatura

El procés comença amb una superfície preparada i una il·luminació general prèviament considerada. La preparació de la miniatura, les eines i les pintures correspon al capítol 7.

Abans d'aplicar l'efecte convé identificar la font, la seva posició i les superfícies que rebran la seva influència. També cal comprovar que la distribució prevista no contradigui elements importants de la geometria.

### 17.5.2. Establiment de la font emissora

La font s'ha de construir de manera que es reconegui com a origen de l'efecte lluminós.

La representació pot incloure una zona central i altres regions cromàtiques al seu voltant, segons la naturalesa de l'element. La distribució ha de mantenir una jerarquia pròpia i diferenciar-se de les superfícies il·luminades.

En una flama, per exemple, l'organització interna pot respondre a la representació del foc. En un cristall màgic, es pot utilitzar una distribució més localitzada o estilitzada.

El capítol 30 desenvolupa la representació específica del foc, el fum i les cendres. El capítol 32 aborda la màgia, l'energia i altres efectes sobrenaturals. Aquí es considera únicament la funció de la font com a origen de la il·luminació.

### 17.5.3. Identificació de les superfícies receptores

Un cop establerta la font, cal identificar les superfícies sobre les quals es representarà la seva influència.

La selecció ha de considerar la distància respecte de la font, l'orientació de cada superfície, l'exposició directa, els possibles obstacles, la geometria i el material representat.

Convé limitar inicialment l'efecte a les regions més justificades. Ampliar-lo després resulta més senzill que haver de recuperar grans zones de color original si la il·luminació s'ha estès massa.

### 17.5.4. Aplicació de la influència lluminosa

La il·luminació es construeix modificant visualment les superfícies receptores.

Es pot recórrer a una aplicació localitzada o a una distribució més àmplia, segons la geometria i la intensitat prevista. La zona il·luminada no ha de cobrir necessàriament tota la superfície receptora. Convé conservar part de la informació del color original i dels volums.

L'efecte es pot desenvolupar mitjançant aplicacions successives, procurant que la modificació cromàtica mantingui una relació progressiva amb la zona il·luminada.

El capítol 8 explica la construcció mitjançant capes; el capítol 9 desenvolupa els degradats i les transicions, i el capítol 10 aborda les veladures i els glassejats. Aquests procediments s'apliquen aquí amb una finalitat específica: representar la influència de la font lluminosa.

No s'estableix un nombre obligatori d'aplicacions ni una proporció universal de dilució.

### 17.5.5. Construcció de les zones de transició

La transició permet integrar la influència lluminosa amb l'aparença original de la superfície. Pot ser àmplia o localitzada, contínua o relativament definida. La seva extensió ha de respondre a la geometria i a la distribució de l'efecte.

Una transició massa brusca pot fer que la il·luminació sembli una taca superficial. Una transició excessivament àmplia pot convertir tota la peça en una superfície acolorida sense una relació clara amb la font.

No és necessari suavitzar tots els límits. En determinades superfícies poden existir canvis definits d'il·luminació.

### 17.5.6. Representació de reflexos localitzats

Algunes superfícies poden mostrar reflexos més intensos o definits de la font. Aquests reflexos s'han de diferenciar de la il·luminació general de la superfície.

La seva representació pot ser especialment rellevant en materials brillants, polits o amb una resposta especular marcada.

La posició ha de ser compatible amb l'orientació de la superfície i amb la posició de l'observador. No totes les superfícies il·luminades necessiten un reflex localitzat. Incorporar-lo indiscriminadament pot generar punts de brillantor que no contribueixen a la coherència de l'efecte.

### 17.5.7. Integració de la font i l'entorn

Un cop construïda la il·luminació sobre les superfícies receptores, convé revisar el conjunt.

La font ha de continuar sent recognoscible i les superfícies il·luminades han de mostrar una influència compatible amb la seva posició.

Pot ser necessari ajustar la intensitat de la font, l'extensió de les zones il·luminades, el contrast entre la font i l'entorn, la transició cap als colors originals, la definició dels reflexos i la relació amb la il·luminació general.

La integració no consisteix a acolorir totes les superfícies pròximes, sinó a aconseguir que la font i els seus efectes formin una mateixa situació lluminosa.

## 17.6. Adaptació a diferents geometries i materials

### 17.6.1. Superfícies planes

En superfícies planes, la il·luminació es pot representar mitjançant regions relativament definides, sempre que la posició de la font i l'orientació de la peça ho justifiquin.

Convé identificar quines parts del pla reben directament la llum i quines queden protegides. L'extensió de la zona il·luminada s'ha d'adaptar a la superfície i evitar cobrir-la uniformement sense considerar-ne l'orientació.

### 17.6.2. Superfícies corbes

Les superfícies corbes presenten canvis continus d'orientació. Per això, la influència lluminosa pot requerir una distribució progressiva que segueixi la forma.

En una esfera, per exemple, la zona il·luminada es pot concentrar en una regió orientada cap a la font i disminuir cap a altres àrees. En una superfície cilíndrica, la distribució pot adaptar-se al recorregut de la curvatura.

No s'ha d'aplicar automàticament el mateix patró a totes les superfícies corbes.

### 17.6.3. Superfícies facetades i arestes

Les superfícies facetades presenten canvis d'orientació més definits. Una mateixa font pot afectar de manera diferent dos plans pròxims.

La representació pot conservar aquests canvis mitjançant regions d'il·luminació diferenciades. Les arestes poden mostrar una influència més visible si la seva orientació i exposició ho justifiquen, però no s'han d'il·luminar totes per defecte.

La geometria ha de continuar sent recognoscible.

### 17.6.4. Superfícies mates

Les superfícies mates es poden representar mitjançant una influència lluminosa distribuïda de manera relativament àmplia, sense dependre necessàriament de reflexos especulars intensos.

L'efecte es pot construir mitjançant canvis de valor i color que mantinguin visible l'estructura de la superfície.

No convé convertir una zona mat en una superfície brillant únicament per utilitzar-hi un color molt clar.

### 17.6.5. Superfícies brillants i reflectants

Les superfícies brillants poden mostrar reflexos més localitzats i definits.

En aquests casos, la representació pot combinar una zona il·luminada amb un reflex de la font. Tots dos elements han de mantenir funcions diferenciades.

Una superfície brillant no ha de presentar sempre un reflex visible des de qualsevol posició. La seva aparició depèn de la relació entre font, superfície i observador.

### 17.6.6. Superfícies transparents i translúcides

Els materials transparents i translúcids poden requerir una representació específica de la font i de la llum que els travessa o dispersa.

La il·luminació pot modificar-ne l'aparença interna, generar zones de més intensitat o influir sobre els objectes pròxims.

La construcció general d'aquests materials correspon al capítol 14. En l'OSL es considera la seva possible funció com a font o com a superfície receptora.

No s'ha de confondre la il·luminació que travessa un material amb un simple reflex de la seva superfície.

### 17.6.7. Adaptació a l'escala

En miniatures petites, la distribució de l'efecte s'ha de simplificar per conservar-ne la llegibilitat.

Pot ser necessari reduir el nombre de superfícies il·luminades, concentrar els accents i limitar l'extensió de les transicions.

En peces més grans es pot incorporar una distribució més complexa, sempre que contribueixi a la lectura de l'efecte.

La finalitat no és reproduir tots els matisos d'una escena real, sinó seleccionar els senyals visuals necessaris per representar una font i la seva influència.

## 17.7. Control tècnic i avaluació del resultat

### 17.7.1. Coherència entre la font i les superfícies il·luminades

La primera comprovació consisteix a verificar que les zones il·luminades es poden relacionar amb la font.

Convé revisar si la font està clarament identificada, si les superfícies receptores es troben en posicions compatibles, si l'orientació justifica la distribució, si hi ha obstacles que haurien de bloquejar part de la llum i si l'extensió de l'efecte resulta raonable dins de l'escena.

Una zona il·luminada sense relació espacial recognoscible pot debilitar el conjunt.

### 17.7.2. Control de la jerarquia visual

La font i les superfícies il·luminades han de conservar funcions visuals diferenciades.

Cal comprovar si la font destaca com a origen de la llum, si les superfícies receptores mostren una influència menor o diferent, si els accents no competeixen innecessàriament amb la font i si l'efecte manté una jerarquia clara respecte de la resta de la miniatura.

No és obligatori que la font sigui sempre l'element més clar de tota la composició, però la seva funció emissora ha de resultar recognoscible.

### 17.7.3. Control de la distribució cromàtica

La influència lluminosa s'ha d'integrar amb els colors originals de les superfícies.

Convé revisar si el color de la font manté la seva identitat, si les superfícies il·luminades presenten modificacions cromàtiques coherents, si les transicions conserven l'aparença del material, si el color lluminós s'ha estès excessivament i si el resultat conserva prou diferenciació tonal.

La il·luminació no ha de convertir tots els objectes pròxims en superfícies del mateix color.

### 17.7.4. Control de la intensitat i l'extensió

La intensitat visual ha de mantenir una relació coherent amb la posició i l'exposició de les superfícies.

Una zona allunyada o protegida no hauria de presentar automàticament la mateixa influència que una altra de pròxima i directament exposada.

Convé comprovar si la distribució manté una pèrdua d'intensitat comprensible i si hi ha regions en què l'efecte s'hauria de reduir o desaparèixer.

L'extensió de l'OSL s'ha de limitar a les zones que aporten informació rellevant.

### 17.7.5. Control de la geometria i el volum

L'aplicació del color lluminós no ha d'eliminar la lectura dels objectes.

Cal revisar si es reconeixen els plans i les curvatures, si les zones il·luminades segueixen la forma de les superfícies, si es mantenen les diferències entre regions exposades i protegides, si les transicions no oculten detalls importants i si l'efecte respecta l'estructura general de la miniatura.

Una il·luminació excessivament uniforme pot fer que els objectes semblin coberts per una capa de color en lloc d'estar il·luminats.

### 17.7.6. Avaluació global de l'OSL

La revisió ha de considerar conjuntament la font, les superfícies receptores i l'entorn.

| Criteri | Resultat esperat |
|---|---|
| Identificació de la font | L'element emissor es reconeix clarament. |
| Coherència espacial | La distribució respon a la posició de la font. |
| Exposició | Les zones il·luminades són compatibles amb l'orientació i els obstacles. |
| Jerarquia | Es distingeix la font de les superfícies receptores. |
| Intensitat | La influència lluminosa presenta una distribució comprensible. |
| Integració cromàtica | L'efecte es relaciona amb els colors originals de les superfícies. |
| Geometria | La il·luminació conserva la lectura dels volums. |
| Materials | La resposta representada resulta compatible amb les superfícies. |
| Coherència global | L'efecte s'integra en la il·luminació general de la miniatura. |

### 17.7.7. Criteri de finalització

L'efecte es pot considerar acabat quan la font es reconeix, les superfícies receptores mostren una influència coherent i la il·luminació s'integra amb l'escena sense perjudicar la lectura dels objectes.

No és necessari estendre el color a totes les zones pròximes ni afegir reflexos a cada superfície. Les intervencions addicionals poden reforçar l'efecte, però també poden convertir-lo en una distribució cromàtica excessiva.

La prioritat és mantenir una relació clara entre l'origen de la llum i les seves conseqüències visuals.

## 17.8. Errors freqüents i procediments de correcció

### 17.8.1. Crear un halo sense una font identificable

El color es distribueix al voltant d'una zona, però no queda clar quin element emet la llum.

**Correcció:** definir i reforçar visualment la font abans d'ampliar-ne la influència sobre les superfícies pròximes.

### 17.8.2. Il·luminar indiscriminadament tots els objectes propers

L'efecte s'estén per proximitat sense considerar orientació, geometria o obstacles.

**Correcció:** revisar les superfícies receptores i limitar la il·luminació a les regions l'exposició de les quals resulti coherent.

### 17.8.3. Confondre la font amb la superfície il·luminada

La font i les zones receptores presenten la mateixa intensitat i aparença cromàtica.

**Correcció:** establir una jerarquia visual que permeti reconèixer l'element emissor i diferenciar-ne els efectes.

### 17.8.4. Utilitzar el color de la font sense modificar els valors

La superfície es cobreix amb un color lluminós, però no mostra una modificació tonal que suggereixi il·luminació.

**Correcció:** revisar els valors de les superfícies receptores i construir una relació entre la seva aparença original i la influència lluminosa.

### 17.8.5. Estendre massa la il·luminació

L'efecte ocupa regions allunyades o protegides sense una justificació visual clara.

**Correcció:** reduir-ne l'extensió i establir una distribució més selectiva.

### 17.8.6. Distribuir l'efecte de manera uniforme

Totes les superfícies presenten una intensitat i una extensió semblants.

**Correcció:** diferenciar les regions segons la seva posició, orientació i exposició.

### 17.8.7. Perdre la geometria dels objectes

L'aplicació cromàtica cobreix plans, detalls i curvatures fins a dificultar la lectura de la forma.

**Correcció:** recuperar selectivament l'estructura tonal i ajustar la il·luminació a la geometria.

### 17.8.8. Confondre il·luminació i reflex

Totes les superfícies il·luminades reben punts o línies de brillantor intensa, independentment de les seves característiques.

**Correcció:** diferenciar la il·luminació general dels reflexos localitzats i reservar aquests últims per a les superfícies i orientacions que els justifiquin.

### 17.8.9. Utilitzar transicions excessivament brusques

Les zones il·luminades apareixen com a taques aïllades sense integració amb el color original.

**Correcció:** revisar la transició entre regions i adaptar-la a la geometria i al tipus de superfície.

### 17.8.10. Suavitzar totes les transicions en excés

La il·luminació perd definició i es converteix en una zona cromàtica extensa i poc estructurada.

**Correcció:** recuperar els límits i contrastos necessaris per mantenir la lectura dels volums.

### 17.8.11. Confondre emissió lluminosa amb color saturat

La font presenta un color intens, però no destaca respecte de l'entorn ni transmet una aparença emissora.

**Correcció:** revisar la jerarquia de valors, el contrast amb l'entorn i la definició de la zona emissora.

### 17.8.12. Introduir diverses fonts sense jerarquia

La miniatura conté diferents elements lluminosos, però els seus efectes se superposen sense una organització clara.

**Correcció:** analitzar cada font per separat, establir-ne la importància i revisar posteriorment la interacció entre elles.

## 17.9. Resultat esperat i criteris d'avaluació

El resultat esperat és una representació en què una font lluminosa es pugui identificar com a origen d'un efecte i les superfícies pròximes mostrin una influència visual compatible amb la seva posició i geometria.

| Criteri | Resultat esperat |
|---|---|
| Identificació de la font | L'element emissor es reconeix clarament. |
| Coherència espacial | La distribució respon a la posició de la font. |
| Exposició | Les zones il·luminades són compatibles amb l'orientació i els obstacles. |
| Jerarquia | Es distingeix la font de les superfícies receptores. |
| Intensitat | La influència lluminosa presenta una distribució comprensible. |
| Integració cromàtica | L'efecte es relaciona amb els colors originals de les superfícies. |
| Geometria | La il·luminació conserva la lectura dels volums. |
| Materials | La resposta representada resulta compatible amb les superfícies. |
| Coherència global | L'efecte s'integra en la il·luminació general de la miniatura. |

L'OSL no s'ha d'avaluar per la quantitat de color lluminós aplicada ni per l'extensió del halo. La seva qualitat depèn de la coherència entre la font, les superfícies receptores i l'entorn.

La simplificació pot ser necessària per millorar la lectura, però ha de mantenir una lògica espacial recognoscible.

## 17.10. Exercicis pràctics

Els exercicis permeten practicar l'anàlisi de la font, la selecció de les superfícies receptores i la planificació de la influència lluminosa abans de construir l'efecte complet.

### 17.10.1. Identificació de la font i les superfícies receptores

**Objectiu:** diferenciar la font emissora de les superfícies que reben la seva llum.

**Procediment:**
1. Seleccionar una miniatura o composició senzilla amb un element que pugui actuar com a font.
2. Identificar i delimitar la font.
3. Assenyalar les superfícies que podrien rebre'n la influència.
4. Distingir les regions exposades de les que quedarien protegides per la geometria.
5. Justificar la selecció de cada superfície receptora.

**Resultat esperat:** una identificació clara de l'origen de la llum i de les superfícies afectades.

### 17.10.2. Planificació d'una font situada en diferents posicions

**Objectiu:** comprendre com la posició de la font modifica la distribució de la il·luminació.

**Procediment:**
1. Utilitzar una mateixa figura.
2. Plantejar tres ubicacions diferents per a la font: superior, lateral i inferior.
3. Dibuixar la distribució prevista de les superfícies il·luminades en cada situació.
4. Identificar els canvis d'exposició i les zones protegides.
5. Comparar la lectura de la figura en els tres esquemes.

**Resultat esperat:** reconèixer la influència de la posició i l'orientació sobre la planificació de l'efecte.

### 17.10.3. Distribució de la intensitat lluminosa

**Objectiu:** planificar una pèrdua progressiva d'influència sense recórrer a una distribució uniforme.

**Procediment:**
1. Seleccionar una font i una superfície receptora.
2. Elaborar un esquema amb zones de màxima influència, influència intermèdia i absència d'il·luminació directa apreciable.
3. Considerar la distància, l'orientació i els obstacles.
4. Revisar que la distribució no segueixi una proporció fixa aplicada indiscriminadament.
5. Comparar el resultat amb una distribució uniforme.

**Resultat esperat:** una planificació selectiva de la intensitat i l'extensió de l'efecte.

### 17.10.4. Influència de la geometria

**Objectiu:** adaptar la distribució de l'OSL a superfícies amb geometries diferents.

**Procediment:**
1. Preparar diverses superfícies de prova: plana, corba i facetada.
2. Situar una mateixa font respecte de cadascuna.
3. Planificar les regions exposades i protegides.
4. Representar les diferències de distribució.
5. Comparar com la geometria modifica l'aparença de la il·luminació.

**Resultat esperat:** comprendre que la forma i l'orientació condicionen la influència lluminosa.

### 17.10.5. Comparació entre il·luminació i reflex

**Objectiu:** diferenciar una zona il·luminada d'un reflex localitzat.

**Procediment:**
1. Seleccionar dues superfícies amb respostes visuals diferents.
2. Representar en una zona mate una influència lluminosa de distribució àmplia.
3. Representar en una superfície brillant un reflex més localitzat.
4. Comparar la funció visual de tots dos recursos.
5. Revisar si els reflexos estan justificats per la geometria i la posició de l'observador.

**Resultat esperat:** evitar que totes les superfícies il·luminades es representin mitjançant punts o línies de brillantor.

### 17.10.6. Exercici integrador: construcció d'un efecte OSL

**Objectiu:** integrar els criteris del capítol en una representació completa d'una font i els seus efectes.

**Procediment:**
1. Seleccionar una miniatura amb un element que pugui actuar com a font lluminosa.
2. Identificar i delimitar la font.
3. Determinar-ne la posició i l'orientació.
4. Seleccionar les superfícies receptores.
5. Identificar possibles obstacles.
6. Establir la jerarquia de valors.
7. Seleccionar l'organització cromàtica.
8. Construir l'aparença de la font.
9. Aplicar-ne la influència sobre les superfícies receptores.
10. Integrar les transicions i els possibles reflexos.
11. Comprovar la coherència amb la geometria i la il·luminació general.
12. Corregir les zones que presentin contradiccions.
13. Avaluar el resultat des de la distància habitual d'observació.

**Resultat esperat:** una representació en què la font sigui recognoscible i les superfícies receptores mostrin una influència coherent amb la situació espacial plantejada.

## Síntesi del capítol

L'OSL representa una font emissora i la influència que exerceix sobre les superfícies pròximes. La coherència depèn de la relació espacial entre font, orientació, exposició, obstacles, geometria i material. El procediment exigeix identificar la font, seleccionar les superfícies receptores, planificar valors i colors, aplicar la influència de manera selectiva i integrar-la amb la il·luminació general. No equival a crear un halo: la qualitat depèn de la relació recognoscible entre l'origen de la llum i les seves conseqüències visuals.
