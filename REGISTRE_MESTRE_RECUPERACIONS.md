# REGISTRE MESTRE DE RECUPERACIONS EDITORIALS
**Manual tècnic de pintura de miniatures**  
**Versió:** 1.0 · **Data:** 05/11/2026  
**Branca:** intervencion-editorial-2026-11

## 1. Funció i abast

Aquest registre és el document operatiu únic per controlar les recuperacions detectades en l'auditoria comparativa dels 39 capítols de la segona síntesi. No substitueix els capítols, les fonts ni el document de seguiment: relaciona diagnòstic, decisió editorial, prioritat, aplicació i validació.

La primera versió és el document amb l'estructura completa sintetitzada, conservat al repositori com a HTML. La segona síntesi és el conjunt dels 39 capítols Markdown, distribuïts actualment en dues carpetes del repositori:
- segunda_sintesis/: capítols 01–11.
- segunda_sintesi/: capítols 12–39.

La tercera versió és el resultat de les intervencions sobre aquests 39 Markdown. L'HTML de la primera versió queda fora d'aquest flux i no s'hi ha d'intervenir durant aquesta fase.

## 2. Fases generals i estat

| Fase | Objectiu | Estat |
|---|---|---|
| 0 | Preservació de versions, fonts i traçabilitat; treball en branca separada | **Completada** |
| 1 | Auditoria comparativa dels 39 capítols i identificació de pèrdues, contingut correcte i incidències | **Completada (39/39)** |
| 2 | Consolidació d'aquest Registre Mestre: categories, prioritats, decisions i estat real de cada intervenció | **En curs** |
| 3 | Aplicació de les recuperacions tècniques, didàctiques i ajustos editorials justificats | **En curs**; capítols 4–19 tenen intervencions registrades a la branca |
| 4 | Validació textual, tècnica, didàctica i estructural de les intervencions | **Pendent / parcial segons capítol** |
| 5 | Depuració i planificació del material gràfic | **Pendent**; no generar ni inserir imatges en aquesta fase |
| 6 | Revisió coordinada d'annexos, referències creuades i coherència global | **Pendent** |
| 7 | Exportació, paginació, maquetació i auditoria final | **Fase final** |

La consolidació del registre és el pas de control immediat perquè les intervencions ja iniciades no es dupliquin ni quedin desconnectades de l'auditoria 39/39. No s'ha de descriure la fase 3 com a no iniciada: ja hi ha canvis aplicats a la branca.

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

## 5. Matriu de classificació de l'auditoria 39/39

Aquesta matriu conserva el dictamen comparatiu recuperat de l'auditoria. La classificació no implica que totes les accions estiguin ja aplicades o validades.

