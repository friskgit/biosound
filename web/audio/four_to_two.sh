# take the input file and mix it down to stereo
sox input.wav output.wav remix 1,3 2,4
# filter away noise
sox input.wav output.wav highpass 200
