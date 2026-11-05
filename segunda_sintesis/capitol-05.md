# 5. LLUM, VOLUM, OMBRES I REFLEXOS

## 5.1. Llum, percepció i representació pictòrica

La llum permet percebre els objectes, reconèixer-ne els contorns i interpretar l'orientació de les superfícies, el volum i la posició a l'espai. En pintura de miniatures, comprendre'n la distribució és fonamental per representar la tridimensionalitat sobre una superfície plana.

Cal distingir tres nivells:
- **Il·luminació:** llum que arriba a una superfície, directament des d'una font o després d'interactuar amb l'entorn.
- **Aparença visual:** informació lluminosa que arriba a l'observador i permet interpretar l'objecte.
- **Representació pictòrica:** interpretació que el pintor construeix mitjançant llums, ombres, reflexos i contrastos.

Aquests nivells estan relacionats, però no són equivalents. L'aparença depèn de la font, la geometria i les propietats de les superfícies, l'entorn i la posició de l'observador. La representació, en canvi, és una decisió artística: pot simplificar transicions o reforçar contrastos per millorar la lectura de la figura, sempre que mantingui una organització visual coherent.

## 5.2. Fonts lluminoses i propagació de la llum

En un medi homogeni i transparent, la llum es pot aproximar mitjançant trajectòries rectilínies. Aquest principi de l'òptica geomètrica permet analitzar com arriba des d'una font fins a un objecte i com altres elements en poden bloquejar el recorregut.

### 5.2.1. Fonts puntuals i extenses

La classificació depèn de la mida aparent de la font respecte de l'objecte:
- **Font puntual:** les dimensions de la font es poden negligir en relació amb la distància. Una llum petita i allunyada pot aproximar-s'hi.
- **Font extensa:** les dimensions aparents són apreciables i diferents parts de la font poden il·luminar des de direccions pròximes. Una finestra o un panell lluminós en són exemples.

Una font puntual ideal pot generar límits d'ombra definits; una d'extensa sol produir transicions i regions de penombra perquè pot quedar bloquejada parcialment. No n'hi ha prou amb considerar la mida física de la làmpada: cal tenir en compte també la distància a l'objecte.

### 5.2.2. Magnituds fotomètriques

Les magnituds següents descriuen aspectes diferents de la llum i no són intercanviables:

| Magnitud | Unitat | Significat |
|---|---|---|
| Flux lluminós | lumen (lm) | Quantitat de llum emesa o transferida per unitat de temps, ponderada segons la sensibilitat visual fotòpica estàndard. |
| Intensitat lluminosa | candela (cd) | Flux lluminós distribuït per unitat d'angle sòlid en una direcció. |
| Il·luminància | lux (lx) | Flux lluminós incident per unitat de superfície. |
| Luminància | cd/m² | Intensitat lluminosa per unitat d'àrea projectada, en una direcció determinada. |

La luminància és una magnitud fotomètrica física i no s'ha de confondre amb la brillantor percebuda, que també depèn de l'adaptació visual i del context. Tampoc no equival al valor cromàtic estudiat al capítol 4.

### 5.2.3. Distància i llei de l'invers del quadrat

Per a una font puntual, la il·luminància disminueix aproximadament amb el quadrat de la distància:

\[
E\propto\frac{1}{d^2}
\]

Així, duplicar la distància redueix la il·luminància a una quarta part; triplicar-la, a una novena part. La llei correspon estrictament al model puntual. En fonts de mida finita només és una aproximació vàlida quan la distància és prou gran respecte de les dimensions de la font. No s'ha d'aplicar indiscriminadament a qualsevol configuració.

Cal separar aquest efecte del de l'orientació: una superfície pot rebre menys llum perquè és més lluny o perquè està orientada de manera menys favorable.

### 5.2.4. Mida aparent de la font

Una font gran i pròxima pot presentar un angle visual considerable i produir transicions d'ombra més àmplies. Una font petita o molt allunyada pot generar límits més definits. Una font extensa pot quedar parcialment bloquejada i il·luminar des de diferents direccions pròximes. El resultat depèn també de la geometria de l'objecte i de la posició de la font.

## 5.3. Geometria de la il·luminació

La il·luminació depèn de la direcció d'arribada de la llum i de l'orientació de cada superfície. Un pla manté una orientació constant; una superfície corba la modifica progressivament.

