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
- [Protocol complementari G042 — documentació física](protocol_prova_fisica_G042.md). Una execució real pot aportar fotografies addicionals, però no és requisit per produir G042 com a E1. El redisseny vectorial s'ha de basar en el capítol 16 i identificar-se com a proposta no assajada.

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


## 16. Iteració gràfica G003 v02 i G042 v02

S'han creat dues noves versions SVG independents, sense sobreescriure les v01:

- **G003 v02:** alternativa conceptual E0. La nota explicativa queda fora de les mostres; els quatre panells mantenen un patró comú i presenten nivells gràfics il·lustratius, sense llindars ni atribució a productes concrets. La prova física i la via E2 continuen pendents.
- **G042 v02:** seqüència E1 proposada no assajada. La forma és una fulla d'espasa consistent en els sis panells; la seqüència diferencia base, masses fosques, transició intermèdia, reflex principal, accents màxims i integració. Cal revisar especialment la lectura de la geometria, el caràcter metàl·lic i la diferència funcional entre els panells 5 i 6.

El workflow de renderització s'ha actualitzat perquè la fulla de contacte s'adapti al nombre de SVG del directori. Les v02 s'han renderitzat correctament. En la revisió visual: G003 v02 presenta encara la nota comuna dins de l'àrea dels panells, per la qual cosa s'ha desplaçat sota aquests; G042 v02 manté la mateixa geometria de fulla i sis canvis progressius llegibles, però continua pendent de judici editorial a mida de pàgina. **Cap de les dues versions està aprovada ni inserida al manual.**


## 17. Iteració G006 v02

S'ha creat [G006 v02](../grafics_prova/fig_C04_4-1_G006_v02.svg) per substituir els modes CSS `mix-blend-mode` de la v01, que no es representaven correctament a CairoSVG. La nova versió utilitza transparència alfa estàndard i manté separats el model additiu RGB i el model sostractiu CMY idealitzat. La representació continua sent conceptual; no equival a una simulació colorimètrica ni a una demostració de mescla de pintures comercials. La v02 s'ha renderitzat i revisat: la composició alfa seqüencial no representa amb prou fidelitat les combinacions RGB/CMY. S'ha creat una v03 que presenta les combinacions ideals de manera explícita i separada; resta pendent de renderització i revisió.


## 18. Iteració G006 v03 i correcció de composició G003 v02

La revisió del PNG de G006 v02 ha mostrat que la composició alfa estàndard evita la fallada dels modes de fusió, però no produeix resultats de mescla prou fidels: l'ordre de superposició condiciona els colors. Per evitar una falsa demostració, s'ha creat G006 v03 amb els colors primaris i les combinacions ideals presentats en mostres separades i etiquetades. La v03 encara no s'ha renderitzat ni aprovat.

En G003 v02, la nota explicativa comuna quedava encara dins de l'alçada dels panells. S'ha desplaçat completament per sota de les quatre mostres. La versió corregida encara ha de passar pel workflow de renderització i una nova comprovació visual.

La revisió de G110 v01 renderitzada confirma que la mateixa escena es conserva recognoscible a través del vidre transparent i acolorit, mentre que l'esmerilat difon els contorns. Es manté l'enfocament conceptual, sense afirmar que simuli refracció, curvatura o reflexos reals. La lectura a mida de pàgina continua pendent.


### Ajust de contrast G006 v03

La renderització inicial de G006 v03 ha mostrat que el títol i les notes del panell RGB tenien contrast insuficient sobre el fons fosc, per una precedència de regles CSS. S'ha corregit l'estil tipogràfic de les classes clares. Cal tornar a renderitzar i comprovar el contrast abans de qualsevol aprovació.


## 19. Iteració G042 v03

La revisió visual de G042 v02 confirma que la geometria de la fulla és constant i recognoscible, però el patró de llum i ombra encara tendeix a llegir-se com una sèrie de franges longitudinals. Per reforçar la relació entre reflexos i geometria, s'ha creat G042 v03 amb dos plans diferenciats a la fulla, una aresta longitudinal i masses de llum/ombra situades en relació amb aquests plans. La v03 resta pendent de renderització i revisió visual; no s'aprova encara cap versió de G042.

### Revisió visual de G003 v02 i G006 v03

