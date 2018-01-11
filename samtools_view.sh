#!/usr/bin/env bash

input=$1
region=$2
outputfile=$3

samtools view -h -b $input $region > $outputfile
samtools index $outputfile