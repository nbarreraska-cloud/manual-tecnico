# F15 — Avaluació de les proves d'estil i prototips vectorials

**Data:** 06/11/2026  
**Branca:** `intervencion-editorial-2026-11`  
**Documents relacionats:** F10, F12, F13 i F14.  
**Estat:** quatre prototips SVG v01 creats; tots quatre pendents d'aprovació.

## 1. Decisió sobre els resultats d'ImageGen

Durant l'exploració inicial s'han generat tres làmines conjuntes que intentaven representar les quatre proves alhora. No s'incorporen al repositori ni es consideren proves vàlides.

Motius de rebuig:
- El format de collage impedia revisar cada composició a la seva mida i proporció de maquetació.
- Es van introduir continguts aliens a les fitxes, com una seqüència de fusteria en lloc de la construcció NMM.
- La seqüència NMM representada no corresponia a les fases del capítol 16 i no mantenia la progressió tècnica requerida.
- La comparació d'opacitat no preservava adequadament el mateix fons i podia confondre opacitat amb altres propietats.
- La figura del vidre no mantenia una comparació prou controlada de la mateixa escena a través de vidre transparent i esmerilat.
- Les etiquetes incorporades automàticament no oferien el control terminològic i editorial necessari.

**Conclusió:** cap dels tres collages és aprovat, reutilitzat o comptabilitzat com a figura del manual. Es manté el principi F12: les figures tècniques s'han de poder revisar individualment i amb el text editable separat de la base gràfica.

## 2. Alternativa adoptada

Per a aquestes quatre proves s'ha adoptat SVG com a màster vectorial editable. És més adequat que una il·lustració generativa quan la funció principal és explicar relacions geomètriques, cromàtiques o de procés amb precisió controlada.

Els quatre fitxers es mantenen a `grafics_prova/`, fora del manual i de la futura còpia il·lustrada:

| Figura | Fitxer | Contingut |
|---|---|---|
| 4.1 / G006 | `fig_C04_4-1_G006_v01.svg` | Mescla additiva RGB i sostractiva CMY, en camps separats |
| 3.1 / G003 | `fig_C03_3-1_G003_v01.svg` | Quatre comportaments orientatius sobre el mateix patró de fons |
| 16.4 / G042 | `fig_C16_16-4_G042_v01.svg` | Sis fases de construcció NMM amb la mateixa geometria |
| 34.1 / G110 | `fig_C34_34-1_G110_v01.svg` | Tres tipus de vidre i comparació de la mateixa escena en transparent/esmerilat |

## 3. Revisió tècnica inicial per composició

### 3.1. Figura 4.1 / G006 — RGB i CMY

- RGB es representa sobre camp fosc amb superposició additiva; CMY sobre camp clar amb superposició sostractiva.
- Es diferencia llum de pigments/colorants.
- La zona central del model CMY s'identifica com a idealitzada; no s'atribueix el resultat a pintures comercials.
- Les anotacions del camp RGB tenen contrast clar sobre el fons fosc.

**Pendent:** comprovar en renderització real que els modes de fusió SVG es mostren correctament a l'entorn de maquetació i exportació.

### 3.2. Figura 3.1 / G003 — Opacitat i transparència

- Es repeteix el mateix patró de fons i la mateixa àrea de mostra.
- Només varia l'opacitat visual de la capa esquemàtica.
- Les quatre denominacions són orientatives; no s'hi fixen llindars quantitatius.
- S'afegeix una nota que separa opacitat, transparència i cobertura.

**Pendent:** revisar que la lectura de «semiopaca» i «semitransparent» sigui prou diferenciada i que no sembli una escala comercial universal.

### 3.3. Figura 16.4 / G042 — Construcció NMM

- S'ha corregit el brief F14 perquè reflecteixi sis moments: base, regions fosques, regions intermèdies, reflexos clars, accents màxims i integració.
- Els sis panells utilitzen la mateixa silueta i la mateixa orientació.
- La base s'ha uniformitzat a tots els panells; els canvis posteriors s'afegeixen progressivament.
- La seqüència es declara proposada i no assajada.

