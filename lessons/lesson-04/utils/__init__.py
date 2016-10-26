from tqdm import tqdm
import requests
import os
import qgrid

def download_data(filename, force=False):
    prefix = "https://s3-us-west-2.amazonaws.com/ga-ds/"
    dest_dir = 'data'

    path = '/'.join([dest_dir,filename])

    ensure_dir_exists(dest_dir)

    if not force and os.path.isfile(path):
        return None

    response = requests.get(prefix + filename, stream=True)

    with open(path, 'wb') as f:

        for data in tqdm(response.iter_content()):
           f.write(data)

def ensure_dir_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

qgrid.nbinstall(overwrite=True)
grid = lambda df: qgrid.show_grid(df)