### 5.3.1. Plans, superfícies corbes i normals

La **normal geomètrica** és una línia imaginària perpendicular a una superfície en un punt. Permet descriure'n l'orientació i mesurar els angles d'incidència i reflexió; no és un raig de llum ni una trajectòria de propagació. En un pla, la normal manté la mateixa direcció; en una superfície corba, varia segons el punt.

Aquesta diferència ajuda a explicar per què la il·luminació pot distribuir-se de manera relativament uniforme sobre un pla i variar progressivament sobre una corba.

### 5.3.2. Angle d'incidència i llei del cosinus

L'angle d'incidència es mesura entre la direcció d'arribada de la llum i la normal, no respecte del pla. Quan la llum arriba perpendicularment a la superfície, l'angle és de 0°. Com més obliqua és la incidència, menor és la il·luminància rebuda per unitat de superfície.

Per a una font puntual, la contribució directa es pot expressar com:

\[
E=\frac{I\cos\theta}{r^2}
\]

On (E) és la il·luminància (lux), (I) la intensitat lluminosa en la direcció del punt (candeles), (r) la distància (metres) i \(\theta\) l'angle entre la normal i la direcció d'il·luminació. L'expressió combina la disminució amb el quadrat de la distància i la reducció per incidència obliqua. No incorpora automàticament fonts extenses, altres fonts, llum indirecta ni tota la interacció amb el material; cal justificar-ne l'ús com a aproximació.

## 5.4. Interacció de la llum amb les superfícies

Quan la llum arriba a un material, una part pot ser absorbida, reflectida o transmesa, simultàniament i en proporcions variables:
- **Absorció:** l'energia radiant és absorbida pel material i es transforma en altres formes d'energia.
- **Reflexió:** la radiació canvia de direcció i torna al medi d'origen.
- **Transmissió:** una part travessa el material i continua propagant-se.

Una superfície opaca pot absorbir i reflectir llum sense transmetre'n una quantitat apreciable. Els materials transparents en transmeten una part important; els translúcids la transmeten dispersant-la.

### 5.4.1. Reflexió especular i difusa

- **Reflexió especular o regular:** la llum es reflecteix en una direcció determinada per la geometria de la superfície. En el model ideal, l'angle de reflexió és igual al d'incidència, tots dos mesurats respecte de la normal.
- **Reflexió difusa:** la llum reflectida es distribueix en diverses direccions i no genera necessàriament una imatge definida de l'entorn.

Les superfícies reals poden combinar components especulars i difuses; són models de comportament, no categories absolutament separades. La dispersió i les reflexions múltiples també modifiquen la distribució de la llum abans que arribi a l'observador.

### 5.4.2. Il·luminació directa, indirecta i ambiental

- **Directa:** arriba des d'una font sense interaccions intermèdies amb altres superfícies.
- **Indirecta:** arriba després d'interactuar amb elements de l'entorn, com ara parets, terra o objectes que reflecteixen part de la radiació.
- **Ambiental:** expressió descriptiva per a la contribució lluminosa general de l'entorn, que pot provenir de diverses fonts i reflexions. No és necessàriament una font física única ni una magnitud fotomètrica independent.

El cel és una font extensa a l'exterior; a l'interior, parets, sostres, terres i altres elements contribueixen a la il·luminació general. Una superfície protegida de la font principal pot continuar rebent llum indirecta. Per tant, una regió en ombra no ha de ser necessàriament foscor absoluta.

## 5.5. Formació i distribució de les ombres

Les ombres apareixen quan un objecte o una part seva bloqueja totalment o parcialment l'arribada de llum des d'una font determinada. La seva forma i distribució depenen de la geometria de l'objecte, la posició i la mida aparent de la font lluminosa, l'orientació de les superfícies i la presència d'altres contribucions d'il·luminació.

Les ombres aporten informació espacial important: permeten reconèixer la posició relativa dels objectes, identificar-ne els volums i comprendre quins elements bloquegen la llum.

### 5.5.1. Bloqueig i oclusió de la llum

Quan un objecte s'interposa en el recorregut de la llum, pot impedir que aquesta arribi a determinades regions. Aquest fenomen s'anomena bloqueig o oclusió de la llum.

L'oclusió depèn de la relació espacial entre la font lluminosa, l'objecte que bloqueja la llum i la superfície sobre la qual es produeix l'ombra. Un mateix objecte pot projectar ombres diferents si canvia la posició de la font o es modifica la relació geomètrica entre els elements.

