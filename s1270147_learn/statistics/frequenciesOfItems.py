import pandas as pd

class frequenciesOfItems:
    def frequenciesOfItems(fileName, separator):
        df = pd.read_csv(fileName, sep = separator)

        hashMap =  dict()
        for data in df.iloc[:, 0]:
            data = data.split(',')
            pos = str(data[0])
            pos = pos.replace("['",'').replace("']",'')
            around = len(data) - 1
            hashMap |= [(pos,[around])]
        return hashMap

if '__main__' == __name__ :
    frequenciesOfItems.frequenciesOfItems('PM24HeavyPollutionRecordingSensors.csv', '\t')