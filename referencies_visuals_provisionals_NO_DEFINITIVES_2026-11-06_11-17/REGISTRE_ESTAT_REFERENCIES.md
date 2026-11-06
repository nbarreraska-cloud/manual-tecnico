# Registre d'estat de les referències visuals

**Carpeta:** referències visuals provisionals, no definitives  
**Data d'inici del registre:** 2026-11-06  
**Hora d'inici:** 11:17 (hora local)  
**Branca de treball:** `intervencion-editorial-2026-11`

Aquest registre controla l'estat de cada figura del programa gràfic. Les referències que s'hi incorporin són provisionals i no constitueixen les imatges finals del manual. Només s'hi desaran imatges després de comparar diverses candidates i acordar-ne una.

## Estat per figura

| Codi | Figura / contingut | Estat | Observacions |
|---|---|---|---|
| G001 | Classificació de la informació tècnica (figura 1.1; identificador original P1 1.2) | **Mètode de producció decidit** | Es farà com un esquema vectorial propi, dissenyat específicament per al manual. No cal cercar una imatge externa ni generar-la amb IA: el contingut és una classificació conceptual definida pel text i requereix una composició clara i editable. Cal representar quatre blocs diferenciats (fonament tècnic, dada del fabricant, proposta tècnica i resultat comprovat), sense jerarquia ni escala de qualitat. Producció gràfica encara pendent; no s'ha generat ni aprovat cap imatge. |
| G002 | Organització documental de la informació sobre les pintures (figura 2.1; identificador original P1 2.2) | **Tancada — prototip v03 aprovat** | La revisió conceptual del v01 va detectar que separar completament documentació i aplicació podia ocultar que els capítols tècnics es nodreixen tant de la documentació específica de les pintures com dels fonaments generals del capítol 3. El v02 va introduir tres funcions diferenciades i les dues aportacions a l'aplicació. En la comprovació geomètrica del codi del v02 es va detectar que el connector entre les fitxes i l'aplicació travessava el requadre del límit informatiu. El v03 redirigeix el connector per la franja superior dels panells. S'ha renderitzat i inspeccionat visualment el v03: la ruta queda lliure de la nota, l'etiqueta és llegible, les dues connexions arriben als blocs corresponents i la composició general és clara. No s'hi detecten defectes que justifiquin una nova versió. Prototips conservats: `.../fig_C02_2-1_G002_v01.svg` (antecedent), `.../fig_C02_2-1_G002_v02.svg` (versió intermèdia) i `prototips_vectorials_provisionals_2026-11-06/fig_C02_2-1_G002_v03.svg` (versió actual). Mètode: vectorial propi; sense fotografia externa ni IA. Referències de disseny consultades: IBM Design Language, Technical diagrams (https://www.ibm.com/design/language/infographics/technical-diagrams/design/); Sample Project–Process–Document Relationships (https://permitting.innovation.gov/resources/data-standard/sample-project/); Figma, Information Architecture (https://www.figma.com/resource-library/what-is-information-architecture/). Cap imatge externa desada. El v03 queda aprovat i tancat com a figura; la inserció al manual es reserva per a la fase de maquetació i producció gràfica. |

