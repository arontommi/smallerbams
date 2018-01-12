


#### this is a simple wrapper around samtools to subset bam files to later view in Igv for less command line literate people for visual validation of variants.

additional objects are for the writer to improve software documentasion as well as use click to manage inputs

for simple regions in single patient it is possible to give parameters

paramenters

    -- inputfile : a bam file
    -- region : region, example : 1:1500-3000 important note, make sure to know if you are supposed to use Chr in front or not
    -- outputfile : a subsetted bamfile

it it is also possible to run multiple files by using a simple headerless csv

##### example of csv :

        inputfile,region,outputfile
##### it is also possible to run bed file indstead of region :

        inputfile,bedfile,outputfile