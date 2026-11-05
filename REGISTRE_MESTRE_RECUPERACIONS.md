# REGISTRE MESTRE DE RECUPERACIONS EDITORIALS
**Manual tècnic de pintura de miniatures**  
**Versió:** 1.30 · **Data:** 05/11/2026  
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
| 2 | Consolidar el Registre Mestre amb categories RT/RD/AE/MG/SC, prioritats, decisions, fonts i estat real dels canvis. | **En curs**; versió vigent 1.25. Resta conciliar la matriu per capítol amb els estats finals de F4 i eliminar contradiccions entre anotacions històriques i estat vigent. |
| 3 | Aplicar les recuperacions tècniques, didàctiques i els ajustos editorials justificats a la tercera versió dels 39 Markdown. | **Completada per a les accions identificades a la matriu**; recuperacions aplicades als capítols 3–19, 25–32, 36 i 38; ajustos AE als capítols 33–34; els capítols SC es mantenen protegits, excepte ajustos editorials documentats. |
| 4 | Validar els 39 capítols i estabilitzar-ne el contingut, les receptes, els exercicis, la numeració i les referències. | **En curs**; coteig documental completat per a C5, C12–C13, C25–C29 i C38, amb els límits de font registrats; correspondència estructural i didàctica principal revisada per a C4 i C6; revisió estructural i operativa de C7, incloent-hi seguretat i exercicis; revisió estructural i procedimental de C8; revisió de contingut disponible completada per a C30–C32 i C36; C19 cotejat dins dels límits de la font disponible. La revisió semàntica de remissions C1–C39 està completada i documentada; s'ha precisat una remissió a C18. Continuen pendents les comprovacions de fidelitat documental, estructura i contingut dels capítols encara no cotejats. |
| 5 | Revisar i reconstruir els annexos A–E després d'estabilitzar els 39 capítols. | **Pendent i diferida** fins al tancament de F4. |
| 6 | Auditoria global de coherència, referències creuades, traçabilitat i absència de pèrdues o duplicacions. | **Completada el 05/11/2026**; auditoria transversal C1–C39 tancada. No s'han detectat contradiccions globals que justifiquin reorganitzacions o retallades. No equival a validació experimental. |
| 7 | Revisió gràfica, consolidació editorial i maquetació Word. | **Pendent**; s'abordarà després de F4 i F5. |

La primera versió amb l'estructura completa sintetitzada i la segona síntesi dels 39 capítols són fonts diferenciades. La tercera versió és el resultat del treball actual sobre els 39 Markdown. La compilació documental única dels capítols 1–39 ja s'ha creat i verificat, però continua sent una compilació de treball fins al tancament de F4. La fase gràfica i els annexos no s'han d'avançar a la validació i estabilització dels capítols.

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
8. Les propostes de figures es mantenen com a especificacions editorials; no es presenten com a imatges produïdes ni com a proves físiques.
9. Cada intervenció ha de distingir quatre estats: **diagnosticada**, **decidida**, **aplicada** i **validada**. Un canvi aplicat no queda automàticament validat.
10. La branca intervencion-editorial-2026-11 és la branca de treball; main no s'ha de modificar.
11. L'objectiu d'extensió de la tercera versió és aproximadament 350–375 pàgines, amb un límit orientatiu d'unes 400. És un criteri de control, no una ordre de retall: no s'ha de suprimir contingut tècnic, procediments, receptes, exercicis, variants ni advertiments només per reduir pàgines.

## 5. Matriu de classificació de l'auditoria 39/39

Aquesta matriu conserva el dictamen comparatiu recuperat de l'auditoria. La classificació no implica que totes les accions estiguin ja aplicades o validades.

