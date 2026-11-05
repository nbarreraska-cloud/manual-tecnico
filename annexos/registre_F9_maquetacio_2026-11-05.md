# Registre d'execució F9 — 05/11/2026

**Branca:** intervencion-editorial-2026-11  
**Fase:** F9 — primera maquetació Word completa, sense imatges.  
**Estat:** F9 tancada — maquetació textual completa, validada i registrada el 05/11/2026.

## Abast congelat

- 39 capítols de TERCERA_SINTESI_CONSOLIDADA_C01-C39.md.
- Annexos A–E des dels cinc fitxers vigents.
- Annex F amb les 48 fitxes individuals, en l'ordre i agrupació de INDEX.md.
- Les set seccions de cada fitxa es conserven íntegrament.

## Treball iniciat

- Especificació a annexos/F9_ESPECIFICACIO_MAQUETACIO.md.
- Generador Word a tools/generate_f9_docx.py.
- Workflow manual a .github/workflows/generate-f9-docx.yml; genera un DOCX com a artefacte quan s'executa des de GitHub Actions.
- Validacions prèvies: 39 capítols, 5 annexos A–E, 48 fitxes i 7 seccions per fitxa.

## Primera generació i comprovacions

- Workflow executat correctament a GitHub Actions: execució 42074514905, conclusió success.
- DOCX generat com a artefacte: 417.239 bytes.
- Conversió de comprovació a PDF: 339 pàgines A4.
- 39 títols de capítol i sis annexos (A–F) presents.
- 48 títols de fitxa únics i 336 encapçalaments de secció (7 × 48) presents a l'Annex F.
- Quatre agrupacions de fitxes visibles: Essential, Dark Future, Fantasy i Special FX.
- 159 taules detectades al document.
- Revisió visual de mostres de l'Annex F: format compacte i llegible en les pàgines examinades.

## Punts pendents abans de tancar F9

- L'índex és un camp automàtic de Word amb actualització en obrir el document; la conversió de comprovació a PDF no l'ha actualitzat i mostra el missatge d'instrucció. Cal verificar/refrescar l'índex a Word.
- Revisió visual integral de taules, salts, pàgines en blanc, capçaleres i divisió de fitxes al llarg del document.
- Comprovació final de fidelitat de text entre les fonts Markdown i el DOCX.

F9 no es declara completada fins a resoldre aquestes comprovacions.

## Restriccions

No s'han alterat capítols, annexos ni fitxes. No s'han afegit imatges ni s'ha iniciat F10. main no forma part de l'àmbit de treball.


## Revisió de la primera maqueta — incidències detectades (05/11/2026)

La inspecció visual de pàgines representatives i l'escaneig del text extret del PDF han detectat dues incidències de composició:

- Pàgines 35 i 284 pràcticament buides, associades als salts de pàgina explícits abans de capítols i annexos.
- Numeració automàtica de Word acumulada entre llistes independents. En alguns punts, els números visibles arribaven a valors superiors a 1.400, tot i que la font Markdown conserva la numeració local de cada llista.

S'ha corregit el generador a la branca de treball (commit `aeec294c8d3c3828f330ee0d0aeef3cdc6388519`):

- Els salts de capítol i annex s'apliquen ara al primer títol del bloc mitjançant `page_break_before`, en lloc d'afegir paràgrafs de salt independents.
- Les llistes numerades conserven el número literal de la font i deixen d'utilitzar el comptador automàtic compartit de Word.

Aquesta correcció és estrictament de maquetació i preservació de la numeració d'origen. La nova generació encara s'ha de validar abans de donar aquestes incidències per resoltes en el DOCX lliurable.

## Revisió global i límits pendents

L'escaneig de les 339 pàgines confirma que, a més de la pàgina de l'índex pendent d'actualització, les pàgines 35 i 284 són les dues pàgines pràcticament buides detectades. S'han revisat visualment mostres de portada, índex, cos dels capítols, annexos i fitxes; això no equival a una inspecció visual individual de cada pàgina ni a una verificació exhaustiva de cada cel·la de les 159 taules.

