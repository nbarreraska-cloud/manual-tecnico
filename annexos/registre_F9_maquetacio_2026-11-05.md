# Registre d'execució F9 — 05/11/2026

**Branca:** intervencion-editorial-2026-11  
**Fase:** F9 — primera maquetació Word completa, sense imatges.  
**Estat:** primera generació completa produïda; revisió editorial final encara pendent.

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