| Cap. | Categoria / prioritat | Dictamen de l'auditoria i estat conegut |
|---:|---|---|
| 1 | SC | Contingut protegit. A més, G-01 es va aplicar a l'HTML, no a aquest Markdown; mantenir aquesta intervenció diferenciada de la classificació general SC. |
| 2 | SC | Contingut protegit; no es va identificar recuperació prioritària. |
| 3 | RT · mitjana; AE puntual | Recuperar/confirmar els vuit errors conceptuals i el mètode cromàtic segons auditoria. G-01 es va aplicar a l'HTML, no a aquest Markdown; G-03 no va justificar recuperacions conceptuals addicionals als capítols 3–5. F4: «vernissatge» normalitzat a «envernissament» en la remissió a C38. |
| 4 | RT · mitjana / AE puntual | Errors conceptuals i desenvolupament del mètode cromàtic. Recuperació aplicada: nou errors, sis exercicis, síntesi, criteri de selecció de paleta, vuit passos de planificació i exemple de l'armadura blava. F4: revisada la correspondència estructural i didàctica principal amb la font: es mantenen els nou errors, sis exercicis, set criteris de planificació, seqüència operativa de vuit passos, exemple de l'armadura i vuit referències. No s'han identificat omissions substancials en aquests elements. Les nou propostes de figures es reserven per a MG; el coteig textual integral continua pendent. |
| 5 | RT · mitjana | Desenvolupament físic de llum i ombres i errors conceptuals. Recuperació aplicada: set errors, sis exercicis, bloqueig/oclusió, geometria de les ombres i llistes d'observació. F4: coteig de contingut i bibliografia completat amb la font disponible; es conserven els conceptes centrals de propagació, fotometria, geometria, absorció/reflexió/transmissió, ombres, reflexos, volum i anàlisi de miniatures. Es mantenen set errors i sis exercicis; s'han recuperat vuit referències bibliogràfiques omeses (12 referències en total). Les 16 propostes de figures es reserven per a MG. No s'han modificat receptes ni s'atribueixen resultats experimentals. |
| 6 | RT · mitjana | Recuperar la fitxa i els criteris de lectura dels materials. Ampliació aplicada amb patrons estructurals, propietats de transmissió, mètode d'observació i quatre exercicis. F4: revisada la correspondència estructural i didàctica principal amb la font; es mantenen els deu errors, el mètode d'observació de set passos, els quatre exercicis i les cinc referències. No s'han identificat omissions substancials en aquests elements. Les vuit propostes de figures originals es reserven per a MG; el coteig textual integral continua pendent. |
| 7 | SC | Contingut base protegit per l'auditoria. Posteriorment s'hi va aplicar una recuperació/ampliació operativa de preparació, eines, manteniment i seguretat; no confondre SC inicial amb absència de canvis posteriors. F4: revisada la correspondència estructural i operativa amb la font, inclosos els quatre exercicis, els criteris de seguretat i les tres referències de consulta; no s'han identificat omissions substancials en aquests blocs. Les vuit propostes de figures originals es reserven a MG. El coteig textual integral continua pendent. |
| 8 | SC | Contingut protegit en l'auditoria inicial. Posteriorment s'hi van ampliar errors, controls i exercicis. F4: revisada la correspondència estructural i procedimental amb la font; es mantenen els blocs 8.1–8.10, els sis errors, els quatre exercicis pràctics i l'exercici integrador, inclosos els procediments, els criteris d'observació i d'avaluació. No s'han identificat omissions substancials en els elements revisats. Les vuit propostes de figures originals es reserven a MG. El coteig textual integral continua pendent. |
| 9 | SC | Contingut protegit; es va reservar una possible redundància interna entre §9.7 i §9.9 per a revisió global, sense reobertura automàtica. |
| 10 | SC | Contingut protegit per l'auditoria inicial. Posteriorment s'hi va desenvolupar i reorganitzar contingut de veladures/glassejats; validació global pendent. |
| 11 | RT · alta | Intervenció aplicada i tancada editorialment. F4: comprovada l'estructura 11.1–11.10.6, els vuit blocs d'errors i els sis exercicis sobre el text consolidat disponible. El mateix document de referència declara que no s'ha recuperat l'original complet; per tant, no es pot afirmar un coteig integral amb l'original. No reobrir sense una incidència substancial. |
| 12 | RT · alta / AE de metadades resolta | F4: coteig de contingut completat amb la font disponible; coincideixen fonaments, cinc tipus de perfilat, selecció cromàtica, materials/eines, sis procediments d'aplicació, cinc exercicis (12.10.1–12.10.5), controls i vuit errors. No s'han identificat omissions substancials en el contingut lector. La nota «Registre editorial del capítol 12» de la font conté una delimitació desfasada: atribueix part de les tècniques de textura a C14. L'índex definitiu i els continguts efectius confirmen que les quatre tècniques (pinzell sec, puntejat, ratllat i esponjat) pertanyen a C13, mentre que C14 tracta transparències. Incidència conciliada com a metadada obsoleta de la font; no es modifica C12, C13 ni C14. |
| 13 | RT · alta | F4: coteig de contingut completat amb la font disponible; es conserven les quatre tècniques (pinzell sec, puntejat, ratllat i esponjat), els procediments, les variables, aplicacions i limitacions, la combinació de tècniques, els nou blocs d'errors i els sis exercicis (13.10.1–13.10.6). No s'han identificat omissions substancials en el contingut lector. Les vuit propostes gràfiques es mantenen reservades a MG. |
| 14 | SC · reobert per incidència substancial F4 | El text original complet no està localitzat; la versió és una consolidació basada en material disponible. En el coteig d'aquest material s'ha recuperat una distinció tècnica central que faltava explícitament al Markdown: transparència del producte pictòric versus transparència de l'objecte representat, inclosa com a error freqüent a la font. Recuperació puntual aplicada; no s'afirma validació integral de l'original. |
| 15 | SC | F4 limitada: comprovada la correspondència estructural de deu apartats, sis exercicis i el focus de planificació lumínica amb el material disponible. No s'ha localitzat un text original complet; el capítol és una consolidació nova basada en l'índex i els acords recuperats. No es pot declarar coteig integral amb l'original. Sense canvis en aquesta passada. |
| 16 | AE | Ajust de numeració i estructura de les geometries aplicat; contingut NMM ampliat posteriorment. F4 limitada: es comproven l'estructura de deu apartats, els sis exercicis i el procediment general disponible. La font declara que no s'ha recuperat un original complet; no es pot afirmar coteig integral. |
| 17 | SC | F4 limitada: comprovada l'estructura de deu apartats, sis exercicis i el criteri central de coherència espacial entre font i superfícies receptores. La font declara que és una versió consolidada nova i que no s'ha recuperat un original complet; no es pot afirmar coteig integral. Sense canvis de contingut. |
| 18 | SC / AE puntual | F4 limitada: comprovada l'estructura de deu apartats, sis exercicis i les eines de planificació/avaluació. La font declara que no s'ha recuperat un original complet; no es pot afirmar coteig integral. S'ha revisat la remissió a C35–C38 i s'ha precisat perquè diferenciï harmonització cromàtica (C35), desgast i transformació (C36), acabats superficials (C37) i protecció/conservació (C38). Sense canvis en receptes ni procediments. |
| 19 | SC · F4 verificat sobre la font disponible | S'han cotejat 16 receptes (acer, plata, or, coure i bronze), els codis i les llistes d'ingredients, i els set exercicis. No s'han detectat codis o ingredients absents/afegits. La font disponible declara que no s'ha recuperat un original complet i no especifica proporcions quantitatives; no s'han d'inventar. Les receptes continuen sent propostes no assajades. |
| 20 | SC | Receptes i contingut protegits; no s'hi va identificar recuperació prioritària en l'auditoria. |
| 21 | SC | Receptes i contingut protegits; conservar la denominació original «Combinació cromàtica proposta». |
| 22 | SC / AE puntual | Contingut protegit; respectar els límits amb pell biològica i queratina. F4: corregit «del brillantor» per «de la brillantor» en la remissió a C37; sense canvis tècnics. |
| 23 | SC / AE puntual | Contingut protegit; conservar la distinció entre estructures tèxtils i acabats/superfícies. F4: corregit «el brillantor» per «la brillantor»; sense canvis tècnics. |
| 24 | SC | Contingut protegit; no reobrir per qüestions menors. |
| 25 | RD / AE / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis complets, la síntesi i les dues referències opcionals absents; restaurat també l'enllaç de la British Horse Society. Reforçats dos errors i el criteri de selecció cromàtica. Les 10 propostes gràfiques originals es reserven per a MG. F4: coteig completat; restituïdes les tres referències de paleta absents, sense alterar receptes. Receptes no assajades. |
| 26 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, materials, procediment i avaluació; recuperada la síntesi; afegits dos errors freqüents absents de la segona síntesi. Les nou propostes gràfiques originals es reserven per a MG. F4: coteig completat; 10 receptes, sis exercicis i 19 referències de paleta preservats. Receptes no assajades. |
| 27 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, materials, procediment i avaluació; recuperada la síntesi; reforçada la delimitació dels efectes sobrenaturals respecte de cristalls i gemmes convencionals. Les 10 propostes gràfiques originals es reserven per a MG. F4: coteig completat; 14 receptes, sis exercicis i 28 referències de paleta preservats. Receptes no assajades. |
| 28 | RT · alta / MG | Recuperació tècnica aplicada. F4: coteig de fidelitat documental completat amb l'original per a les 11 receptes A–K, els materials dels sis exercicis i els codis de pintura; sense omissions ni incorporacions detectades en aquests elements. Resta la validació semàntica i la conciliació transversal de coherència tècnica i referències. Les 10 propostes gràfiques originals es reserven per a MG. |
| 29 | RT · alta / MG | Recuperació tècnica aplicada. F4: coteig de fidelitat documental completat amb l'original per a les 17 receptes A–Q, els materials dels sis exercicis i els codis de pintura; sense omissions ni incorporacions detectades en aquests elements. També es conserva la integració de pedres i fragments amb el terreny. Resta la validació semàntica i la conciliació transversal de coherència tècnica i referències. Les 10 propostes gràfiques originals es reserven per a MG. |
| 30 | RT / RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperada la divisió entre planificació de valors, temperatura cromàtica i preparació; ampliada l'estructura de les cinc receptes amb objectiu, materials, procediment, control i variants; recuperats els cinc exercicis amb objectiu i síntesi del capítol. F4: revisió de contingut completada; cinc receptes i cinc exercicis preservats. Receptes no assajades. Les vuit figures originals es reserven per a MG. |
| 31 | RT / RD / MG · baixa / AE puntual | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, procediment i avaluació; recuperada la síntesi; mantinguda la distinció entre sang fresca, coagulada, seca i altres fluids. Les vuit propostes gràfiques originals es reserven per a MG. F4: revisió de contingut completada; cinc receptes i sis exercicis preservats. Receptes no assajades. Corregides tres aparicions de «del brillantor» per «de la brillantor»; sense canvis tècnics. F4: precisada la remissió de 31.7: C37 per a selecció/control de brillantor; C38 per a vernissos protectors, envernissament i conservació. Sense canvis en receptes ni procediments. |
| 32 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, procediment i avaluació; recuperada la síntesi; mantinguda la distinció entre efecte cromàtic, font lluminosa, OSL, fluorescència i fosforescència. Les vuit propostes gràfiques originals es reserven per a MG. F4: revisió de contingut completada; cinc receptes i sis exercicis preservats. Receptes no assajades. |
| 33 | SC / AE / MG | Contingut protegit; revisat el límit amb vidre i superfícies transparents (34), i amb acabats/vernissos (37). G-05 i G-11 són intervencions històriques de l'HTML, no canvis d'aquest Markdown. Les 10 propostes gràfiques originals es reserven per a MG. F4: remissions a C34 i C37 conciliades; ara es diferencia C37 (acabat/brillantor) de C38 (vernissos protectors/envernissament/conservació). Corregits tres usos de «el/del brillantor» i sis «hendidures» per «cavitats». Sense canvis en receptes o contingut tècnic. |
| 34 | SC / AE / MG | Ajust editorial aplicat el 05/11/2026: explicitada la diferenciació respecte de ceràmica, porcellana i plàstics (33), i la remissió de vernissos/acabats. Les 10 propostes gràfiques originals es reserven per a MG. F4: remissions a C33, C31 i C37 conciliades; ara es diferencia C37 (acabat/brillantor) de C38 (vernissos protectors/envernissament/conservació). Corregit «el brillantor» per «la brillantor» i regularitzada la concordança de la remissió. Receptes i contingut SC preservats. |
| 35 | SC | Contingut protegit; no es va identificar recuperació prioritària. |
| 36 | RD / MG · baixa | Intervenció aplicada el 05/11/2026: recuperats i desenvolupats els sis exercicis amb objectiu i procediment; afegits criteris d'avaluació proposats com a millora didàctica, diferenciats del text original; recuperada la síntesi; mantinguts els criteris de selecció i adaptació per material. Les 10 propostes gràfiques originals es reserven per a MG. F4: revisió de contingut completada; sis exercicis, deu errors i set famílies d'adaptació material preservats. Criteris d'avaluació identificats com a propostes editorials. |
| 37 | SC / AE puntual | Contingut protegit. G-08 va ajustar §§37.1, 37.6 i 37.7 a l'HTML i va preservar els apartats 38.1 i 38.2.5; no és una modificació del Markdown actual. F4: normalitzades les formes «barnissos/barnissat» a «vernissos/envernissament» i corregit «el brillantor» per «la brillantor», sense alterar el contingut tècnic. |
| 38 | RT / RD / MG · alta / AE puntual | F4: estructura i procediments cotejats amb l'original; sis exercicis conservats i desenvolupats, amb criteris d'avaluació identificats com a propostes editorials. Recuperats tres detalls tècnics omesos: comprovacions per seleccionar vernissos acrílics, distinció dels poliuretans de base aquosa i condicions/riscos específics dels aerosols. Passada transversal immediata: terminologia normalitzada a «vernís/envernissament»; corregit «el brillantor» per «la brillantor». Resta la revisió global de coherència i referències. Les 10 propostes gràfiques es reserven per a MG. |
| 39 | SC / MG / AE puntual | Contingut textual protegit; mantenir i planificar el material gràfic de suport sense convertir propostes en imatges ja produïdes. F4: normalitzada la terminologia de barnissat en les referències a C38; contingut tècnic protegit. |

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
| 4 | F4: revisada la correspondència estructural i didàctica principal amb la font; el coteig textual integral continua pendent. |
| 5 | F4: coteig de contingut i bibliografia completat amb la font disponible; s'han recuperat vuit referències bibliogràfiques omeses. Les figures originals continuen reservades a MG. |
| 6 | F4: revisada la correspondència estructural i didàctica principal amb la font; el coteig textual integral continua pendent. |
| 7 | F4: revisada la correspondència estructural i operativa, inclosos els blocs de seguretat, els quatre exercicis i les tres referències de consulta; el coteig textual integral continua pendent. |
| 8 | F4: revisada la correspondència estructural i procedimental, inclosos errors, exercicis i criteris d'avaluació; el coteig textual integral continua pendent. |
| 9–13 | Recuperacions/ampliacions aplicades i documentades en commits individuals; fer validació global sense repetir diagnòstics ja tancats. |
| 14–18 | Ampliacions aplicades i documentades. C14, C15, C16 i C18 tenen límits de font: no s'ha localitzat un original complet; les ampliacions es basen en la consolidació disponible de la primera versió i els acords recuperats. |
| 19 | F4: coteig de la font disponible completat per a 16 receptes i set exercicis; codis i ingredients coincideixen. No hi ha proporcions exactes documentades a la font; no s'afegeixen quantitats inventades i es manté l'avís de propostes no assajades. Original complet no recuperat. |
| 20–24, 35, 37, 39 | Capítols auditats i classificats com a SC. No hi ha recuperacions RT/RD pendents identificades per executar en aquests capítols; es mantenen protegits de canvis innecessaris. La seva coherència es comprovarà transversalment a F4/F6 quan afecti referències o límits amb altres capítols. |
| 28 | Recuperació tècnica aplicada. F4 (05/11/2026): coteig complet de fidelitat amb l'original; receptes A–K (ingredients), sis exercicis (materials) i codis de pintura contrastats sense omissions ni incorporacions. Correccions lingüístiques puntuals aplicades. Validada la correspondència documental; resta la revisió transversal de coherència tècnica i referències. |
| 29 | Recuperació tècnica aplicada. F4 (05/11/2026): coteig complet de fidelitat amb l'original; receptes A–Q (ingredients), sis exercicis (materials) i codis de pintura contrastats sense omissions ni incorporacions. Es comprova també la conservació de la integració de pedres i fragments amb el terreny. Correccions lingüístiques puntuals aplicades. Validada la correspondència documental; resta la revisió transversal de coherència tècnica i referències. |
| 25 | F4 (05/11/2026): coteig amb la font disponible completat; 13 receptes A–M i sis exercicis preservats. Detectada i corregida l'omissió de tres referències complementàries de la paleta (Dark Sea Blue, Light Flesh i Skin Tone); ara es conserven les 12 pintures de la taula original. No s'han alterat ingredients ni combinacions de receptes. Les propostes continuen sense validació experimental. |
| 26 | F4 (05/11/2026): coteig de contingut amb la font disponible completat; deu receptes A–J, sis exercicis i la paleta de 19 referències es mantenen. No s'han identificat omissions substancials en classificació, procediments, errors, avaluació ni delimitacions. Receptes no assajades. |
| 27 | F4 (05/11/2026): coteig de contingut amb la font disponible completat; catorze receptes A–N, sis exercicis i la paleta de 28 referències es mantenen. Es conserva la delimitació entre roca/mineral (C26), cristall, gel, neu i gemma (C27), i els efectes sobrenaturals (C32). Receptes no assajades. |
| 30 | F4 (05/11/2026): revisió de contingut amb la font disponible completada; cinc receptes A–E i cinc exercicis preservats. Es conserven la planificació de valors, la temperatura cromàtica, la preparació, els errors i la delimitació respecte dels efectes sobrenaturals de C32. Receptes no assajades. |
| 31 | F4 (05/11/2026): revisió de contingut amb la font disponible completada; cinc receptes A–E i sis exercicis preservats. Es manté la distinció entre sang fresca, acumulada/coagulada, seca i fluids no sanguinis, així com la separació entre color, consistència, distribució i acabat. Receptes no assajades. |
| 32 | F4 (05/11/2026): revisió de contingut amb la font disponible completada; cinc receptes A–E i sis exercicis preservats. Es mantenen les distincions entre efecte cromàtic, font lluminosa i OSL, i entre fluorescència i fosforescència. Els tutorials no s'atribueixen com a receptes pròpies ni s'afegeixen productes externs. Receptes no assajades. |
| 33 | Revisió editorial AE realitzada el 05/11/2026: confirmada la coherència de les remissions a vidre (34), acabats/brillantor (37) i protecció/envernissament (38), brutícia (29) i desgast (36). G-05 i G-11 afecten l'HTML, no aquest Markdown. Sense modificacions de contingut tècnic; SC preservat. |
| 34 | Ajust editorial AE aplicat el 05/11/2026: explicitats els límits respecte de ceràmica, porcellana i plàstics (33), i conciliada la remissió entre acabats/brillantor (37) i vernissos protectors/envernissament/conservació (38). Les 10 propostes gràfiques originals es reserven per a MG. Sense reescriure receptes. |
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