La fidelitat estructural queda confirmada per recompte (39 capítols, A–F, 48 fitxes i 336 seccions), però la comparació textual exhaustiva caràcter a caràcter amb totes les fonts Markdown continua pendent. També resta pendent actualitzar i verificar l'índex amb Microsoft Word; la conversió de comprovació no n'ha calculat els camps.


## Segona generació — desencadenament de validació (05/11/2026)

Després de corregir el generador, s'ha actualitzat aquest registre per desencadenar una nova execució del workflow F9 a la branca de treball. La nova maqueta només es considerarà validada quan s'hagi descarregat i inspeccionat l'artefacte resultant.


S'ha ajustat també el camp de l'índex automàtic perquè mostri els nivells 1–2 en lloc d'1–3. La primera actualització amb LibreOffice va generar un índex de 30 pàgines, massa extens per a una consulta funcional; es manté el nivell de capítols i apartats principals, evitant desplegar tots els subapartats i les 48 fitxes a l'índex general. Cal validar la paginació de la nova versió.


## Segona generació i validació de composició — 05/11/2026

- Workflow GitHub Actions: execució `42075834908`, conclusió `success`, branca `intervencion-editorial-2026-11`, commit de generació `9ac70c6055ff035337466167a06f721f3fc35b63`.
- Artefacte de la segona generació: `Manual-tecnic-pintura-miniatures-F9`, ID `13439430358`, mida ZIP informada per GitHub 417.440 bytes.
- S'ha actualitzat l'índex amb LibreOffice UNO i s'ha desat el DOCX amb l'índex ja calculat. L'índex ocupa les pàgines 2–12 i mostra capítols i apartats principals (nivells 1–2); el cos comença a la pàgina 13. La primera prova amb nivells 1–3 ocupava 30 pàgines i s'ha descartat per excés d'extensió.
- PDF de comprovació de la versió amb índex actualitzat: 352 pàgines A4.
- Escaneig de les 352 pàgines: no s'han detectat pàgines pràcticament buides. Les antigues pàgines 35 i 284 ja no són pàgines buides; són pàgines de contingut normal.
- Inspecció visual de mostres: portada, índex, cos del capítol, taula d'annex i final de l'Annex F. La mostra de taula examinada és llegible i manté les columnes.
- Validació DOCX: 159 taules; 39 capítols; annexos A–F; 48 títols de fitxa; 336 encapçalaments de secció (7 × 48); quatre grups comercials; cap paràgraf utilitza l'estil automàtic `List Number` després de la correcció.
- DOCX de treball verificat després d'actualitzar l'índex: 476.244 bytes; SHA-256 `6b4add0d3bd53cbfc87eb0988601e533d6c4644da9c60423ae28c6cf440ba7d3`.

## Estat de les comprovacions després de la segona generació

Resoltes: salts que generaven pàgines gairebé buides; numeració automàtica acumulativa de llistes; índex calculat i llegible amb nivells 1–2; estructura i recompte de fitxes; mostres visuals indicades.

Encara obertes: comparació textual exhaustiva amb totes les fonts Markdown; inspecció visual individual de totes les pàgines i de totes les taules; verificació final de les divisions de cada fitxa i de les capçaleres/peus a tot el document. Per tant, la segona generació corregeix les incidències detectades però **no tanca encara F9**.

La versió DOCX amb l'índex actualitzat és una instantània textual de F9. Quan s'integrin imatges a F11 caldrà recalcular l'índex i repaginar; no s'ha d'interpretar la paginació de 352 pàgines com a definitiva.


## Tercera generació — auditoria de fidelitat textual (05/11/2026)

- Workflow GitHub Actions: execució `42079264650`, conclusió `success`, commit `7be0962faba6e9b6056f558b9024386ae566a15c`.
- Generació del DOCX: correcta; el generador confirma 39 capítols, 5 annexos A–E i 48 fitxes amb 7 seccions cadascuna.
- Auditoria de fonts: 55 fitxers, 174.623 paraules font i 174.682 paraules al cos del DOCX. Resultat: totes les paraules de les fonts apareixen en el document i en el mateix ordre.
- L'auditoria va requerir corregir la normalització dels guions baixos de les URL i identificadors (per exemple, `Game_Color`); no era una pèrdua del document, sinó un fals positiu del comparador.
- L'artefacte DOCX s'ha pujat correctament a GitHub Actions (artefacte `13438389777`, retenció fins al 05/12/2026).

