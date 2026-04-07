#dataparser
import pickle
import tqdm
import os

def EasyQM9(path = './data'):
    pbar = tqdm.tqdm(total=5, desc="Loading QM9 data parts")
    data = []
    for i in range(5):
        dataipath = os.path.join(path, f'qm9_data_part{i+1}.pkl')
        with open(dataipath, 'rb') as f:
            part = pickle.load(f)
            data.extend(part)
        pbar.update(1)
    pbar.close()
    print("Load Complete! Found {} samples.".format(len(data)))
    return data