| Cap. | Categoria / prioritat | Dictamen de l'auditoria i estat conegut |
|---:|---|---|
| 1 | SC | Contingut protegit. A més, G-01 va aprovar l'ajust editorial del §1.5; mantenir aquesta aprovació diferenciada de la classificació general SC. |
| 2 | SC | Contingut protegit; no es va identificar recuperació prioritària. |
| 3 | RT · mitjana; AE puntual | Recuperar/confirmar els vuit errors conceptuals i el mètode cromàtic segons auditoria. G-01 va aprovar els §§3.1 i 3.4.3; G-03 no va justificar recuperacions conceptuals addicionals als capítols 3–5. |
| 4 | RT · mitjana | Errors conceptuals i desenvolupament del mètode cromàtic. Recuperació aplicada: nou errors, sis exercicis, síntesi, criteri de selecció de paleta, set criteris de planificació i exemple de l'armadura blava. Validació integral pendent. |
| 5 | RT · mitjana | Desenvolupament físic de llum i ombres i errors conceptuals. Recuperació aplicada: set errors, sis exercicis, bloqueig/oclusió, geometria de les ombres i llistes d'observació. Validació integral pendent. |
| 6 | RT · mitjana | Recuperar la fitxa i els criteris de lectura dels materials. Ampliació aplicada amb patrons estructurals, propietats de transmissió, mètode d'observació i quatre exercicis; validació integral pendent. |
| 7 | SC | Contingut base protegit per l'auditoria. Posteriorment s'hi va aplicar una recuperació/ampliació operativa de preparació, eines, manteniment i seguretat; no confondre SC inicial amb absència de canvis posteriors. |
| 8 | SC | Contingut protegit en l'auditoria inicial. Posteriorment s'hi van ampliar errors, controls i exercicis; validació global pendent. |
| 9 | SC | Contingut protegit; es va reservar una possible redundància interna entre §9.7 i §9.9 per a revisió global, sense reobertura automàtica. |
| 10 | SC | Contingut protegit per l'auditoria inicial. Posteriorment s'hi va desenvolupat i reorganitzat contingut de veladures/glassejats; validació global pendent. |
| 11 | RT · alta | Recuperar sis procediments que s'havien comprimit. Intervenció aplicada amb modalitats de rentats, tintes, pigments, acumulacions, sis procediments, vuit errors i sis exercicis; validació pendent. |
| 12 | RT · alta | Recuperar passos específics dels perfilats. Intervenció aplicada amb fonaments, cinc tipus de perfilat, sis procediments, controls, errors i exercicis; validació pendent. |
| 13 | RT · alta | Recuperar variables i limitacions de les tècniques de textura. Intervenció aplicada a pinzell sec, puntejat, ratllat i esponjat, amb criteris, errors i exercicis; validació pendent. |
| 14 | SC | Contingut protegit en l'auditoria inicial. Ampliació posterior documentada sobre la consolidació disponible de la primera versió; no hi ha text original complet localitzat. |
| 15 | SC | Contingut protegit en l'auditoria inicial. Ampliació posterior documentada sobre la consolidació disponible de la primera versió; no hi ha text original complet localitzat. |
| 16 | AE | Ajust de numeració i estructura de les geometries. Correcció aplicada; contingut NMM ampliat posteriorment. |
| 17 | SC | Contingut protegit en l'auditoria inicial. Ampliació posterior d'OSL aplicada; validació global pendent. |
| 18 | SC | Contingut protegit en l'auditoria inicial. Ampliació posterior de planificació, seqüenciació, control, avaluació i exercicis aplicada; no hi ha text original complet localitzat. |
| 19 | SC | Receptes i ingredients protegits per l'auditoria. Posteriorment s'ha ampliat el contingut de metalls i la paleta/formulació; les propostes no s'han de presentar com a assajades. |
| 20 | SC | Receptes i contingut protegits; no s'hi va identificar recuperació prioritària en l'auditoria. |
| 21 | SC | Receptes i contingut protegits; conservar la denominació original «Combinació cromàtica proposta». |
| 22 | SC | Contingut protegit; respectar els límits amb pell biològica i queratina. |
| 23 | SC | Contingut protegit; conservar la distinció entre estructures tèxtils i acabats/superfícies. |
| 24 | SC | Contingut protegit; no reobrir per qüestions menors. |
| 25 | RD / AE · mitjana | Recuperació didàctica i ajust de referències opcionals. Tres referències opcionals s'havien omès; comprovar-ne la necessitat abans d'incorporar-les, sense alterar receptes ni ingredients. |
| 26 | RD · mitjana | Recuperació didàctica; mantenir les distincions i l'aplicació pròpies del capítol. |
| 27 | RD · mitjana | Recuperació didàctica; mantenir les distincions de cristalls, gel, neu i gemmes. |
| 28 | RT · alta / MG | Recuperació tècnica prioritària. La centralització de codis no es va considerar una pèrdua; preservar-la. Recuperació aplicada el 05/11/2026; validació tècnica i de contingut pendent. Les 10 propostes gràfiques originals es reserven per a la fase MG. |
| 29 | RT · alta / MG | Recuperació tècnica prioritària. La centralització de codis no es va considerar una pèrdua; preservar-la. Recuperació aplicada el 05/11/2026; validació tècnica i de contingut pendent. Les 10 propostes gràfiques originals es reserven per a la fase MG. |
| 30 | RT / RD · mitjana | Recuperar contingut tècnic i didàctic identificat; l'estat editorial previ constava pendent de confirmació. |
| 31 | RT / RD · baixa | Recuperació complementària de materials i contingut didàctic; l'auditoria va observar que la segona síntesi havia recuperat materials respecte de la primera versió. |
| 32 | RD · mitjana | Recuperació didàctica; preservar la distinció entre efecte intens, font lluminosa/OSL i fluorescència/fosforescència. |
| 33 | SC / AE | Contingut protegit; ajustos editorials de límits i referències, sense reescriure les receptes. |
| 34 | SC / AE | Contingut protegit; ajustos editorials de límits i referències, sense reescriure les receptes. |
| 35 | SC | Contingut protegit; no es va identificar recuperació prioritària. |
| 36 | RD · baixa | Recuperació didàctica complementària; no reobrir més enllà del que justifiqui l'auditoria global. |
| 37 | SC | Contingut protegit. Mantenir la seva funció d'acabats visuals i control del brillantor. |
| 38 | RT / RD / MG · alta | Recuperació tècnica i didàctica aplicada el 05/11/2026: recuperats els fonaments i límits de protecció, criteris d'assecat/estabilització, avaluació final i sis exercicis desenvolupats. Validació semàntica i coteig complet pendents. Les 10 propostes gràfiques originals es reserven per a la fase MG. |
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
| 1 | G-01 aprovada per al §1.5. Verificar l'aplicació efectiva al fitxer i conservar-ne la traça. |
| 2 | Sense canvi prioritari identificat. |
| 3 | G-01 aprovada per als §§3.1 i 3.4.3; G-03 no va justificar recuperació conceptual addicional. Anomalia HTML <<p és una tasca separada de la primera versió. |
| 4–5 | Recuperacions aplicades. Comprovació estructural inicial registrada; validació textual, semàntica i coteig complet encara necessaris. |
| 6–13 | Recuperacions/ampliacions aplicades i documentades en commits individuals; fer validació global sense repetir diagnòstics ja tancats. |
| 14–18 | Ampliacions aplicades i documentades. C14, C15, C16 i C18 tenen límits de font: no s'ha localitzat un original complet; les ampliacions es basen en la consolidació disponible de la primera versió i els acords recuperats. |
| 19 | Recuperació de contingut metàl·lic i criteris de formulació aplicada; les receptes són propostes si no hi ha assaig documentat. |
| 20–27, 30–37, 39 | Capítols presents a la segona síntesi i auditats comparativament. Les accions RT/RD/AE de la matriu encara s'han de conciliar amb el registre de commits i executar segons prioritat; SC es protegeix de canvis innecessaris. |\n| 28 | Recuperació tècnica aplicada el 05/11/2026: desenvolupament dels procediments per a A–K, ampliació de controls i correccions, recuperació dels sis exercicis amb objectius/materials/procediment/avaluació i síntesi del capítol. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |\n| 29 | Recuperació tècnica aplicada el 05/11/2026: desenvolupament dels procediments de les 17 receptes A–Q, adaptació a geometries i escales, controls i correccions, recuperació dels sis exercicis complets, síntesi i enllaços de referència. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |\n| 38 | Recuperació tècnica i didàctica aplicada el 05/11/2026: incorporats els fonaments i límits de la protecció, distinció entre assecat superficial, assecat al tacte i estabilització, sis exercicis desenvolupats i criteris d'avaluació final. Primera comprovació estructural superada; validació semàntica i coteig final pendents. |

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

