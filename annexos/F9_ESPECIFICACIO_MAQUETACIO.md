# F9 — Especificació de maquetació Word (05/11/2026)

**Branca:** intervencion-editorial-2026-11  
**Estat:** F9 oberta — primera maqueta textual generada; les correccions editorials autoritzades s'han aplicat a la branca de treball i la regeneració i validació posteriors estan pendents.  
**Límit:** no modificar main ni reobrir contingut tècnic aprovat.

## 1. Estructura del document

1. Portada.
2. Índex general automàtic.
3. Capítols 1–39, en l'ordre de la compilació consolidada.
4. Annexos A, B, C, D i E.
5. Annex F: les 48 fitxes individuals, agrupades segons els quatre conjunts comercials i en l'ordre de l'índex de fitxes.

## 2. Criteris de composició

- Format A4 i marges equilibrats.
- Tipografia llegible i jerarquia estable per a títols, apartats i subapartats.
- Taules amb capçaleres identificables, marges interns reduïts i repetició de capçalera quan travessin pàgina.
- Paràgrafs amb espaiat contingut, sense comprimir fins a perjudicar la lectura.
- Capítols i annexos iniciats en pàgina nova.
- El manual s'identifica al llarg de les cinc parts: marcador discret al començament de cada part i capçalera corrent amb la part corresponent a totes les pàgines del seu àmbit. Les parts coincideixen amb l'organització definida a l'apartat 1.3 del capítol 1: I (C1–C6), II (C7–C18), III (C19–C34), IV (C35–C39) i V (annexos A–F). Els marcadors comparteixen la pàgina d'inici del contingut i no creen portadelles ni pàgines addicionals.
- Cap salt de pàgina forçat entre fitxes si no és necessari per evitar una ruptura visual greu.
- Annex F amb cos tipogràfic i espaiat més compactes que el cos principal, mantenint íntegres les set seccions, taules, llistes i fonts.
- Cap imatge durant F9.

## 3. Protecció del contingut

La generació és de maquetació, no de reescriptura. No es permet resumir o eliminar paràgrafs, fusionar passos, alterar receptes, codis, noms, proporcions o advertiments, completar propietats pendents ni convertir propostes en resultats validats.

Només es permet aplicar estils, ajustar espais, marges, salts, amplades de taula i jerarquia visual.

## 4. Validacions automàtiques abans de generar

- 39 capítols detectats a la compilació consolidada.
- Cinc fitxers font d'annex A–E presents; l'Annex F es genera a partir de les 48 fitxes individuals i de l'índex general.
- 48 fitxes identificades a l'índex general i incloses a l'Annex F.
- Set seccions numerades a cadascuna de les 48 fitxes.
- Cap fitxa omesa o duplicada en l'ordre d'integració.

## 5. Validació editorial posterior

Revisar índex i jerarquia real, taules que travessen pàgina, fitxes dividides de manera poc funcional, capçaleres, peus, numeració, pàgines en blanc, salts innecessaris, llegibilitat de l'Annex F i integritat textual respecte de les fonts Markdown.

La paginació definitiva no es fixa en F9 perquè les imatges s'integraran en fases posteriors.


## 6. Resultat de la primera generació (05/11/2026)

La primera compilació DOCX s'ha generat correctament. La conversió de comprovació ha produït 339 pàgines A4. La validació del paquet Word confirma 39 capítols, annexos A–F, 48 fitxes úniques, 336 encapçalaments de secció i quatre agrupacions comercials. L'índex automàtic és un camp Word amb actualització en obrir; cal verificar-lo a Word perquè l'exportació de comprovació no l'ha actualitzat. La revisió visual integral i la verificació de fidelitat són pendents.


## 7. Segona generació — validació de composició (05/11/2026)

