import sys
import os
import numpy as np
import pandas as pd


def predict(df):
    return df['6']**2 + df['7']


if __name__ == "__main__":
    assert len(sys.argv) == 2, "incorrect count of arguments"
    csv_file = sys.argv[1]
    assert os.path.isfile(csv_file), "File not found"
    assert csv_file.endswith('.csv'), "This is not csv file"
    path = csv_file.split('/')
    path.pop()
    path = '/'.join(path)
    data = pd.read_csv(csv_file)
    assert data.shape[1] == 53, "incorrect num of columns"
    predictions = predict(data)
    pred_transpose = predictions.T
    np.savetxt(path+'/' + 'target.csv', pred_transpose, delimiter=",")
    print("Runned Successful")

