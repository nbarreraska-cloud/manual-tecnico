# REGISTRE MESTRE DE RECUPERACIONS EDITORIALS
**Manual tècnic de pintura de miniatures**  
**Versió:** 1.73 · **Data:** 05/11/2026  
**Branca:** intervencion-editorial-2026-11

## 1. Funció i abast

Aquest registre és el document operatiu únic per controlar les recuperacions detectades en l'auditoria comparativa dels 39 capítols de la segona síntesi. No substitueix els capítols, les fonts ni el document de seguiment: relaciona diagnòstic, decisió editorial, prioritat, aplicació i validació.

La primera versió és el document amb l'estructura completa sintetitzada, conservat al repositori com a HTML. La segona síntesi font consta de **dos fitxers** i conté exclusivament els 39 capítols del manual, sense els annexos. Per facilitar el treball i la traçabilitat per capítol, aquesta branca desplega el contingut en **39 fitxers Markdown individuals**, distribuïts en dues carpetes:
- segunda_sintesis/: capítols 01–11.
- segunda_sintesi/: capítols 12–39.

Aquests 39 Markdown són la representació operativa de treball sobre els continguts de la segona síntesi i el suport de la tercera versió; no s'han de confondre amb els dos fitxers font de la segona síntesi. La tercera versió és el resultat de les intervencions aplicades a aquesta representació per capítol. L'HTML de la primera versió queda fora d'aquest flux i no s'hi ha d'intervenir durant aquesta fase.

## 2. Fases generals i estat

| Fase | Objectiu i lliurable | Estat |
|---|---|---|
| 0 | Preservar les versions, les fonts, la traçabilitat i la branca de treball; vincular cada intervenció amb capítol/apartat/font i mantenir main intacta. | **Completada** |
| 1 | Auditoria comparativa dels 39 capítols Markdown: contingut conservat, simplificacions, pèrdues, redundàncies i millores de la segona síntesi. | **Completada (39/39)** |
| 2 | Consolidar el Registre Mestre amb categories RT/RD/AE/MG/SC, prioritats, decisions, fonts i estat real dels canvis. | **En curs**; versió vigent 1.72. S'ha actualitzat la matriu amb el tancament documental de F4 per als 39 capítols: coteigs complets, revisions limitades per absència d'original íntegre i revisions del contingut disponible, amb els límits de font documentats. Resta una conciliació final de totes les files i anotacions històriques per assegurar que no quedin estats contradictoris. |
| 3 | Aplicar les recuperacions tècniques, didàctiques i els ajustos editorials justificats a la tercera versió dels 39 Markdown. | **Completada per a les accions identificades a la matriu**; recuperacions aplicades als capítols 3–19, 25–32, 36 i 38; ajustos AE als capítols 33–34; els capítols SC es mantenen protegits, excepte ajustos editorials documentats. |
| 4 | Validar els 39 capítols i estabilitzar-ne el contingut, les receptes, els exercicis, la numeració i les referències. | **Completada el 05/11/2026, amb límits documentals registrats**; els 39 capítols han rebut una revisió de contingut o una comprovació documental del material disponible. C1–C10, C12–C13, C20–C29, C33–C35 i C37–C39 tenen coteig documental completat; C11 i C14–C19 s'han contrastat amb material consolidat disponible, però les fonts declaren que no s'han recuperat originals complets; C30–C32 i C36 tenen revisió de contingut completada amb la font disponible; C38 té coteig documental completat dins dels límits registrats. La revisió semàntica de remissions C1–C39 i la comprovació estructural global dels 39 Markdown estan completades. Aquesta fase no equival a validació experimental de receptes ni de resultats pictòrics. |
| 5 | Revisar i reconstruir els annexos A–E després d'estabilitzar els 39 capítols. | **En curs**; iniciada l'auditoria de l'Annex C: 183/183 entrades contrastades amb les receptes dels capítols 19–34; 170 referències actualitzades i 13 ja correctes. Resta la comprovació de coherència amb l'Annex D i l'auditoria dels annexos A, B, D i E. |
| 6 | Auditoria global de coherència, referències creuades, traçabilitat i absència de pèrdues o duplicacions. | **Completada el 05/11/2026**; auditoria transversal C1–C39 tancada. No s'han detectat contradiccions globals que justifiquin reorganitzacions o retallades. No equival a validació experimental. |
| 7 | Revisió gràfica, consolidació editorial i maquetació Word. | **Pendent**; les 243 propostes MG (153 originals i 90 addicionals) s'han separat del contingut lector i es conserven a `PLANIFICACIO_GRAFICA_MG_FASE_POSTERIOR.md`; la producció i maquetació gràfica encara no s'han iniciat i s'abordaran després de F5. |

La primera versió amb l'estructura completa sintetitzada i la segona síntesi dels 39 capítols són fonts diferenciades. La tercera versió és el resultat del treball actual sobre els 39 Markdown. La compilació documental única dels capítols 1–39 s'ha creat i sincronitzat amb els 39 Markdown. F4 i F6 estan tancades amb els límits documentals registrats; abans d'iniciar F5 cal completar la conciliació de F2 i confirmar la sincronització final. La fase gràfica i la maquetació (F7) queden després dels annexos.

### 2.1. Intervencions editorials històriques G-01–G-11

Aquestes intervencions pertanyen al treball previ sobre la primera versió HTML, principalment el fitxer copia_trabajo/index.html. No s'han de confondre amb les recuperacions RT/RD/AE que s'estan aplicant ara als 39 Markdown.

| Intervenció | Abast i decisió | Estat i traça |
|---|---|---|
| G-01 | Cap. 1 §1.5; cap. 3 §§3.1 i 3.4.3. Manté les quatre categories de fonts d'informació, elimina la formulació de «tres nivells» i separa la naturalesa/procedència de la informació del seu estat per propietat (Observed, Checked, Pending verification). | Aprovada i aplicada a l'HTML. Commit 4f8fed338ba515a21ce826749e6c0a3a59941ec3. |
| G-02 | Cap. 1 §§1.1–1.2 i cap. 2 §§2.1, 2.4–2.6; depuració de redundàncies. | Aplicada a l'HTML. Commit eeca29efcbb9541bd23c4705eccd0c75fb77dbd0. |
| G-03 | Coteig dels capítols 3–5; no es van justificar canvis conceptuals addicionals. | Tancada sense canvis ni commit. |
| G-04 | Intervenció revisada; no es va justificar cap modificació. | Tancada sense canvis ni commit. |
| G-05 | Cap. 33 §33.2.2; precisió de la referència a la translucidesa. | Aplicada a l'HTML. Commit 472362b9abe02549b937e9ef61257efe221af673. |
| G-06 | Revisada segons l'auditoria editorial. | Tancada sense canvis. |
| G-07 | Revisada segons l'auditoria editorial. | Tancada sense canvis. |
| G-08 | Cap. 37 §§37.1, 37.6 i 37.7; delimitació de l'acabat i la protecció. Es van preservar els §§38.1 i 38.2.5; no es van alterar procediments, exercicis ni advertiments. | Aprovada, aplicada i verificada a l'HTML. Commit ac14f4557ad07ec0165c63985479e5a2dc8b74c6. |
| G-09 | Annex A §A.6; compactació de la traçabilitat i actualització, preservant sis criteris operatius. | Aprovada i aplicada a l'HTML. Commit 2cc7d492d69a7dd0ba0ca54a38071f7f8f1eaba9. |
| G-11 | Revisió de l'abast de les fonts; el canvi registrat concreta l'abast de les fonts al capítol 33 dins de la primera versió HTML. | Aplicada a copia_trabajo/index.html. Commit 1cc8f7c293a5cbfac1d8f1e04d8810790ca8e3cd. No s'ha de tornar a aplicar automàticament als 39 Markdown. |

Els commits G-01, G-02, G-05, G-08, G-09 i G-11 afecten el fitxer HTML de la primera versió, no constitueixen per si mateixos canvis als fitxers Markdown de la tercera versió. G-03, G-04, G-06 i G-07 es van tancar sense modificacions.

## 3. Categories de classificació

Una mateixa intervenció pot tenir més d'una categoria.

| Codi | Categoria | Què inclou |
|---|---|---|
| **RT** | Recuperació tècnica | Fonaments, explicacions físiques o materials, procediments, variables, criteris de control, correccions, formulacions o detalls operatius que s'havien comprimit o omès. |
| **RD** | Recuperació didàctica | Exercicis, objectius, seqüències d'aprenentatge, errors explicats, criteris d'avaluació, exemples i recursos que milloren la comprensió i l'aplicació. |
| **AE** | Ajust editorial | Terminologia, numeració, estructura, límits entre capítols, referències creuades, coherència i retirada de notes internes del cos del manual. |
| **MG** | Material gràfic | Figures, esquemes, comparatives, seqüències i planificació de recursos visuals per a una fase gràfica posterior. |
| **SC** | Sense canvis | Contingut que l'auditoria considera correcte, suficient i que s'ha de protegir de modificacions innecessàries. |

### Prioritats

- **Alta:** pèrdua tècnica o didàctica rellevant que afecta la comprensió, l'execució o la consulta.
- **Mitjana:** recuperació o ajust útil, però no crític per a la funcionalitat immediata del capítol.
- **Baixa:** millora complementària o de refinament; no ha de bloquejar el progrés.

## 4. Criteris de decisió i protecció

1. Recuperar el màxim contingut tècnic, didàctic i pràctic que aporti valor, mantenint síntesi i evitant redundàncies.
2. No recuperar una explicació completa quan ja estigui ben conservada en un altre capítol; aplicar referències creuades quan sigui suficient.
3. No eliminar procediments, receptes, ingredients, seqüències ni advertiments per assolir una xifra de pàgines.
4. No inventar proporcions, proves físiques, resultats, compatibilitats ni propietats de productes que no estiguin documentades.
5. Distingir les propostes de mescla dels resultats experimentals. Les receptes no assajades continuen identificades com a propostes.
6. Respectar l'arquitectura de 39 capítols. No crear capítols nous ni alterar-ne l'ordre sense una justificació substancial.
7. No reobrir capítol tancat per observacions menors. Reobrir només davant errors reals, contradiccions importants o incidències de coherència global.
8. Les propostes de figures es mantenen com a especificacions editorials en un document MG independent; no formen part del contingut lector de la tercera síntesi ni es presenten com a imatges produïdes o proves físiques.
9. Cada intervenció ha de distingir quatre estats: **diagnosticada**, **decidida**, **aplicada** i **validada**. Un canvi aplicat no queda automàticament validat.
10. La branca intervencion-editorial-2026-11 és la branca de treball; main no s'ha de modificar.
11. L'objectiu d'extensió de la tercera versió és aproximadament 350–375 pàgines, amb un límit orientatiu d'unes 400. És un criteri de control, no una ordre de retall: no s'ha de suprimir contingut tècnic, procediments, receptes, exercicis, variants ni advertiments només per reduir pàgines.

## 5. Matriu de classificació de l'auditoria 39/39

Aquesta matriu conserva el dictamen comparatiu recuperat de l'auditoria. La classificació no implica que totes les accions estiguin ja aplicades o validades.

