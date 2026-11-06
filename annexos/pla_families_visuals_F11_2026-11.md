# Pla de producció per famílies visuals — F11

**Branca:** `auditoria-cobertura-visual-incidencies-2026-11`  
**Abast:** G001–G170  
**Estat:** classificació de producció i arquitectura de plantilles; no és aprovació de cap figura.

## Criteri de treball

La classificació agrupa figures que comparteixen una lògica de representació, no simplement un tema. Cada família ha de reutilitzar una gramàtica visual i uns components gràfics comuns, però cada figura conservarà la seva composició i contingut específics. La plantilla no pot substituir la informació de la fitxa ni afegir procediments, proporcions, temps o resultats no documentats.

Els noms de plantilla que segueixen són **propostes de desenvolupament**, no plantilles ja implementades. Les figures G001 i G151 conserven les seves especificacions pròpies. Els esborranys automàtics G002–G150 i G152–G170 continuen sense aprovació.

## Famílies i arquitectura proposada

| Família | Figures | Lògica visual compartida | Plantilla o gramàtica proposada | Requisit específic abans de produir |
|---|---|---|---|---|
| F01. Classificació i organització documental | G001–G002 | Categories, procedència i relacions entre fonts d'informació | Matriu jeràrquica / flux documental | No confondre categoria d'informació amb grau de certesa; mostrar relacions reals de la font |
| F02. Comportament òptic i superfície | G003–G005, G020–G024 | Resposta de pintura/material, fons, relleu, transparència i lectura a escala | Comparativa de mostres sobre geometria constant; secció o superfície ampliada | Fixar variables comparades i mantenir geometria, llum i escala constants quan pertoqui |
| F03. Sistemes i planificació cromàtica | G006–G011, G051 | Relacions cromàtiques, dimensions del color, contrast i planificació | Rodes/mapes cromàtics, eixos i esquemes de paleta | No convertir esquemes orientatius en receptes universals ni barrejar models additiu/sostractiu |
| F04. Llum, ombra i reflexió localitzada | G012–G019, G044–G049, G099–G100, G103 | Font, direcció, geometria, bloqueig, valors i resposta de la superfície | Esquema geomètric amb raigs, normals i zones; comparativa de valors | Definir una única situació física per esquema; distingir llum incident, reflexió i emissió |
| F05. Eines, preparació i protecció | G025–G029, G137–G143 | Components, preparació, aplicació, inspecció i protecció | Làmina anatòmica/funcional i seqüència operativa | Separar instrucció general de dades dependents del producte; no inventar temps ni compatibilitats |
| F06. Rentats, tintes i pigments | G030–G034 | Naturalesa del producte, dipòsit, distribució, fixació i errors | Comparativa sobre peces equivalents i seqüència d'aplicació | Mantenir el mateix relleu per a comparacions; diferenciar producte, tècnica i resultat |
| F07. Anàlisi, mapes i presa de decisions | G035–G038, G050, G052–G053, G144–G150 | Diagnòstic, planificació, selecció, procés i avaluació | Mapa de procés, arbre de decisió i mapa de valors | Cada node i decisió ha de correspondre al text; evitar fluxos circulars o alternatives inventades |
| F08. Metall i representació metàl·lica | G039–G043, G054–G058 | Geometria, mapa tonal, TMM/NMM, construcció i control | Comparativa de materials i seqüència tonal sobre formes equivalents | Distingir aparença material de procediment pictòric; evitar reflexos genèrics no justificats |
| F09. Fusta i vegetació | G059–G070 | Direcció estructural, morfologia, agrupació i patrons naturals | Atles morfològic, esquemes de tall i patrons de direcció | Respectar morfologia i orientació; no reduir espècies/estructures diferents a una textura única |
| F10. Cuir i teixits | G071–G082 | Gra, estructura, trama, plecs, tensió i acabat | Mostres comparatives ampliades i esquemes de plecs/trama | Diferenciar estructura del material de la seva representació pictòrica |
| F11. Pell i teixits orgànics | G083–G088 | Pigmentació, mapa facial, volum muscular i diferenciació de teixits | Mapa anatòmic/cromàtic i comparativa de masses | Evitar codis cromàtics universals i separar anatomia de simplificació pictòrica |
| F12. Foc, sang i fluids | G089–G098 | Estructura, estat, distribució i construcció d'efectes | Seccions, mostres d'estat i distribució sobre geometries | No confondre aparença visual amb composició física; mantenir superfícies comparables |
| F13. Energia i emissió lluminosa | G101–G102 | Esferes, descàrregues i estructures energètiques | Esquema radial/ramificat amb jerarquia de valors | Diferenciar font emissora, halo, descàrrega i llum projectada |
| F14. Ceràmica, vidre i plàstics | G104–G114 | Cos, esmalt, transparència, difusió, reflexos i fractura | Atles de superfícies i seccions òptiques | No representar transparència com una simple opacitat baixa; conservar gruix, fons i reflexos |
| F15. Integració i harmonització cromàtica | G115–G120 | Relació entre masses, materials, figura/peanya i correccions | Comparativa global/local i seqüència de revisió | Diferenciar ajust local de canvi global; no imposar uniformitat cromàtica |
| F16. Envelliment, desgast i dany | G121–G128 | Mecanismes de desgast, geometria, ús, capes i pèrdua de recobriment | Atles de danys i seqüència de superfície | Distingir abrasió, impacte, pèrdua de capa i deteriorament; no assignar causes sense base |
| F17. Acabats i brillantor | G129–G136 | Reflexió especular/difusa, orientació, textura i selecció d'acabats | Comparativa de reflexos sobre geometries constants i mapa local | Controlar font i orientació; no equiparar brillantor percebuda amb material concret |
| F18. Capes, degradats i perfils | G151–G155 | Construcció progressiva i comparació de procediments d'integració | Seqüència sobre forma constant i comparativa de quatre procediments | Mantenir igual rang visual entre mètodes; no fixar nombre de capes, dilucions o temps |
| F19. Transparència i translucidesa | G156–G157 | Senyals òptics i construcció pictòrica de superfícies transmissives | Comparativa de transmissió, difusió, gruix i fons; seqüència pictòrica | Separar fenomen òptic de recursos pictòrics; no confondre transparència i translucidesa |
| F20. Materials biològics estructurals | G158–G160 | Os, teixit dental, queratina, banyes i estructures | Atles comparatiu de morfologia i superfície | Distingir materials i estructures; no atribuir a tots la mateixa textura ni color |
| F21. Geologia, cristalls, gel i gemmes | G161–G165 | Famílies de roca, estructura mineral, cristalls, neu/gel i gemmes | Atles geològic/morfològic i mostres ampliades | No presentar una textura genèrica com a representativa de totes les roques o minerals |
| F22. Corrosió, pàtines i dipòsits | G166–G170 | Oxidació, pàtines, pols, sediments i fang segons superfície/ús | Atles de processos i distribució sobre geometries comparables | Distingir material, procés i dipòsit; no inferir composició química ni cronologia només per aparença |

## Ordre de desenvolupament recomanat

1. **Validar les gramàtiques reutilitzables** amb una figura representativa de cada família abans d'aplicar-les a la resta.
2. Desenvolupar primer les famílies amb lògica geomètrica més explícita: F04, F08, F12, F13, F14, F16, F18 i F19.
3. Desenvolupar els atles morfològics F09–F11 i F20–F21 amb referències documentals verificables quan la forma o l'estructura natural sigui el contingut central.
4. Desenvolupar diagrames de procés i decisió F01, F05, F07 i F15 a partir del text exacte dels capítols.
5. Fer una revisió transversal de coherència gràfica després d'obtenir mostres representatives de totes les famílies.

## Límits de validació

- **Renderitzat:** l'SVG/PNG s'ha generat sense error.
- **Revisió visual:** composició, jerarquia, llegibilitat i consistència observades.
- **Fidelitat documental:** correspondència amb el capítol i les fonts tècniques.
- **Llegibilitat de maqueta:** comprovació a la mida real d'impressió.
- **Validació física/experimental:** només quan la figura afirma resultats o comportaments que requereixen prova.

Aquests estats no són intercanviables. Cap figura queda aprovada automàticament per pertànyer a una família ni per haver-se renderitzat.