La renderització del commit `0b9bec6b62d408a12c47edaed32260586efa1e8b` confirma que G003 v02 ja situa la nota comuna fora de l'àrea dels panells i manté llegibles les quatre mostres conceptuals. G006 v03 presenta els resultats ideals RGB/CMY com a combinacions explícites i separades; després de corregir el contrast de la tipografia clara sobre fons fosc, la lectura és satisfactòria a la resolució del PNG. Ambdues continuen pendents de lectura en la mida real de maquetació i d'aprovació editorial.


## 20. Renderització i revisió visual de G042 v03

El workflow [Render SVG prototype review](https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42136936577) ha completat correctament la validació XML i la renderització dels prototips. El PNG de G042 v03 confirma que la fulla manté la mateixa geometria als sis panells i que els plans superior i inferior es distingeixen millor que a v02. Les masses fosques, la transició intermèdia, el reflex principal i els accents tenen una relació més clara amb els plans de la fulla. La fase 6 introdueix un ajust addicional de transició i jerarquia respecte de la fase 5.

**Dictamen provisional:** G042 v03 és una millora tècnica clara i apta per passar a revisió editorial de contingut i lectura a mida real de pàgina. No queda aprovada ni inserida. Continua identificada com a E1 proposada i no assajada.

La mateixa execució confirma que G003 v02 i G006 v03 renderitzen correctament i que les correccions de composició i contrast es veuen al PNG. Això no substitueix la comprovació a la mida final de maquetació ni l'aprovació editorial.


## 21. Ampliació de producció i revisió preliminar — 06/11/2026

S'han incorporat v01 per a vuit composicions addicionals: G020–G024, G025, G035 i G036. També s'han creat v02 de redisseny per a G007, G009, G011, G012, G013, G014, G016 i G018. Les versions anteriors es conserven.

### 21.1. Revisió conceptual preliminar de les noves v01

| Figura | Criteri de control abans d'aprovar |
|---|---|
| G020 | El pas material → indicis visuals → representació és conceptual, no un procediment físic. |
| G021 | No convertir exemples de metall, vidre i fusta en propietats universals; ajustar-los al contingut exacte de 6.3. |
| G022 | Diferenciar opacitat, transparència i translucidesa sense suggerir llindars mesurats. |
| G023 | La mida i continuïtat del reflex són esquemàtiques; no equiparar-les automàticament amb un únic acabat. |
| G024 | Evitar confondre transmissió definida amb difusió; el fons és un patró conceptual. |
| G025 | La forma del pinzell és esquemàtica i no a escala; contrastar la terminologia amb 7.3.1. |
| G035 | Les formes no representen una miniatura concreta; comprovar les categories d'anàlisi exactes de la fitxa F10. |
| G036 | Escala tonal neutra, no mapa de valors d'una figura; comprovar que no impliqui una distribució tonal concreta. |

Aquestes v01 encara no s'han renderitzat en el workflow actualitzat. Són proves de composició i contingut, no lliuraments finals.

### 21.2. Revisió preliminar dels redissenys v02

Els v02 de G007, G009, G011, G012, G013, G014, G016 i G018 implementen els ajustos descrits a F14. La seva geometria i jerarquia s'han redissenyat, però encara no hi ha validació automàtica de render ni coteig complet amb les fitxes F10. G009 és expressament no quantitativa; G011 requereix verificar el cercle cromàtic exacte del manual; G012–G014 necessiten revisió geomètrica; G016 depèn de la coherència font-objecte-superfície receptora; G018 és un gradient explicatiu, no una simulació.

### 21.3. Dictamen

- Nous prototips v01 creats: 8.
- Redissenys v02 creats: 8.
- Nous prototips renderitzats en aquesta iteració: 0 verificats.
- Aprovacions editorials: 0.
- Insercions al manual: 0.

La prioritat següent és executar el workflow de renderització sobre el conjunt ampliat, revisar les làmines de contacte i després fer el coteig de cada figura amb el capítol i la fitxa F10 corresponents. No s'ha d'inferir aprovació a partir de la mera creació del fitxer SVG.


## 22. Coteig editorial i redisseny de la tanda de 15 prototips — 06/11/2026

### 22.1. Validació del lot anterior

El workflow [Render SVG prototype review](https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42139381801), executat sobre el commit `6f014bddc7bd198224b9bf8da986a671722fd710`, ha finalitzat correctament. Ha validat el XML i ha renderitzat tots els SVG presents al directori en aquell commit. L'artefacte `SVG-prototypes-rendered-review` (ID `13467196423`) conté 33 PNG i una fulla de contacte. Aquesta validació acredita la lectura tècnica del format i l'exportació amb CairoSVG, no la correcció editorial ni l'aprovació de les figures. El lot de 15 redissenys que es documenta a continuació es va crear després d'aquest run i encara no hi estava inclòs.

