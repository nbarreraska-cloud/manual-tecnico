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

