# Registre d'execució F9 — 05/11/2026

**Branca:** intervencion-editorial-2026-11  
**Fase:** F9 — primera maquetació Word completa, sense imatges.  
**Estat:** iniciada; preparació de l'especificació, el generador i el flux de compilació.

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

## Estat del lliurable

El DOCX complet encara no s'ha generat ni revisat visualment. El workflow queda preparat però requereix executar-lo manualment des de GitHub Actions; l'entorn connector disponible no exposa l'acció de dispatch. F9 està iniciada, però no es declara completada.

## Restriccions

No s'han alterat capítols, annexos ni fitxes. No s'han afegit imatges ni s'ha iniciat F10. main no forma part de l'àmbit de treball.
