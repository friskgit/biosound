#!/bin/bash

date_stamp=`date +"%F_%H%M%S"`
suffix=".wav"
file_name="$date_stamp$suffix"
echo ${file_name}

arecord -D -c 4 -d 60 $file_name