La comprovació textual de la tercera generació és satisfactòria, però la prova d'ordre per subseqüència no és per si sola una equivalència exacta caràcter a caràcter. S'ha reforçat el validador perquè també exigeixi la multiplicitat de cada token font, evitant que una ocurrència posterior compensi silenciosament una ocurrència perduda. Aquesta millora s'ha compromès després de la tercera generació i resta pendent la seva execució automàtica.

## Revisió visual ampliada de la maqueta amb índex actualitzat

S'ha tornat a escanejar el PDF de comprovació de 352 pàgines A4: no hi ha pàgines sense contingut o pràcticament buides; el cos comença a la pàgina 13 i l'índex ocupa les pàgines 2–12. S'han generat fulls de contacte de totes les 352 pàgines per inspecció visual global, a més de la inspecció de pàgines representatives ja registrada. Les taules apareixen integrades al flux de lectura i no s'observen pàgines desplaçades o en blanc en la visió general.

Aquesta inspecció global no substitueix una lectura ampliada de cada taula ni garanteix que cada divisió de taula entre pàgines sigui editorialment òptima. La verificació de fitxes de l'Annex F i la comprovació final de capçaleres/peus continuen formant part del tancament.


## Tancament formal F9 — 05/11/2026

- Auditoria reforçada final: execució GitHub Actions `42079639659`, conclusió `success`; 55 fitxers font, 174.623 paraules font i 174.682 paraules al DOCX. La comprovació exigeix ara multiplicitat suficient de cada token i preservació de l'ordre de totes les paraules font.
- Generació final de la branca: correcta; 39 capítols, 5 annexos A–E i 48 fitxes amb set seccions cadascuna. L'Annex F integra les 48 fitxes en quatre grups comercials.
- Composició: 352 pàgines A4 a la versió de comprovació amb índex actualitzat; índex a les pàgines 2–12 i cos des de la 13. Escaneig textual de totes les pàgines: cap pàgina en blanc o pràcticament buida.
- Revisió visual: inspecció de fulls de contacte de les 352 pàgines i mostres ampliades representatives; sense anomalies globals de composició detectades. Es mantenen els límits indicats a l'especificació: no és una correcció tipogràfica manual de cada cel·la i la paginació s'haurà de recalcular quan s'afegeixin imatges.
- Estructura del DOCX validat: 159 taules, 39 capítols, annexos A–F, 48 títols de fitxa, 336 encapçalaments de secció i cap paràgraf amb estil automàtic `List Number`.
- Artefacte GitHub Actions de la darrera generació: `Manual-tecnic-pintura-miniatures-F9`, ID `13438624073`, associat a l'execució `42079639659`.
- Branca de treball actualitzada sense alterar `main`; `main` continua a `a4ce8192e30178b0171ea02a3af230b60efd3768`.

**Conclusió:** F9 queda tancada en el seu abast aprovat de maquetació textual sense imatges. No s'ha iniciat F10.


## Revisió final del PDF i correcció de files de taula — 05/11/2026

La inspecció ampliada del PDF va detectar una incidència concreta a l'Annex B: la fila «Perfilat de vores» de la taula B.3 es dividia entre pàgines i el fragment de continuació quedava sense la primera cel·la. Es va provar la protecció de files en una còpia de treball i es va confirmar que mantenia la fila completa sense modificar-ne el contingut.

S'ha incorporat la propietat `cantSplit` a totes les files de taula del generador (1.385 files en 159 taules). També s'ha ampliat el disparador del workflow PDF perquè es torni a executar quan canviïn el generador, el validador o les fonts que formen el manual. El workflow fixa el runner `ubuntu-26.04` i registra la versió de LibreOffice i la suma SHA-256 del PDF.

