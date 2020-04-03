import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn


def gen_cm(not_not, off_not, not_off, off_off, langauge):
    conf_mat = np.array([[not_not, not_off], [off_not, off_off]])
    labels = ["NOT", "OFF"]
    df_cm = pd.DataFrame(conf_mat, index=[i for i in labels], columns=[i for i in labels])
    plt.figure(figsize=(10, 7))
    plt.title('Confusion matrix')
    sn.heatmap(df_cm, annot=True, fmt='g')
    # plt.show()
    plt.savefig('data/' + langauge + '/' + langauge + '_cm')


gen_cm(534, 77, 31, 58, "arabic")
gen_cm(251, 19, 2, 24, "danish")
gen_cm(578, 89, 52, 150, "greek")
gen_cm(2555, 494, 15, 112, "turkish")
