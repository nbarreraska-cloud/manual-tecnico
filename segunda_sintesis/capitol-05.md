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

Les ombres apareixen quan un objecte o una part seva bloqueja totalment o parcialment la llum. La forma depèn de la geometria, la posició i la mida aparent de la font, l'orientació de les superfícies i la il·luminació de l'entorn.

### 5.5.1. Ombra pròpia i projectada

- **Ombra pròpia:** regió del mateix objecte que no rep il·luminació directa d'una font determinada, a causa de la seva geometria o de la protecció d'altres parts.
- **Ombra projectada:** apareix sobre una altra superfície quan l'objecte bloqueja la llum.

La diferència és la localització: l'ombra pròpia pertany a l'objecte; la projectada recau sobre una altra superfície. La seva forma i posició depenen de la relació entre font, objecte i superfície receptora.

### 5.5.2. Umbra i penombra

Quan una font extensa queda parcialment bloquejada es poden distingir:
- **Umbra:** zona on la font queda completament oculta.
- **Penombra:** zona on només queda bloquejada una part de la font.

Una font puntual ideal pot produir ombres de límit definit; una d'extensa acostuma a generar transicions. La longitud, l'orientació i la forma de l'ombra projectada varien amb la posició de la font.

### 5.5.3. Ombres de contacte i oclusió

Les ombres de contacte apareixen en regions on dues superfícies són molt pròximes o entren en contacte: unions amb el terra, separacions entre parts de la figura i cavitats estretes. La geometria dificulta que hi arribi la llum. La intensitat depèn de la proximitat, la forma i la quantitat de llum directa i indirecta disponible. És una expressió descriptiva, no una magnitud fotomètrica independent ni una indicació que no hi hagi gens de llum.

### 5.5.4. Influència de la il·luminació indirecta

La llum indirecta pot arribar a zones que no reben llum directa i reduir el contrast entre llums i ombres. La seva contribució depèn de les superfícies reflectants de l'entorn. Una ombra s'ha d'interpretar com una regió on s'ha reduït la contribució d'algunes fonts, no necessàriament com un espai sense llum.

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

Abans de decidir com representar llums, ombres i reflexos, convé analitzar la miniatura com un objecte tridimensional. El procés es pot organitzar en quatre passos:

1. **Identificar la il·luminació:** observar la direcció principal, la mida aparent i la distància de la font, les contribucions ambientals i la posició de l'observador. Si hi ha diverses fonts, identificar-ne primer la principal sense ignorar les altres.
2. **Analitzar la geometria:** localitzar plans, corbes, arestes, relleus, cavitats i regions protegides; separar l'estructura general dels detalls locals.
3. **Interpretar les regions:** distingir llum directa, llum principalment indirecta, ombres pròpies i projectades, zones de contacte i reflexos visibles. Una zona fosca no és automàticament una ombra, ni una de brillant un reflex.
4. **Decidir què representar:** la il·luminació observada correspon a unes condicions físiques concretes; la representació és la interpretació pictòrica, que pot simplificar o reforçar fenòmens per millorar la lectura del volum.

Aquest anàlisi no és una recepta de pintura: proporciona la base per planificar-la. Els procediments tècnics es desenvolupen als capítols posteriors.

## 5.9. Exercicis d'observació i comprensió

Els exercicis són propostes didàctiques, no resultats experimentals del manual.

1. **Comparació de fonts:** observar un mateix objecte amb una font petita i pròxima, una d'extensa i pròxima, una de més allunyada i un entorn amb llum ambiental apreciable. Comparar distribució, definició de les ombres i transicions.
2. **Plans i orientació:** il·luminar un objecte geomètric senzill, com un cub. Identificar plans, normals i diferències d'orientació; moure la font i observar els canvis.
3. **Estudi de les ombres:** comparar les ombres projectades per un mateix objecte amb fonts de mides aparents diferents. Analitzar direcció, extensió, definició, umbra i penombra.
4. **Observació de reflexos:** modificar la posició de l'observador i de la font per distingir reflexos direccionals i reflexió difusa.
5. **Interpretació de volums:** observar objectes amb plans, corbes, arestes i cavitats sota una il·luminació estable. Relacionar la llum amb la geometria i distingir ombres pròpies i projectades.
6. **Anàlisi d'una miniatura:** identificar font principal, plans, zones il·luminades, regions protegides, ombres, reflexos i contribucions indirectes. Explicar com intervenen la geometria, la il·luminació i el punt de vista en la percepció del volum.

## Referències

- Aubuchon, C. i Fleming, R. W. (2026). “Visual Perception of 3D Shape: From Local 2D Image Measurements to 3D Surface Properties”. *Annual Review of Vision Science*, 12, 413–436. https://doi.org/10.1146/annurev-vision-121225-090634
- Commission Internationale de l’Éclairage (CIE). (2020). *ILV: International Lighting Vocabulary*. 2a edició. CIE S 017/E:2020. https://cie.co.at/e-ilv
- CIE. (2020). “Photometric distance law”, entrada 17-25-104 de l’*International Lighting Vocabulary*. https://cie.co.at/eilvterm/17-25-104
- CIE. (2020). Entrades “Luminous flux” (17-21-039), “Luminous intensity” (17-21-045), “Illuminance” (17-21-060) i “Luminance” (17-21-050) de l’*International Lighting Vocabulary*. https://cie.co.at/e-ilv

Les referències sustenten els fonaments d'òptica, fotometria i percepció visual. Els exercicis són propostes d'observació i no s'han de presentar com a resultats experimentals del manual.