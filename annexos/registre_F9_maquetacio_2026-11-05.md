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