### 5.5.2. Ombra pròpia i ombra projectada

Cal diferenciar dos tipus d'ombres:

- **Ombra pròpia:** regió d'un objecte que no rep il·luminació directa d'una font determinada a causa de la seva geometria. Apareix en les parts que queden orientades de manera desfavorable respecte de la font o protegides per altres parts del mateix objecte.
- **Ombra projectada:** apareix sobre una superfície quan un objecte bloqueja l'arribada de llum procedent d'una font. Pot projectar-se sobre el terra, una paret, un altre objecte o qualsevol superfície situada en la trajectòria de la llum.

L'ombra pròpia forma part de l'objecte i contribueix a interpretar-ne el volum. La projectada apareix sobre una altra superfície. La seva forma i posició depenen de la geometria de l'objecte que la genera, de la superfície receptora i de la posició de la font lluminosa.

### 5.5.3. Umbra i penombra

La formació de les ombres també depèn de la mida aparent de la font lluminosa. Quan una font extensa queda parcialment bloquejada poden aparèixer diferents regions:

- **Umbra:** regió en què la font lluminosa queda completament oculta.
- **Penombra:** regió en què la font queda bloquejada només parcialment.

La transició entre aquestes regions depèn de la geometria de la font, de l'objecte que bloqueja la llum i de la posició de la superfície receptora. Una font puntual ideal pot produir ombres amb límits definits. Una font extensa acostuma a generar zones de transició perquè diferents parts de la font poden quedar ocultes parcialment.

### 5.5.4. Mida, direcció i extensió de les ombres

La direcció d'una ombra projectada depèn de la posició de la font lluminosa respecte de l'objecte i de la superfície receptora.

La seva mida i extensió depenen de la geometria relativa entre la font, l'objecte i la superfície sobre la qual es projecta. Quan canvia la posició de la font, l'ombra pot modificar la direcció, la longitud i la forma.

També hi influeix la mida aparent de la font. Una font extensa pot generar límits més graduals, mentre que una font petita o puntual pot produir ombres més definides. No hi ha, per tant, una forma d'ombra única associada a cada objecte: la seva aparença depèn de les condicions d'il·luminació.

### 5.5.5. Ombres de contacte i oclusió geomètrica

Les ombres de contacte apareixen en regions on dues superfícies es troben molt pròximes o entren en contacte. En aquestes zones, la geometria dificulta que la llum arribi a determinats espais. Es poden observar, per exemple:

- A la unió entre un objecte i el terra.
- Entre diferents parts d'una figura.
- En cavitats i separacions estretes.
- En zones on diversos elements queden molt pròxims.

La seva intensitat depèn de la geometria, de la proximitat entre les superfícies i de la quantitat d'il·luminació directa i indirecta que pot arribar a la regió.

L'expressió «ombra de contacte» s'utilitza aquí com a descripció d'una regió d'ombra associada a la proximitat i l'oclusió entre superfícies, no com una categoria fotomètrica independent. No s'ha de confondre amb una zona necessàriament mancada d'il·luminació.

### 5.5.6. Influència de la il·luminació indirecta en les ombres

La il·luminació indirecta pot arribar a regions que no reben llum directa. Com a conseqüència, les ombres poden conservar una certa il·luminació procedent de l'entorn.

La diferència entre una regió il·luminada directament i una altra que rep únicament llum indirecta depèn de les condicions de l'escena. En un espai envoltat de superfícies reflectants, les ombres poden presentar una il·luminació secundària apreciable. En un entorn amb poques superfícies capaces de reflectir-hi llum, aquesta contribució pot ser menor.

Les ombres s'han d'interpretar, per tant, com a regions on s'ha reduït la contribució de determinades fonts lluminoses, no necessàriament com a espais sense il·luminació.

## 5.6. Reflexos i posició de l'observador

Els reflexos formen part de la informació visual de les superfícies. Depenen de la direcció d'arribada de la llum, de l'orientació de la superfície i de la posició de l'observador. En una reflexió especular, el reflex és visible només des de determinades relacions angulars i pot desaparèixer quan l'observador es desplaça. En una superfície amb reflexió difusa important, l'aparença pot variar menys amb el punt de vista.

