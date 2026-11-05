# Seguiment de la tercera versió del manual

**Data d'actualització:** 2026-11-05  
**Branca de treball:** `intervencion-editorial-2026-11`

## Abast i versions

- **Primera versió:** document amb l'estructura completa del manual, sintetitzat a partir de l'original.
- **Segona síntesi:** versió posterior formada exclusivament pels 39 capítols en Markdown. És la base de treball de la revisió actual.
- **Tercera versió:** resultat de la revisió de la segona síntesi, amb recuperació selectiva de contingut tècnic, didàctic i pràctic que s'hagi comprimit en excés.

Les intervencions actuals s'apliquen als fitxers Markdown de la segona síntesi. No s'ha de confondre aquesta feina amb la revisió estructural del HTML de la primera versió.

## Criteri editorial general

**Objectiu: recuperar el màxim contingut possible sense perdre la síntesi.**

L'original tenia aproximadament 900 pàgines. La primera síntesi quedà al voltant de 500 pàgines; la segona podria situar-se prop de 350, però aquesta extensió encara s'ha de verificar en el document real. L'objectiu orientatiu de la tercera versió és de 350–375 pàgines, sense superar aproximadament les 400.

Cal recuperar procediments, explicacions tècniques, fonaments, advertiments, detalls operatius, exemples, comparacions, aclariments, exercicis i variants que aportin valor. Cal conservar les receptes, mescles i seqüències útils. S'han d'evitar redundàncies i no s'ha d'eliminar contingut valuós només per ajustar una xifra de pàgines. No es tracta de tornar a la primera síntesi ni de recuperar indiscriminadament l'original.

## Decisions de treball

- Mantenir la branca `intervencion-editorial-2026-11`; no intervenir en `main`.
- Aplicar les recuperacions a la segona síntesi, no al HTML de la primera versió.
- Utilitzar el document original `manual con estructura completa.docx` com a font de contrast.
- Conservar l'idioma català dels 39 fitxers Markdown de la segona síntesi.
- Continuar amb iniciativa per detectar pèrdues addicionals, justificant les intervencions i sense afegir contingut per volum.
- Les revisions i actualitzacions poden continuar sense demanar aprovació prèvia per a cada pas. Cal informar amb precisió de les modificacions efectuades.

## Treball efectuat en aquesta actualització

### Capítol 4 — Teoria del color

- Recuperats els nou errors conceptuals originals amb les seves explicacions i correccions.
- Conservats els sis exercicis, ampliant-los amb objectius, procediments i criteris d'avaluació originals.
- Recuperada la síntesi conceptual.
- Recuperat el criteri operatiu de selecció de paletes de vuit passos.
- Recuperat el desenvolupament dels set criteris de planificació de paletes (intenció, dominant, secundaris, accents, neutres, distribució per superfícies i comprovació a diferents distàncies).
- Ampliat l'exemple de l'armadura blava amb la seqüència original de sis fases, incloent-hi la selecció de matís, valor i croma, la relació cromàtica, la funció dels elements secundaris, la comprovació de jerarquia i les correccions possibles.
- Mantingut el procediment d'adaptació visual de l'apartat 4.2, que ja es trobava conservat a la segona síntesi.

### Capítol 5 — Llum, volum, ombres i reflexos

- Recuperats els set errors conceptuals originals.
- Conservats els sis exercicis i restituïdes les instruccions observacionals més desenvolupades.
- Ampliat l'apartat 5.5 amb el bloqueig i l'oclusió de la llum, la geometria de les ombres, la seva mida, direcció i extensió, mantenint els continguts de l'ombra pròpia i projectada, umbra i penombra, ombres de contacte i il·luminació indirecta.
- Ampliat l'apartat 5.8 amb les llistes d'observació originals per identificar la font, analitzar la geometria, interpretar les regions i separar il·luminació observada i representada.

## Tasques pendents

1. Validar la integritat textual i estructural dels capítols 4 i 5 després de les recuperacions.
2. Continuar la revisió comparativa de la resta dels 39 capítols, en ordre, amb el mateix criteri editorial.
3. Verificar l'extensió real de la segona síntesi i de la tercera versió en una exportació maquetada.
4. Mantenir com a tasca separada la revisió HTML de la primera versió: tres marcadors `<<p`, tres H1 buits i reconstrucció de l'encapçalament del capítol 31. Aquesta intervenció no forma part de l'actualització dels 39 Markdown.

## Traçabilitat

Les modificacions d'aquesta actualització afecten:
- `segunda_sintesis/capitol-04.md`
- `segunda_sintesis/capitol-05.md`
- Aquest document de seguiment.

La branca `main` no forma part d'aquesta intervenció.