**Pendent:** revisar si la representació de la peça metàl·lica és prou inequívoca i si la transició de les regions tonals comunica el procés sense suggerir un patró universal de reflexos.

### 3.4. Figura 34.1 / G110 — Vidre

- Es mostren tres tipus: transparent incolor, transparent acolorit i esmerilat.
- La comparació inferior utilitza la mateixa escena i les mateixes dimensions.
- El vidre esmerilat difon la imatge transmesa; no es representa com a opac absolut ni com un acabat simplement mat.

**Pendent:** comprovar que l'efecte de difusió es percep clarament en renderització i que no s'interpreta com una textura superficial decorativa.

## 4. Controls pendents abans de l'aprovació

Cap prototip no es considera aprovat fins que s'hagin completat aquests controls:

1. Renderitzar cada SVG per separat i comprovar que no hi ha errors de visualització, filtres o modes de fusió.
2. Revisar llegibilitat i contrast a una mida de figura realista dins de la pàgina.
3. Comparar cada composició amb el paràgraf exacte del manual i la fitxa F10.
4. Comprovar la terminologia catalana i la correcció de totes les anotacions.
5. Confirmar que no s'hi han afegit dades, mesures, marques ni resultats no documentats.
6. Registrar qualsevol correcció i conservar versions anteriors.

## 5. Verificació de repositori i integritat bàsica

Després de crear els quatre SVG s'ha tornat a consultar cada fitxer a GitHub:

- Els quatre fitxers existeixen a la branca de treball i presenten una única arrel `<svg>` amb tancament corresponent.
- Els identificadors interns utilitzats per a patrons, filtres i escenes estan declarats; les dues referències a l'escena de vidre apunten a l'element declarat.
- F13 conserva 150 composicions úniques i 156 identificadors P1 únics.
- Els quatre registres pilot enllacen directament amb els SVG corresponents.
- La compilació consolidada conserva el SHA `193b7b0fa60e10fef7dc46910b03957c2f9c3a5a`.

Aquesta és una comprovació d'integritat del contingut i de la traçabilitat a GitHub, **no** una validació de renderització. Encara cal obrir els SVG en un renderitzador compatible i comprovar-ne el resultat visual a mida de pàgina abans d'aprovar-los.

## 6. Estat de producció

| Element | Estat |
|---|---|
| Briefs F14 | 4 preparats |
| Collages generatius exploratoris | 3 rebutjats |
| Prototips SVG editables | 4 creats |
| Prototips aprovats | 0 |
| Exportacions finals | 0 |
| Insercions al manual | 0 |
| Canvis al manual mestre | 0 |

Els quatre registres corresponents de F13 passen a «Prototip vectorial v01 · en revisió». Les altres 146 composicions continuen pendents d'encàrrec.

## 7. Decisió de continuïtat

No s'ha d'estendre encara l'estil a les altres 146 figures. Primer cal validar la renderització i la lectura dels quatre SVG. Si els quatre casos superen la revisió, es podrà congelar una primera guia visual comuna i començar la producció per tandes. Si un cas falla, es corregirà abans d'estendre'n les convencions.

La producció continua separada del manual mestre. Aquests prototips són materials de treball i no s'han inserit a cap document lector.


## 8. Segona revisió estàtica dels prototips

S'ha fet una lectura addicional del codi SVG, no una validació visual en navegador o en maquetació:

- **G006:** s'ha detectat i corregit el baix contrast del subtítol RGB sobre el camp fosc. La comprovació de modes de fusió `screen` i `multiply` continua pendent de renderització.
- **G003:** l'estructura repeteix el mateix patró de fons i modifica l'opacitat de la capa. Cal revisar visualment la diferència perceptiva entre els dos estats intermedis.
- **G042:** els sis panells mantenen la mateixa silueta i una base uniforme; la seqüència és una simplificació didàctica. Cal validar si els canvis tonals són prou llegibles i si la forma es reconeix com a superfície metàl·lica.
- **G110:** s'ha corregit la fila superior perquè els tres tipus de vidre es mostrin sobre la mateixa escena, no com a mostres de color aïllades. La comparació inferior manté la mateixa escena i aplica difusió a la versió esmerilada.

### Límit de la verificació

No s'ha pogut executar un renderitzador SVG en aquest entorn. Per tant, no es declara superada la comprovació de renderització, tipografia, filtres, modes de fusió ni llegibilitat a mida de pàgina. La revisió anterior és només estàtica, basada en el contingut del codi. Els quatre fitxers continuen en estat «revisió tècnica», sense aprovació.



## 9. Revisió de fidelitat representativa i contrast amb el contingut

Aquesta revisió contrasta cada SVG amb el brief F14 i amb el contingut efectiu de la compilació consolidada. No avalua només si el dibuix «s'assembla» al tema: comprova si representa les distincions i els processos que el text explica.

### 9.1. Figura 4.1 / G006 — RGB i CMY

**Correspondència amb el text:** alta a nivell conceptual.

- El camp RGB sobre fons fosc i el camp CMY sobre fons clar separen correctament mescla de llum i mescla sostractiva.
- La disposició de tres components superposats permet llegir les combinacions i el centre blanc/negre idealitzat.
- La nota sobre la idealització del CMY és coherent amb l'advertiment del capítol: els pigments i colorants reals no reprodueixen necessàriament el resultat teòric.
- No s'hi introdueixen CMYK, perfils d'impressió ni altres continguts que el text no desenvolupi.

**Reserva tècnica:** la representació depèn de `mix-blend-mode: screen` i `multiply`. El codi estàtic no demostra que aquests modes es renderitzin igual en tots els entorns. Cal comprovar el PNG de prova i, posteriorment, l'exportació del document. Si el renderitzador no respecta els modes, cal substituir-los per colors de superposició explícits o per una construcció SVG més compatible.

**Dictamen de fidelitat:** representa el contingut correcte; pendent de verificació de renderització, no de reformulació conceptual.

### 9.2. Figura 3.1 / G003 — Opacitat i transparència

**Correspondència amb el text:** bona, amb una limitació didàctica.

- El mateix patró de fons es conserva als quatre camps i només varia l'opacitat de la capa blava.
- La progressió permet observar com el fons queda ocult, es percep poc o continua visible.
- La nota inferior separa explícitament opacitat/transparència de cobertura, en coherència amb el capítol 3.2.1.
- La imatge es presenta com a esquema conceptual, no com a prova de productes.

**Limitació:** els valors d'opacitat del SVG (1; 0,78; 0,48; 0,18) són valors gràfics triats per construir una progressió. No proven categories físiques normalitzades ni permeten classificar pintures reals. La figura no ha d'induir a llegir «semiopaca» i «semitransparent» com a llindars universals. La llegenda o el peu han de conservar la qualificació orientativa.

**Dictamen de fidelitat:** representa correctament la idea d'ocultació del fons; cal mantenir inequívoc el caràcter esquemàtic i no experimental.

### 9.3. Figura 16.4 / G042 — Construcció NMM

**Correspondència amb el text:** parcial; no és suficient encara per aprovar-la.

El prototip representa una peça allargada semblant a una fulla metàl·lica i acumula zones fosques, intermèdies i clares. Això s'aproxima a l'ordre general de les fases 16.5.2–16.5.7, però no arriba a representar amb prou precisió el que fa que la superfície es llegeixi com a metàl·lica.

Problemes identificats:

1. **Materialitat insuficient:** la peça es pot llegir com una superfície grisa amb ombres i llums. No hi ha una estructura de reflexos prou inequívoca per diferenciar NMM d'un ombreig genèric sobre un material mat.
2. **Relació amb la geometria poc demostrada:** la forma és constant, però la distribució de les masses tonals no explica de manera clara com els reflexos responen als plans, arestes o curvatures de la peça.
3. **Direcció i entorn de reflexió absents:** el capítol explica que les regions fosques i clares responen a un patró de reflexos i a la geometria. El dibuix no explicita cap esquema de llum/reflexió ni fa visible aquesta relació.
4. **Fase d'integració feble:** els panells 5 i 6 són molt semblants. La darrera fase no mostra prou clarament quina revisió o integració s'ha dut a terme.
5. **Gradient declarat però no utilitzat:** el SVG defineix `bladeBase`, però cap de les sis siluetes l'utilitza. No és un error conceptual per si sol, però és codi inactiu i no correspon a una base cromàtica realment representada.

**Correcció necessària abans de l'aprovació:** redissenyar la seqüència perquè la peça presenti un patró de reflexos deliberat i coherent amb la seva geometria; distingir visualment plans, reflexos clars i bandes fosques; fer que el pas final mostri una integració identificable, no només una variació menor. Cal mantenir la nota que la seqüència és didàctica i no universal: el capítol permet començar des d'una base fosca o intermèdia i adaptar els reflexos a cada forma.

**Dictamen de fidelitat:** el tema és correcte, però la representació actual no demostra prou bé el fenomen tècnic. No aprovar G042 en la versió v01.

### 9.4. Figura 34.1 / G110 — Tipus de vidre

**Correspondència amb el text:** bona a nivell introductori.

- L'escena comuna permet comparar la visió definida a través d'un material transparent amb la difusió del vidre esmerilat.
- La mostra acolorida afegeix una tonalitat sense eliminar la visibilitat del fons, coherent amb el capítol 34.2.
- La versió esmerilada difumina l'escena i els contorns, en lloc de convertir el material en una superfície simplement mate o completament opaca.
- La comparació inferior manté el mateix escenari i les mateixes dimensions, de manera que la variable principal és la difusió.

**Límits de representació:** el dibuix és un esquema de transmissió visual, no una simulació òptica completa. No representa refracció, distorsió per gruix o curvatura, ni reflexos superficials; aquests fenòmens apareixen al text, però no són l'objectiu d'aquesta figura introductòria. No s'ha de presentar com si resumís totes les propietats del vidre.

**Punt de control:** comprovar que el desenfocament no quedi retallat ni sembli una textura decorativa. Si el renderitzat no fa evident la pèrdua de definició del fons, cal augmentar o ajustar la difusió.

**Dictamen de fidelitat:** representa correctament la distinció central entre transparència definida i transmissió difusa. Pot continuar a revisió tècnica, sense aprovació fins a veure el render.

## 10. Via de renderització i estat actualitzat

S'ha afegit el workflow `.github/workflows/render-svg-prototypes.yml` a la branca de treball. El procés:
- comprova que hi siguin els quatre prototips esperats;
- analitza l'estructura XML de cada SVG;
- els renderitza a PNG amb CairoSVG;
- genera una làmina de contacte per facilitar la comparació;
- publica les previsualitzacions com a artefacte de GitHub Actions.

Aquest workflow permet obtenir una prova visual reproduïble sense incorporar cap imatge al manual. La renderització de CairoSVG és una comprovació d'un entorn concret, no una garantia que Word, LibreOffice o tots els navegadors reprodueixin exactament els mateixos filtres i modes de fusió.

**Estat després de la revisió de fidelitat:**

| Prototip | Fidelitat conceptual | Estat editorial |
|---|---|---|
| G006 — RGB/CMY | Bona | Pendent de renderització i compatibilitat dels modes de fusió |
| G003 — Opacitat/transparència | Bona, amb caràcter esquemàtic obligatori | Pendent de renderització i lectura a mida de pàgina |
| G042 — NMM | Insuficient en la v01 | Requereix redisseny abans de continuar |
| G110 — Vidre | Bona per a la distinció introductòria | Pendent de renderització i comprovació de la difusió |