### 22.2. Incidències detectades en el coteig de les versions prèvies

La revisió visual a 1400 × 900 px i el contrast amb F10 i el text consolidat han detectat:

- **G007:** el cercle de matís repetia el vermell i no identificava els matisos; l'escala de croma modificava també el valor i no aïllava prou la dimensió. Redissenyada amb sis sectors identificats i escales separades.
- **G009:** la forma tridimensional anterior no representava de manera clara les relacions entre els tres eixos i podia llegir-se com un sòlid regular, contrari al límit F10. Redissenyada com a espai conceptual d'eix neutre, gir de matís i distància radial de croma, amb escales independents.
- **G011:** les línies del cercle no distingien correctament les quatre harmonies. Redissenyada en quatre esquemes separats: monocromàtica, anàloga, complementària i complementària dividida.
- **G012:** el símbol de perpendicularitat no es representava correctament al render i un dels raigs no arribava al pla inclinat. Redissenyada amb etiquetatge textual i punts d'incidència coherents.
- **G013:** la geometria dels angles era simètrica, però faltaven caps de fletxa que distingissin el sentit incident i el reflectit. Afegits.
- **G014:** les normals locals dibuixades sobre la corba no eren perpendiculars a les tangents corresponents. Redissenyada sobre un arc circular, amb normals radials que passen pels punts de la superfície; s'han eliminat marques tangencials incorrectes.
- **G016:** la divisió de llum i ombra pròpia no corresponia a la direcció de la font. Redissenyada amb el límit de llum/ombra orientat segons la direcció incident. La projecció exacta de l'ombra encara requereix revisió visual del nou render.
- **G018:** la versió anterior mostrava només una superfície corba i no comparava un pla d'orientació constant amb una corba sota condicions de llum equivalents. Redissenyada en dos panells.
- **G021:** la versió anterior associava respostes superficials a materials concrets sense correspondre a la funció F10. Redissenyada amb quatre patrons genèrics de reflex: definit, estès, fragmentat i poc perceptible.
- **G022:** la translucidesa no difuminava prou la informació del fons. Redissenyada amb superposicions difuses; cal comprovar el resultat al render.
- **G023:** la versió anterior repetia la comparació de reflexos de G021 en lloc de mostrar materials diferents que comparteixen un indici visual. Redissenyada per a aquesta funció F10.
- **G024:** la versió anterior duplicava la comparació d'opacitat/transmissió, en lloc de representar la selecció i simplificació d'indicis a escala miniatura. Redissenyada com a seqüència referència–selecció–representació.
- **G025:** la versió anterior mostrava parts del pinzell però ometia la comparació de formes de punta prevista a F10. Afegides quatre formes.
- **G035:** la versió anterior utilitzava formes abstractes sense representar una miniatura anotada. Redissenyada amb una figura simplificada i crides a silueta, volums, plans, corbes, arestes, superposicions i zones protegides.
- **G036:** la versió anterior era una escala de quatre valors, però F10 demana dos mapes coordinats diferenciats. Redissenyada amb mapa d'il·luminació i mapa de valors sobre siluetes equivalents.

### 22.3. Versions noves creades

- G007, G009, G011, G012, G013, G014, G016 i G018: v03.
- G021, G022, G023, G024, G025, G035 i G036: v02.
- S'han actualitzat F13 i el workflow perquè aquestes 15 versions quedin incloses en la validació obligatòria.

**Estat en tancar aquesta actualització documental:** 15 redissenys creats; pendent executar el workflow sobre el nou commit, inspeccionar els 15 renders a resolució completa i a mida de maquetació, i completar la revisió editorial. Cap dels 15 queda aprovat ni inserit. Els originals i les versions anteriors es conserven.

### 22.4. Límits de la comprovació

La mida de render 1400 × 900 px permet revisar la composició general, però no equival a una prova de maquetació. Cal definir o recuperar la mida física d'inserció i comprovar la llegibilitat dels textos, les línies, les fletxes i les notes a aquesta mida. També cal validar que els esquemes conceptuals no es confonguin amb fotografies, mesures o resultats experimentals.