1. Conciliar aquest registre amb l'historial real de commits i el document SEGUIMENT_TERCERA_VERSIO.md; corregir qualsevol estat desfasat.
2. Completar les intervencions RT/RD/AE pendents en ordre de prioritat, sense tornar a auditar des de zero els capítols SC.
3. Després de cada bloc d'intervenció, executar comprovacions estructurals i de contingut proporcionades i registrar per separat aplicació i validació.\n4. C28 i C29 aplicats: mantenir pendent la validació completa abans de marcar-los com a tancats.
5. Prioritzar les recuperacions RT/RD de prioritat mitjana i baixa que encara no s'hagin aplicat, sense reobrir els capítols SC.
6. Després d'estabilitzar els 39 capítols, abordar annexos, referències globals i fase gràfica.
7. Mantenir la branca intervencion-editorial-2026-11; no modificar main.

## 9. Historial del registre

| Versió | Data | Canvis |
|---|---|---|
| 1.0 | 05/11/2026 | Primera consolidació de categories RT/RD/AE/MG/SC, prioritats, dictamen 39/39, estat de les intervencions 4–19 i fases del projecte. |

Aquest registre és una consolidació operativa basada en l'auditoria i els resultats recuperats del projecte. Els punts marcats com a pendents o no validats s'han de comprovar amb el fitxer real i la font corresponent abans de declarar-los tancats.
