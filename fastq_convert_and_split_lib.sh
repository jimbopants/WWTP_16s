#!/usr/bin/env bash
# JG 5/11/15

# This file prepares fastq files that have already been quality filtered in usearch and had barcodes from labels added to the sequences
# for OTU assignment in QIIME by running convert_fastaqual_fastq and split_libraries on each fastq and resulting fasta + qual files.
# Results are stored in /path/convert_fastq and /path/post_split

mkdir ./Alex_convert_fastq
mkdir ./Alex_post_split


FILES=./Alex2/*

# Run fasta convert on each file:
for f in $FILES; do
    convert_fastaqual_fastq.py -f $f -o ./Alex_convert_fastq/ -c fastq_to_fastaqual
done


# Run split_libraries.py on each set of fasta and quality files from previous command
LINE_COUNT=0
PREVLINE=""

find ./Alex_convert_fastq/* | while read LINE
  do LINE_COUNT=$(($LINE_COUNT+1));
        if [ $LINE_COUNT = 2 ]; then  # Need a space between if [ stuff ] 
        LINE_COUNT=0      
        split_libraries.py -m ./map/map_v1_corrected.txt -f $PREVLINE -q $LINE -l 230 -L 290 -t -b 10 -o ./Alex_post_split/$PREVLINE -z truncate_remove --reverse_primer_mismatches 1 -M 1
    fi
    PREVLINE=$LINE;
done



################################
# Junk

#   echo $LINE
#done


#echo $FQUALS


#FQUALS=./convert_fastq/*

#var=(ls ./convert_fastq)
#for f in $var; do
#    echo $f
#done


# Run split libraries on each fna + qual file:
#QUALS=./fasta_qual_files/*.qual
#FNAS=./fastq_qual_files/*.fna

#echo $QUALS
#NUMFASTAS=$(find ./fixed/* -maxdepth 1 -type f | wc -l)
#echo $NUMFASTAS

#for f in $FASTAQUALS; do
#echo $f
#done



#while read LINE;
#do
#    echo LINE
#done < "$OUTPUT"

#echo "${OUTPUT}"


#indir="$./fixed"
#dir2="$stuff"

#while read LINE;
#do
#    convert_fastaqual_fastq.py -f stuff -o ./fasta_qual_files/ -c fastq_to_fastaqual
#done < input_file_list
#
#while read LINE;
#do
#    split_libraries.py -m map.txt -f putthenamehere -q qualhere -l 230 -L 290 -t -b 10 -o ./post_split/ -z truncate_remove --reverse_primer_mismatches 2 -M 2
#done < 2nd_input_list
