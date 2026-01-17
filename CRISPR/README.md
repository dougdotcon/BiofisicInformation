# AwesomeCRISPR

[![Awesome](https://awesome.re/badges/note.svg)](https://awesome.re)

> A curated list of software, databases, websites, and papers for CRISPR-Cas genome engineering.

Inspired by the [awesome-single-cell](https://github.com/seandavi/awesome-single-cell) project and other awesome lists, this repository aims to centralize resources for CRISPR research. It covers guide design, off-target prediction, genome editing outcome analysis, screening pipelines, and relevant databases.

**Note:** The **"Recommended"** label indicates personal favorites and does not imply rigorous evaluation. Contributions are welcome!

## Contents

- [Guide Design Tools](#guide-design-tools)
- [Off-Target Prediction Algorithms](#off-target-prediction-algorithms)
- [Genome Editing Outcomes & Predictions](#genome-editing-outcomes--predictions)
- [Screening Analysis Algorithms](#screening-analysis-algorithms)
- [Databases](#databases)
- [CRISPR Identification & Diversity](#crispr-identification--diversity)
- [Reviews](#reviews)

## Guide Design Tools

*   **ATUM** - [Webserver](https://www.atum.bio/eCommerce/cas9/input) - Designs gRNAs to minimize off-target effects using proprietary scoring algorithms.
*   **BE-DICT** - [Python, Webserver](http://www.be-dict.org) - Attention-based deep learning algorithm for predicting base editing outcomes.
*   **beditor** - [Python](https://github.com/rraadd88/beditor) - Computational workflow for designing libraries of sgRNAs for CRISPR-Mediated Base Editing.
*   **Benchling** - [Webserver](https://benchling.com/crispr) - Design platform for optimal CRISPR gRNAs analyzing target location, specificity, and efficiency.
*   **Breaking-Cas** - [Webserver](http://bioinfogp.cnb.csic.es/tools/breakingcas/) - Design tool supporting multiple organisms and extensive customization.
*   **Cas-Designer** - [Webserver](http://www.rgenome.net/cas-designer/) - Quick guide-RNA designer for CRISPR/Cas derived RGENs, supports bulges.
*   **Cas13design** - [Webserver](https://cas13design.nygenome.org/) - Optimized guide RNAs for targeting transcripts in human, model organisms, and viral RNA genomes.
*   **CRISPOR** - [Webserver](http://crispor.org) - Highly popular tool for gRNA design and off-target scoring (Cas9, Cpf1, etc.).
*   **CHOPCHOP** - [Webserver](https://chopchop.cbu.uib.no/) - Web tool for searching gene knockout and genome editing targets.
*   **DeepCRISPR** - [Python](https://github.com/qianlab/DeepCRISPR) - Deep learning-based guide design and off-target prediction.

## Off-Target Prediction Algorithms

*   **CCTop** - [Webserver](https://cctop.cos.uni-heidelberg.de:8080/) - CRISPR/Cas9 target online predictor.
*   **Cas-OFFinder** - [Webserver](http://www.rgenome.net/cas-offinder/) - Ultra-fast search for potential off-target sites.
*   **CRISPRitz** - [Python](https://github.com/quadram-institute-bioscience/CRISPRitz) - Software suite for CRISPR target search and off-target analysis.
*   **E-CRISP** - [Webserver](https://www.e-crisp.org/) - Design of sgRNAs considering off-target effects.
*   **GuideScan** - [Webserver](https://guidescan.com/) - Optimized guide RNA design for maximal specificity.

## Genome Editing Outcomes & Predictions

*   **InDelphi** - [Webserver](http://indelphi.gs.washington.edu/) - Prediction of genome editing outcomes for SpCas9.
*   **CRISPResso2** - [Python](https://github.com/pinellolab/CRISPResso2) - Analysis of CRISPR-Cas9 genome editing outcomes from deep sequencing data.
*   **ICE Analysis** - [Webserver](https://ice.synthego.com/) - Analysis of Sanger sequencing data to quantify editing efficiency.
*   **TIDE** - [Webserver](https://tide.nki.nl/) - Tracking of Indels by DEcomposition.

## Screening Analysis Algorithms

*   **MAGeCK** - [R, Python](https://sourceforge.net/projects/mageck/) - Model-based analysis of genome-wide CRISPR-Cas9 knockout and activation screens.
*   **CRISPRAnalyzeR** - [Webserver](https:// crispr-analyzer.ibg.uni-freiburg.de/) - Interactive analysis and visualization of CRISPR screening data.
*   **DrugZ** - [R, Python](https://github.com/yuan237/DrugZ) - Identification of synthetic lethality in drug combination screens.
*   **SCREEN** - [Webserver](https://screen.unc.edu/) - Statistical analysis of pooled CRISPR screens.

## Databases

*   **CRISPRme** - [Webserver](https://crisprme.crs4.it/) - Database and tool for CRISPR off-target evaluation.
*   **CRISPOR** - [Webserver](http://crispor.org) - Includes a database of pre-computed targets.
*   **Cas9 Database** - [Webserver](http://crispr.ccgb.umn.edu/) - Collection of Cas9 orthologs and variants.

## CRISPR Identification & Diversity

*   **CRISPRCasFinder** - [Webserver](https://crisprcasfinder.inrae.fr/) - Identification of CRISPR-Cas systems in genomes.
*   **PILER-CR** - [Software](http://www.drive5.com/piler/) - Fast identification of CRISPR arrays.

## Reviews

*   [Zhang et al. Cell Press 4(1), 2, 2015](https://www.sciencedirect.com/science/article/pii/S216225311630049X)
*   [Li et al. Signal Transduction and Targeted Therapy 5(1), 2, 2020](https://www.nature.com/articles/s41392-020-00186-9)
*   [Leenay et al. Molecular Cell 62(1), 137–147, 2016](https://www.cell.com/molecular-cell/pdf/S1097-2765(16)00175-1.pdf)
*   [Yan et al. Science 363, 88-91, 2019](https://science.sciencemag.org/content/363/6422/88.full.pdf)

## Contributing

Contributions are welcome! Please read the [Contribution Guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Wei Li has waived all copyright and related or neighboring rights to this work.