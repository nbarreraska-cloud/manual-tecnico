# REGISTRE MESTRE DE RECUPERACIONS EDITORIALS
**Manual tècnic de pintura de miniatures**  
**Versió:** 1.16 · **Data:** 05/11/2026  
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
| 2 | Consolidar el Registre Mestre amb categories RT/RD/AE/MG/SC, prioritats, decisions, fonts i estat real dels canvis. | **En curs**; versió 1.2 creada, amb les intervencions G-01–G-11 separades de la tercera versió. Continua la conciliació fina dels estats i commits dels 39 capítols. |
| 3 | Aplicar les recuperacions tècniques, didàctiques i els ajustos editorials justificats a la tercera versió dels 39 Markdown. | **Completada per a les accions identificades a la matriu**; intervencions aplicades als capítols 3–19, 25–32, 36 i 38; ajust AE als capítols 33–34; els capítols SC es mantenen sense canvis. |
| 4 | Validar els 39 capítols i estabilitzar-ne el contingut, les receptes, els exercicis, la numeració i les referències. | **En curs**; primera comprovació estructural dels 29 Markdown intervinguts sense encapçalaments ni numeracions duplicats, ni encapçalaments buits. Corregits salts de línia literals als capítols 28 i 29. Primera comprovació semàntica de C28–C29: procediments de receptes i materials dels exercicis cotejats amb l'original; codis de pintura restituïts a les llistes. El coteig semàntic complet continua pendent. |
| 5 | Revisar i reconstruir els annexos A–E després d'estabilitzar els 39 capítols. | **Pendent i diferida**; no intervenir-hi ara. |
| 6 | Auditoria global de coherència, referències creuades, traçabilitat i absència de pèrdues o duplicacions. | **Pendent** |
| 7 | Revisió gràfica, consolidació editorial, normalització i maquetació Word. | **Fase final**; les imatges s'aborden després dels annexos. |

