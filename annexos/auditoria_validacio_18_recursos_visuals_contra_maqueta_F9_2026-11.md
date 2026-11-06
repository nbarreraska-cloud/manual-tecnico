# Auditoria de validació dels recursos visuals contra la maqueta F9

**Data:** 06/11/2026  
**Branca del registre:** `auditoria-cobertura-visual-incidencies-2026-11`  
**Maqueta contrastada:** F9 — PDF textual sense imatges, 296 pàgines A4.  
**Branca de la maqueta:** `intervencion-editorial-2026-11`.  
**Artefacte GitHub Actions:** `Manual-tecnic-pintura-miniatures-F9-PDF`, ID `13460155051`, execució `42121260751`.  
**SHA-256 del PDF:** `8c79ab0a2140a6ad2ae7dd4e28b7df780eea244209abe7fad6a8adbb1532e6f9`.

## 1. Abast i límit de la comprovació

S'ha recuperat l'artefacte PDF de F9, s'ha comprovat que conté 296 pàgines A4 i s'han revisat les pàgines d'ancoratge dels recursos proposats mitjançant extracció de text i full de contacte de pàgines representatives. També s'han contrastat els identificadors, títols i ubicacions amb la llista F10.

**Límit important:** F9 és una maqueta textual sense imatges ni espais reservats per a figures. Per tant, aquesta passada pot validar la correspondència entre contingut i ubicació, detectar duplicacions amb taules o explicacions i estimar la densitat de les pàgines. No pot validar encara la mida final de cada figura, els salts de pàgina després d'inserir-la ni la llegibilitat a escala d'impressió. La incorporació de figures obligarà a repaginar.

## 2. Resultat de la revisió

La proposta anterior de 22 recursos visuals no s'ha de mantenir íntegrament. Quatre grups poden resoldre's sense figura autònoma perquè el text o les taules de F9 ja cobreixen la funció:

- **G032+G033:** taula/text. Les seccions 11.4.2 i 11.4.5 descriuen l'aplicació de pigments i la diferència entre pigment sec i fixat. Sense mostres físiques comparables, una imatge que sembli documentar resultats seria inadequada; la comparació es pot resoldre amb una taula conceptual.
- **G115+G119:** taula o seqüència textual. El capítol 35 ja desenvolupa el diagnòstic cromàtic (35.2), els ajustos (35.7) i una seqüència general d'intervenció (35.8). Una figura abans/després sense un cas documentat seria més decorativa que probatòria.
- **G148+G150:** no crear figura nova. A la pàgina 261 ja hi ha una taula de nivells d'intervenció i, a continuació, els apartats 39.5.1–39.5.2 expliquen corregir/conservar i valorar el risc. Es pot ajustar la taula existent si cal, sense duplicar-la amb un arbre visual.
- **G153:** text numerat. El procediment de veladura ja es desplega en 10.5.1–10.5.6 (pàgines 70–71), amb preparació, prova, càrrega, distribució i avaluació. La figura no és imprescindible per a la primera edició.

Així, el conjunt queda en **18 recursos visuals no condicionals**, més **G019 com a recurs condicional**. El sostre és de 19; no s'ha d'assumir que G019 s'ha de produir.

## 3. Contrast dels 22 grups visuals anteriors

