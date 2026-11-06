# Generació de figures editorials

Aquest sistema genera figures vectorials SVG a partir d'especificacions JSON versionades al repositori.

## Primera prova

A la branca `auditoria-cobertura-visual-incidencies-2026-11`:

```bash
python -m pip install cairosvg
python tools/graphics/render_figure.py --figure G001
```

Els resultats es desen a `dist/graphics/` (SVG i PNG).

## GitHub Actions

Executa el workflow **Render editorial figure** des de la pestanya Actions i introdueix l'identificador (per exemple, `G001`). Els fitxers es publiquen com a artefacte de previsualització; el workflow no escriu ni confirma fitxers generats al repositori.

## Criteris

- Les especificacions i els textos de les figures són en català.
- L'SVG és el màster vectorial; el PNG només és una previsualització.
- La generació no implica validació editorial ni tècnica.
- Les fotografies documentals i les imatges externes segueixen un procés de selecció i verificació diferent.