No s'aprova cap dels quatre prototips. La G042 necessita una correcció conceptual/visual abans de considerar-la apta; les altres tres necessiten encara comprovació gràfica real. No s'ha modificat F10, la compilació consolidada ni cap capítol del manual.


## 11. Resultat de la primera renderització real

S'ha executat el workflow `.github/workflows/render-svg-prototypes.yml`. La validació XML i la generació dels quatre PNG han acabat correctament. L'artefacte de revisió és:
- Workflow: https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42133854476
- Artefacte: `SVG-prototypes-rendered-review` (PNG individuals i làmina de contacte; retenció fins al 06/12/2026).

La renderització confirma que els fitxers són processables per CairoSVG, però també revela problemes que la lectura del codi no havia permès verificar.

### 11.1. G006 — Error visual confirmat

**No supera la prova.** En el PNG generat, els cercles RGB i CMY apareixen com a superfícies opaques superposades per ordre, sense mostrar correctament les mescles de les zones d'intersecció. El mode CSS `mix-blend-mode` no queda aplicat en aquesta renderització.

Això és un defecte substantiu, no només una diferència estètica: la figura afirma explicar la mescla additiva i la sostractiva, però el resultat visual no mostra els colors de les interseccions ni el centre blanc/negre esperat.

**Acció:** substituir els modes de fusió CSS per una construcció SVG compatible i controlada (interseccions explícites o composició amb transparències comprovades). No aprovar ni exportar la v01.

### 11.2. G003 — Problema de composició i jerarquia

La progressió de visibilitat del patró sí que es percep i les quatre mostres es diferencien. La representació és coherent amb el caràcter esquemàtic declarat.

Tanmateix, la nota «La representació és esquemàtica...» queda situada dins l'alçada dels quatre panells i travessa visualment la zona inferior de les targetes. Això crea una interferència de jerarquia i pot semblar una etiqueta comuna superposada a les mostres.

**Acció:** treure aquesta nota de l'interior dels panells, reservar-li una franja pròpia i revisar l'espai entre els textos inferiors. Mantenir els quatre comportaments orientatius i la separació entre opacitat, transparència i cobertura. No aprovar la v01.

### 11.3. G042 — La renderització confirma la insuficiència conceptual

La imatge es veu neta i els sis panells mantenen la mateixa silueta, però la lectura visual confirma la reserva de l'apartat 9.3: el resultat sembla una peça grisa amb bandes tonals successives. No comunica amb prou força una superfície metàl·lica ni explica per què les zones fosques i clares constitueixen reflexos coherents amb la geometria.

A més, els panells 5 i 6 són gairebé idèntics. La fase d'integració no es diferencia prou de l'aplicació dels accents màxims.

**Acció:** redissenyar des del plantejament visual, no limitar-se a retocar colors. Cal definir primer una geometria i un patró de reflexos que es puguin justificar, i després construir una seqüència on cada fase aporti una modificació llegible. No aprovar la v01.

### 11.4. G110 — Representació coherent, amb abast delimitat

La comparació es renderitza correctament: l'escena es conserva definida a través del vidre transparent i perd definició a través de l'esmerilat. La mostra acolorida manté visible l'escena amb una tonalitat afegida. Per tant, la distinció central entre transparència i difusió és perceptible.

El resultat és vàlid com a esquema introductori de transmissió visual, no com a simulació completa de tots els fenòmens del vidre. No mostra refracció, distorsió per curvatura, gruix ni reflexos superficials; aquests límits ja queden delimitats a l'apartat 9.4.

**Acció:** conservar l'enfocament i revisar la llegibilitat final a mida de pàgina. No aprovar encara la v01 fins a fer aquesta comprovació.

## 12. Dictamen després de renderitzar

