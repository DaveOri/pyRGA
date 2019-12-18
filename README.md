# pyRGA
compute RGA approximation and compare with DDA

## RGA submodule
This submodule has a very short list of requirements, like numpy and scipy and you can use it without problems.
The shapefiles can be passed as lists of triplets or textfile containing one triplet per line.

## comparison with DDA
If you want to compare with DDA it is assumed that you have compiled ADDA https://github.com/adda-team/adda
This module assumes you to have installed pamtra2 https://github.com/maahn/pamtra2 for the refractiveIndex submodule
Also the shapefile is required to have a regular grid for DDA.