La segona generació de GitHub Actions ha finalitzat correctament (run 42075834908). El generador corregeix els salts de pàgina i la numeració de llistes, i el camp de l'índex s'ha ajustat a nivells 1–2. Després d'actualitzar el contingut de l'índex amb LibreOffice UNO, el DOCX de comprovació produeix un PDF de 352 pàgines A4, amb l'índex a les pàgines 2–12 i el cos a partir de la 13. L'escaneig de pàgines no detecta pàgines pràcticament buides. La inspecció visual de mostres confirma llegibilitat en portada, índex, text corrent, taules d'annex i final de l'Annex F.

La validació estructural confirma 39 capítols, annexos A–F, 48 fitxes i 336 seccions de fitxa. La comparació textual exhaustiva i la revisió visual pàgina per pàgina continuen pendents; no es declara F9 tancada.


## 8. Tancament F9 — 05/11/2026

F9 queda tancada en el seu abast aprovat: maquetació textual completa sense imatges. La generació automàtica i l'auditoria reforçada de fidelitat han finalitzat correctament a GitHub Actions (execució `42079639659`, commit de codi `bea43da327067f00f9b7d4f121d29de39d57ca17`). L'auditoria cobreix 55 fitxers font, 174.623 paraules font i 174.682 paraules al cos del DOCX; verifica tant la multiplicitat dels tokens com la seva seqüència.

La revisió visual global de les 352 pàgines de la versió de comprovació amb índex actualitzat no ha detectat pàgines en blanc o gairebé buides, desbordaments evidents, ni anomalies generals de composició. S'han revisat els fulls de contacte de totes les pàgines i mostres ampliades de portada, índex, capítols, taules i fitxes. La maqueta manté 159 taules, 39 capítols, annexos A–F, 48 fitxes i 336 encapçalaments de secció de fitxa; no utilitza numeració automàtica acumulativa.

**Límits coneguts:** aquesta fase és deliberadament textual i no incorpora imatges. La inspecció de pàgina sencera no equival a una correcció tipogràfica minuciosa de cada cel·la de cada taula. La paginació s'ha de recalcular quan s'incorporin imatges en una fase posterior. L'índex és un camp automàtic de Word i pot requerir actualització després de canvis de contingut o paginació.

**Resultat:** F9 tancada. No s'ha modificat `main`; no s'ha iniciat F10 ni cap altra fase posterior.


## 9. PDF de referència i auditoria de sortida — 05/11/2026

Després de la inspecció visual s'ha detectat una ruptura de fila en una taula de l'Annex B: la fila «Perfilat de vores» quedava dividida entre dues pàgines i el fragment de continuació perdia el contingut de la primera cel·la. S'ha corregit el generador perquè les 1.385 files de les 159 taules es mantinguin senceres en els salts de pàgina mitjançant la propietat de maquetació `cantSplit`. La correcció no altera cap text, dada, recepta ni estructura de taula.

La nova generació ha superat els workflows de Word i PDF:

- Workflow PDF: execució `42085900835`, conclusió `success`, commit `7775a03c741482fd190bec93b0a52c9e4e9354fc`.
- Artefacte PDF: `Manual-tecnic-pintura-miniatures-F9-PDF`, ID `13442523341`.
- PDF de 326 pàgines A4, 7.614.626 bytes, generat amb LibreOffice 26.2.6.3; PDF etiquetat i sense xifrar. SHA-256: `e66ace0ab29d14f61a80160880fd139d567432ad10a59d3e859f463ae285c61d`.
- Índex actualitzat a les pàgines 2–11; el cos comença a la pàgina 12. L'índex inclou els capítols, els annexos i els quatre grups de fitxes de l'Annex F. No hi queda el text provisional d'actualització.
- Estructura DOCX: 39 capítols, 159 taules, 48 fitxes, 336 seccions de fitxa i quatre grups comercials. Les 1.385 files tenen activada la protecció contra divisió entre pàgines.
- L'auditoria de fidelitat DOCX continua amb 55 fitxers font, 174.623 paraules font i 174.682 paraules al cos del DOCX; es preserven multiplicitats i ordre.
- La comparació de text PDF–DOCX no detecta pèrdues de contingut font. Les úniques diferències de tokens corresponen al text provisional del camp de l'índex, eliminat en actualitzar-lo.
- S'han inspeccionat els fulls de contacte de les 326 pàgines i mostres ampliades de portada, índex, taules d'annex i fitxes. No s'han detectat pàgines en blanc o pràcticament buides, ni la ruptura de fila observada abans de la correcció.

