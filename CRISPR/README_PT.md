# AwesomeCRISPR

[![Awesome](https://awesome.re/badges/note.svg)](https://awesome.re)

> Uma lista curada de softwares, bancos de dados, websites e artigos para engenharia genética via CRISPR-Cas.

Inspirado pelo projeto [awesome-single-cell](https://github.com/seandavi/awesome-single-cell) e outras listas "awesome", este repositório tem como objetivo centralizar recursos para pesquisa em CRISPR. Ele abrange design de guias, predição de off-targets, análise de resultados de edição genômica, pipelines de screenings e bancos de dados relevantes.

**Nota:** A etiqueta **"Recommended"** (Recomendado) indica favoritos pessoais e não implica em uma avaliação rigorosa. Contribuições são bem-vindas!

## Conteúdos

- [Ferramentas de Design de Guia](#ferramentas-de-design-de-guia)
- [Algoritmos de Predição de Off-Target](#algoritmos-de-predição-de-off-target)
- [Resultados e Predições de Edição Genômica](#resultados-e-predições-de-edição-genômica)
- [Algoritmos de Análise de Screening](#algoritmos-de-análise-de-screening)
- [Bancos de Dados](#bancos-de-dados)
- [Identificação e Diversidade de CRISPR](#identificação-e-diversidade-de-crispr)
- [Reviews (Revisões)](#reviews-revisões)

## Ferramentas de Design de Guia

*   **ATUM** - [Webserver](https://www.atum.bio/eCommerce/cas9/input) - Designa gRNAs para minimizar efeitos off-target usando algoritmos de pontuação proprietários.
*   **BE-DICT** - [Python, Webserver](http://www.be-dict.org) - Algoritmo de deep learning baseado em atenção para predizer resultados de edição de bases.
*   **beditor** - [Python](https://github.com/rraadd88/beditor) - Fluxo de trabalho computacional para design de bibliotecas de sgRNAs para Edição de Base via CRISPR.
*   **Benchling** - [Webserver](https://benchling.com/crispr) - Plataforma de design para gRNAs ótimos analisando localização do alvo, especificidade e eficiência.
*   **Breaking-Cas** - [Webserver](http://bioinfogp.cnb.csic.es/tools/breakingcas/) - Ferramenta de design suportando múltiplos organismos e extensa customização.
*   **Cas-Designer** - [Webserver](http://www.rgenome.net/cas-designer/) - Designer rápido de guia-RNA para RGENs derivados de CRISPR/Cas, suporta bulgas (bulges).
*   **Cas13design** - [Webserver](https://cas13design.nygenome.org/) - Guia RNAs otimizados para alvo de transcritos em humanos, organismos modelo e genomas virais de RNA.
*   **CRISPOR** - [Webserver](http://crispor.org) - Altamente popular para design de gRNA e pontuação off-target (Cas9, Cpf1, etc.).
*   **CHOPCHOP** - [Webserver](https://chopchop.cbu.uib.no/) - Web tool para busca de knockout genético e alvos de edição genômica.
*   **DeepCRISPR** - [Python](https://github.com/qianlab/DeepCRISPR) - Predição de off-target e design de guias baseado em deep learning.

## Algoritmos de Predição de Off-Target

*   **CCTop** - [Webserver](https://cctop.cos.uni-heidelberg.de:8080/) - Preditor online de alvos CRISPR/Cas9.
*   **Cas-OFFinder** - [Webserver](http://www.rgenome.net/cas-offinder/) - Busca ultra-rápida por sítios off-target potenciais.
*   **CRISPRitz** - [Python](https://github.com/quadram-institute-bioscience/CRISPRitz) - Suíte de software para busca de alvos CRISPR e análise off-target.
*   **E-CRISP** - [Webserver](https://www.e-crisp.org/) - Design de sgRNAs considerando efeitos off-target.
*   **GuideScan** - [Webserver](https://guidescan.com/) - Design de RNA guia otimizado para máxima especificidade.

## Resultados e Predições de Edição Genômica

*   **InDelphi** - [Webserver](http://indelphi.gs.washington.edu/) - Predição de resultados de edição genômica para SpCas9.
*   **CRISPResso2** - [Python](https://github.com/pinellolab/CRISPResso2) - Análise de resultados de edição genômica CRISPR-Cas9 a partir de dados de sequenciamento profundo.
*   **ICE Analysis** - [Webserver](https://ice.synthego.com/) - Análise de dados de sequenciamento Sanger para quantificar eficiência de edição.
*   **TIDE** - [Webserver](https://tide.nki.nl/) - Rastreamento de Indels por Decomposição.

## Algoritmos de Análise de Screening

*   **MAGeCK** - [R, Python](https://sourceforge.net/projects/mageck/) - Análise baseada em modelo de CRISPR-Cas9 em larga escala (knockout e ativação).
*   **CRISPRAnalyzeR** - [Webserver](https://crispr-analyzer.ibg.uni-freiburg.de/) - Análise interativa e visualização de dados de screening CRISPR.
*   **DrugZ** - [R, Python](https://github.com/yuan237/DrugZ) - Identificação de letalidade sintética em telas de combinação de drogas.
*   **SCREEN** - [Webserver](https://screen.unc.edu/) - Análise estatística de telas CRISPR em pooled.

## Bancos de Dados

*   **CRISPRme** - [Webserver](https://crisprme.crs4.it/) - Banco de dados e ferramenta para avaliação de off-target CRISPR.
*   **CRISPOR** - [Webserver](http://crispor.org) - Inclui um banco de dados de alvos pré-computados.
*   **Cas9 Database** - [Webserver](http://crispr.ccgb.umn.edu/) - Coleção de ortólogos e variantes de Cas9.

## Identificação e Diversidade de CRISPR

*   **CRISPRCasFinder** - [Webserver](https://crisprcasfinder.inrae.fr/) - Identificação de sistemas CRISPR-Cas em genomas.
*   **PILER-CR** - [Software](http://www.drive5.com/piler/) - Identificação rápida de arrays CRISPR.

## Reviews (Revisões)

*   [Zhang et al. Cell Press 4(1), 2, 2015](https://www.sciencedirect.com/science/article/pii/S216225311630049X)
*   [Li et al. Signal Transduction and Targeted Therapy 5(1), 2, 2020](https://www.nature.com/articles/s41392-020-00186-9)
*   [Leenay et al. Molecular Cell 62(1), 137–147, 2016](https://www.cell.com/molecular-cell/pdf/S1097-2765(16)00175-1.pdf)
*   [Yan et al. Science 363, 88-91, 2019](https://science.sciencemag.org/content/363/6422/88.full.pdf)

## Contribuindo

Contribuições são bem-vindas! Por favor, leia as [Diretrizes de Contribuição](CONTRIBUTING.md) antes de enviar um pull request.

## Licença

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

Na medida do possível sob a lei, Wei Li renunciou a todos os direitos autorais e relacionados ou vizinhos a este trabalho.