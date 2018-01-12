


#### this is a simple wrapper around samtools to subset bam files to later view in Igv for less command line literate people for visual validation of variants.

additional objects are for the writer to improve software documentasion as well as use click to manage inputs

it is possible to run multiple files by using a simple headerless csv

##### example of csv :

        inputfile,region,outputfile
##### it is also possible to run bed file indstead of region :

        inputfile,bedfile,outputfile