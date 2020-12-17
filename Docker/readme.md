To build enter docker build . --tag name

Also there is already built version by link https://hub.docker.com/r/zhenyagnatyuk/winstars

This image predicts target values of given input file and store it to target.csv file.

Usage: docker run -v {Input folder}:{Path in container} name {Path in container}/{input file}

Where: {Input folder} - folder, where your csv file is located

{Path in container} - folder, where you want to store input and output files in container

{input file} - name of csv file

So, for example, full command can be: docker run -v D:/somefolder/input/:/input zhenyagnatyuk/winstars:model /input/file.csv