Les superfícies poden reflectir tant les fonts lluminoses com els elements de l'entorn. El reflex no ha de ser necessàriament un punt brillant: pot ocupar una regió extensa i contenir informació sobre l'entorn.

Cal distingir:
- **Zona il·luminada:** superfície que rep llum.
- **Reflex visible:** llum reflectida que arriba a l'observador.

Una superfície pot estar il·luminada sense mostrar un reflex especular definit. Per tant, no totes les zones il·luminades s'han de representar com a reflexos.

## 5.7. Construcció visual del volum

La distribució de la llum aporta informació sobre la geometria, l'orientació, la curvatura i la profunditat. En els plans, l'orientació constant pot afavorir una il·luminació relativament uniforme; les diferències entre plans adjacents ajuden a reconèixer canvis d'orientació. En superfícies corbes, la normal canvia progressivament i pot generar transicions que suggereixen curvatura. Tanmateix, un degradat també pot aparèixer en un pla per variacions de distància, ombres parcials o il·luminació no uniforme: no demostra per si sol que la superfície sigui corba.

La percepció del volum integra diverses senyals:
- Distribució de llums i ombres.
- Canvis d'orientació i curvatura.
- Reflexos i transicions.
- Contorns i límits.
- Superposició i relacions espacials.

El sombreig és una senyal important, però s'interpreta en funció de la direcció de llum que pressuposa l'observador i de les altres dades visuals. La pintura de miniatures trasllada un objecte tridimensional a una superfície bidimensional: el pintor pot simplificar transicions i reforçar contrastos per fer més llegible el volum. Aquesta simplificació és una decisió artística, no necessàriament una reconstrucció física literal, però ha de mantenir una lògica recognoscible.

## 5.8. Anàlisi i planificació de la il·luminació en miniatures

Els principis anteriors permeten analitzar la informació lluminosa d'una miniatura abans de prendre decisions pictòriques. L'objectiu d'aquest apartat no és ensenyar una tècnica concreta d'il·luminació, sinó establir un procediment d'observació que ajudi a comprendre la geometria i la distribució de la llum sobre un objecte tridimensional. L'aplicació tècnica d'aquests fonaments es desenvolupa en els capítols posteriors dedicats a la planificació de valors i als procediments específics de pintura.

### 5.8.1. Identificació de la font lluminosa

L'anàlisi comença identificant les condicions generals d'il·luminació de l'objecte. Convé observar:

- La direcció principal des de la qual arriba la llum.
- La mida aparent de la font.
- La distància aproximada respecte de l'objecte.
- La presència d'altres fonts o contribucions ambientals.
- L'existència de superfícies pròximes que puguin reflectir llum.
- La posició des de la qual s'observa l'objecte.

Aquesta observació estableix un marc de referència per interpretar les zones il·luminades, les ombres i els reflexos. Quan la il·luminació és complexa, pot resultar útil simplificar inicialment l'anàlisi i reconèixer una font principal, sense ignorar que hi ha altres contribucions.

### 5.8.2. Identificació de plans, arestes, relleus i concavitats

Un cop reconegudes les condicions d'il·luminació, cal observar la geometria de l'objecte. S'hi poden identificar:

- Plans principals.
- Superfícies corbes.
- Arestes i canvis d'orientació.
- Relleus i sortints.
- Concavitats i regions protegides de la llum directa.
- Zones on apareixen ombres pròpies.
- Superfícies sobre les quals es projecten ombres.
- Regions de contacte i oclusió.

Aquesta identificació permet comprendre per què unes zones reben més il·luminació directa que altres i com s'organitza el volum de l'objecte.

En una miniatura, les dimensions reduïdes i la presència de molts detalls poden dificultar-ne la interpretació. Per això convé distingir l'estructura volumètrica general dels detalls locals.

### 5.8.3. Interpretació de llums, ombres i reflexos

Una regió aparentment fosca pot correspondre a una ombra pròpia, una ombra projectada, una cavitat o una combinació de fenòmens diferents. De la mateixa manera, una zona brillant pot correspondre a una superfície que rep una il·luminació intensa, a un reflex direccional o a una característica pròpia del material.

La interpretació s'ha de basar en la relació entre geometria, il·luminació i posició de l'observador, i evitar classificar automàticament cada regió per la seva aparença. És important distingir:

