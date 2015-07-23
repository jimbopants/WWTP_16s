#!/bin/bash

# This file takes a directory of raw sequence data from UIC and runs it through PEAR - Paired End reAd meRger
# Then outputs the results to an output directory

FILE=$1  #can't put spaces lolll lmao
IN=$2
OUT=$3

LINE_COUNT=0
PREVLINE=""
while read LINE;
  do LINE_COUNT=$(($LINE_COUNT+1));
      #echo $LINE_COUNT
        if [ $LINE_COUNT = 2 ]; then  # Need a space between if [ stuff ] 
        LINE_COUNT=0
        #echo $IN$PREVLINE
        pear -f $IN$PREVLINE -r $IN$LINE -o $OUT$PREVLINE -m 300 -n 230 -t 230
    fi
    PREVLINE=$LINE;
    echo $LINE_COUNT
done <$1