| Grup | Pàgines F9 i ubicació real | Decisió després de revisar la maqueta | Motiu i ancoratge recomanat |
|---|---|---|---|
| G003 | p. 16; apartat 3.2.1, no 3.1 | **Mantenir** | Esquema conceptual de comportament d'opacitat/transparència. La ubicació de F10 que diu 3.1 no coincideix amb la maqueta: corregir-la a 3.2.1. No atribuir comportaments a pintures concretes sense proves. |
| G012+G013+G015+G016 | pp. 31–32; 5.3.1–5.3.2 i 5.5.1–5.5.2 | **Mantenir** | Un recurs compacte en dos blocs: geometria/incidència i formació d'ombres. No intentar encabir tots els subapartats de 5.3–5.5 en una làmina. |
| G032+G033 | pp. 80–81; 11.4.2 i 11.4.5 | **Taula/text** | El text ja descriu aplicació, fixació i diferències. Sense mostres reals comparables, una il·lustració podria suggerir resultats no documentats. |
| G036 | p. 114; 15.6 | **Mantenir** | El mapa de valors i il·luminació aporta una representació espacial que el text no substitueix del tot. Un únic mapa simplificat, no un exemple complet de miniatura. |
| G039+G040 | pp. 118–119; 16.1–16.2 | **Mantenir** | Comparació TMM/NMM i influència de la geometria en els reflexos. Dos panells breus, sense seqüència addicional de construcció. |
| G044+G048 | pp. 125 i 128–129; 17.2.1–17.2.3 i 17.5.1–17.5.7 | **Mantenir** | Una composició de dos blocs: font/superfícies receptores i seqüència OSL. Col·locar-la després de 17.5.7 i remetre-hi des dels fonaments; evitar una làmina excessivament carregada. |
| G060 | pp. 154–155; 20.8.1–20.8.2 | **Mantenir** | Detall visual de vetes i desviació de fibres al voltant d'un nus. És una relació geomètrica difícil de transmetre només amb text. |
| G064+G065+G066 | pp. 158–162; 21.1–21.2 i apartats relacionats | **Mantenir** | Atles molt breu amb pocs exemples representatius de formes, fulles i agrupació. La taula de paleta existent no substitueix la morfologia visual. |
| G072+G074 | pp. 164–166; 22.2 i 22.9 | **Mantenir** | Una composició de dos panells: tipus de cuir i plecs/deformacions. Situar-la després de 22.2 i remetre-hi des de 22.9; no crear dues figures independents. |
| G081 | pp. 172–173; 23.9.1–23.9.2 | **Mantenir** | Esquema de plecs, punts de suport i tensions dels teixits. No fusionar amb cuir, perquè la resposta del material és diferent. |
| G083+G084 | pp. 176–178; 24.2 i 24.7 | **Mantenir** | Dos panells: mapa comparatiu de pigmentacions i mapa cromàtic facial. Les taules de paleta no substitueixen l'organització espacial del rostre. |
| G091 | pp. 214–216; recepta 30.5 | **Mantenir** | Seqüència curta de construcció pictòrica de flama. Ha de ser esquemàtica i identificada com a proposta, no com a resultat assajat. |
| G093+G095 | pp. 217–218; 31.1–31.4.3 | **Mantenir** | Dos blocs: estats visuals de sang i distribució de fluids segons geometria. No establir cronologies cromàtiques universals ni presentar mostres fictícies com a reals. |
| G099+G100+G102 | pp. 222–225; 32.2–32.3 i 32.4.1 | **Mantenir** | Una composició amb tres elements jerarquitzats: estructura/jerarquia, diferència entre fluorescència i emissió simulada, i traçat de descàrrega. No convertir-la en un atles d'efectes. |
| G110+G112 | pp. 232–235; 34.2 i 34.4 | **Mantenir** | Comparació de transparència/difusió i exemple de construcció de vidre. Situar-la després de 34.4 i remetre-hi des de 34.2. |
| G115+G119 | pp. 236–238; 35.2 i 35.7–35.8 | **Taula/seqüència textual** | El capítol ja conté diagnòstic, procediments i seqüència d'intervenció. No cal una figura abans/després sense cas documentat. |
| G125 | p. 241; 36.5.1 | **Mantenir** | Tall esquemàtic de capes i material exposat. És útil per distingir pintura, recobriment, suport i metall/base; no representar una prova real. |
| G129+G133 | pp. 246–247; 37.2.1 i 37.5 | **Mantenir** | Un recurs de dos blocs: reflex especular/difús i aplicació selectiva d'acabats. Col·locar-lo després de 37.5 i remetre des de 37.2.1. |
| G148+G150 | p. 261; taula de nivells i 39.5.1–39.5.2 | **No crear figura** | La taula existent ja presenta nivells, situacions i decisions; el text explica corregir/conservar i valorar el risc. Evitar duplicació. |
| G153 | pp. 70–72; 10.5.1–10.5.6 | **Text numerat** | El procediment ja està desglossat en fases. No afegir una figura només per il·lustrar una seqüència que el text explica de manera operativa. |
| G164 | pp. 194–195; 27.5–27.6 | **Mantenir** | Comparació visual de gel i neu, amb èmfasi en estructura i aparença. No establir un codi cromàtic universal. |
| G166+G167 | pp. 198–202; 28.4–28.5 i 28.7.2–28.7.3 | **Mantenir** | Una comparació conjunta amb dos blocs clarament diferenciats: corrosió de ferro/acer i pàtines de coure/bronze/llautó. No suggerir que comparteixen la mateixa química ni una cronologia cromàtica universal. |