La primera versió amb l'estructura completa sintetitzada i la segona síntesi dels 39 capítols són fonts diferenciades. La tercera versió és el resultat del treball actual sobre els 39 Markdown. La fase gràfica i els annexos no s'han d'avançar a la validació i estabilització dels capítols.

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
| 3 | RT · mitjana; AE puntual | Recuperar/confirmar els vuit errors conceptuals i el mètode cromàtic segons auditoria. G-01 es va aplicar a l'HTML, no a aquest Markdown; G-03 no va justificar recuperacions conceptuals addicionals als capítols 3–5. |
| 4 | RT · mitjana | Errors conceptuals i desenvolupament del mètode cromàtic. Recuperació aplicada: nou errors, sis exercicis, síntesi, criteri de selecció de paleta, vuit passos de planificació i exemple de l'armadura blava. Validació integral pendent. |
| 5 | RT · mitjana | Desenvolupament físic de llum i ombres i errors conceptuals. Recuperació aplicada: set errors, sis exercicis, bloqueig/oclusió, geometria de les ombres i llistes d'observació. Validació integral pendent. |
| 6 | RT · mitjana | Recuperar la fitxa i els criteris de lectura dels materials. Ampliació aplicada amb patrons estructurals, propietats de transmissió, mètode d'observació i quatre exercicis; validació integral pendent. |
| 7 | SC | Contingut base protegit per l'auditoria. Posteriorment s'hi va aplicar una recuperació/ampliació operativa de preparació, eines, manteniment i seguretat; no confondre SC inicial amb absència de canvis posteriors. |
| 8 | SC | Contingut protegit en l'auditoria inicial. Posteriorment s'hi van ampliar errors, controls i exercicis; validació global pendent. |
| 9 | SC | Contingut protegit; es va reservar una possible redundància interna entre §9.7 i §9.9 per a revisió global, sense reobertura automàtica. |
| 10 | SC | Contingut protegit per l'auditoria inicial. Posteriorment s'hi va desenvolupar i reorganitzar contingut de veladures/glassejats; validació global pendent. |
| 11 | RT · alta | Intervenció aplicada i tancada editorialment. F4: comprovada l'estructura 11.1–11.10.6, els vuit blocs d'errors i els sis exercicis sobre el text consolidat disponible. El mateix document de referència declara que no s'ha recuperat l'original complet; per tant, no es pot afirmar un coteig integral amb l'original. No reobrir sense una incidència substancial. |
| 12 | RT · alta | F4: coteig de contingut completat amb la font disponible; coincideixen fonaments, cinc tipus de perfilat, selecció cromàtica, materials/eines, sis procediments d'aplicació, cinc exercicis (12.10.1–12.10.5), controls i vuit errors. No s'han identificat omissions substancials en el contingut lector. Es manté una incidència separada: el registre editorial de la font conté una delimitació antiga que assigna tècniques de textura a C14; l'índex definitiu i C13 confirmen que C14 correspon a transparències. Reconciliar només les metadades/remissions, sense reescriure el capítol. |
| 13 | RT · alta | F4: coteig de contingut completat amb la font disponible; es conserven les quatre tècniques (pinzell sec, puntejat, ratllat i esponjat), els procediments, les variables, aplicacions i limitacions, la combinació de tècniques, els nou blocs d'errors i els sis exercicis (13.10.1–13.10.6). No s'han identificat omissions substancials en el contingut lector. Les vuit propostes gràfiques es mantenen reservades a MG. |
| 14 | SC · reobert per incidència substancial F4 | El text original complet no està localitzat; la versió és una consolidació basada en material disponible. En el coteig d'aquest material s'ha recuperat una distinció tècnica central que faltava explícitament al Markdown: transparència del producte pictòric versus transparència de l'objecte representat, inclosa com a error freqüent a la font. Recuperació puntual aplicada; no s'afirma validació integral de l'original. |
| 15 | SC | F4 limitada: comprovada la correspondència estructural de deu apartats, sis exercicis i el focus de planificació lumínica amb el material disponible. No s'ha localitzat un text original complet; el capítol és una consolidació nova basada en l'índex i els acords recuperats. No es pot declarar coteig integral amb l'original. Sense canvis en aquesta passada. |
| 16 | AE | Ajust de numeració i estructura de les geometries aplicat; contingut NMM ampliat posteriorment. F4 limitada: es comproven l'estructura de deu apartats, els sis exercicis i el procediment general disponible. La font declara que no s'ha recuperat un original complet; no es pot afirmar coteig integral. |
| 17 | SC | F4 limitada: comprovada l'estructura de deu apartats, sis exercicis i el criteri central de coherència espacial entre font i superfícies receptores. La font declara que és una versió consolidada nova i que no s'ha recuperat un original complet; no es pot afirmar coteig integral. Sense canvis de contingut. |
| 18 | SC | F4 limitada: comprovada l'estructura de deu apartats, sis exercicis i les eines de planificació/avaluació. La font declara que no s'ha recuperat un original complet; no es pot afirmar coteig integral. Sense canvis de contingut. |
| 19 | SC · F4 verificat sobre la font disponible | S'han cotejat 16 receptes (acer, plata, or, coure i bronze), els codis i les llistes d'ingredients, i els set exercicis. No s'han detectat codis o ingredients absents/afegits. La font disponible declara que no s'ha recuperat un original complet i no especifica proporcions quantitatives; no s'han d'inventar. Les receptes continuen sent propostes no assajades. |
| 20 | SC | Receptes i contingut protegits; no s'hi va identificar recuperació prioritària en l'auditoria. |
| 21 | SC | Receptes i contingut protegits; conservar la denominació original «Combinació cromàtica proposta». |
| 22 | SC | Contingut protegit; respectar els límits amb pell biològica i queratina. |
| 23 | SC | Contingut protegit; conservar la distinció entre estructures tèxtils i acabats/superfícies. |
| 24 | SC | Contingut protegit; no reobrir per qüestions menors. |
| 25 | RD / AE / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis complets, la síntesi i les dues referències opcionals absents; restaurat també l'enllaç de la British Horse Society. Reforçats dos errors i el criteri de selecció cromàtica. Les 10 propostes gràfiques originals es reserven per a MG. Validació semàntica pendent. |
| 26 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, materials, procediment i avaluació; recuperada la síntesi; afegits dos errors freqüents absents de la segona síntesi. Les nou propostes gràfiques originals es reserven per a MG. Validació semàntica pendent. |
| 27 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, materials, procediment i avaluació; recuperada la síntesi; reforçada la delimitació dels efectes sobrenaturals respecte de cristalls i gemmes convencionals. Les 10 propostes gràfiques originals es reserven per a MG. Validació semàntica pendent. |
| 28 | RT · alta / MG | Recuperació tècnica prioritària. La centralització de codis no es va considerar una pèrdua; preservar-la. Recuperació aplicada el 05/11/2026; validació tècnica i de contingut pendent. Primera comprovació semàntica: receptes A–K, materials dels sis exercicis i seqüències de procediment contrastats amb l'original; codis de pintura complets a les llistes. G-08 va preservar §§38.1 i 38.2.5 a l'HTML; la recuperació actual del Markdown és una intervenció diferent. Les 10 propostes gràfiques originals es reserven per a la fase MG. |
| 29 | RT · alta / MG | Recuperació tècnica prioritària. La centralització de codis no es va considerar una pèrdua; preservar-la. Recuperació aplicada el 05/11/2026; validació tècnica i de contingut pendent. Primera comprovació semàntica: receptes A–Q i materials dels sis exercicis contrastats amb l'original; codis de pintura complets a les llistes. Les 10 propostes gràfiques originals es reserven per a la fase MG. |
| 30 | RT / RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperada la divisió entre planificació de valors, temperatura cromàtica i preparació; ampliada l'estructura de les cinc receptes amb objectiu, materials, procediment, control i variants; recuperats els cinc exercicis amb objectiu i síntesi del capítol. Validació semàntica pendent. Les vuit figures originals es reserven per a MG. |
| 31 | RT / RD / MG · baixa | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, procediment i avaluació; recuperada la síntesi; mantinguda la distinció entre sang fresca, coagulada, seca i altres fluids. Les vuit propostes gràfiques originals es reserven per a MG. Validació semàntica pendent. L'auditoria va observar que la segona síntesi ja havia recuperat materials respecte de la primera versió. |
| 32 | RD / MG · mitjana | Intervenció aplicada el 05/11/2026: recuperats els sis exercicis amb objectiu, procediment i avaluació; recuperada la síntesi; mantinguda la distinció entre efecte cromàtic, font lluminosa, OSL, fluorescència i fosforescència. Les vuit propostes gràfiques originals es reserven per a MG. Validació semàntica pendent. |
| 33 | SC / AE / MG | Contingut protegit; revisat el límit amb vidre i superfícies transparents (34), i amb acabats/vernissos (37). G-05 i G-11 són intervencions històriques de l'HTML, no canvis d'aquest Markdown. Les 10 propostes gràfiques originals es reserven per a MG. No s'ha reescrit el contingut ni les receptes; SC preservat. |
| 34 | SC / AE / MG | Ajust editorial aplicat el 05/11/2026: explicitada la diferenciació respecte de ceràmica, porcellana i plàstics (33), i la remissió de vernissos/acabats al capítol 37. Les 10 propostes gràfiques originals es reserven per a MG. Receptes i contingut SC preservats; validació final pendent. |
| 35 | SC | Contingut protegit; no es va identificar recuperació prioritària. |
| 36 | RD / MG · baixa | Intervenció aplicada el 05/11/2026: recuperats i desenvolupats els sis exercicis amb objectiu i procediment; afegits criteris d'avaluació proposats com a millora didàctica, diferenciats del text original; recuperada la síntesi; mantinguts els criteris de selecció i adaptació per material. Les 10 propostes gràfiques originals es reserven per a MG. Validació semàntica pendent. |
| 37 | SC | Contingut protegit. G-08 va ajustar §§37.1, 37.6 i 37.7 a l'HTML i va preservar els apartats 38.1 i 38.2.5; no és una modificació del Markdown actual. Mantenir la seva funció d'acabats visuals i control del brillantor. |
| 38 | RT / RD / MG · alta | F4: estructura i procediments cotejats amb l'original; sis exercicis conservats i desenvolupats, amb criteris d'avaluació identificats com a propostes editorials. Recuperats tres detalls tècnics omesos: comprovacions per seleccionar barnissos acrílics, distinció dels poliuretans de base aquosa i condicions/riscos específics dels aerosols. Resta la revisió transversal de terminologia, coherència i referències. Les 10 propostes gràfiques es reserven per a MG. |
| 39 | SC / MG | Contingut textual protegit; mantenir i planificar el material gràfic de suport sense convertir propostes en imatges ja produïdes. |

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
| 4–5 | Recuperacions aplicades. Comprovació estructural inicial registrada; validació textual, semàntica i coteig complet encara necessaris. |
| 6–13 | Recuperacions/ampliacions aplicades i documentades en commits individuals; fer validació global sense repetir diagnòstics ja tancats. |
| 14–18 | Ampliacions aplicades i documentades. C14, C15, C16 i C18 tenen límits de font: no s'ha localitzat un original complet; les ampliacions es basen en la consolidació disponible de la primera versió i els acords recuperats. |
| 19 | F4: coteig de la font disponible completat per a 16 receptes i set exercicis; codis i ingredients coincideixen. No hi ha proporcions exactes documentades a la font; no s'afegeixen quantitats inventades i es manté l'avís de propostes no assajades. Original complet no recuperat. |
| 20–24, 35, 37, 39 | Capítols auditats i classificats com a SC. No hi ha recuperacions RT/RD pendents identificades per executar en aquests capítols; es mantenen protegits de canvis innecessaris. La seva coherència es comprovarà transversalment a F4/F6 quan afecti referències o límits amb altres capítols. |
| 28 | Recuperació tècnica aplicada. F4 (05/11/2026): coteig complet de fidelitat amb l'original; receptes A–K (ingredients), sis exercicis (materials) i codis de pintura contrastats sense omissions ni incorporacions. Correccions lingüístiques puntuals aplicades. Validada la correspondència documental; resta la revisió transversal de coherència tècnica i referències. |
| 29 | Recuperació tècnica aplicada. F4 (05/11/2026): coteig complet de fidelitat amb l'original; receptes A–Q (ingredients), sis exercicis (materials) i codis de pintura contrastats sense omissions ni incorporacions. Es comprova també la conservació de la integració de pedres i fragments amb el terreny. Correccions lingüístiques puntuals aplicades. Validada la correspondència documental; resta la revisió transversal de coherència tècnica i referències. |
| 25 | Recuperació didàctica/editorial aplicada el 05/11/2026: sis exercicis amb objectiu, materials, procediment i avaluació; recuperació de la síntesi; incorporació de dues referències absents i restauració de l'enllaç BHS; ampliació de dos errors i del criteri de selecció cromàtica. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |
| 26 | Recuperació didàctica aplicada el 05/11/2026: sis exercicis amb objectiu, materials, procediment i avaluació; recuperació de la síntesi; ampliació de dos errors de representació. Les sis referències existents es mantenen. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |
| 27 | Recuperació didàctica aplicada el 05/11/2026: sis exercicis amb objectiu, materials, procediment i avaluació; recuperació de la síntesi i reforç de la delimitació respecte dels efectes sobrenaturals del capítol 32. Les nou referències existents es mantenen. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |
| 30 | Recuperació tècnica i didàctica aplicada el 05/11/2026: estructurades les cinc receptes A–E amb objectiu, pintures, procediment, control visual i variants; restituïdes la planificació de valors, la temperatura cromàtica, la preparació, els errors, l'avaluació, els cinc exercicis i la síntesi. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |
| 31 | Recuperació didàctica aplicada el 05/11/2026: sis exercicis amb objectiu, procediment i avaluació; recuperada la síntesi i reforçada la distinció entre sang fresca, coagulada, seca i fluids no sanguinis. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |
| 32 | Recuperació didàctica aplicada el 05/11/2026: sis exercicis amb objectiu, procediment i avaluació; síntesi conceptual; conservació de la distinció entre efecte cromàtic, font lluminosa i OSL, i entre fluorescència i fosforescència. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |
| 33 | Revisió editorial AE realitzada el 05/11/2026: confirmada la coherència de les remissions a vidre (34), acabats (37), brutícia (29) i desgast (36). G-05 i G-11 afecten l'HTML, no aquest Markdown. Sense modificacions de contingut; SC preservat. |
| 34 | Ajust editorial AE aplicat el 05/11/2026: explicitats els límits respecte de ceràmica, porcellana i plàstics (33), i la remissió dels acabats i vernissos al capítol 37. Les 10 propostes gràfiques originals es reserven per a MG. Sense reescriure receptes. |
| 36 | Recuperació didàctica aplicada el 05/11/2026: sis exercicis amb objectiu, procediment i avaluació; síntesi conceptual; reforç de la diferenciació entre envelliment, desgast i deteriorament. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |
| 38 | Recuperació tècnica i didàctica aplicada el 05/11/2026: incorporats els fonaments i límits de la protecció, distinció entre assecat superficial, assecat al tacte i estabilització, sis exercicis desenvolupats i criteris d'avaluació final. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |

**No interpretar “aplicat” com “validat”.** La validació ha de comprovar el capítol complet, la coherència amb l'original o la font disponible, la numeració, les referències, les receptes i els exercicis que pertoquin.

## 7. Decisions transversals que cal mantenir

- Arquitectura fixa de 39 capítols.
- Primera versió i segona síntesi són fonts diferenciades; la tercera versió s'aplica als 39 Markdown.
- El contingut de la segona síntesi es conserva en català, d'acord amb el criteri específic establert per a aquests fitxers.
- La primera versió HTML no es modifica en aquesta fase.
- Els annexos A–E s'aborden després d'estabilitzar els capítols.
- La distinció entre capítol 37 (aparença, acabats i brillantor) i capítol 38 (barnissos, protecció i conservació) s'ha de mantenir a totes les referències creuades.
- No confondre propostes de figures amb recursos visuals produïts.
- No atribuir validació física a cap recepta o barreja que no tingui registre d'assaig.

## 8. Properes actuacions operatives

1. Completar la conciliació fina de la traçabilitat entre la matriu, els fitxers Markdown, els commits i el document de seguiment.
2. Continuar F4: validar semànticament i tècnicament els 29 capítols Markdown intervinguts, sense repetir l'auditoria F1 ni reobrir els capítols SC sense una incidència substancial.
3. Continuar F4 amb els capítols d'alta prioritat C12–C13. C11 queda amb el límit documental explícit de no disposar de l'original complet; C28–C29 tenen el coteig de fidelitat documental completat; C38 té recuperats els detalls tècnics omesos i resta la revisió transversal.
4. Comprovar, per a cada capítol, la fidelitat a la font disponible, la conservació de receptes i ingredients, la seqüència dels procediments, els exercicis, la numeració, les referències i les delimitacions.
5. Mantenir explícits els límits documentals de C14, C15, C16 i C18: no atribuir al document original complet continguts que s'han ampliat a partir de la primera versió o d'acords recuperats.
6. Després d'estabilitzar els 39 capítols, abordar els annexos A–E, la coherència global, les referències creuades i la fase gràfica.
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

Aquest registre és una consolidació operativa basada en l'auditoria i els resultats recuperats del projecte. Els punts marcats com a pendents o no validats s'han de comprovar amb el fitxer real i la font corresponent abans de declarar-los tancats.


### Incidència transversal de terminologia detectada durant F4

En C37–C39 conviuen les formes `barnís/barnissos/barnissat` i `vernís/vernissar`. Cal normalitzar la terminologia catalana de manera transversal i coherent, no corregir un sol capítol de forma aïllada. La forma normativa de referència és `vernís` i els derivats corresponents (`vernissar`, `envernissar`, `vernissat`); la normalització queda pendent d'una passada conjunta pels 39 Markdown i de la revisió de totes les remissions. No s'ha fet encara cap canvi terminològic d'aquest tipus.
