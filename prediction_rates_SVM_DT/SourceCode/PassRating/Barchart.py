import csv
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1


def view(list):

        plt.rcdefaults()
        objects = ('SVM','DT')
        y_pos = np.arange(len(objects))
        plt.bar(y_pos,list, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Accuracy')
        plt.xlabel('Algorithms')
        plt.title('Classification Analysis')
        plt.show()
