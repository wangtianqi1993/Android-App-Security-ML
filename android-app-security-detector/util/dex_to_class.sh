#!/bin/sh
# dex_to_java.sh input_file output_file
# first parameter end with / second parameter end without /
echo $1
filelist=`ls $1`
echo "waiting..."
for file in $filelist
do 
 filename=${file%.*}
 sh /home/wtq/develop/developtools/dex2jar-2.0/d2j-dex2jar.sh -o $2/$filename/$filename $1$file
done
apkjar=$2
jad=/home/wtq/develop/developtools/jad-tools/jad
jarlist=`ls $apkjar`
for jarname in $jarlist
do
 cd $2/$jarname/
 jar xf $2/$jarname/$jarname
 rm $2/$jarname/$jarname
done
echo "end!"
