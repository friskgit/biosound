#!/bin/bash
sec='10'
date_stamp=`date +"%F_%H%M%S"`
suffix=".wav"
file_name="$date_stamp$suffix"
mp3_name=${file_name%.wav}".mp3"
echo "Recording to $sec seconds of audio to ${file_name}"
echo "Encoding into $mp3_name"
arecord -D plughw:1,0 -f cd -c 2 -d $sec $file_name

echo "Creating stereo file"
sox $file_name output_stereo.wav remix 1v0.9723,2v0.80901 1v0.23344,2v0.5877
echo "High pass filter, reverb and fades"
sox output_stereo.wav filtered_stereo.wav channels 2 highpass 600 pad 0 3 reverb 50 50 75 fade 1
echo "Encode the file to mp3"
lame --preset medium $file_name $mp3_name
echo "Upload the file to server"
scp filtered_stereo.wav henrikfr@henrikfrisk.com:www/rain/audio/$mp3_name
echo "Cleaning up."
rm ./output_stereo.wav
rm ./filtered_stereo.wav
rm ./$file_name
rm ./mp3_name
echo "Done"