## 23. Conciliació de discrepàncies entre F10 i F13 — C5 i C7 — 06/11/2026

El coteig de les fitxes F10 amb el text consolidat ha detectat que diverses llegendes de F13 no corresponien a la proposta gràfica d'origen. S'han corregit les files de F13, mantenint F10 com a referència editorial:

- **G015 / P1 5.11:** correspon al bloqueig de llum i formació de l'ombra, no a orientacions de plans i normals.
- **G017 / P1 5.13:** correspon a umbra i penombra, no a la llei de la reflexió (ja tractada per G013).
- **G018 / P1 5.15:** correspon a les senyals visuals que suggereixen volum, no a la comparació de plans i superfícies corbes (G014). La v03 de G018 duplicava parcialment G014 i no es considera vàlida per a aquesta composició; s'ha creat G018 v04 amb el contingut correcte.
- **G026 / P1 7.4:** correspon a la comparació entre aplicació manual amb pinzell, aerògraf i aerosol. L'anatomia del pinzell és G025 / P1 7.2.
- **G028 / P1 7.6:** correspon al control de la imprimació. La classificació E2 es manté bloquejada perquè no hi ha mostres físiques documentades; no es produirà cap comparativa que sembli un resultat observat. F10 permet considerar una alternativa conceptual E0, però encara no s'ha convertit ni aprovat.
- **G029 / P1 7.7:** correspon a la preparació operativa de pintures, no a la preparació de la miniatura (G027 / P1 7.5).

S'han creat prototips per a G015, G017, G018 v04, G026 i G029. G028 continua sense SVG fins a resoldre la condició E2 o autoritzar formalment la via conceptual E0.

**Estat:** conciliació documental feta; cinc SVG nous pendents de renderització i revisió; G028 bloquejada; cap aprovació ni inserció. Aquesta actuació no modifica F10, la selecció de 150 composicions, els capítols consolidats ni la branca `main`.


## 24. Revisió dels renders a 1400 × 900 px i refinament addicional — 06/11/2026

### 24.1. Validació tècnica del lot

El run [Render SVG prototype review](https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42140315249) ha finalitzat amb `success` sobre el commit `61de8f36120a3315bd2464e3d703010a8acebcc8`. L'artefacte `SVG-prototypes-rendered-review` (ID `13467146825`) conté 53 renders PNG i la fulla de contacte. La validació XML i l'exportació amb CairoSVG han estat correctes. El run inclou els 15 redissenys de la secció 22 i els cinc prototips de la secció 23. No inclou encara les set versions refinades d'aquesta secció.

### 24.2. Dictàmens visuals preliminars

- **G007 v03:** lectura clara de les tres dimensions i escales separades; apta per continuar. Cal verificar-la a mida física de maquetació.
- **G009 v03:** el peu de figura desbordava el panell i el croma apareixia etiquetat redundantment als dos extrems. Corregit a v04: peu en dues línies i etiquetatge simplificat.
- **G011 v03:** quatre harmonies diferenciades de manera comprensible. Apta per continuar.
- **G012 v03:** els raigs arriben als plans i les normals es representen perpendiculars; el símbol problemàtic ha estat substituït per text. Apta per continuar.
- **G013 v03:** els caps de fletxa diferencien la direcció incident i reflectida; els angles són simètrics respecte de la normal. Apta per continuar.
- **G014 v03:** la marca central estava al centre de l'arc i no sobre la superfície. Corregit a v04.
- **G016 v03:** el límit de l'ombra pròpia ja responia a la direcció de la font, però F10 demana dos panells amb una mateixa font i geometria de referència. Redissenyat a v04 amb panells separats.
- **G018 v04:** la representació bidimensional no corresponia prou clarament a l'objecte tridimensional. Redissenyat a v05 amb el mateix volum prismàtic i les mateixes relacions de llum, ombra i contorn.
- **G021 v02:** quatre respostes superficials diferenciades, sense assignació automàtica de materials. Apta per continuar.
- **G022 v02:** la translucidesa es diferencia mitjançant difusió esquemàtica; no és simulació òptica. Apta per continuar amb aquest límit explícit.
- **G023 v02:** el suposat indici compartit canviava de forma entre panells. Corregit a v03 amb el mateix reflex horitzontal i estructures diferents.
- **G024 v02:** la seqüència referència–selecció–representació comunica la simplificació. Apta per continuar.
- **G025 v02:** la punta fina era morfològicament incorrecta i la crida al pèl no era prou precisa. Corregit a v03 amb una punta afuada i fletxes de crida.
- **G035 v02:** algunes línies d'anotació es creuaven i dificultaven la lectura. Corregit a v03 amb connectors separats.
- **G036 v02:** els dos mapes mantenen la mateixa silueta i diferencien plantejament lumínic i traducció tonal. Apta per continuar.
- **G015 v01 i G017 v01:** els esquemes de bloqueig, umbra i penombra es llegeixen correctament com a models geomètrics conceptuals. Pendent comprovació a mida de pàgina.
- **G026 v01 i G029 v01:** les funcions previstes es distingeixen; cal revisar la llegibilitat dels pictogrames i de les etiquetes a mida física.
- **G003 v02, G006 v03, G042 v03 i G110 v01:** els renders mantenen els límits conceptuals declarats. No s'atorga aprovació editorial ni s'infereix evidència física.

