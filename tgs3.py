import csv
import math
import collections


K = 50

def cekDataTrain():
    with open('DataTrain_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')   
        next(reader)
        data = []
        for row in reader:
            data.append(list(map(lambda x: float(x), row[1:])))
        return data

def cekDataTest():
    with open('DataTest_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        data = []
        for row in reader:
            data.append(list(map(lambda x: float(x), row[1:6])))
        return data

def jarakEuclidean(inputX, inputY):
    euclidean = list(map(lambda x,y: (x - y)**2, inputX, inputY))
    return math.sqrt(sum(euclidean))


if __name__ == '__main__':
    training_data = cekDataTrain()
    test_data = cekDataTest()
    dataHasil = []
    for test in test_data:
        list_jarak = []
        for train in training_data:
            list_jarak.append([jarakEuclidean(test, train[:5]), train[5]])
        list_jarak.sort(key=(lambda x:x[0]))
        jarak_terdekat = list_jarak[:K]
        jarak, class_type = zip(*jarak_terdekat)
        counter = collections.Counter(class_type)
        hasil = counter.most_common(1)[0][0]
        print (hasil)
        dataHasil.append(int(hasil))
        with open('TebakanTugas3.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            i = 1
            for hasil in dataHasil:
                writer.writerow([i, hasil])
                i += 1