| Prototip | Resultat de renderització | Fidelitat representativa | Decisió |
|---|---|---|---|
| G006 | Renderitza, però falla la mescla de les interseccions | No representa correctament el fenomen en el PNG actual | Corregir |
| G003 | Renderitza; nota comuna mal situada | Correcta, amb problema de composició | Corregir |
| G042 | Renderitza; seqüència visual massa genèrica | Insuficient per explicar NMM | Redissenyar |
| G110 | Renderitza; difusió visible | Correcta per a una figura introductòria | Mantenir enfocament i ajustar si cal |

La prova tècnica ha superat el pas de processament XML i exportació a PNG, però això no equival a l'aprovació de les figures. Cap prototip queda aprovat. Les versions v01 es conserven com a antecedents i no s'han d'esborrar ni sobreescriure.

La següent iteració s'ha de centrar en G006, G003 i G042. G110 no necessita un redisseny conceptual amb l'evidència actual. Encara queda pendent comprovar la lectura de cada figura a la mida real de maquetació i, més endavant, en l'entorn d'exportació del document.


## 13. Protocols de proves físiques i conciliació de G003

S'han preparat protocols específics per separar la producció gràfica de l'obtenció d'evidència física:

- [Protocol G003 — opacitat, transparència i cobertura](protocol_prova_fisica_G003.md). La prova continua pendent d'execució. Fins que no hi hagi mostres identificades i fotografies documentades, G003 no es pot presentar com a resultat E2; es manté disponible l'alternativa conceptual E0 prevista a F14.
- [Protocol G042 — construcció NMM](protocol_prova_fisica_G042.md). Defineix una seqüència fotogràfica de sis estats reals de la mateixa peça, basada en els apartats 16.5.2–16.5.7. El protocol no valida ni aprova el SVG v01; el redisseny s'ha de basar en una execució real i no en retocs cromàtics del prototip que no va superar la revisió de fidelitat.

### Conciliació de l'ancoratge G003

La lectura del capítol 3 i de la tanda F11 confirma que la ubicació lectora adequada és **3.2.1**, no 3.1. El registre F13 s'ha corregit per reflectir aquesta ubicació. La correcció és documental i no altera el contingut del manual, la selecció gràfica ni la compilació consolidada.

### Estat després d'aquesta actualització

- Proves físiques G003 i G042 executades: **0**.
- Fotografies de resultats reals incorporades: **0**.
- Prototips SVG aprovats: **0**.
- Insercions al manual lector: **0**.
- Modificacions de la compilació consolidada: **0**.

La preparació documental no s'ha de confondre amb l'execució de les proves ni amb l'aprovació editorial de les figures.


## 14. Matriu documental de selecció G003

S'ha creat `matriu_seleccio_mostres_G003.md` després de contrastar l'annex A i les fitxes individuals de sis referències candidates: quatre Model Color i dues Game Color Ink. La matriu diferencia les declaracions de família de les propietats individuals no documentades. No classifica prèviament cap pintura com a opaca, semiopaca, semitransparent o transparent.

La selecció és provisional i no confirma disponibilitat física. La via E0 de F14 continua sent l'alternativa si no es realitza la prova; la via E2 només és admissible amb mostres reals identificades, fotografies originals i condicions registrades. F14 s'ha ajustat a l'ancoratge lector 3.2.1 i a aquests límits d'evidència.


## 15. Aclariment de la naturalesa E1 de G042

La consulta de F12 confirma que E1 significa procediment o seqüència proposats i no assajats. Per tant, la prova física descrita al protocol G042 és complementària i no és un requisit per produir la figura 16.4. G042 es pot redissenyar com una seqüència vectorial didàctica, sempre identificada com a proposta no assajada. La nova versió ha de corregir la lectura genèrica de la v01 i fer visible la relació entre geometria, patró de reflexos i sis funcions del procediment 16.5.2–16.5.7. La v01 es conserva i no s'aprova.
