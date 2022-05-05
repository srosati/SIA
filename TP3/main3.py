from utils import Utils
from multilayer import Multilayer
from plotter import plot_error, plot_metric
import numpy as np

ej = 2

if ej == 1:
    or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
    or_out_set = [[1], [1], [-1], [-1]]
    print("XOR")

    errors = Multilayer([2, 1], 2, 0.5).solve(or_in_set, or_out_set, 0.001)
    plot_error(errors)
else:
    in_set = []
    with open("./number_set.txt", "r") as training_file:
            readlines = training_file.readlines()
            for idx in range(int(len(readlines) / 7)):
                line_range = readlines[idx * 7 : (idx + 1) * 7]
                num_array = [-1]
                for line in line_range:
                    num_array +=  [int(n) for n in line.split()]
                in_set.append(num_array)
            training_file.close()

    if ej == 2:
        # EJERCICIO 2: PAR O IMPAR

        out_set = [[1], [-1]] * 5

        in_set, out_set = Utils.shuffle_two_arrays(in_set, out_set)

        k = 10
        in_parts = np.array_split(in_set, k)
        out_parts = np.array_split(out_set, k)

        met = []
        best_metric = [0]

        for i in range(k):
            training_set_in = []
            training_set_out = []
            for idx, part in enumerate(in_parts):
                if idx != i:
                    training_set_in += list(part)
                    training_set_out += list(out_parts[idx])
            
            training_set = {"in": training_set_in, "out": training_set_out}
            test_set = {"in": in_parts[i], "out": out_parts[i]}
            print("[ k =", i, "]:", end=" ")
            errors, metrics = Multilayer([10, 1], 35, 0.01).solve(training_set, test_set, 0.01)

            if max(metrics) > max(best_metric):
                print("METRICA:", max(metrics))
                best_metric = metrics

            plot_error(errors)
        plot_metric(met, k)

    else:
        # EJERCICIO 3: NUMERO
        # el training set es el mismo
        
        ## PRINTS INTERFERENCE NUMBER ##
        for i, picture in enumerate(in_set):
            picture = picture[1:]
            for j in range(len(picture)):
                rnd = np.random.uniform()
                if rnd < 0.02:
                    picture[j] = 1 - picture[j]
                if j % 5 == 0:
                    print()
                else:
                    print(picture[j], end=" ")
            print()


        out_set = []
        for num in range(10):
            expected_output = [0] * 10
            expected_output[num] = 1
            out_set.append(expected_output)
        # 5, 11, 10 anduvo bastante bien
        multilayer = Multilayer([5,11,10], 35, 0.1)
        errors = multilayer.solve(in_set, out_set, 0.01) 
        plot_error(errors)

        print(in_set)

        # agregamos ruido a los datos
        for i, picture in enumerate(in_set):
            for j in range(len(picture)):
                rnd = np.random.uniform()
                if rnd < 0.02:
                    picture[j] = 1 - picture[j]
                print[j]
            print()
        # print(in_set)


        pe = 0
        nope = 0
        for i, in_ix in enumerate(in_set):
            res = multilayer.predict(in_ix)            
            
            if (sum([abs(n) for n in np.subtract(out_set[i], np.array(res))]) <= 0.01):
                pe+=1
                print("pega")
            else:
                print("no pega")
                nope+=1

        
    
        