| G003 | Opacitat, transparència, cobertura i influència del fons (figura de treball 3.1; integra l'antic 3.2) | **Prototip vectorial v03 creat — pendent de revisió** | La revisió del text 3.2.1 confirma tres qüestions diferents: ocultació del fons, influència del valor del suport sobre una mateixa capa i uniformitat de cobertura. S'han comparat alternatives: fotografia real només seria preferible si es documentessin mostres i condicions d'aplicació; IA no ofereix control suficient per representar una comparació tècnica; un esquema vectorial permet explicitar que els exemples són conceptuals. Es crea el v03 amb tres zones coordinades: quatre comportaments orientatius sobre suport contrastat, mateixa capa sobre fons blanc/gris/negre i comparació de cobertura uniforme/irregular. No és una escala mesurada ni una prova de productes. El prototip v02 es conserva com a antecedent. Nou fitxer: `prototips_vectorials_provisionals_2026-11-06/fig_C03_3-1_G003_v03.svg`. Referències: Leneta, Opacity Charts (https://leneta.com/product-category/sealed-charts-and-cards-for-coatings-tests/opacity-charts/), i fitxa de producte/ús de contrast (https://leneta.com/product-category/sealed-charts-and-cards-for-coatings-tests/); la documentació del fabricant descriu àrees blanques i negres per a observació visual de l'opacitat i el color. El v03 encara no està aprovat; no s'ha renderitzat ni validat externament. |
| G004 | Influència del fons en una mateixa capa de pintura (figura 3.2) | **En revisió retrospectiva** | El prototip v02 compara esquemàticament una mateixa capa sobre fons blanc, gris i negre. El tancament anterior queda suspès perquè no es va documentar una comparació suficient dels mètodes possibles. Cal valorar si l'esquema vectorial comunica adequadament el canvi d'aparença, si duplica parcialment G003 i si una fotografia controlada d'una mateixa aplicació sobre suports diferents aportaria evidència visual més fidel. El SVG es conserva com a prototip provisional, no aprovat. No es farà renderització ni validació tècnica externa del fitxer. |

## Criteri operatiu de treball — autonomia i compactació (06/11/2026)

El procés gràfic s'ha de dirigir amb autonomia tècnica i editorial, sense demanar autoritzacions rutinàries per a cada figura. Cal qüestionar tant les propostes de l'usuari com les decisions pròpies, i consultar-lo només quan la decisió depengui realment d'una preferència personal, d'informació que només ell pugui aportar o d'una qüestió estratègica no resoluble amb criteri tècnic.

Per efectivitzar el treball, s'han d'agrupar en una mateixa intervenció tots els processos compatibles: consulta del manual i de la fitxa editorial, anàlisi de la funció, cerca i comparació de referències quan sigui útil, selecció del mètode, disseny, revisió crítica, correccions i actualització del registre. No cal esperar una nova indicació de «continúa» quan el pas següent sigui clar i es pugui executar autònomament. La compactació no justifica ometre comprovacions ni reduir el rigor: s'han de mantenir la traçabilitat, la verificació dels fitxers i l'aprovació només quan la figura compleixi realment els criteris.

## Estat de revisió i següent pas

**G003: PROTOTIP VECTORIAL v03 CREAT — PENDENT DE REVISIÓ.** Integra l'ocultació del fons, la influència del valor del suport i la uniformitat de cobertura en una sola composició. El v02 es conserva com a antecedent. El v03 no està aprovat per a inserció; aquesta revisió no inclou renderització ni validació tècnica externa.

**G004: INTEGRADA EDITORIALMENT A G003.** L'antic identificador 3.2 deixa de correspondre a una figura independent. El prototip v02 es conserva com a antecedent documental, sense aprovació per a inserció.

La revisió manté el contrast de contingut, funció didàctica, referències i adequació del mètode; no inclou renderització ni validació tècnica externa dels SVG.

**G002 — Organització documental de la informació sobre les pintures (figura 2.1; identificador original P1 2.2): TANCADA.** El prototip vectorial v03 queda aprovat després de la revisió conceptual, tècnica i visual. Connecta la documentació específica (capítol 2, annex A i fitxes), els fonaments generals (capítol 3) i l'aplicació pràctica (capítols tècnics i receptes). El connector de les fitxes a l'aplicació discorre per la franja superior dels panells i no interfereix amb la nota de rigor. Els v01 i v02 es conserven com a antecedents. No s'ha desat cap imatge externa. La inserció al manual es farà en la fase de maquetació i producció gràfica.

**Següent pas: revisar editorialment el prototip G003 v03; després, anàlisi editorial de G005.**

## Criteris d'estat

- **Mètode de producció decidit:** s'ha acordat el tipus de producció, però la imatge encara no s'ha creat ni aprovat.
- **En revisió de contingut:** s'està contrastant la funció, l'estructura i els elements que ha de representar la figura abans de decidir-ne el disseny.
- **En comparació:** s'han localitzat diverses referències visuals i se n'està valorant l'adequació; encara no s'ha seleccionat ni desat cap candidata.
- **Prototip vectorial creat — pendent de revisió:** s'ha produït una primera versió editable a partir del contingut contrastat; encara no està aprovada ni preparada per inserir-se.
- **Pendent de cerca:** encara no s'han buscat candidates.
- **En cerca:** s'estan localitzant diverses candidates.
- **Possible generació:** es considera més adequat crear una imatge específica que cercar-ne una de preexistent.
- **Seleccionada provisionalment:** s'ha acordat una candidata per desar com a referència provisional.
- **Desada provisionalment:** el fitxer s'ha incorporat i verificat en aquesta carpeta.
- **Pendent de revisió:** cal revisar l'adequació o la procedència de la referència.
- **Tancada:** decisió finalitzada, sense que això impliqui necessàriament que la referència sigui una imatge final del manual.