La paginació varia segons la versió de LibreOffice: les conversions de contrast amb 25.2.3.2 han produït 352–353 pàgines i alguna continuació molt curta; la versió de referència és l'artefacte de GitHub Actions generat amb 26.2.6.3, que presenta un flux més compacte sense pàgines pràcticament buides. No s'ha afegit espaiat ni contingut per perseguir una xifra de pàgines. El rang de 350–375 continua sent orientatiu, no un requisit que justifiqui empitjorar la composició.

**Límits:** la inspecció visual global i les mostres ampliades no equivalen a una correcció manual individual de cada cel·la. La versió és textual i sense imatges; quan s'integrin imatges en una fase posterior, caldrà regenerar el PDF, actualitzar l'índex i repaginar.

**Resultat:** F9 queda tancada en el seu abast aprovat. No s'ha modificat `main` i no s'ha iniciat F10.


## 10. Identificació visual de les cinc parts — 05/11/2026

A petició de l'usuari, la generació final incorpora la divisió en cinc parts ja definida al capítol 1.3:
- Part I — Fonaments: capítols 1–6.
- Part II — Tècniques i procediments: capítols 7–18.
- Part III — Receptari de materials i efectes: capítols 19–34.
- Part IV — Acabats i correcció: capítols 35–39.
- Part V — Annexos i eines de consulta: annexos A–F.

Cada part s'identifica amb un marcador discret al començament, integrat a la primera pàgina de contingut, i una capçalera corrent que indica la part a totes les pàgines corresponents. La numeració de pàgina continua sense reiniciar-se. No es creen portadelles ni salts de pàgina addicionals per introduir les parts. Cal comprovar el PDF resultant per confirmar que les capçaleres canvien a cada límit, que no apareixen pàgines en blanc i que l'extensió no augmenta per pàgines de separació.


## 11. Actualització editorial de l'Annex F — fitxes de consulta

La presentació de les 48 fitxes prioritza informació útil, consulta ràpida i llegibilitat:

- Composició validada en quadrícula de dues columnes i tres files: sis fitxes per pàgina, vuit pàgines per als quatre conjunts.
- La jerarquia tipogràfica diferencia el nom, la referència, les dades d'identificació, els epígrafs i els textos descriptius. El cos de les funcions i característiques s'ha ampliat a 7,25–7,45 pt, amb interlineat i separació entre blocs més generosos; el nom de cada pintura és de 10,4 pt.
- Cada fitxa mostra nom, referència, conjunt, família comercial, característiques de gamma documentades i funcions/relacions traçables als capítols.
- Se suprimeix de la fitxa visual el camp repetitiu «estat de verificació». Les limitacions documentals es concentren en la introducció de l'annex i en les fonts de treball.
- Les característiques tècniques s'atribueixen a la família només quan la font del fabricant les descriu expressament. No s'infereixen valors individuals de duresa, opacitat, cobertura, transparència, viscositat, assecat o acabat quan no hi ha dades específiques.
- Quan la font només identifica Model Color sense caracterització tècnica individual recuperada, la fitxa ho indica de manera breu, sense omplir el buit amb propietats suposades.
- La funció cromàtica o tècnica dins del manual es manté vinculada als capítols i a les taules d'origen; no es presenta com a prova experimental.
- La densitat del contingut s'ha de resoldre a favor de la llegibilitat: si una fitxa no hi cap amb espaiat suficient, cal adaptar la distribució abans de reduir de nou la mida del cos.

Aquesta actualització modifica la presentació de l'Annex F i la seva síntesi visual, no l'arquitectura de 39 capítols ni les fonts individuals. La regeneració es fa mitjançant GitHub Actions a la branca de treball.