## 4. Llista reduïda resultant

Els **18 recursos visuals no condicionals** són:

1. G003 — Opacitat i transparència de les pintures.
2. G012+G013+G015+G016 — Geometria de la llum i formació de les ombres.
3. G036 — Mapa de valors.
4. G039+G040 — TMM/NMM i geometria dels reflexos.
5. G044+G048 — Font emissora, superfícies receptores i construcció OSL.
6. G060 — Vetes i nusos de la fusta.
7. G064+G065+G066 — Atles breu de vegetació.
8. G072+G074 — Tipus de cuir i plecs/deformacions.
9. G081 — Plecs i tensions dels teixits.
10. G083+G084 — Pigmentacions i mapa cromàtic del rostre.
11. G091 — Construcció pictòrica d'una flama.
12. G093+G095 — Estats de la sang i distribució dels fluids.
13. G099+G100+G102 — Jerarquia d'efectes energètics, fluorescència i descàrrega.
14. G110+G112 — Transparència/difusió i construcció del vidre.
15. G125 — Capes i pèrdua de recobriment.
16. G129+G133 — Reflexió i acabats selectius.
17. G164 — Gel i neu.
18. G166+G167 — Corrosió i pàtines.

**G019 — Anàlisi d'il·luminació d'una miniatura:** queda com a única opció condicional. Només s'ha de conservar si, després d'integrar G012–G016, aporta un exemple d'aplicació global que el text i la composició anterior no resolen. La seva ubicació real és 5.8.4, pàgina 34.

## 5. Correccions de traçabilitat

- G003: la llista F10 indica apartat 3.1, però la maqueta situa el contingut d'opacitat/transparència a **3.2.1, pàgina 16**. Cal actualitzar la ubicació de treball abans de producció.
- G153: és una incorporació del **capítol 10**, no del 39; la ubicació és després de 10.5.6.
- G164: és una incorporació del **capítol 27**, no del 34; la ubicació és després de 27.6.
- G166 i G167: són incorporacions del **capítol 28**, no del 34; les ubicacions són després de 28.7.2 i 28.7.3 respectivament.
- Els recursos que combinen apartats distants dins d'un mateix capítol s'han de col·locar una sola vegada i remetre'ls des de l'altre apartat. No duplicar la figura.

## 6. Condicions per a la fase de producció

1. Tancar l'inventari en 18 recursos més G019 condicional.
2. Produir primer els esquemes E0 de funció més clara; les seqüències E1 han de portar una identificació explícita de procediment proposat.
3. No simular fotografies, mostres físiques ni resultats de productes concrets sense evidència.
4. Fer les composicions amb la mida final de maquetació en ment, però no inserir-les fins que s'hagin comprovat llegendes, ancoratges i remissions.
5. Després de cada inserció, regenerar el DOCX/PDF i revisar salts, taules, llegendes, numeració i llegibilitat.
6. Si un recurs no es llegeix bé a la mida real o repeteix el text, retirar-lo o convertir-lo en taula.

## 7. Conclusió

La maqueta F9 confirma que els 18 recursos seleccionats tenen una funció didàctica identificable i una ubicació textual concreta. Quatre grups de la proposta anterior no necessiten figura autònoma. La revisió no pot validar encara l'espai real que ocuparan les imatges perquè F9 és una maqueta sense imatges; aquesta comprovació s'ha de fer durant la inserció i la repaginació.

No s'ha modificat el cos del manual, no s'ha generat ni inserit cap imatge i no s'ha alterat `main` ni la branca `intervencion-editorial-2026-11`.
