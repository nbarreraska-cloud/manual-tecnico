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