- Commit de correcció del generador: `7e525f5516781eb543a46cbb6d5d54a179963d85`.
- Commit del workflow i metadades: `7775a03c741482fd190bec93b0a52c9e4e9354fc`.
- Workflow PDF de comprovació posterior a la correcció: execució `42085900835`, conclusió `success`, commit `7775a03c741482fd190bec93b0a52c9e4e9354fc`.
- Artefacte PDF d'aquesta execució: ID `13442523341`.
- PDF resultant: 326 pàgines A4; 7.614.626 bytes; LibreOffice 26.2.6.3; índex a les pàgines 2–11 i cos des de la 12; sense instrucció provisional d'actualització de l'índex.
- SHA-256 del PDF: `e66ace0ab29d14f61a80160880fd139d567432ad10a59d3e859f463ae285c61d`.
- DOCX: 39 capítols, 159 taules, 1.385 files protegides contra divisió, 48 fitxes i 336 seccions de fitxa.
- Auditoria PDF–DOCX: es localitzen els 39 títols de capítol i les 48 fitxes; no s'hi detecten dèficits de tokens de contingut. Les diferències restants són únicament el text provisional del camp de l'índex, que s'elimina en actualitzar-lo.
- Inspecció visual: fulls de contacte de les 326 pàgines i mostres ampliades; la fila B.3 queda íntegra. No s'observen pàgines en blanc o gairebé buides.

La diferència respecte de les paginacions anteriors de 352–353 pàgines es deu al motor de maquetació. Les conversions amb LibreOffice 25.2.3.2 van produir 352–353 pàgines i continuacions de text molt curtes; l'artefacte de referència s'ha generat amb LibreOffice 26.2.6.3 i presenta 326 pàgines sense pàgines pràcticament buides. La longitud objectiu és orientativa i no s'ha d'assolir afegint espaiat artificial ni alterant contingut.

**Conclusió final:** F9 queda tancada en el seu abast textual sense imatges. No s'ha modificat `main`, no s'ha fusionat la branca de treball i no s'ha iniciat F10.


## Redisseny de l'Annex F — 05/11/2026

S'ha actualitzat el generador de F9 a la branca `intervencion-editorial-2026-11` (commit `20192bbd7985fc160ea929dcba56ce60f39d5be9`) per substituir la presentació anterior de les fitxes per una composició de quatre targetes per pàgina, en quadrícula 2 × 2, amb jerarquia tipogràfica i separació visual més clara.

Canvis editorials:
- Es retira de la fitxa visual el peu repetitiu sobre l'estat de verificació.
- Es dona prioritat a les característiques de gamma declarades pel fabricant i a les funcions traçables de cada pintura dins del manual.
- Es manté explícita la distinció entre propietats de família i dades individuals: no s'inventen valors de duresa, opacitat, cobertura, transparència, viscositat, assecat o acabat.
- Quan no hi ha caracterització tècnica específica recuperada per a Model Color, s'indica aquesta limitació de manera breu.
- Es conserven les 48 referències, els quatre conjunts i l'ordre de l'índex.

La generació Word a GitHub Actions ha finalitzat correctament (execució `42118619973`, artefacte `13457976522`). La validació de fidelitat del DOCX també ha finalitzat correctament. La regeneració PDF i la comprovació visual de la nova paginació queden pendents de tancament abans de considerar substituïda la maqueta anterior.


La regeneració PDF de la nova composició també ha finalitzat correctament:
- Workflow PDF: execució `42118619951`, conclusió `success`.
- Artefacte PDF: `Manual-tecnic-pintura-miniatures-F9-PDF`, ID `13456843490`.
- PDF: 299 pàgines A4, 6.620.662 bytes, LibreOffice 26.2.6.3.
- SHA-256: `be8f8552bc0997605b30f4a33f4d69586d2d57540f81894f6952842f32e34f18`.
- Índex actualitzat; instrucció provisional absent; comprovacions d'integritat i paginació del workflow superades.
- Auditoria DOCX: 39 capítols, annexos A–E i 48 identitats de fitxa; comprovació de referències de capítol superada.

La nova maqueta substitueix la composició anterior dins de l'artefacte F9 generat. La comprovació automàtica no equival a una inspecció visual manual ampliada de cadascuna de les 12 pàgines de l'Annex F; aquesta revisió queda identificada com a control editorial pendent abans de donar per tancada la nova presentació.
