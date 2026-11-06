# Generació de figures editorials

Aquest sistema genera figures vectorials SVG a partir d'especificacions JSON versionades al repositori. La generació tècnica, la validació visual i l'aprovació editorial són estats diferents.

## Execució local

Instal·la el rasteritzador i executa:

```bash
python -m pip install cairosvg
python tools/graphics/render_figure.py --figure G001
```

Els resultats es desen a `dist/graphics/` (SVG i PNG).

## Auditoria de la llista completa

```bash
python tools/graphics/build_manifest.py
python tools/graphics/render_batch.py --render
```

El primer pas valida que F10-R1 contingui exactament G001–G170, en ordre i sense duplicats, i crea `dist/graphics/manifest.json`. El segon inspecciona totes les especificacions JSON i genera `batch_report.json` i `batch_report.csv`.

## Estats de l'auditoria

- `rendered`: especificació compatible i renderització completada.
- `brief_structured_not_renderable`: brief editorial íntegre i traçable, però encara pendent de desenvolupament d'una composició gràfica i una plantilla adequada. És un estat deliberat, no un error.
- `missing_spec`: encara no existeix una especificació individual.
- `unsupported_template`: hi ha una especificació individual, però no correspon a cap plantilla de renderització disponible.
- `invalid_spec`: JSON, identificador o estructura incomplets o inconsistents.
- `render_error`: error durant la renderització.

Els briefs G151–G170 es conserven com a especificacions estructurades. No s'han de forçar dins la plantilla de quatre targetes: cada figura necessita una solució gràfica coherent amb la seva composició.

La primera plantilla específica és `layer_sequence_4`, aplicada a G151. Representa quatre fases sobre una geometria repetida i constant. El seu ús no implica que la figura estigui aprovada: cal revisar el SVG/PNG generat, contrastar-ne la lectura amb el capítol i comprovar-ne la llegibilitat a mida de maquetació.

## GitHub Actions

El workflow **Render editorial figure** s'executa automàticament en canvis rellevants de la branca `auditoria-cobertura-visual-incidencies-2026-11`. També es pot iniciar manualment:
- `batch`: valida i audita les 170 entrades, renderitzant només les especificacions compatibles.
- `single`: renderitza l'identificador indicat.

Els resultats es publiquen com a artefacte de previsualització; el workflow no confirma ni insereix imatges al manual.

## Criteris editorials i tècnics

- Les especificacions i els textos de les figures són en català.
- L'SVG és el màster vectorial; el PNG és una previsualització.
- La generació no implica validació editorial, tècnica ni física.
- No s'infereix una composició a partir del títol: cada figura necessita una especificació contrastada amb la fitxa i el capítol corresponents.
- Les fotografies documentals i les imatges externes segueixen un procés de selecció, verificació de procedència i drets diferent.
- No s'insereixen imatges al document mestre sense imatges; la futura integració es farà en una còpia separada.
