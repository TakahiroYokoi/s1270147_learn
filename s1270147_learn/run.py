from statistics.frequenciesOfItems import frequenciesOfItems
from visualization.heatMapItemsFrequencies import heatMapItemsFrequencies

map = frequenciesOfItems.frequenciesOfItems('PM24HeavyPollutionRecordingSensors.csv', '\t')

heatMapItemsFrequencies.show(map)