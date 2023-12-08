import numpy as np
import string
import io

#day 5 challenge 2

#the real input is input05.
#There's also a test05-1, which is used to make sure that the code runs correctly.

# need a parser to:
# * generate the mappings
# * run the inputs through each mapping,
# and then the outputs into the next mapping, etc
# at the location outputs, sort to get the location

# there's no reason that these inputs have to be a single horrible file.
# can easily have seed inputs, then a map file (or series of map files)

testseedsin = [79,14,55,13]
seedsin=[3139431799,50198205,3647185634,110151761,2478641666,139825503,498892555,8913570,961540761,489996751,568452082,100080382,907727477,42158689,1617552130,312026427,342640189,97088268,2049289560,336766062]

# but now, these initial seed runs are mapping. Converting them into seed ranges like in part 1:
testseedstemp = np.reshape(testseedsin, [2,2])
seedstemp = np.reshape(seedsin, [int(len(seedsin)/2),2])

testseeds = []
for test in testseedstemp:
		for x in np.arange(test[0],(test[0]+test[1]-1)):
			testseeds.append(x)

seeds = testseeds
#this can't work because there are too many array values
#need to find a way to do fewer computations
# if we just note start and range, but break up each set when it crosses a boundary for soil etc....?
#extremely good news: the mappings appear to have no overlaps (or gaps)!
'''
seeds = []
for test in seedstemp:
		for x in np.arange(test[0],(test[0]+test[1]-1)):
			seeds.append(x)
'''
#All remappings work the same, so we can just reuse a single function!
def remap(inputs, map):
	outputs = []
	for input in inputs:
		output = input
		for mapline in map:
			if input >= mapline[1] and input <=(mapline[1]+mapline[2]-1):
				output = mapline[0] + (input - mapline[1])
		outputs.append(output)
	return outputs

# assuming I have a 'map' file which contains in each line: destination start, source start, range length:
#real files are .51, test ones are .51t
seedtosoil = np.genfromtxt("seedtosoil.51t", delimiter=' ', dtype=int)
soils = remap(seeds, seedtosoil)

soiltofertilizer = np.genfromtxt("soiltofertilizer.51t", delimiter=' ', dtype=int)
fertilizers = remap(soils, soiltofertilizer)

fertilizertowater = np.genfromtxt("fertilizertowater.51t", delimiter=' ', dtype=int)
waters = remap(fertilizers, fertilizertowater)

watertolight = np.genfromtxt("watertolight.51t", delimiter=' ', dtype=int)
lights = remap(waters, watertolight)

lighttotemperature = np.genfromtxt("lighttotemperature.51t", delimiter=' ', dtype=int)
temperatures = remap(lights, lighttotemperature)

temperaturetohumidity = np.genfromtxt("temperaturetohumidity.51t", delimiter=' ', dtype=int)
humiditys = remap(temperatures, temperaturetohumidity)

humiditytolocation = np.genfromtxt("humidtytolocation.51t", delimiter=' ', dtype=int)
locations = remap(humiditys, humiditytolocation)

locations.sort()
print(locations[0])