### 24.3. Noves versions creades

- G009 v04: correcció de peu i etiquetatge.
- G014 v04: punt normal identificat sobre la superfície.
- G016 v04: dos panells comparables per separar ombra pròpia i projectada.
- G018 v05: correspondència entre objecte tridimensional i representació bidimensional.
- G023 v03: indici visual compartit amb la mateixa forma als tres exemples.
- G025 v03: correcció de punta fina i crides anatòmiques.
- G035 v03: connectors d'anotació sense creuaments.

F13 s'ha actualitzat amb aquestes versions i el workflow ara les exigeix com a fitxers esperats.

**Estat:** les set versions noves resten pendents de renderització i inspecció. Els dictàmens «apta per continuar» són només preliminars i no equivalen a aprovació. Cap figura ha estat inserida al manual.

### 24.4. Mida de maquetació

La inspecció de l'artefacte F9 de text confirma pàgina A4 (210 × 297 mm), amb marges esquerre de 18 mm i dret de 16,5 mm. L'amplada útil màxima de text és, per tant, aproximadament 175,5 mm. No s'ha confirmat encara si les figures ocuparan tota aquesta amplada o una columna menor.

A una amplada d'inserció de 175,5 mm, les mides actuals dels SVG de 1400 unitats equivalen aproximadament a: títol 30 unitats = 10,8 pt; subtítol 22 = 7,9 pt; text 18 = 6,5 pt; nota 16 = 5,7 pt. Els textos de 18 i 16 unitats són massa petits per considerar-los aprovables en una pàgina impresa. Com a objectiu provisional, caldria assolir almenys 8 pt en etiquetes i text principal i 7 pt en notes, cosa que requereix aproximadament 23 i 20 unitats SVG respectivament si la figura s'insereix a 175,5 mm. Si la figura s'insereix a una amplada menor, les mides han de créixer proporcionalment.

S'ha actualitzat el workflow perquè generi també renders a 2073 px d'amplada, equivalents a uns 175,5 mm a 300 dpi. Aquests renders permetran inspeccionar la composició a la mida màxima de pàgina, però no substitueixen la revisió tipogràfica ni la prova real de maquetació. Cap figura s'aprovarà fins a resoldre la llegibilitat física.


## 25. Correccions posteriors a la inspecció individual — 06/11/2026

La inspecció individual dels renders ha detectat quatre problemes que no quedaven prou visibles a la fulla de contacte:

- **G016 v04:** la zona d'ombra pròpia formava una geometria triangular no coherent i el raig no acabava exactament a la superfície. Redissenyat a v05 amb el límit d'ombra calculat a partir de la direcció font-centre i amb dos panells diferenciats; el primer aïlla l'ombra pròpia i el segon mostra l'ombra projectada.
- **G018 v05:** la representació bidimensional no incorporava amb prou claredat el mateix reflex del model tridimensional. Afegit el reflex corresponent a v06 per mantenir la correspondència entre les dues representacions.
- **G025 v03:** les fletxes de crida acabaven al costat de les etiquetes, no als components, i la forma de punta fina tenia una concavitat incorrecta. Corregit a v04, invertint les fletxes perquè apuntin a les parts i definint la punta fina com una forma afuada.
- **G035 v03:** dues línies de crida de la banda dreta es creuaven i la línia de zones protegides apuntava massa avall. Redissenyat a v04 amb recorreguts ortogonals separats i un punt d'ancoratge més pertinent.

