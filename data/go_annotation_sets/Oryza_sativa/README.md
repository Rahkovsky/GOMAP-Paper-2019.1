# Gold Standard
The Gold Standard was downloaded on 08/07/2019 from [Gramene Biomart](http://ensembl.gramene.org/biomart/martview) with the following selections:

1. *CHOOSE DATABASE* -> Plant Genes 61
2. *CHOOSE DATASET* -> Oryza sativa Japonica Group genes (IRGSP-1.0)
3. on the left hand side, select *Filters*, open *GENE ONTOLOGY* and select all evidence codes but IEA (IBA,IC,IDA,IEP,IGC,IGI,IMP,IPI,ISO,ISS,NAS,ND,RCA,TAS)
4. again on the left hand side, select *Attributes*, open *GENE* and make sure only Gene stable ID is checked, then open *EXTERNAL* and check _GO term accession, GO term evidence code,_ and _GO domain_.
5. Then click *Results* in the black top bar menu and export all results to a TSV file (check *Unique results only*).

We then converted that downloaded TSV file to a GAF file with the `transformGoldStandard2GAF.sh` script so we don't have to deal with different file types in further analyses.