| Cap. | Categoria / prioritat | Dictamen de l'auditoria i estat conegut |
|---:|---|---|
| 1 | SC / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». S'han recuperat les dues propostes gràfiques per a MG: organització general del manual i classificació de la informació tècnica, amb ubicació, format, contingut i funció. Es manté diferenciada l'antiga intervenció G-01 aplicada a HTML, no a aquest Markdown. No s'han modificat els continguts tècnics. La compilació conté exactament el fitxer vigent. |
| 2 | SC / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserva l'inventari de 48 pintures en quatre conjunts. S'han recuperat la síntesi del capítol i les dues propostes gràfiques per a MG: organització de la paleta i relació entre inventari, annex A, caracterització tècnica i aplicació pràctica. No s'han modificat les referències ni la composició de la paleta. La compilació conté exactament el fitxer vigent. |
| 3 | RT · mitjana; AE puntual | Recuperar/confirmar els vuit errors conceptuals i el mètode cromàtic segons auditoria. G-01 es va aplicar a l'HTML, no a aquest Markdown; G-03 no va justificar recuperacions conceptuals addicionals als capítols 3–5. F4: coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven les distincions entre opacitat, transparència i cobertura; càrrega de pigment, intensitat i poder tintori; fluïdesa, consistència i distribució sobre relleus; acabat i assecat; les set famílies comercials, la selecció funcional, les proves proposades, la traçabilitat per procedència i estat, els vuit errors i la síntesi operativa. S'han recuperat les sis propostes de figures amb ubicació i descripció, i els criteris de producció gràfica. No s'han atribuït propietats individuals no verificades ni s'han presentat proves proposades com a resultats. La compilació s'ha sincronitzat. Aquest coteig documental no constitueix validació experimental. |
| 4 | RT · mitjana / AE puntual | Errors conceptuals i desenvolupament del mètode cromàtic. Recuperació aplicada: nou errors, sis exercicis, síntesi, criteri de selecció de paleta, vuit passos de planificació i exemple de l'armadura blava. F4: coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven els fonaments de percepció i context (llum, context visual i adaptació); els models RYB, RGB i CMY; les dimensions de matís, valor i croma; la temperatura cromàtica; les harmonies, els contrastos i la jerarquia visual; la mescla física, òptica i la superposició transparent; el registre de mescles; els set criteris de planificació; l'exemple de l'armadura blava; els nou errors; els sis exercicis; i les vuit referències bibliogràfiques. Les nou propostes de figures originals es mantenen reservades a MG. No s'han identificat omissions substancials que justifiquin modificar el capítol. No s'ha modificat C4; la compilació conté exactament el fitxer vigent. Aquest coteig documental no constitueix validació experimental. |
| 5 | RT · mitjana | Desenvolupament físic de llum i ombres i errors conceptuals. Recuperació aplicada: set errors, sis exercicis, bloqueig/oclusió, geometria de les ombres i llistes d'observació. F4: coteig de contingut i bibliografia completat amb la font disponible; es conserven els conceptes centrals de propagació, fotometria, geometria, absorció/reflexió/transmissió, ombres, reflexos, volum i anàlisi de miniatures. Es mantenen set errors i sis exercicis; s'han recuperat vuit referències bibliogràfiques omeses (12 referències en total). Les 16 propostes de figures es reserven per a MG. No s'han modificat receptes ni s'atribueixen resultats experimentals. |
| 6 | RT · mitjana | Recuperar la fitxa i els criteris de lectura dels materials. Ampliació aplicada amb patrons estructurals, propietats de transmissió, mètode d'observació i quatre exercicis. F4: coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven els fonaments de material i aparença; estructura, geometria, textura i patrons; resposta òptica i respostes direccionals; transparència, translucidesa, opacitat i profunditat interna; reconeixement i límits de la identificació visual; selecció, jerarquia i simplificació de senyals a escala miniatura; fitxa d'anàlisi; deu errors; mètode d'observació de set passos; quatre exercicis; i cinc referències. Les vuit propostes de figures originals es mantenen reservades a MG. No s'han identificat omissions tècniques o didàctiques substancials que justifiquin modificar C6. No s'ha modificat C6; la compilació conté exactament el fitxer vigent. Aquest coteig documental no constitueix validació experimental. |
| 7 | SC / MG | Contingut base protegit en l'auditoria inicial; posteriorment ampliat en preparació, eines, manteniment i seguretat. F4: coteig de contingut completat amb «manual con estructura completa.docx»; es conserven els blocs 7.1–7.9, incloses les subdivisions operatives agrupades, els quatre exercicis complets, els criteris de seguretat i les tres referències de consulta. No s'han identificat omissions tècniques o didàctiques substancials que justifiquin una recuperació addicional. Les vuit propostes de figures originals es mantenen fora del text de lectura i reservades a MG. No s'ha modificat C7. |
| 8 | SC / RD / MG | Contingut protegit en l'auditoria inicial, posteriorment ampliat en errors, controls i exercicis. F4: coteig de contingut completat amb «manual con estructura completa.docx»; es mantenen els fonaments de construcció per capes, la distinció entre cobertura/transparència/continuïtat/uniformitat, els procediments de capa base i aplicacions successives, les variants de construcció, el control tècnic, els sis errors i les correccions, els criteris d'avaluació i els cinc exercicis pràctics, inclòs l'integrador. No s'han identificat omissions substancials que justifiquin recuperacions addicionals. Les vuit propostes de figures originals es mantenen reservades a MG. No s'ha modificat C8. |
| 9 | SC / MG | Contingut protegit. F4: coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven els fonaments i distincions entre degradat, transició contínua, esglaonada i separació de plans; les dimensions de matís, valor i croma; les variables de pintura, geometria, extensió, quantitat i seqüència; els tres procediments principals i la combinació; la planificació i execució; les variants de transició; el control tècnic; els sis errors i les correccions; els criteris d'avaluació; els sis exercicis, inclòs l'integrador; i la síntesi final. No s'han identificat omissions tècniques o didàctiques substancials que justifiquin recuperar més contingut. La referència de l'original a la planificació de llum i ombra del capítol 17 s'ha actualitzat correctament al capítol 15, d'acord amb l'arquitectura vigent. Les vuit propostes de figures originals es mantenen reservades a MG, fora del text de lectura. No s'ha modificat C9. |
| 10 | SC / MG | Contingut protegit per l'auditoria inicial; posteriorment desenvolupat i reorganitzat. F4: coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven les definicions i diferències entre veladura i glassejat, transparència pròpia del producte i efecte de l'aplicació, delimitació respecte de capes base, degradats, rentats, tintes i transparències de materials; les sis funcions; selecció de pintures, aigua i mitjans, preparació i estat de la superfície; procediment complet; cinc variants; cinc controls i criteri de finalització; set errors amb causes, conseqüències i correccions; criteris d'avaluació; sis exercicis complets, inclòs l'integrador; i síntesi. No s'han identificat omissions tècniques o didàctiques substancials. Les vuit propostes de figures originals es mantenen reservades a MG, fora del text lector. No s'ha modificat C10. Aquest coteig no constitueix validació experimental. |
| 11 | RT · alta | Intervenció aplicada i tancada editorialment. F4: s'ha contrastat el Markdown amb el contingut consolidat disponible a «manual con estructura completa.docx». Es mantenen els blocs 11.1–11.10, els vuit errors, els sis exercicis i la síntesi, sense omissions substancials identificades en aquesta versió de referència. Les vuit propostes de figures continuen reservades a MG. La font declara que no s'ha recuperat l'original complet; per tant, no es pot afirmar un coteig integral amb l'original ni una validació experimental. No s'ha modificat C11. |
| 12 | RT · alta / AE de metadades resolta | F4: coteig de contingut completat amb la font disponible; coincideixen fonaments, cinc tipus de perfilat, selecció cromàtica, materials/eines, sis procediments d'aplicació, cinc exercicis (12.10.1–12.10.5), controls i vuit errors. No s'han identificat omissions substancials en el contingut lector. La nota «Registre editorial del capítol 12» de la font conté una delimitació desfasada: atribueix part de les tècniques de textura a C14. L'índex definitiu i els continguts efectius confirmen que les quatre tècniques (pinzell sec, puntejat, ratllat i esponjat) pertanyen a C13, mentre que C14 tracta transparències. Incidència conciliada com a metadada obsoleta de la font; no es modifica C12, C13 ni C14. |
| 13 | RT · alta | F4: coteig de contingut completat amb la font disponible; es conserven les quatre tècniques (pinzell sec, puntejat, ratllat i esponjat), els procediments, les variables, aplicacions i limitacions, la combinació de tècniques, els nou blocs d'errors i els sis exercicis (13.10.1–13.10.6). No s'han identificat omissions substancials en el contingut lector. Les vuit propostes gràfiques es mantenen reservades a MG. |
| 14 | SC / RD / AE / MG · F4 limitada | No s'ha recuperat un original complet; la revisió es limita al material consolidat disponible. Es mantenen els fonaments de transparència, translucidesa i opacitat; les senyals de transmissió, fons, contorns, reflexos, refracció, difusió i estructura interna; la planificació, els procediments, els controls, nou errors, sis exercicis i vuit propostes gràfiques. S'han recuperat precisions sobre longitud d'ona, absorció selectiva i coloració interna, variacions de color aparent i distorsió per gruix/curvatura, avaluació des de la distància habitual i tractament no uniforme de vores i reflexos. La compilació s'ha sincronitzat. No es pot afirmar fidelitat integral a un original no recuperat ni validació experimental. |
| 15 | SC / RD / AE / MG · F4 limitada | No s'ha localitzat un text original complet; el capítol és una consolidació basada en material disponible i acords recuperats. S'ha revisat aquest material i s'han recuperat desenvolupaments condensats en la versió Markdown: distincions de funció del valor, jerarquia tonal de cinc nivells funcionals, planificació específica per zones, diagnòstic i correcció dels deu errors, vuit criteris d'avaluació i desenvolupament procedimental dels sis exercicis. Les vuit propostes de figures es mantenen reservades a MG. S'ha corregit «sombra» per «ombra». No es pot declarar coteig integral amb un original no recuperat ni validació experimental. |
| 16 | AE / RD / MG · F4 limitada | Ajust de numeració i estructura de les geometries aplicat; contingut NMM ampliat posteriorment. No s'ha recuperat un original complet; la revisió es limita al contingut consolidat disponible. S'han recuperat desenvolupaments sobre aparença metàl·lica, funció del contrast, reflexos com a informació de l'entorn, simplificació pictòrica, orientació i patrons de reflexos, planificació prèvia, criteris d'avaluació i procediment dels sis exercicis. Es mantenen les deu tipologies d'error i les vuit propostes gràfiques reservades a MG. S'ha evitat repetir les famílies cromàtiques desenvolupades a 16.4. No es pot afirmar coteig integral amb l'original ni validació experimental. |
| 17 | SC / MG · F4 limitada | La font declara que és una versió consolidada nova i que no s'ha recuperat un original complet. S'ha revisat la correspondència amb el material consolidat disponible: es mantenen els fonaments de l'OSL, la distinció entre font, superfície il·luminada i reflex, la planificació espacial i cromàtica, el procediment, l'adaptació a geometries i materials, els controls, els dotze errors, els sis exercicis i les deu propostes de figures. No s'han detectat omissions substancials en aquests blocs. No s'ha modificat C17; la compilació ja conté exactament el fitxer vigent. No es pot afirmar coteig integral amb l'original ni validació experimental. |
| 18 | SC / AE / MG · F4 limitada | La font declara que no s'ha recuperat un original complet; la revisió es limita al material consolidat disponible. Es mantenen els deu apartats, sis exercicis i les eines de planificació i avaluació. La remissió a C35–C38 està precisada per diferenciar harmonització cromàtica (C35), desgast i transformació (C36), acabats superficials (C37) i protecció/conservació (C38). S'ha detectat i recuperat una proposta gràfica absent: el mapa del procés integral que relaciona anàlisi, planificació, selecció, execució, control i avaluació. Ara es conserven nou propostes de figures. No es pot afirmar coteig integral amb l'original ni validació experimental. |
| 19 | SC / RD / AE · F4 limitada | La font és una versió consolidada nova i declara que no s'ha recuperat un original complet. S'han contrastat els cinc metalls, les quatre pintures metàl·liques disponibles, les 16 receptes, els procediments TMM, els acabats, les taules d'errors, la comparació TMM/NMM, els criteris de selecció i control, els set exercicis i les nou propostes de figures. S'han recuperat les causes dels errors, els objectius i resultats esperats dels exercicis, la taula comparativa TMM/NMM i precisions de jerarquia visual; s'ha retirat una taula de paleta duplicada. No s'han alterat ingredients, codis ni combinacions, ni s'han inventat proporcions. Les receptes continuen sent propostes no assajades. La compilació s'ha sincronitzat. No es pot afirmar coteig integral amb l'original ni validació experimental. |
| 20 | SC / RD / MG · F4 completada | Coteig documental de contingut completat amb l'original. Es conserven les nou receptes A–I i les referències de les deu pintures de la paleta; no s'han inventat proporcions ni s'han presentat les mescles com a assajades. S'han recuperat les seqüències de les receptes G, H i I, el desenvolupament dels patrons de vetes, nusos i anells, l'adaptació per escala i geometria, el diagnòstic i la correcció dels deu errors, els sis exercicis amb procediment i avaluació, i les tres referències bibliogràfiques omeses. Les nou propostes de figures es mantenen. La compilació s'ha sincronitzat. |
| 21 | SC / RD / MG · F4 completada | Coteig documental de contingut completat amb l'original. Es conserven les setze combinacions A–P i les referències de les divuit pintures; es manté la denominació «combinació cromàtica proposada» i no s'inventen proporcions ni proves. S'han recuperat seqüències d'aplicació de les combinacions A, D, F, G i P, els criteris d'adaptació a escala, els diagnòstics i correccions dels deu errors, set criteris d'avaluació, els set exercicis amb avaluació i les set referències bibliogràfiques omeses. Les deu propostes de figures es mantenen. La compilació s'ha sincronitzat. Les combinacions continuen sent propostes no assajades. |
| 22 | SC / RD / AE / MG · F4 completada | Coteig documental de contingut completat amb l'original. Es conserven les disset receptes A–Q i les referències de les dotze pintures; no s'afegeixen proporcions ni propietats tècniques no verificades. S'han recuperat el desenvolupament dels deu errors amb diagnòstic i correcció, deu criteris d'avaluació, els sis exercicis amb objectius, materials, procediments i avaluació, les set referències de conservació i indústria de la pell i els límits editorials de verificació. Es mantenen les deu propostes gràfiques i les delimitacions amb pell corporal (C24), tèxtils (C23), acabats (C37), protecció (C38) i diagnòstic general (C39). La compilació s'ha sincronitzat. Les receptes continuen sent propostes no assajades. |
| 23 | SC / RD / AE / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven les deu receptes A–J, les pintures i les seqüències cromàtiques proposades, sense afegir proporcions ni atribuir resultats experimentals. S'han recuperat els objectius, materials, procediments i criteris d'avaluació dels sis exercicis, així com les cinc referències bibliogràfiques amb els seus enllaços. Es mantenen les vuit propostes de figures. S'han comprovat també les distincions entre fibres, estructures de teixit, textura, gruix, caiguda i acabats; els procediments per a teixits clars, llana, superfícies setinades i vellut; l'adaptació d'estampats, brodats i bandes; els nou errors i els criteris d'avaluació. S'ha eliminat una segona secció «Referències i recursos» duplicada al Markdown; la primera còpia s'ha conservat. La compilació s'ha sincronitzat i verificat després de l'ajust editorial. Les receptes continuen sent propostes no assajades. |
| 24 | SC / RD / AE / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven les catorze receptes A–N i les seves combinacions sense afegir proporcions ni atribuir resultats experimentals. S'han recuperat els objectius, materials, procediments i criteris d'avaluació dels sis exercicis, que la síntesi havia reduït a instruccions breus; també s'han recuperat els enllaços de les set referències anatòmiques, de pigmentació i d'aplicació. S'han explicitat els criteris d'avaluació diferenciats per a pell i teixits orgànics. Es mantenen les nou propostes de figures. C24 i la compilació s'han sincronitzat i verificat. Les receptes continuen sent propostes no assajades. |
| 25 | RD / AE / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis complets, la síntesi i les dues referències opcionals absents; restaurat també l'enllaç de la British Horse Society. Reforçats dos errors i el criteri de selecció cromàtica. Les 10 propostes gràfiques originals es reserven per a MG. F4: coteig completat; restituïdes les tres referències de paleta absents, sense alterar receptes. Receptes no assajades. |
| 26 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, materials, procediment i avaluació; recuperada la síntesi; afegits dos errors freqüents absents de la segona síntesi. Les nou propostes gràfiques originals es reserven per a MG. F4: coteig completat; 10 receptes, sis exercicis i 19 referències de paleta preservats. Receptes no assajades. S'ha normalitzat «arenisca» a «gres» a C26, amb concordança gramatical revisada segons la terminologia de ciències de la Terra (TERMCAT/IEC: https://cit.iec.cat/progdct/default.asp?id=51290&opcio=99). |
| 27 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, materials, procediment i avaluació; recuperada la síntesi; reforçada la delimitació dels efectes sobrenaturals respecte de cristalls i gemmes convencionals. Les 10 propostes gràfiques originals es reserven per a MG. F4: coteig completat; 14 receptes, sis exercicis i 28 referències de paleta preservats. Receptes no assajades. Normalitzada «gema» a «gemma» a C27 segons el Diccionari de gemmologia del TERMCAT (https://www.termcat.cat/ca/diccionaris-en-linia/168). |
| 28 | RT · alta / MG | Recuperació tècnica aplicada. F4: coteig de fidelitat documental completat amb l'original per a les 11 receptes A–K, els materials dels sis exercicis i els codis de pintura; sense omissions ni incorporacions detectades en aquests elements. F4: validació documental completada; F6: revisió semàntica de remissions i coherència transversal completada. No resten comprovacions editorials pendents d'aquest capítol; les receptes no es consideren validades experimentalment. Les 10 propostes gràfiques originals es reserven per a MG. |
| 29 | RT · alta / MG | Recuperació tècnica aplicada. F4: coteig de fidelitat documental completat amb l'original per a les 17 receptes A–Q, els materials dels sis exercicis i els codis de pintura; sense omissions ni incorporacions detectades en aquests elements. També es conserva la integració de pedres i fragments amb el terreny. F4: validació documental completada; F6: revisió semàntica de remissions i coherència transversal completada. No resten comprovacions editorials pendents d'aquest capítol; les receptes no es consideren validades experimentalment. Les 10 propostes gràfiques originals es reserven per a MG. |
| 30 | RT / RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperada la divisió entre planificació de valors, temperatura cromàtica i preparació; ampliada l'estructura de les cinc receptes amb objectiu, materials, procediment, control i variants; recuperats els cinc exercicis amb objectiu i síntesi del capítol. F4: revisió de contingut completada; cinc receptes i cinc exercicis preservats. Receptes no assajades. Les vuit figures originals es reserven per a MG. |
| 31 | RT / RD / MG · baixa / AE puntual | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, procediment i avaluació; recuperada la síntesi; mantinguda la distinció entre sang fresca, coagulada, seca i altres fluids. Les vuit propostes gràfiques originals es reserven per a MG. F4: revisió de contingut completada; cinc receptes i sis exercicis preservats. Receptes no assajades. Corregides tres aparicions de «del brillantor» per «de la brillantor»; sense canvis tècnics. F4: precisada la remissió de 31.7: C37 per a selecció/control de brillantor; C38 per a vernissos protectors, envernissament i conservació. Sense canvis en receptes ni procediments. |
| 32 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, procediment i avaluació; recuperada la síntesi; mantinguda la distinció entre efecte cromàtic, font lluminosa, OSL, fluorescència i fosforescència. Les vuit propostes gràfiques originals es reserven per a MG. F4: revisió de contingut completada; cinc receptes i sis exercicis preservats. Receptes no assajades. |
| 33 | SC / RD / AE / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven les tretze receptes A–M, les pintures de referència i els sis exercicis; no s'afegeixen proporcions ni resultats experimentals. S'han recuperat les explicacions del problema i les correccions dels deu errors, els vuit criteris d'avaluació i les descripcions completes de les deu propostes gràfiques per a MG, que la síntesi anterior havia reduït o omès. Es mantenen les delimitacions amb vidre (C34), acabats/brillantor (C37) i protecció/envernissament (C38). S'ha recuperat també el criteri explícit de finalització, la taula d'ubicació prevista de les deu figures i el bloc de control editorial i límits de verificació. La compilació s'ha sincronitzat i verificat. |
| 34 | SC / RD / AE / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven les receptes A–H, els procediments i els sis exercicis, sense afegir proporcions ni resultats experimentals. S'han recuperat les explicacions del problema i les correccions dels nou errors, els vuit criteris d'avaluació i el criteri de finalització. També s'han recuperat les descripcions completes de les deu propostes gràfiques per a MG, que la síntesi anterior havia omès. Es mantenen els límits amb transparència/translucidesa general (C14), cristalls i gemmes (C27), contingut líquid (C31) i acabats (C37). S'ha recuperat també la taula d'ubicació prevista de les deu figures i el bloc de control editorial i límits de verificació. La compilació s'ha sincronitzat i verificat després d'aquests ajustos. |
| 35 | SC / RD / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven els procediments d'harmonització, els sis exercicis i les sis referències disponibles, sense afegir receptes ni filtres universals. S'han recuperat les explicacions del problema i les correccions dels deu errors, els nou criteris d'avaluació, el criteri de finalització i les descripcions completes de les deu propostes gràfiques per a MG, que la síntesi anterior havia omès. Es manté la distinció entre unitat cromàtica i uniformitat, integració de materials i pèrdua d'identitat. S'ha recuperat també la taula d'ubicació prevista de les deu figures i el bloc de control editorial i límits de verificació. La compilació s'ha sincronitzat i verificat després d'aquests ajustos. |
| 36 | RD / MG · baixa | Intervenció aplicada el 05/11/2026: recuperats i desenvolupats els sis exercicis amb objectiu i procediment; afegits criteris d'avaluació proposats com a millora didàctica, diferenciats del text original; recuperada la síntesi; mantinguts els criteris de selecció i adaptació per material. Les 10 propostes gràfiques originals es reserven per a MG. F4: revisió de contingut completada; sis exercicis, deu errors i set famílies d'adaptació material preservats. Criteris d'avaluació identificats com a propostes editorials. |
| 37 | SC / RD / AE / MG · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». Es conserven els sis exercicis i les referències disponibles, sense afegir recomanacions universals ni resultats experimentals. S'han recuperat les explicacions dels problemes dels deu errors, els vuit criteris d'avaluació i les descripcions completes de les deu propostes gràfiques per a MG, que la síntesi anterior havia omès. Es mantenen les distincions entre acabat i protecció, reflexió especular i difusa, brillantor i identitat material, i el límit amb C38. S'ha recuperat també la síntesi de criteris d'aplicació, la taula d'ubicació prevista de les deu figures i el bloc de control editorial i límits de verificació. La compilació s'ha sincronitzat i verificat després d'aquests ajustos. |
| 38 | RT / RD / MG · alta / AE puntual | F4: estructura i procediments cotejats amb l'original; sis exercicis conservats i desenvolupats, amb criteris d'avaluació identificats com a propostes editorials. Recuperats tres detalls tècnics omesos: comprovacions per seleccionar vernissos acrílics, distinció dels poliuretans de base aquosa i condicions/riscos específics dels aerosols. Passada transversal immediata: terminologia normalitzada a «vernís/envernissament»; corregit «el brillantor» per «la brillantor». La revisió global de coherència, remissions i referències (F6) s'ha completat el 05/11/2026. El coteig documental de contingut amb la font disponible es considera completat dins dels límits registrats; no equival a validació experimental. Les 10 propostes gràfiques es reserven per a MG. |
| 39 | SC / MG / AE puntual · F4 completada | Coteig documental de contingut completat amb «manual con estructura completa.docx». S'han contrastat el mètode de diagnòstic, la classificació dels problemes, els set procediments generals de correcció, els criteris per decidir l'abast, la compatibilitat i seguretat, la prevenció, el registre del procés, l'avaluació final i els sis exercicis desenvolupats. No s'han identificat omissions substancials que justifiquin modificar el capítol. La compilació conté exactament el fitxer vigent. Aquest coteig documental no constitueix validació experimental. |

### Lectura global de la matriu

- Auditoria comparativa completada: **39/39 capítols**.
- Capítols 1–2, 7–10, 14–15, 17–24, 33–35, 37 i 39 van quedar protegits com a SC en el dictamen inicial, amb les excepcions AE/MG o les intervencions posteriors indicades individualment.
- Recuperacions tècniques d'alta prioritat identificades inicialment: capítols 11, 12, 13, 28, 29 i 38.
- Recuperacions tècniques/didàctiques mitjanes: capítols 3–6, 30 i 32; altres ajustos didàctics o editorials consten a la matriu.
- L'auditoria va registrar 101 receptes als capítols 25–34 sense pèrdua d'ingredients i 143 propostes gràfiques als capítols 25–39. Un inventari gràfic global posterior va recollir 280 propostes; són propostes pendents de depuració, no 280 imatges que s'hagin de produir automàticament.

## 6. Estat de les intervencions aplicades a la branca

| Capítols | Estat documentat a 05/11/2026 |
|---|---|
| 1 | G-01 aplicada a l'HTML copia_trabajo/index.html (§1.5); no confondre amb un canvi al Markdown. |
| 2 | G-02 aplicada a l'HTML ( §§2.1, 2.4–2.6); el contingut SC del Markdown es manté protegit. |
| 3 | G-01 aplicada a l'HTML (§§3.1 i 3.4.3); G-03 va tancar el seu coteig 3–5 sense canvis conceptuals. Recuperació de la tercera versió aplicada el 05/11: vuit errors, síntesi operativa i vuit passos de selecció. L'anomalia HTML <<p és una tasca separada de la primera versió. |
| 4 | F4: coteig documental de contingut completat amb «manual con estructura completa.docx». S'han contrastat els fonaments de percepció i context, models cromàtics, dimensions del color, temperatura, harmonies, contrastos, mescles, set criteris de planificació, exemple de l'armadura blava, nou errors, sis exercicis i vuit referències. Les nou propostes gràfiques es mantenen reservades a MG. No s'han identificat omissions substancials ni s'ha modificat el capítol; compilació exacta. No equival a validació experimental. |
| 5 | F4: coteig de contingut i bibliografia completat amb la font disponible; s'han recuperat vuit referències bibliogràfiques omeses. Les figures originals continuen reservades a MG. |
| 6 | F4: coteig documental de contingut completat amb «manual con estructura completa.docx». S'han contrastat estructura, geometria, textura, patrons, resposta òptica, transparència, reconeixement de materials, adaptació a escala, fitxa d'anàlisi, deu errors, mètode d'observació de set passos, quatre exercicis i cinc referències. Les vuit propostes gràfiques es mantenen reservades a MG. No s'han identificat omissions substancials ni s'ha modificat el capítol; compilació exacta. No equival a validació experimental. |
| 7 | F4: revisada la correspondència estructural i operativa, inclosos els blocs de seguretat, els quatre exercicis i les tres referències de consulta; el coteig textual integral continua pendent. |
| 8 | F4: revisada la correspondència estructural i procedimental, inclosos errors, exercicis i criteris d'avaluació; el coteig textual integral continua pendent. |
| 9 | F4: revisada la correspondència estructural i procedimental; conciliada la possible redundància 9.6/9.8 sense retallada. |
| 10 | F4: coteig documental de contingut completat amb la font; set errors, sis exercicis i vuit propostes gràfiques identificats i preservats. Sense canvis al capítol. |
| 11–13 | Recuperacions/ampliacions aplicades i documentades en commits individuals; fer validació global sense repetir diagnòstics ja tancats. |
| 14–18 | Ampliacions aplicades i documentades. C14: recuperat el desenvolupament procedimental dels sis exercicis i preservada la distinció tècnica central. C15: recuperats desenvolupaments de jerarquia de valors, planificació per zones, errors, criteris i exercicis. C16: recuperats fonaments visuals, planificació dels reflexos, criteris d'avaluació i procediments dels exercicis. C17: revisat el contingut consolidat disponible; preservats els dotze errors, sis exercicis i deu figures. C18: recuperada una proposta gràfica absent del mapa del procés integral; nou figures en total. C14–C18 mantenen límits de font: no s'ha localitzat un original complet; les revisions es basen en la consolidació disponible i els acords recuperats. |
| 19 | F4: revisió del contingut consolidat disponible ampliada; contrastats cinc metalls, 16 receptes, procediments, acabats, taules d'errors, comparació TMM/NMM i set exercicis. Recuperades causes, objectius i resultats esperats; retirada una taula duplicada. Sense alteracions d'ingredients, codis o combinacions ni proporcions inventades. Original complet no recuperat; receptes no assajades. |
| 23–24, 35, 37, 39 | Capítols auditats i classificats com a SC. No hi ha recuperacions RT/RD pendents identificades per executar en aquests capítols; es mantenen protegits de canvis innecessaris. La seva coherència es comprovarà transversalment a F4/F6 quan afecti referències o límits amb altres capítols. |
| 28 | Recuperació tècnica aplicada. F4 (05/11/2026): coteig complet de fidelitat amb l'original; receptes A–K (ingredients), sis exercicis (materials) i codis de pintura contrastats sense omissions ni incorporacions. Correccions lingüístiques puntuals aplicades. Validada la correspondència documental; resta la revisió transversal de coherència tècnica i referències. |
| 29 | Recuperació tècnica aplicada. F4 (05/11/2026): coteig complet de fidelitat amb l'original; receptes A–Q (ingredients), sis exercicis (materials) i codis de pintura contrastats sense omissions ni incorporacions. Es comprova també la conservació de la integració de pedres i fragments amb el terreny. Correccions lingüístiques puntuals aplicades. Validada la correspondència documental; resta la revisió transversal de coherència tècnica i referències. |
| 25 | F4 (05/11/2026): coteig amb la font disponible completat; 13 receptes A–M i sis exercicis preservats. Detectada i corregida l'omissió de tres referències complementàries de la paleta (Dark Sea Blue, Light Flesh i Skin Tone); ara es conserven les 12 pintures de la taula original. No s'han alterat ingredients ni combinacions de receptes. Les propostes continuen sense validació experimental. |
| 26 | F4 (05/11/2026): coteig de contingut amb la font disponible completat; deu receptes A–J, sis exercicis i la paleta de 19 referències es mantenen. No s'han identificat omissions substancials en classificació, procediments, errors, avaluació ni delimitacions. Receptes no assajades. |
| 27 | F4 (05/11/2026): coteig de contingut amb la font disponible completat; catorze receptes A–N, sis exercicis i la paleta de 28 referències es mantenen. Es conserva la delimitació entre roca/mineral (C26), cristall, gel, neu i gemma (C27), i els efectes sobrenaturals (C32). Receptes no assajades. |
| 30 | F4 (05/11/2026): revisió de contingut amb la font disponible completada; cinc receptes A–E i cinc exercicis preservats. Es conserven la planificació de valors, la temperatura cromàtica, la preparació, els errors i la delimitació respecte dels efectes sobrenaturals de C32. Receptes no assajades. |
| 31 | F4 (05/11/2026): revisió de contingut amb la font disponible completada; cinc receptes A–E i sis exercicis preservats. Es manté la distinció entre sang fresca, acumulada/coagulada, seca i fluids no sanguinis, així com la separació entre color, consistència, distribució i acabat. Receptes no assajades. |
| 32 | F4 (05/11/2026): revisió de contingut amb la font disponible completada; cinc receptes A–E i sis exercicis preservats. Es mantenen les distincions entre efecte cromàtic, font lluminosa i OSL, i entre fluorescència i fosforescència. Els tutorials no s'atribueixen com a receptes pròpies ni s'afegeixen productes externs. Receptes no assajades. |
| 33 | F4: coteig documental de contingut completat; recuperades les explicacions dels deu errors, els criteris d'avaluació i les deu descripcions gràfiques detallades per a MG. Remissions a C34, C37 i C38 conciliades; sense alteracions de receptes ni proporcions. Compilació sincronitzada i verificada. |
| 34 | F4: coteig documental de contingut completat; recuperades les explicacions dels nou errors, els vuit criteris d'avaluació, el criteri de finalització i les deu descripcions gràfiques per a MG. Remissions a C33, C31 i C37 conciliades; receptes i proporcions preservades. Compilació sincronitzada i verificada. |
| 36 | F4 (05/11/2026): revisió de contingut amb la font disponible completada; sis exercicis i els deu blocs d'errors es mantenen. Es conserven les set famílies d'adaptació material i els procediments d'abrasió, ratllades, desconxats, decoloració i combinació d'alteracions. Els criteris d'avaluació dels exercicis continuen identificats com a propostes editorials. Sense validació experimental. |
| 38 | Recuperació tècnica i didàctica aplicada el 05/11/2026: incorporats els fonaments i límits de la protecció, distinció entre assecat superficial, assecat al tacte i estabilització, sis exercicis desenvolupats i criteris d'avaluació final. Coteig documental amb la font disponible completat; terminologia normalitzada i errada «la brillantor» corregida. Resta la revisió global de coherència i referències. |

**No interpretar “aplicat” com “validat”.** La validació ha de comprovar el capítol complet, la coherència amb l'original o la font disponible, la numeració, les referències, les receptes i els exercicis que pertoquin.

## 7. Decisions transversals que cal mantenir

- Arquitectura fixa de 39 capítols.
- Primera versió i segona síntesi són fonts diferenciades; la tercera versió s'aplica als 39 Markdown.
- El contingut de la segona síntesi es conserva en català, d'acord amb el criteri específic establert per a aquests fitxers.
- La primera versió HTML no es modifica en aquesta fase.
- Els annexos A–E s'aborden després d'estabilitzar els capítols.
- La distinció entre capítol 37 (aparença, acabats i brillantor) i capítol 38 (vernissos, protecció i conservació) s'ha de mantenir a totes les referències creuades.
- No confondre propostes de figures amb recursos visuals produïts.
- No atribuir validació física a cap recepta o barreja que no tingui registre d'assaig.

## 8. Properes actuacions operatives

1. Completar la conciliació final de F2: revisar les 39 files de la matriu, contrastar-les amb els estats finals de F4, els fitxers Markdown vigents i els commits; retirar o marcar com a històriques les instruccions superades.
2. Mantenir F4 tancada amb les limitacions documentals explícites. No repetir cotejos completats ni reobrir capítols SC sense una incidència tècnica o documental substancial.
3. Preservar els límits de font de C11 i C14–C18, i els límits de revisió de C30–C32 i C36; no atribuir a originals complets continguts contrastats només amb material parcial o consolidat.
4. Mantenir sincronitzada la compilació `TERCERA_SINTESI_CONSOLIDADA_C01-C39.md` amb els 39 Markdown i tornar a verificar-ne la correspondència exacta després de qualsevol canvi.
5. Un cop tancada F2 i confirmada l'estabilitat de C1–C39, iniciar F5: regenerar i auditar els annexos A–E, contrastant-ne contingut, denominacions, referències i correspondència amb els capítols.
6. Després de F5, abordar F7: producció gràfica a partir del document MG independent i maquetació Word, comprovant el volum real sense retallar contingut valuós per ajustar pàgines.
7. Mantenir la branca `intervencion-editorial-2026-11`; no modificar `main` ni intervenir en l'HTML de la primera versió durant aquesta fase.

## 9. Historial del registre

| Versió | Data | Canvis |
|---|---|---|
| 1.0 | 05/11/2026 | Primera consolidació de categories RT/RD/AE/MG/SC, prioritats, dictamen 39/39, estat de les intervencions i fases. |
| 1.1 | 05/11/2026 | Correcció de la seqüència F0–F7; incorporació de la traçabilitat G-01–G-11 a l'HTML; distinció explícita entre les intervencions històriques de la primera versió i les recuperacions actuals dels 39 Markdown; actualització de l'estat de C33–C34 i correcció del recompte de passos de C4. |
| 1.2 | 05/11/2026 | Precisió de la fase F0 (traçabilitat) i incorporació del criteri d'extensió de 350–375 pàgines, amb límit orientatiu de 400 i prohibició de retallar contingut tècnic per raons quantitatives. |
| 1.3 | 05/11/2026 | Precisió de l'origen dels criteris d'avaluació afegits als exercicis dels capítols 36 i 38: es marquen com a propostes didàctiques editorials, no com a contingut recuperat del text original. |
| 1.4 | 05/11/2026 | Registre de la recuperació del capítol 3 (vuit errors i síntesi operativa de vuit passos), actualització de la fase F3 i precisió dels estats d'aplicació/validació dels capítols 36 i 38. |
| 1.5 | 05/11/2026 | F3 completada per a les accions identificades; inici de F4; comprovació estructural dels 29 Markdown intervinguts i correcció dels salts de línia literals als capítols 28 i 29. |
| 1.6 | 05/11/2026 | Primera comprovació semàntica dels capítols 28–29: procediments de receptes i materials dels exercicis cotejats amb l'original; codis de pintura restituïts a les llistes. F4 continua oberta. |
| 1.7 | 05/11/2026 | Precisió de la relació entre les dues fonts de la segona síntesi i els 39 fitxers Markdown de treball; correcció de l'estat dels capítols SC i de les properes actuacions, que passen a centrar-se en F4. |
| 1.8 | 05/11/2026 | F4: coteig de fidelitat documental completat per a C28–C29; comprovades les receptes A–K/A–Q, els materials dels sis exercicis de cada capítol i la correspondència dels codis de pintura. Correccions lingüístiques menors aplicades; revisió transversal tècnica encara oberta. |
| 1.9 | 05/11/2026 | F4: recuperació de detalls tècnics omesos a C38; comprovació limitada de C11 amb preservació del límit documental (original complet no recuperat i tancament editorial previ). Continuïtat de F4 prioritzada a C12–C13. |
| 1.10 | 05/11/2026 | F4 estructural: C12 (deu apartats i cinc exercicis) i C13 (deu apartats, quatre tècniques, nou blocs d'errors i sis exercicis) coincideixen amb l'estructura de la font disponible. Es registra una remissió editorial antiga a la font de C12 que no concorda amb l'índex definitiu; coteig semàntic encara pendent. |
| 1.11 | 05/11/2026 | F4: coteig de contingut de C12 i C13 completat amb la font disponible; no s'identifiquen omissions substancials en procediments, criteris, limitacions ni exercicis. Es manté pendent la conciliació de la metadada antiga de C12 i la normalització terminològica transversal. |
| 1.12 | 05/11/2026 | F4: C14 reobert per una omissió tècnica substantiva identificada en el material font disponible: diferència entre transparència del producte pictòric i transparència de l'objecte representat. Recuperació puntual aplicada; límit documental preservat. |
| 1.13 | 05/11/2026 | F4: comprovació limitada de C15; es preserva el límit de font (original complet no localitzat) i es confirma la correspondència estructural disponible de deu apartats i sis exercicis. Sense canvis de contingut. |
| 1.14 | 05/11/2026 | F4: comprovació limitada de C16; es preserva el límit de font (versió consolidada nova, original complet no recuperat) i es confirma l'estructura de deu apartats i sis exercicis. Sense canvis de contingut. |
| 1.15 | 05/11/2026 | F4: comprovació limitada de C17 i C18; es preserven els límits documentals (originals complets no recuperats) i es confirma l'estructura de deu apartats i sis exercicis en tots dos capítols. Sense canvis de contingut. |
| 1.16 | 05/11/2026 | F4: coteig de la font disponible de C19; 16 receptes, ingredients/codis i set exercicis comprovats. La font no documenta proporcions exactes ni s'ha recuperat un original complet; no s'inventen quantitats. |
| 1.17 | 05/11/2026 | F4: validació de contingut de C25–C27, C30–C32 i C36 amb la font disponible. Restituïdes a C25 tres referències complementàries de paleta que faltaven; sense alteracions a les receptes. Coteig documental i didàctic registrat, sense atribuir validació experimental a les receptes. |
| 1.18 | 05/11/2026 | F4: revisió transversal immediata de C38 i normalització terminològica en C3 i C37–C39; correcció gramatical de «la brillantor» a C38. Cap canvi en receptes, ingredients o procediments. Revisió global de coherència i referències encara pendent. |
| 1.19 | 05/11/2026 | F4: conciliació AE de C33–C34 amb la font disponible; remissions a C31, C33 i C37 confirmades. Correccions de concordança de «brillantor» a C22, C23, C31, C33, C34 i C37; «hendidures» de C33 normalitzat a «cavitats». Sense canvis en receptes o procediments. Revisió global de coherència i referències pendent. |
| 1.20 | 05/11/2026 | F4: primera passada de referències dels 39 Markdown; cap destinació numèrica fora de l'arquitectura 1–39. Conciliada la metadada obsoleta del registre editorial de C12: les quatre tècniques de textura corresponen a C13 i C14 a transparències. Sense modificacions dels capítols per aquesta incidència. |
| 1.21 | 05/11/2026 | F4: revisió semàntica de remissions; corregida a C31 la confusió entre acabat/brillantor (C37) i vernissos protectors/envernissament/conservació (C38), en coherència amb la delimitació de la font. Sense canvis en receptes, ingredients o procediments. |
| 1.22 | 05/11/2026 | F4: precisada la remissió de C4.10.5; C5 queda com a fonament físic i perceptiu, i C15 com a planificació aplicada de llums, ombres i valors. No es modifica la resta del contingut. |
| 1.23 | 05/11/2026 | F4: precisades les remissions de C33.8 i C34.4.1: C37 per a selecció de l'acabat i control de brillantor; C38 per a vernissos protectors, envernissament i conservació. Coherència amb les delimitacions de C37–C38 i amb la font. Sense canvis en receptes o procediments. |

Aquest registre és una consolidació operativa basada en l'auditoria i els resultats recuperats del projecte. Els punts marcats com a pendents o no validats s'han de comprovar amb el fitxer real i la font corresponent abans de declarar-los tancats.


### Incidència transversal de terminologia — resolució inicial F4 (05/11/2026)

La passada pels 39 Markdown va identificar variants no homogènies a C3, C37, C38 i C39. S'han normalitzat aquests quatre fitxers amb el criteri següent: `vernís/vernissos`, `envernissar`, `envernissat/envernissada` i `envernissament`. A C3, `vernissatge` s'ha substituït per `envernissament`. A C37–C39 s'han corregit les formes derivades de `barnís/barnissos/barnissar/barnissat`. També s'ha corregit a C38 `el brillantor` per `la brillantor`.

La forma `vernís` i el verb `envernissar` coincideixen amb el DIEC; TERMCAT recull les formes tècniques `envernissada` i `envernissament`. La comprovació dels 39 Markdown no ha identificat altres aparicions de les variants corregides. Aquesta resolució terminològica immediata no tanca la revisió de totes les referències creuades ni la coherència global, que continuen pendents.


### Segona passada terminològica i conciliació AE de C33–C34 (05/11/2026)

- C33 i C34 s'han contrastat amb la font disponible. C33 conserva 13 receptes A–M i sis exercicis; C34 conserva vuit receptes A–H i sis exercicis.
- La remissió de C33 i C34 a C37 per a la selecció i aplicació dels acabats superficials coincideix amb el criteri editorial de la font. No s'ha de traslladar aquesta funció a C38: aquest últim tracta la protecció i conservació de la pel·lícula pictòrica.
- S'ha confirmat la coherència de les remissions C33→C34 (translucidesa/vidre), C34→C33 (materials), C34→C31 (contingut líquid) i C33/C34→C37 (acabats).
- S'han corregit les concordances de «brillantor» a C22, C23, C31, C33, C34 i C37. La comprovació dirigida dels 39 Markdown no ha detectat altres aparicions de les formes masculines errònies.
- A C33, sis aparicions de «hendidures» s'han normalitzat com a «cavitats», d'acord amb el sentit de depressions o zones enfonsades en els contextos de relleu de les receptes.
- No s'han modificat receptes, ingredients, proporcions ni procediments. C33–C34 continuen protegits quant al contingut tècnic.


### Auditoria semàntica de remissions — blocs C19–C29, C30–C32 i C35–C39 (05/11/2026)

S'ha revisat la coherència funcional de les remissions entre els capítols dels blocs indicats. No s'han identificat remissions incorrectes que justifiquin canvis de contingut. Es mantenen les delimitacions entre material i efectes (C19–C27), corrosió i pàtines (C28), brutícia i dipòsits (C29), foc (C30), sang i fluids (C31), efectes sobrenaturals (C32), integració cromàtica (C35), desgast (C36), acabats (C37), protecció i conservació (C38) i diagnòstic (C39). Aquesta passada és una auditoria semàntica de remissions; no constitueix un nou coteig integral de tots els procediments amb la font original. No s'han modificat capítols tècnics, receptes, ingredients ni procediments.


### Auditoria global de coherència — primera passada transversal (05/11/2026)

S'ha iniciat la fase 6 amb una primera passada sobre l'arquitectura, les delimitacions i els punts de contacte de C3–C14 i C19–C39. Es mantenen com a separacions funcionals correctes: C5 (fonaments de llum) / C15 (planificació aplicada); C6 (reconeixement i comportament visual dels materials) / capítols específics de materials; C11 (procediments generals de rentats, tintes, pigments i acumulacions) / C29 (aplicació a terra, fang, pols i brutícia); i capítols de materials / C36 (alteracions per ús, exposició i deteriorament). També es manté la distinció entre C3 (propietats de les pintures), C7 (preparació i gestió operativa), C8–C10 (construcció cromàtica, degradats i veladures), C12–C13 (perfilat i textures) i C14 (comportament pictòric de transparències i translucidesa).

S'han revisat dues numeracions que podien semblar anòmales: C28.5.6 i C38.9.10. El coteig amb el document original confirma que totes dues numeracions ja hi apareixen així; es conserven i no es consideren errors introduïts en la tercera versió. No s'han modificat capítols tècnics ni receptes en aquesta passada. La fase 6 continua oberta: aquesta comprovació d'arquitectura i delimitacions no equival encara a una lectura exhaustiva de cada paràgraf dels 39 capítols ni a la validació tècnica experimental de les receptes.


### Tancament de l'auditoria global de coherència F6 (05/11/2026)

S'ha completat la passada transversal final de C1–C39, centrada en terminologia tècnica, criteris d'aplicació i avaluació, compatibilitat, assecat/estabilització, acabats i protecció, i abast de les correccions. No s'han identificat contradiccions globals ni divergències terminològiques que justifiquin una normalització general, reorganitzacions, noves remissions o eliminacions de contingut. Es conserven les distincions entre imprimació i capa base; rentat, tinta i veladura; llum, reflex, OSL i fluorescència; transparència, translucidesa i opacitat; pigment, fixador i vernís; acabat i protecció; desgast, corrosió i dipòsit; i assecat, estabilització i curat.

S'ha resolt l'ambigüitat de la recepta A de C27 amb una aclaració perquè la base clara no s'interpreti com una capa opaca general: s'indica limitar-la als plans o zones que necessiten aclariment i conservar, quan la representació i la geometria ho permetin, informació cromàtica del fons o de les capes subjacents. No s'han alterat la paleta, les proporcions ni la resta de la seqüència de la recepta.

La passada de coherència global F6 queda tancada. Aquest tancament no constitueix validació experimental de receptes, comprovació de comportament de productes ni validació tècnica independent. La fidelitat documental, la coherència interna i la validació experimental continuen sent nivells de comprovació diferenciats. No es modifica l'arquitectura de 39 capítols ni la branca main.


### Compilació documental dels capítols 1–39 (05/11/2026)

S'ha creat a l'arrel del repositori el fitxer `TERCERA_SINTESI_CONSOLIDADA_C01-C39.md`, com a compilació de treball del contingut vigent dels 39 Markdown. Inclou els capítols 1–39 en ordre numèric i no incorpora els annexos A–E. S'ha afegit una capçalera d'identificació i s'han utilitzat separadors horitzontals entre fitxers; el contingut de cada capítol s'ha conservat sense reescriptura ni resum.

La verificació s'ha fet tornant a recuperar els 39 fitxers font i comprovant que cadascun apareix íntegrament a la compilació (39/39). La compilació té 871.188 caràcters i 39 encapçalaments principals de capítol. Aquesta comprovació acredita la integritat de la unió documental, no la validació editorial final de F4 ni l'assaig experimental de les receptes. Si F4 comporta modificacions als fitxers font, la compilació s'haurà de regenerar o sincronitzar abans de declarar-la definitiva.


### F4 — auditoria semàntica de remissions C1–C18 (05/11/2026)

S'ha completat la revisió de les remissions explícites dels capítols 1–18 i s'han contrastat amb la funció i l'abast dels capítols de destinació. No s'han detectat destinacions errònies ni confusions funcionals que requereixin reorganitzar l'arquitectura. La remissió de C2 a l'annex A és coherent amb la funció d'inventari i traçabilitat d'aquest annex, encara pendent de reconstrucció.

S'ha identificat una imprecisió a C18.8.5: la frase atribuïa als capítols 35–38, en conjunt, els «procediments d'acabat, protecció i conservació», tot i que C35 tracta l'harmonització cromàtica i C36 el desgast i la transformació de superfícies. La frase s'ha precisat per enumerar els continguts que corresponen a cada bloc: harmonització cromàtica, desgast i transformació, acabats superficials, protecció i conservació. La modificació s'ha aplicat a `segunda_sintesi/capitol-18.md` i s'ha sincronitzat a `TERCERA_SINTESI_CONSOLIDADA_C01-C39.md`.

No s'han modificat receptes, ingredients, proporcions ni procediments. Amb aquesta passada, la revisió semàntica de remissions C1–C39 queda documentada com a completada. F4 continua oberta perquè encara resten cotejos documentals i comprovacions estructurals de capítols no validats; aquest tancament parcial no equival a validació experimental.


### F4 — coteig de contingut de C4–C5 (05/11/2026)

**C4 — teoria del color:** s'ha contrastat l'estructura i els elements didàctics principals amb la font disponible. Es mantenen els apartats de fonaments i planificació, els nou errors conceptuals, els sis exercicis, els set criteris de planificació de paletes, la seqüència operativa de vuit passos i l'exemple de l'armadura blava amb les seves fases. No s'han identificat omissions substancials en aquests elements. Les vuit referències bibliogràfiques es conserven. Les nou propostes de figures originals no s'han incorporat al Markdown perquè continuen reservades a MG. Aquest resultat és una comprovació estructural i didàctica principal, no un coteig textual integral.

**C5 — llum, volum, ombres i reflexos:** s'ha completat el coteig de contingut i bibliografia amb la font disponible. La síntesi conserva els conceptes de propagació rectilínia, fonts puntuals i extenses, magnituds fotomètriques, distància i incidència, normals i geometria, absorció/reflexió/transmissió, reflexió especular i difusa, dispersió, il·luminació directa/indirecta/ambiental, formació de les ombres, reflexos segons l'observador i construcció visual del volum. Les seccions 5.6 i 5.7 agrupen en forma compacta subdivisions de l'original, sense pèrdua dels seus eixos conceptuals principals. Es mantenen els set errors conceptuals i els sis exercicis d'observació.

S'han recuperat vuit referències bibliogràfiques omeses respecte de l'original: dues entrades CIE sobre reflexió regular/difusa i dispersió; dues definicions IES sobre llei de l'invers del quadrat i llei del cosinus; i quatre referències sobre forma a partir de l'ombreig, llei de reflexió i percepció tridimensional. C5 conserva així les dotze entrades bibliogràfiques de la font. Les 16 propostes de figures originals continuen reservades a MG i no s'han inserit com si fossin imatges produïdes.

No s'han modificat receptes, ingredients, proporcions ni procediments. El coteig documental no implica validació experimental dels exercicis o dels fenòmens descrits.


### F4 — revisió estructural i didàctica principal de C6 (05/11/2026)

S'ha contrastat l'estructura i els elements didàctics principals de C6 amb la font disponible. Es mantenen els blocs sobre estructura, geometria i textura; patrons superficials; resposta òptica; transparència, translucidesa i profunditat interna; reconeixement dels materials; representació a escala miniatura; fitxa d'anàlisi i mètode d'observació. Es conserven els deu errors conceptuals/visuals, el mètode d'observació de set passos, els quatre exercicis i les cinc referències bibliogràfiques. No s'han identificat omissions substancials en aquests elements.

Les vuit propostes de figures originals no s'han incorporat al Markdown perquè continuen reservades a MG. Aquesta passada és una comprovació estructural i didàctica principal, no un coteig textual integral. No s'han modificat receptes, ingredients, proporcions ni procediments.


### F4 — revisió estructural i operativa de C7 (05/11/2026)

S'ha contrastat la correspondència estructural i operativa de C7 amb la font disponible. La síntesi manté els blocs d'organització de l'espai, eines i selecció, preparació de la miniatura, imprimació, gestió de pintures, control de l'aplicació, manteniment i conservació, seguretat i prevenció. Les subdivisions de l'original s'han agrupat en apartats més compactes sense perdre les funcions operatives principals.

S'han comprovat especialment les precaucions sobre eines de tall, consulta d'etiquetes i fitxes de dades de seguretat, aerosols pressuritzats, ventilació i exposició a partícules, protecció personal, pols, higiene, emmagatzematge i eliminació. Es mantenen els quatre exercicis de preparació i les tres referències de consulta sobre seguretat. No s'han identificat omissions substancials en aquests blocs. Les vuit propostes de figures originals continuen reservades a MG.

Aquesta passada és una revisió estructural i operativa, no un coteig textual integral de cada paràgraf. No s'han modificat receptes, ingredients, proporcions ni procediments.


### F4 — revisió estructural i procedimental de C8 (05/11/2026)

S'ha contrastat la correspondència estructural i procedimental de C8 amb la font disponible. Es mantenen els blocs sobre construcció mitjançant capes, materials i condicions d'aplicació, procediment de capa base, construcció progressiva, variants, control tècnic, errors i correccions, criteris d'avaluació i exercicis.

S'han comprovat especialment els procediments d'aplicació i superposició, la conservació dels límits, la construcció de superfícies uniformes i plans cromàtics diferenciats, la modificació progressiva de l'aparença, el control de la superfície acumulada i la decisió de continuar, corregir o aturar-se. Es mantenen els sis errors, els quatre exercicis pràctics i l'exercici integrador, amb els seus procediments, aspectes d'observació i criteris d'avaluació. No s'han identificat omissions substancials en els elements revisats.

Les vuit propostes de figures originals continuen reservades a MG. Aquesta passada és una revisió estructural i procedimental, no un coteig textual integral de cada paràgraf. No s'han modificat receptes, ingredients, proporcions ni procediments.


### F4 — revisió estructural i procedimental de C9 (05/11/2026)

S'ha contrastat la correspondència estructural i procedimental de C9 amb la font disponible. Es mantenen els fonaments de les transicions contínues, esglaonades i la separació entre plans; les variables de pintura, geometria, extensió i quantitat; els tres procediments de construcció (mescles preparades, mescla humida i aplicacions successives); el procediment general de planificació i execució; les variants segons matís, valor, croma i distribució; el control tècnic; els sis errors i els sis exercicis, inclòs l'integrador.

S'ha revisat la possible redundància interna entre 9.6 (control tècnic i avaluació durant la construcció) i 9.8 (resultat esperat i criteris d'avaluació). Les funcions són complementàries: 9.6 guia el control de la transició mentre s'executa; 9.8 sintetitza les competències i els criteris de valoració final. No es justifica eliminar ni fusionar contingut.

Les vuit propostes de figures originals continuen reservades a MG. No s'han modificat receptes, ingredients, proporcions ni procediments.


### F4 — revisió estructural i tècnica de C10 (05/11/2026)

S'ha contrastat la correspondència estructural i tècnica de C10 amb la font disponible. Es mantenen les distincions entre veladura i glassejat, transparència pròpia de la pintura i efecte de transparència de l'aplicació, i les diferències respecte de capes base, degradats, rentats, tintes i representació de materials transparents o translúcids.

Es conserven les funcions i aplicacions de les veladures, la selecció de materials, l'ús d'aigua i mitjans, la preparació de la mescla, la prova prèvia, la càrrega i el control del pinzell, la distribució, l'assecat, les aplicacions successives, les variants d'ús, els controls tècnics i els set errors amb els seus procediments de correcció. També es mantenen els sis exercicis, inclòs l'integrador. No s'han identificat omissions substancials en els blocs revisats.

No s'han modificat receptes, ingredients, proporcions ni procediments. No s'atribueixen resultats experimentals a les propostes didàctiques.


### F4 — comprovació estructural global dels 39 Markdown (05/11/2026)

S'ha executat una comprovació estructural dels 39 fitxers Markdown de treball. Resultat: 39/39 fitxers amb un únic encapçalament principal H1, tots corresponents al número de capítol; no s'han detectat encapçalaments buits o duplicats, numeracions d'apartat repetides, numeracions que pertanyin a un altre capítol ni marcadors evidents de contingut pendent (TODO/TBD/XXX o equivalents).

Aquesta comprovació acredita la consistència formal bàsica dels encapçalaments i la numeració. No substitueix el coteig de contingut amb les fonts, la revisió tècnica de procediments ni la validació experimental de receptes.

| 1.34 | 05/11/2026 | Conciliació de la metadada de F2 amb la versió vigent del Registre Mestre; es manté F2 en curs perquè la matriu per capítol i les anotacions històriques encara requereixen conciliació. Confirmada la sincronització de C18.8.5 i de les vuit referències recuperades a C5 en la compilació consolidada. |


### F4 — coteig documental de contingut de C6 (05/11/2026)

S'ha realitzat el coteig de contingut de C6 amb el tram corresponent de «manual con estructura completa.docx». Es confirma la conservació dels blocs conceptuals sobre estructura, geometria, textura i patrons; resposta òptica i comportaments direccionals; transparència, translucidesa, opacitat i profunditat interna; reconeixement i límits de la identificació visual; representació a escala miniatura; fitxa d'anàlisi; errors freqüents; mètode d'observació i quatre exercicis. Les cinc referències bibliogràfiques del capítol coincideixen amb les de la font consultada. No s'identifica cap pèrdua tècnica o didàctica substancial que justifiqui una recuperació addicional. Les vuit propostes de figures continuen reservades a MG i no s'han incorporat al Markdown. No s'ha modificat C6; la compilació consolidada conté exactament el fitxer actual. Aquest coteig documental no constitueix validació experimental.

| 1.35 | 05/11/2026 | F4: coteig documental de contingut de C6 completat; sense recuperacions addicionals justificades ni canvis al capítol. Compilació C1–C39 verificada com a sincronitzada amb C6. |


### F4 — coteig documental de contingut de C7 (05/11/2026)

S'ha completat el coteig del contingut de C7 amb «manual con estructura completa.docx». S'han comprovat l'organització de l'espai i les condicions de treball; la selecció i les funcions de les eines; la preparació, inspecció, neteja, muntatge i correcció de la miniatura; la imprimació i el control de cobertura; la comprovació, homogeneïtzació, dosificació, dilució i conservació de pintures; el control bàsic de càrrega, pressió, contacte i recorregut; la neteja i el manteniment; la prevenció, ventilació, exposició, protecció personal, higiene, emmagatzematge i eliminació; els quatre exercicis amb objectius, materials, procediments i criteris d'avaluació; i les tres referències de seguretat. Les subdivisions de la font s'han agrupat en apartats més compactes sense perdre les funcions operatives principals. No s'han identificat omissions substancials que justifiquin modificar el capítol. Les vuit propostes de figures es mantenen separades com a material MG, no com a text de lectura ni com a imatges produïdes. La compilació consolidada conté exactament el C7 vigent. Aquest coteig documental no constitueix validació experimental.

| 1.36 | 05/11/2026 | F4: coteig documental de contingut de C7 completat; sense recuperacions addicionals justificades ni canvis al capítol. Verificada la presència exacta de C7 a la compilació C1–C39. |


### F4 — coteig documental de contingut de C8 (05/11/2026)

S'ha completat el coteig de C8 amb «manual con estructura completa.docx». Es conserven els fonaments de construcció mitjançant capes; les distincions entre capa base, aplicació, capa pictòrica, superposició, cobertura, transparència, continuïtat i uniformitat; els criteris de selecció de pintures i comprovació de les superfícies; el procediment de capa base adaptat a diferents geometries; l'organització de les aplicacions successives i la conservació dels límits cromàtics; les variants de construcció uniforme, plans diferenciats i modificació progressiva; el control de cada aplicació i de la superfície acumulada; els sis errors freqüents amb criteris de correcció; els resultats i criteris d'avaluació; i els cinc exercicis pràctics, inclòs l'integrador amb registre de decisions i criteris d'avaluació. No s'han identificat omissions tècniques o didàctiques substancials que justifiquin una recuperació addicional. No s'ha modificat C8. La compilació consolidada conté exactament el fitxer vigent. Aquest coteig documental no constitueix validació experimental.

| 1.37 | 05/11/2026 | F4: coteig documental de contingut de C8 completat; sense recuperacions addicionals justificades ni canvis al capítol. Verificada la presència exacta de C8 a la compilació C1–C39. |


### F4 — coteig documental de contingut de C9 (05/11/2026)

S'ha completat el coteig de C9 amb «manual con estructura completa.docx», des de la introducció fins a la síntesi i les propostes de figures. S'han comprovat els fonaments i les distincions entre degradat, transició contínua, transició esglaonada i separació entre plans; les variacions de matís, valor i croma; les variables relatives a les pintures, la geometria, l'extensió, la quantitat i la seqüència; els procediments de mescles preparades a la paleta, integració humida i aplicacions successives, així com la seva combinació; les fases de planificació, distribució, aplicació, assecat i avaluació; les variants de transició; els controls de continuïtat, extensió, colors intermedis i estat superficial; els sis errors amb causes i correccions; els criteris d'avaluació; els cinc exercicis i l'exercici integrador; i la síntesi final. No s'han identificat omissions tècniques o didàctiques substancials que justifiquin una recuperació addicional. La referència de l'original al capítol 17 per a la planificació de llums i ombres no correspon a l'arquitectura actual: el capítol 15 és el que tracta la planificació de la il·luminació i els valors. La versió actual de C9 ja remet al capítol 15, de manera coherent. Les vuit propostes de figures de l'original es mantenen fora del text de lectura i reservades a MG. La compilació consolidada conté exactament el fitxer C9 vigent. No s'ha modificat C9. Aquest coteig documental no constitueix validació experimental.

| 1.38 | 05/11/2026 | F4: coteig documental de contingut de C9 completat; sense recuperacions addicionals justificades ni canvis al capítol. Verificada la presència exacta de C9 a la compilació C1–C39. |


### F4 — coteig documental de contingut de C10 (05/11/2026)

S'ha completat el coteig del capítol 10 amb «manual con estructura completa.docx», des de la introducció fins a la síntesi i les propostes de figures. S'han contrastat les definicions de veladura i glassejat i la convenció terminològica adoptada; la diferència entre transparència del producte i efecte de la pel·lícula; les delimitacions respecte de capes base, degradats, rentats, tintes i representació de materials transparents; les sis funcions cromàtiques; la selecció de pintures, l'ús d'aigua i mitjans, la preparació i l'estat de la superfície; el procediment d'aplicació; les cinc variants; els controls tècnics i el criteri de finalització; els set errors amb causes i correccions; els criteris d'avaluació; els cinc exercicis i l'exercici integrador; i la síntesi. La versió actual conserva aquests continguts sense omissions tècniques o didàctiques substancials. Les vuit propostes de figures de l'original es mantenen reservades a MG i no s'incorporen al text lector. No s'ha modificat C10. La compilació consolidada conté exactament el fitxer C10 vigent. Aquest coteig documental no constitueix validació experimental.

| 1.39 | 05/11/2026 | F4: coteig documental de contingut de C10 completat; sense recuperacions addicionals justificades ni canvis al capítol. Conciliació parcial del resum de F2 i F4. |


### F4 — revisió limitada i recuperació didàctica de C14 (05/11/2026)

S'ha revisat C14 contra el text consolidat disponible a «manual con estructura completa.docx», respectant la declaració expressa que no s'ha localitzat un original complet. La revisió confirma que el Markdown conserva la distinció central entre transparència del producte pictòric i transparència de l'objecte representat, tant en els fonaments com en els errors freqüents; manté els nou errors, els sis exercicis i les vuit propostes gràfiques. S'ha detectat que els exercicis estaven molt més condensats que el desenvolupament disponible. S'han recuperat les seqüències procedimentals de les sis activitats, sense afegir objectius, materials ni criteris no documentats. També s'ha corregit l'interferència lèxica «recetari» per «receptari». La compilació C1–C39 s'ha sincronitzat i conté exactament el C14 actual. Aquesta revisió no constitueix coteig integral amb l'original ni validació experimental.

| 1.40 | 05/11/2026 | F4: revisió limitada de C14; recuperat desenvolupament procedimental dels sis exercicis a partir de material consolidat disponible. Original complet no recuperat. Compilació sincronitzada. |


### F4 — revisió limitada i recuperació didàctica de C15 (05/11/2026)

S'ha revisat C15 contra el contingut consolidat disponible a «manual con estructura completa.docx», respectant que la mateixa font declara que no s'ha recuperat un original complet. La versió Markdown ja conservava l'estructura general, els deu errors, els sis exercicis i les vuit propostes gràfiques, però havia condensat desenvolupaments didàctics presents en el material disponible. S'han recuperat i ampliat les funcions del valor, la jerarquia tonal i els cinc nivells funcionals no obligatoris, la planificació per zones amb criteris específics per al cap, el tronc, les extremitats i els accessoris, el diagnòstic i la correcció dels deu errors, una taula de vuit criteris d'avaluació i les seqüències dels sis exercicis, inclòs l'integrador. S'ha corregit «sombra» per «ombra». Les vuit figures continuen reservades a MG. La compilació s'ha sincronitzat amb el C15 actual. Aquesta revisió no equival a coteig integral amb l'original ni a validació experimental.

| 1.41 | 05/11/2026 | F4: revisió limitada de C15; recuperat desenvolupament didàctic i procedimental a partir del material consolidat disponible. Original complet no recuperat. Compilació sincronitzada. |


### F4 — revisió limitada i recuperació tècnica/didàctica de C16 (05/11/2026)

S'ha revisat C16 contra el contingut consolidat disponible a «manual con estructura completa.docx», que identifica expressament el capítol com una versió consolidada nova i no com un original íntegre recuperat. El Markdown ja conservava el procediment general, les adaptacions geomètriques, els controls, els deu errors i els sis exercicis, però havia condensat fonaments visuals i planificació. S'han recuperat l'explicació funcional del contrast, el reflex com a informació visual de l'entorn, els criteris de simplificació pictòrica, la influència de l'orientació i l'entorn, els patrons possibles de reflexos i els passos de planificació prèvia; també s'ha desenvolupat la taula de vuit criteris d'avaluació i les seqüències dels sis exercicis. S'ha evitat duplicar les famílies cromàtiques que ja es detallen a 16.4. Les vuit figures continuen reservades a MG. La compilació s'ha sincronitzat amb C16. Aquesta revisió no equival a coteig integral amb l'original ni a validació experimental.

| 1.42 | 05/11/2026 | F4: revisió limitada de C16; recuperats fonaments visuals i desenvolupament didàctic a partir del material consolidat disponible. Original complet no recuperat. Compilació sincronitzada. |


### F4 — revisió limitada de C17 (05/11/2026)

S'ha revisat C17 contra el contingut consolidat disponible a «manual con estructura completa.docx». La mateixa font declara que el capítol és una versió consolidada nova i que no s'ha recuperat un original complet. La revisió confirma la conservació dels fonaments de l'OSL, la distinció entre font emissora, superfície il·luminada i reflex, la planificació espacial i cromàtica, el procediment general, l'adaptació a geometries i materials, els controls tècnics, els dotze errors, els sis exercicis i les deu propostes de figures. No s'han detectat omissions substancials en aquests blocs. No s'ha modificat C17; la compilació ja conté exactament el fitxer vigent. Aquesta revisió no equival a coteig integral amb l'original ni a validació experimental.

| 1.43 | 05/11/2026 | F4: revisió limitada de C17; correspondència amb el material consolidat disponible comprovada. Sense canvis al capítol. Original complet no recuperat. |


### F4 — revisió limitada i recuperació gràfica de C18 (05/11/2026)

S'ha revisat C18 contra el contingut consolidat disponible a «manual con estructura completa.docx», que declara que no s'ha recuperat un original complet. Es mantenen els deu apartats, els sis exercicis, les eines de planificació i avaluació i la remissió conciliada a C35–C38. S'ha detectat que la versió Markdown havia omès una de les propostes gràfiques de la font: el mapa del procés integral, que relaciona anàlisi, planificació, selecció, execució, control i avaluació. La proposta s'ha recuperat i ara el capítol conserva nou figures. La compilació s'ha sincronitzat i verificat. Aquesta revisió no equival a coteig integral amb l'original ni a validació experimental.

| 1.44 | 05/11/2026 | F4: revisió limitada de C18; recuperada una proposta gràfica omesa (mapa del procés integral). Nou figures preservades. Original complet no recuperat. Compilació sincronitzada. |


### F4 — coteig documental complet de C20 (05/11/2026)

S'ha completat el coteig de C20 amb «manual con estructura completa.docx». S'han contrastat la identitat visual, els patrons longitudinals i transversals, nusos, escorça i diferenciació respecte d'altres materials; la paleta de deu pintures i les seves referències; les nou receptes A–I i els seus ingredients; les seqüències de construcció de fustes clares, mitjanes, rogenques i fosques; les variants envellida, desgastada, humida i deteriorada; els procediments per a vetes, nusos i anells; l'adaptació a escala i geometria; els deu errors i les correccions; els sis exercicis; la síntesi; les nou propostes de figures i les referències. No s'han modificat ingredients ni combinacions, i no s'han afegit proporcions absents de la font. S'han recuperat desenvolupaments procedimentals condensats de les receptes G–I, dels patrons, dels exercicis i dels errors, així com tres referències bibliogràfiques omeses. La compilació C1–C39 s'ha sincronitzat i conté exactament el C20 actual. Les receptes continuen classificades com a propostes no assajades.

| 1.45 | 05/11/2026 | F4: coteig documental complet de C20; recuperacions procedimentals i bibliogràfiques aplicades; nou receptes, sis exercicis i nou figures preservats. Compilació sincronitzada. |


### F4 — coteig documental complet de C21 (05/11/2026)

S'ha completat el coteig de C21 amb «manual con estructura completa.docx». S'han contrastat la identitat i l'estructura de fullatge, coníferes, herbes, molsa, líquens i matèria vegetal seca; la morfologia de les quatre formes de creixement dels líquens; les divuit pintures de referència i les setze combinacions A–P; els procediments de construcció i les seqüències d'aplicació disponibles; l'adaptació a l'escala; els deu errors i les correccions; els criteris d'avaluació; els set exercicis; les deu propostes de figures i les set referències botàniques. S'han recuperat seqüències de les combinacions A, D, F, G i P, el desenvolupament dels errors i l'avaluació, els procediments dels exercicis i les set referències bibliogràfiques omeses. No s'han alterat les combinacions cromàtiques ni s'han afegit proporcions. La compilació C1–C39 s'ha sincronitzat i conté exactament el C21 actual. Les combinacions continuen sent propostes no assajades.

| 1.46 | 05/11/2026 | F4: coteig documental complet de C21; recuperacions procedimentals i bibliogràfiques aplicades; setze combinacions, set exercicis i deu figures preservats. Compilació sincronitzada. |


### F4 — revisió del contingut disponible de C11 i recuperacions tècniques de C14 (05/11/2026)

S'ha contrastat C11 amb la versió consolidada accessible a «manual con estructura completa.docx». Es mantenen els deu apartats, els vuit blocs d'errors, els sis exercicis i la síntesi; no s'han identificat omissions substancials respecte d'aquest material. La mateixa font indica que no s'ha recuperat l'original complet, de manera que el resultat no es registra com a coteig integral amb l'original. C11 no s'ha modificat.

En C14, revisat també contra el material consolidat disponible i no contra un original complet, s'han recuperat precisions sobre la influència de la longitud d'ona, l'absorció selectiva i la dispersió en la coloració interna, les variacions de color aparent i de distorsió associades al gruix i la curvatura, l'avaluació des de la distància habitual d'observació i el tractament no uniforme de vores i reflexos. No s'han alterat les receptes ni s'han afegit resultats experimentals. La compilació C1–C39 s'ha sincronitzat amb C14 i la verificació posterior ha de confirmar-ne la correspondència exacta. Les vuit figures continuen reservades a MG.

| 1.47 | 05/11/2026 | F4: C11 contrastat amb el contingut consolidat disponible, sense omissions substancials ni canvis; original complet no recuperat. C14: recuperades precisions tècniques a partir del material consolidat disponible; compilació sincronitzada. |

| 1.48 | 05/11/2026 | F4: coteig documental de contingut de C4 completat; sense recuperacions addicionals justificades ni canvis al capítol. Verificada la correspondència exacta de C4 amb la compilació C1–C39. Conciliació de la matriu i dels resums de F2/F4. |

| 1.49 | 05/11/2026 | F4: coteig documental de contingut de C6 completat; sense recuperacions addicionals justificades ni canvis al capítol. Verificada la correspondència exacta de C6 amb la compilació C1–C39. |

### F4 — coteig documental complet de C22 (05/11/2026)

S'ha completat el coteig de C22 amb «manual con estructura completa.docx». S'han contrastat les diferències entre cuir de gra natural i corregit, ante, nobuk, cuir rígid, superfícies encerades o polides, pells amb pèl, pell sense adobar, cuir curtit i pergamí; la paleta de dotze pintures; les disset receptes A–Q i els seus ingredients; els procediments de construcció de cuirs clars, marrons, rogencs, foscos, ante, nobuk i superfícies tractades; els plecs, vores, gruix, costures, perforacions i unions; els deu errors amb diagnòstic i correcció; els criteris d'avaluació; els sis exercicis amb objectius, materials, procediments i avaluació; les set referències i les deu propostes de figures. S'han recuperat els desenvolupaments d'errors, criteris, exercicis, referències i límits editorials que s'havien condensat o omès. No s'han modificat les receptes ni s'han afegit proporcions. La compilació C1–C39 s'ha sincronitzat i conté exactament el C22 actual. Les receptes continuen sent propostes no assajades.

| 1.50 | 05/11/2026 | F4: coteig documental complet de C22; recuperacions didàctiques i bibliogràfiques aplicades; disset receptes, sis exercicis i deu figures preservats. Compilació sincronitzada. |


| 1.51 | 05/11/2026 | F2: conciliat el resum de la versió vigent amb el registre 1.51 i incorporat C22 al resum de cotejos documentals completats. |


### F4 — revisió ampliada del contingut consolidat de C19 (05/11/2026)

S'ha ampliat el contrast de C19 amb el material consolidat disponible a «manual con estructura completa.docx», que declara que no s'ha recuperat un original complet. S'han revisat els cinc metalls, les quatre pintures metàl·liques de la paleta, les 16 receptes, els procediments TMM, els acabats, les taules de diagnòstic, la comparació TMM/NMM, els criteris de selecció i control, els set exercicis i les nou propostes gràfiques. S'han recuperat les causes dels errors, els objectius i resultats esperats dels exercicis i la taula comparativa TMM/NMM; també s'ha reforçat el criteri de jerarquia visual en combinar metalls. S'ha eliminat la repetició de la taula de les quatre pintures metàl·liques a l'apartat introductori, mantenint-ne la taula completa a 19.1.1. No s'han modificat ingredients, codis de pintura ni combinacions; no s'han afegit proporcions quantitatives ni resultats experimentals. Les receptes continuen identificades com a propostes no assajades. La compilació s'ha sincronitzat amb el C19 actual.

| 1.48 | 05/11/2026 | F4: revisió ampliada de C19 contra el contingut consolidat disponible; recuperats diagnòstics, desenvolupament dels set exercicis i comparació TMM/NMM; retirada una taula duplicada. Original complet no recuperat. Compilació sincronitzada. |

| 1.52 | 05/11/2026 | F4: coteig documental de contingut de C23 completat; recuperats els sis exercicis desenvolupats i cinc referències amb enllaços. Les deu receptes i vuit figures es conserven. C23 i la compilació sincronitzats i verificats. |

| 1.53 | 05/11/2026 | F4: coteig documental de contingut de C24 completat; recuperats els sis exercicis desenvolupats, els enllaços de set referències i els criteris d'avaluació. Les catorze receptes i nou figures es conserven. C24 i la compilació sincronitzats i verificats. |

### F4 — ajust editorial puntual de C23 (05/11/2026)

En la comprovació final de C23 s'ha detectat que el Markdown contenia dues seccions idèntiques «Referències i recursos». S'ha conservat la primera i eliminat la segona, sense alterar cap referència, contingut tècnic, recepta ni exercici. La compilació C1–C39 s'ha sincronitzat i verificat amb el fitxer actual. El coteig documental de contingut de C23 continua tancat; aquest ajust no constitueix una reobertura tècnica del capítol.

| 1.53 | 05/11/2026 | C23: eliminada una duplicació editorial de la secció de referències; cap canvi tècnic. Compilació sincronitzada i verificada. |

| 1.54 | 05/11/2026 | F2/F4: conciliat el resum general de F4 amb els cotejos complets de C4 i C6; actualitzades també les anotacions de seguiment per capítol. |

| 1.56 | 05/11/2026 | F4: coteig documental complet de C33; recuperades les explicacions dels errors i les descripcions detallades de les deu figures per a MG. Compilació sincronitzada i verificada. Conciliats els resums F2/F4 amb C4, C6 i C23–C24. |

### F4 — recuperació de control editorial i planificació gràfica de C33 (05/11/2026)

En el coteig de C33 s'ha completat la recuperació del criteri explícit de finalització del treball, la taula que vincula les deu figures amb els apartats on s'han d'ubicar i el bloc de control editorial i límits de verificació. Les descripcions de les deu figures ja es conservaven al Markdown i s'han mantingut. No s'han modificat receptes, codis de pintura ni procediments. La compilació s'ha sincronitzat amb el fitxer actual.

| 1.57 | 05/11/2026 | C33: recuperats criteri de finalització, ubicació de les deu figures i control editorial/límits de verificació. Compilació sincronitzada. |

| 1.58 | 05/11/2026 | F4: coteig documental complet de C34; recuperades les explicacions dels errors, criteris d'avaluació, criteri de finalització i les deu descripcions de figures per a MG. Compilació sincronitzada i verificada. Conciliats els resums F2/F4. |

### F4 — recuperació de la ubicació gràfica i dels límits editorials de C34 (05/11/2026)

En el coteig de C34 s'ha recuperat la taula que vincula les deu figures amb els apartats on s'han d'ubicar i el bloc de control editorial i límits de verificació. Les descripcions de les deu figures, el criteri de finalització i el contingut tècnic ja es conservaven i s'han mantingut. No s'han modificat les vuit receptes ni els sis exercicis. La compilació s'ha sincronitzat amb el fitxer actual.

| 1.59 | 05/11/2026 | C34: recuperats ubicació de les deu figures i control editorial/límits de verificació. Compilació sincronitzada. |

| 1.60 | 05/11/2026 | F4: coteig documental complet de C35; recuperades les explicacions dels deu errors, els criteris d'avaluació, el criteri de finalització i les deu descripcions de figures per a MG. Compilació sincronitzada i verificada. |

### F4 — recuperació de la ubicació gràfica i dels límits editorials de C35 (05/11/2026)

En el coteig de C35 s'ha recuperat la taula que vincula les deu figures amb els apartats on s'han d'ubicar i el bloc de control editorial i límits de verificació. Les descripcions de les deu figures, el criteri de finalització i el contingut tècnic ja es conservaven i s'han mantingut. No s'han afegit receptes ni filtres cromàtics universals. La compilació s'ha sincronitzat amb el fitxer actual.

| 1.61 | 05/11/2026 | C35: recuperats ubicació de les deu figures i control editorial/límits de verificació. Compilació sincronitzada. |

| 1.62 | 05/11/2026 | F4: coteig documental complet de C37; recuperades les explicacions dels deu errors, els criteris d'avaluació i les deu descripcions de figures per a MG. Compilació sincronitzada i verificada. |

| 1.63 | 05/11/2026 | F4: coteig documental complet de C39; sense omissions substancials ni canvis de contingut. Verificada la correspondència exacta amb la compilació C1–C39. |

### F4 — recuperació de síntesi, ubicació gràfica i límits editorials de C37 (05/11/2026)

En el coteig de C37 s'ha recuperat la síntesi final de criteris d'aplicació que figurava a la font, la taula que vincula les deu figures amb els apartats on s'han d'ubicar i el bloc de control editorial i límits de verificació. Es mantenen els deu errors, els vuit criteris d'avaluació i els sis exercicis; no s'han afegit recomanacions universals ni resultats experimentals. La compilació s'ha sincronitzat amb el fitxer actual.

| 1.64 | 05/11/2026 | C37: recuperades síntesi final, ubicació de les deu figures i control editorial/límits de verificació. Compilació sincronitzada. |

### F4 — coteig documental i recuperació gràfica de C3 (05/11/2026)

S'ha completat el coteig de C3 amb «manual con estructura completa.docx». Es conserven les distincions entre opacitat, transparència i cobertura; càrrega de pigment, intensitat i poder tintori; fluïdesa, consistència i distribució sobre relleus; acabat i assecat; les set famílies comercials, la selecció funcional, les proves proposades, la traçabilitat per procedència i estat, els vuit errors i la síntesi operativa. S'han recuperat les sis propostes de figures amb ubicació i descripció, i els criteris de producció gràfica. No s'han atribuït propietats individuals no verificades ni s'han presentat proves proposades com a resultats. La compilació C1–C39 s'ha sincronitzat amb C3.

| 1.65 | 05/11/2026 | F4: coteig documental de C3 completat; recuperades sis propostes gràfiques i criteris de producció; compilació sincronitzada. No equival a validació experimental. |

| 1.66 | 05/11/2026 | F4: cotejos documentals de C1 i C2 completats; recuperades les dues propostes gràfiques de cada capítol i la síntesi de C2. No s'han modificat els continguts tècnics ni la composició de la paleta. Compilació sincronitzada i verificada. |

| 1.67 | 05/11/2026 | F4 tancada amb limitacions documentals explícites: els 39 capítols disposen de coteig complet, revisió limitada o revisió del contingut disponible, segons la font recuperada. La revisió semàntica i estructural global està completada. No equival a validació experimental. |

### F4 — tancament de la validació documental dels 39 capítols (05/11/2026)

S'ha completat la revisió de contingut o del material documental disponible per als 39 capítols. Els límits de font de C11 i C14–C19 queden explícits: no s'han recuperat originals complets i, per tant, no s'afirma fidelitat integral a aquests originals. C30–C32 i C36 s'han revisat contra el contingut disponible. La resta de capítols tenen coteig documental completat segons l'abast descrit a la matriu. La revisió semàntica de remissions i la comprovació estructural global ja estaven completades. F4 queda tancada com a validació documental/editorial dins de les fonts disponibles, no com a validació experimental de receptes, mescles o resultats pictòrics.

| 1.67 | 05/11/2026 | F4 tancada: revisats els 39 capítols amb coteig complet o límits de font explícits; no equival a validació experimental. |

### Correcció de separació editorial MG (05/11/2026)

S'han retirat els blocs de propostes gràfiques dels fitxers Markdown de C1, C2, C3, C33, C34, C35 i C37, així com de la compilació C1–C39. També s'han retirat els criteris de producció gràfica de C3 i les mencions a figures incloses en els resums de control editorial de C33–C35 i C37. Les 50 propostes de figures i els criteris de producció s'han conservat, sense resumir-los, a «PLANIFICACIO_GRAFICA_MG_FASE_POSTERIOR.md». La compilació s'ha sincronitzat amb els fitxers corregits. No s'ha alterat contingut tècnic, didàctic o procedimental destinat a la lectura.

| 1.68 | 05/11/2026 | Correcció editorial MG: 50 propostes i criteris gràfics traslladats a document independent; retirats del cos de set capítols i de la compilació. |



### Sincronització final de la compilació C1–C39 (05/11/2026)

S'ha comprovat la presència íntegra dels 39 fitxers Markdown vigents a la compilació consolidada. S'ha actualitzat el bloc de C24, que no contenia encara les darreres recuperacions didàctiques i bibliogràfiques, i s'han restaurat els títols C2–C4 després de la depuració MG. La compilació queda amb 39 títols de capítol i sense apartats MG ni criteris de producció gràfica. Les 50 propostes gràfiques i els criteris del C3 es conserven al document independent «PLANIFICACIO_GRAFICA_MG_FASE_POSTERIOR.md». No s'ha modificat main.

| 1.69 | 05/11/2026 | Compilació C1–C39 sincronitzada amb els 39 Markdown; C24 actualitzat; títols C2–C4 restaurats; 39 capítols i zero blocs MG al text lector. |


### F4 — depuració documental MG i correcció de l'inventari gràfic (05/11/2026)

S'han retirat del cos lector les 90 propostes gràfiques incloses durant la tercera síntesi als capítols C15–C24 i s'han conservat íntegrament al document independent «PLANIFICACIO_GRAFICA_MG_FASE_POSTERIOR.md», identificades com a material elaborat durant la síntesi i no com a material del Word original. També s'han retirat els registres editorials de C15–C24 i els blocs «Control editorial i límits de verificació» de C22, C23, C33, C34, C35 i C37. La compilació C1–C39 s'ha sincronitzat amb els fitxers individuals corregits.

La verificació directa del Word original «manual con estructura completa.docx» corregeix l'inventari gràfic anterior: s'hi identifiquen 153 propostes úniques, no 340. D'aquestes, 50 ja es conserven al document MG (C1, C2, C3, C33, C34, C35 i C37); queden 103 propostes originals pendents de trasllat (C4–C7, C11, C30–C32, C36, C38 i C39). Les 90 propostes de C15–C24 són addicionals i proceden de la tercera síntesi, no del Word original. Per tant, el document MG contenia en aquell moment 140 propostes arxivades: 50 recuperades del Word original i 90 elaborades durant la tercera síntesi. Restaven 103 propostes originals pendents de trasllat.

| 1.70 | 05/11/2026 | Depuración editorial de C15–C24 y controles C22–C23/C33–C35/C37; 90 propuestas trasladadas a MG; inventario corregido a 153 propuestas originales, 50 archivadas y 103 pendientes. Main intacta. |


### F4 — recuperació completa de l'inventari gràfic original i depuració documental (05/11/2026)

S'ha completat la recuperació de les 103 propostes gràfiques originals pendents. El document Word original conté 153 propostes úniques, distribuïdes en C1–C7, C11 i C30–C39; les 153 queden ara conservades al document independent «PLANIFICACIO_GRAFICA_MG_FASE_POSTERIOR.md». També s'hi conserven les 90 propostes addicionals elaborades durant la tercera síntesi als capítols C15–C24, identificades separadament per procedència. L'arxiu MG conté, per tant, 243 propostes: 153 originals i 90 addicionals.

La depuració del text lector s'ha completat per als apartats identificats: s'han retirat les propostes i registres editorials de C15–C24 i els blocs de control editorial de C22, C23, C33, C34, C35 i C37. La compilació C1–C39 s'ha sincronitzat amb els fitxers individuals. La validació confirma 39 capítols, cap apartat de planificació MG ni registre/control editorial residual a la compilació, i correspondència exacta dels 14 capítols modificats amb els seus fitxers individuals. La branca main continua intacta.

| 1.71 | 05/11/2026 | Recuperades les 153 propostes del Word original i arxivades separadament de les 90 propostes addicionals de C15–C24; total MG 243. Depuració documental C15–C24/C22–C23/C33–C35/C37 i compilació sincronitzada. |
| 1.72 | 05/11/2026 | Normalització terminològica de «arenisca» a «gres» a C26, amb ajust de concordança; compilació C1–C39 sincronitzada. Actualitzats els estats de F2/F4/F5/F6/F7 i les properes actuacions per reflectir el tancament de F4 i F6 i la prioritat de conciliació final de F2. |
| 1.73 | 05/11/2026 | Conciliats els estats obsolets de C28 i C29: F4 documental i F6 transversal consten com a completades; es manté explícit que les receptes no han estat validades experimentalment. |