F13 i el workflow s'han actualitzat amb aquestes versions. **Estat:** quatre noves versions creades, pendents de renderització i inspecció; cap aprovació ni inserció.


## 26. Prova de mida física màxima A4 i observacions addicionals — 06/11/2026

### 26.1. Execució del workflow

El run [Render SVG prototype review](https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42140985098) ha finalitzat correctament sobre el commit `7814c3661bbd07f824ea9686079226dc2ac16757`. L'artefacte `SVG-prototypes-rendered-review` (ID `13467778182`) conté 64 renders estàndard, 64 renders addicionals a 2073 px d'amplada i una fulla de contacte. El workflow valida XML, exporta amb CairoSVG i comprova que els fitxers esperats existeixen. Els renders a 2073 px corresponen aproximadament a 175,5 mm a 300 dpi.

### 26.2. Inspecció a mida màxima

S'han inspeccionat individualment diversos renders a mida màxima:

- **G007 v03:** les tres escales i les etiquetes es mantenen llegibles a amplada màxima.
- **G009 v04:** les etiquetes principals i el peu caben dins la composició; continua sent un esquema conceptual, no un sòlid Munsell.
- **G014 v04:** les tres normals passen pels punts de l'arc i són radials; la marca central s'ha corregit perquè se situï sobre la superfície.
- **G016 v05:** els dos panells separen ombra pròpia i projectada; la direcció de la zona d'ombra pròpia és coherent amb la font.
- **G018 v06:** el mateix prisma es representa en el model tridimensional i en la traducció bidimensional, amb relacions de llum, ombra i reflex corresponents.
- **G025 v04:** les fletxes apunten als components i la punta fina té una forma afuada.
- **G035 v04:** les línies de crida ja no es creuen; els punts d'ancoratge són més específics.
- **G017 v01:** la distribució de penombra–umbra–penombra és coherent amb la font extensa, l'objecte opac i la pantalla.
- **G015 v01:** l'etiqueta «raig bloquejat» s'havia col·locat sobre el raig tangent que defineix el límit de l'ombra. Corregit a v02 amb un raig bloquejat interromput per l'objecte i una etiqueta separada per al límit geomètric.

Aquesta inspecció no equival a una prova d'impressió. No s'han inspeccionat encara, a mida màxima i amb el mateix nivell de detall, tots els 64 fitxers.

### 26.3. Tipografia i criteri de llegibilitat

Les mides actuals de text de 16–18 unitats SVG equivalen aproximadament a 5,7–6,5 pt si la figura ocupa tota l'amplada útil. Encara que algunes etiquetes es llegeixin al render ampliat, són petites per a una publicació tècnica impresa. Es manté com a objectiu provisional un mínim de 8 pt per a etiquetes i text principal i 7 pt per a notes. Caldrà adaptar els SVG actius a aquesta escala o justificar excepcions per a etiquetes auxiliars, i tornar a renderitzar i comprovar els possibles desbordaments. Per tant, **cap figura queda aprovada per a inserció**.

### 26.4. Estat del màster

L'artefacte F9 inspeccionat és una compilació de text sense imatges, en format A4. Aquesta inspecció només s'ha utilitzat per calcular l'amplada màxima útil; no s'ha modificat ni substituït el màster. La còpia il·lustrada encara no s'ha creat ni s'ha inserit cap imatge.


## 27. Protocol preparatori per a G028 — 06/11/2026

S'ha creat `annexos/protocol_prova_fisica_G028.md` per documentar la comparació entre cobertura insuficient, adequada i excessiva de la imprimació i la conservació del relleu. El protocol exigeix mostres comparables, variables d'aplicació registrades, rèpliques quan sigui possible, fotografia amb configuració controlada i separació entre observació i interpretació.

**No s'ha executat cap prova.** No hi ha mostres, fotografies ni resultats. G028 continua classificada E2 i bloquejada. El protocol no autoritza a representar cap resultat hipotètic com a observat. Si no es pot executar la prova, només es podrà utilitzar una figura conceptual E0 després de la decisió i actualització formal corresponents.


## 28. Ampliació de la recerca visual — tandes 02–04 — 06/11/2026

S'han documentat tres tandes addicionals de recursos amb autoria, llicència, dimensions i límits d'ús:

- **Tanda 02:** 12 candidatures (fusta, roca, líquens, vellut, fibra de seda, foc, aigua i condensació), més 2 recursos en reserva o descartats.
- **Tanda 03:** 8 candidatures (pinzells, aerògraf, aerosols i paletes), més 4 recursos en reserva o descartats.
- **Tanda 04:** 8 candidatures (cuir, metall corroït, ceràmica esmaltada, terracota digital i pergamí), més 4 recursos en reserva o descartats.

S'ha creat l'índex `annexos/registre_recerca_visual_index.md`. El balanç de les tandes 02–04 és de 28 candidatures amb llicència identificada i 10 recursos en reserva o descartats. No són 28 recursos necessàriament únics ni 28 seleccions finals: tots resten pendents de coteig amb F10 i el text lector.

**Cap recurs s'ha descarregat, adaptat ni inserit.** No s'ha modificat F10 ni la selecció de 150 composicions. Les textures PBR, mapes normals, imatges generades i fotografies de materials reals s'han mantingut com a tipologies diferenciades.


## 29. Validació final del lot SVG i G015 v02 — 06/11/2026

El run [Render SVG prototype review](https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42141686934) ha finalitzat correctament sobre el commit `7a262b94bb99c8f805fa637c52236d9cecda42a6`. L'artefacte `SVG-prototypes-rendered-review` (ID `13468480370`) conté:
- 65 renders PNG estàndard;
- 65 renders PNG a 2073 px d'amplada (mida màxima A4 útil aproximada);
- una fulla de contacte.

Els 65 fitxers SVG del directori han superat la validació XML i l'exportació CairoSVG. El recompte inclou versions històriques i redissenys, no 65 composicions diferents. F13 conté 29 referències SVG actives corresponents a 24 composicions G diferents.

**G015 v02** ha estat renderitzada a mida màxima: el raig interromput per l'objecte queda separat del raig tangent que defineix el límit de l'ombra. La distinció entre raig bloquejat, raig no bloquejat i límit de l'ombra és ara llegible.

Aquesta validació confirma el render tècnic dels 65 fitxers, no la seva aprovació editorial. La inspecció individual a mida màxima s'ha fet sobre una selecció representativa i sobre les figures amb incidències detectades; no s'ha completat encara una revisió exhaustiva de cada versió històrica. Les 24 composicions amb prototip continuen pendents de revisió editorial i tipogràfica; les altres 126 composicions no tenen encara un prototip SVG actiu referenciat a F13.

Cap SVG s'ha inserit al manual. F10, la selecció de 150 composicions, els capítols consolidats, `main` i el màster de text sense imatges romanen sense modificacions.


## 30. Recerca visual — tanda 05 — 06/11/2026

S'ha afegit `annexos/registre_recerca_visual_tanda_05.md`, centrada en escorça, molsa, líquens, falgueres, gel i malla metàl·lica. S'hi documenten 13 recursos amb autoria i llicència identificades i un recurs descartat per resolució molt baixa i permís de reutilització insuficientment acreditat.

Amb les tandes 02–05, el registre acumula 41 candidatures noves amb autoria i llicència identificades i 11 recursos en reserva o descartats. Aquest recompte és documental: no equival a 41 recursos únics ni a 41 imatges aptes per al manual. No s'ha descarregat ni incorporat cap recurs; tots resten pendents de coteig amb F10, del text lector i dels drets subjacents.


## 31. Verificació dels workflows sobre el commit actual — 06/11/2026

- El run [Render SVG prototype review](https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42141938963), sobre el commit `ba446439c849ee0ea90d85717969f6363b7d5b1`, ha finalitzat correctament. L'artefacte `SVG-prototypes-rendered-review` (ID `13467714801`) conté 65 renders estàndard, 65 renders a mida màxima de pàgina i una fulla de contacte. S'han validat els SVG i s'han exportat amb CairoSVG.
- El run [Build F9 Word master](https://github.com/nbarreraska-cloud/manual-tecnico/actions/runs/42141938930) també ha finalitzat correctament. La generació del DOCX i l'auditoria d'ordre i fidelitat textual han estat correctes; l'artefacte de sortida és `Manual-tecnic-pintura-miniatures-F9` (ID `13468297679`). És una compilació d'artefacte, no una modificació de `main` ni del màster de treball.

Aquests dos runs corresponen al commit de treball amb els registres de recerca fins a la tanda 05. No s'ha canviat cap capítol consolidat ni F10. La branca `main` continua al SHA `a4ce8192e30178b0171ea02a3af230b60efd3768`; els canvis d'aquesta fase romanen a `intervencion-editorial-2026-11`.
