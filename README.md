# Create a benchmark dataset with GO annotations through the following procedures.
<b>[1] Download go-basic.obo from http://purl.obolibrary.org/obo/go/go-basic.obo.  
<b>[2] Download goa_uniprot_all.gaf from http://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/goa_uniprot_all.gaf.gz.    
<b>[3] Extract GO terms from goa_uniprot_all.gaf.gz:  
>(a)Extract_From_GOA.py  
>(b)Generate_GO_Terms.py  
>(c)Complementary_All_Term.py  
>(d)Find_Parents.py
>
<b>[4] Total the number of all proteins for MF, BP, and CC aspects:
>Total_Protein_Number.py
>
<b>[5] Download protein sequences with information from UniProt database:
> download_sequence_uniprot.py
> 
<b>[6] Create training dataset, validation dataset, and test dataset using the deposition date:
> Extract_Sequence_By_Date.py
> 
<b>[7] Remove homology sequences using CD-HIT software among training, validation, and test datasets.  

<b>[8] Create the corresonding labels and names for each dataset:
>(a) Extract_protein_list_from_sequence.py
>(b) Create_Term_Set.py