- Les zones que reben llum directa.
- Les zones que reben principalment il·luminació indirecta.
- Les regions protegides de determinades fonts.
- Les ombres pròpies i projectades.
- Els reflexos visibles des del punt d'observació.
- Les transicions produïdes pels canvis d'orientació.

Aquesta classificació no constitueix una recepta de pintura. És una eina d'anàlisi per comprendre l'estructura lluminosa de l'objecte.

### 5.8.4. Diferència entre il·luminació observada i il·luminació representada

La il·luminació observada és la que presenta físicament l'objecte sota unes condicions determinades. La il·luminació representada és la interpretació que el pintor decideix traslladar a la superfície de la miniatura.

Totes dues poden coincidir, però no necessàriament ho fan del tot. La representació pot simplificar l'escena, reforçar determinats contrastos o modificar algunes relacions per facilitar la lectura del volum.

La decisió pictòrica ha de ser conscient i coherent amb el resultat que es pretén aconseguir. No cal reproduir tots els fenòmens lluminosos d'una escena, però sí comprendre quina informació es conserva, quina se simplifica i quin efecte pot produir aquesta decisió.

## 5.9. Errors conceptuals i exercicis d'observació

### 5.9.1. Errors conceptuals freqüents

**Confondre llum amb color clar**

Una zona de color clar no ha d'estar necessàriament més il·luminada que una altra. L'aparença visual depèn de la il·luminació, de les propietats de la superfície i de la informació que arriba a l'observador. No s'ha de deduir la distribució lluminosa únicament a partir de la claredat aparent d'una regió.

**Confondre ombra pròpia i ombra projectada**

L'ombra pròpia apareix sobre el mateix objecte que bloqueja la llum. L'ombra projectada apareix sobre una altra superfície. Tot i que poden estar relacionades, el seu origen geomètric és diferent i s'han d'analitzar per separat.

**Confondre il·luminació indirecta i reflexió especular**

La il·luminació indirecta descriu la llum que arriba a una superfície després d'interactuar amb l'entorn. La reflexió especular descriu una forma direccional de reflexió. No són conceptes equivalents.

**Interpretar les ombres com a zones de foscor absoluta**

Una ombra indica que una font de llum directa ha quedat bloquejada totalment o parcialment. Tanmateix, altres fonts i les reflexions de l'entorn poden continuar il·luminant aquella regió. Una ombra no ha de presentar necessàriament una absència total de llum.

**Ignorar la geometria de les superfícies**

L'orientació de cada superfície condiciona la seva relació amb la font lluminosa. Si s'analitza un objecte únicament per la seva aparença general, poden passar desapercebudes diferències importants entre plans, curvatures i regions protegides.

**Confondre reflexos i zones il·luminades**

Una superfície il·luminada rep llum, però no necessàriament presenta un reflex especular visible. Un reflex depèn de la direcció en què la superfície retorna la llum cap a l'observador. No totes les zones il·luminades s'han d'interpretar com a reflexos.

**Interpretar convencions pictòriques com a lleis físiques**

La pintura pot modificar o simplificar la il·luminació real per millorar la lectura visual. Aquestes decisions formen part de la representació artística i no s'han de confondre amb les lleis físiques que descriuen el comportament de la llum.

### 5.9.2. Exercicis d'observació i comprensió

Els exercicis següents tenen com a objectiu desenvolupar la capacitat d'observar i interpretar els fenòmens lluminosos abans d'aplicar-los a la pintura. No es plantegen com a receptes tècniques ni com a exercicis d'execució pictòrica. Són propostes didàctiques, no resultats experimentals del manual.

#### Exercici 1. Comparació de fonts lluminoses

Observar un mateix objecte sota diferents condicions d'il·luminació:

- Una font petita i pròxima.
- Una font extensa i pròxima.
- Una font situada a més distància.
- Un entorn amb il·luminació ambiental apreciable.

Identificar les diferències en la distribució de la il·luminació i en la formació de les ombres.

#### Exercici 2. Anàlisi de plans i orientació

Utilitzar un objecte geomètric senzill, com ara un cub o una figura formada per diversos plans.

Situar una font lluminosa en una posició fixa i observar quines superfícies reben la llum més directament. Identificar les normals geomètriques i comparar les orientacions dels plans.

Modificar la posició de la font i observar com canvia la distribució de la il·luminació.

#### Exercici 3. Estudi comparatiu de les ombres

Observar les ombres projectades per un mateix objecte sota fonts lluminoses de mida aparent diferent.