1. Completar la conciliació de la matriu per capítol amb els estats finals de F4, els fitxers Markdown i els commits; retirar o marcar com a històriques les instruccions que ja han quedat superades.
2. Completar F4: continuar el coteig documental i la validació estructural dels capítols encara no revisats, sense repetir F1 ni reobrir capítols SC sense incidència substancial. La revisió semàntica de remissions C1–C39 ja està completada; C5 té coteig de contingut/bibliografia completat i C4 revisió estructural/didàctica principal.
3. Mantenir explícits els límits documentals de C11 i C14–C18: no atribuir a un original complet continguts que s'han ampliat a partir de la primera versió o d'acords recuperats.
4. Verificar per als capítols pendents la fidelitat a la font disponible, la conservació de receptes i ingredients, la seqüència dels procediments, els exercicis, la numeració, les referències i les delimitacions.
5. La compilació documental dels capítols 1–39 ja està creada a `TERCERA_SINTESI_CONSOLIDADA_C01-C39.md` i la correspondència textual dels 39 capítols amb els fitxers font s'ha comprovat. Cal mantenir-la sincronitzada si F4 exigeix canvis posteriors.
6. Després d'estabilitzar els 39 capítols, abordar els annexos A–E (F5); la fase gràfica i la maquetació Word (F7) queden per després.
7. Mantenir la branca intervencion-editorial-2026-11; no modificar main ni intervenir en l'HTML de la primera versió durant aquesta fase.

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