Comparar:
- La direcció de les ombres.
- La seva extensió.
- La definició dels seus límits.
- L'aparició de regions d'umbra i penombra.

Identificar quins canvis es deuen a la geometria i quins a les característiques de la font.

#### Exercici 4. Observació de reflexos

Seleccionar una superfície que permeti observar reflexos i modificar progressivament la posició de l'observador.

Comprovar com canvia la informació visual rebuda i distingir entre reflexos direccionals i reflexió difusa. Observar també com varia el reflex quan es modifica la posició de la font lluminosa.

#### Exercici 5. Interpretació de volums geomètrics

Observar diferents objectes geomètrics sota una il·luminació estable.

Comparar superfícies planes, superfícies corbes, arestes, cavitats, regions d'ombra pròpia i ombres projectades. Intentar explicar quines característiques geomètriques produeixen les diferències d'il·luminació observades.

#### Exercici 6. Anàlisi integradora d'una miniatura

Seleccionar una miniatura i analitzar-la sota una font de llum estable. Identificar:

- La font lluminosa principal, la seva posició i la mida aparent.
- Els plans i les superfícies principals.
- Les regions que reben il·luminació directa.
- Les zones protegides de la font.
- Les ombres pròpies i projectades.
- Els reflexos visibles.
- Les possibles contribucions de la il·luminació indirecta.
- Les diferències entre la il·luminació observada i la interpretació pictòrica que es podria realitzar.

L'exercici ha de concloure amb una explicació raonada de com la geometria, la il·luminació i la posició de l'observador contribueixen a la percepció del volum.

## Referències

- Aubuchon, C. i Fleming, R. W. (2026). “Visual Perception of 3D Shape: From Local 2D Image Measurements to 3D Surface Properties”. *Annual Review of Vision Science*, 12, 413–436. https://doi.org/10.1146/annurev-vision-121225-090634
- Commission Internationale de l’Éclairage (CIE). (2020). *ILV: International Lighting Vocabulary*. 2a edició. CIE S 017/E:2020. https://cie.co.at/e-ilv
- CIE. (2020). “Photometric distance law”, entrada 17-25-104 de l’*International Lighting Vocabulary*. https://cie.co.at/eilvterm/17-25-104
- CIE. (2020). Entrades “Luminous flux” (17-21-039), “Luminous intensity” (17-21-045), “Illuminance” (17-21-060) i “Luminance” (17-21-050) de l’*International Lighting Vocabulary*. https://cie.co.at/e-ilv
- CIE. (2020). “Regular reflection” i “Diffuse reflection”, entrades 17-24-052 i 17-24-054 de l’*International Lighting Vocabulary*. https://cie.co.at/eilvterm/17-24-052 i https://cie.co.at/eilvterm/17-24-054
- CIE. (2020). “Scattering”, entrada 17-24-049 de l’*International Lighting Vocabulary*. https://cie.co.at/eilvterm/17-24-049
- Illuminating Engineering Society (IES). (s. f.). “Inverse-square law”. *IES Lighting Definitions*. https://ies.org/definitions/inverse-square-law/
- IES. (s. f.). “Cosine law”. *IES Lighting Definitions*. https://www.ies.org/definitions/cosine-law/
- Johnston, A. i Passmore, P. J. (1994). “Shape from shading. I: Surface curvature and orientation”. *Perception*, 23(2), 169–189. https://doi.org/10.1068/p230169
- Ling, S. J., Sanny, J. i Moebs, W. (2016). *University Physics, Volume 3*. OpenStax, Rice University. Apartat 1.2, “The Law of Reflection”. https://openstax.org/books/university-physics-volume-3/pages/1-2-the-law-of-reflection
- Liu, B. i Todd, J. T. (2004). “Perceptual biases in the interpretation of 3D shape from shading”. *Vision Research*, 44(18), 2135–2145. https://doi.org/10.1016/j.visres.2004.03.024
- Nielsen, K. J. i Connor, C. E. (2024). “How Shape Perception Works, in Two Dimensions and Three Dimensions”. *Annual Review of Vision Science*, 10, 47–68. https://doi.org/10.1146/annurev-vision-112823-031607

Les referències sustenten els fonaments d'òptica, fotometria, reflexió, geometria de la il·luminació i percepció visual. Els exercicis són propostes d'observació i no s'han de presentar com a resultats experimentals del manual.