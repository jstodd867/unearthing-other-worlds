import requests
import os

def get_data(query):
    '''
    Retrieve results of a query of the NASA exoplanet archive.

    Parameters
    ----------
    query: string
        the query formatted per the API instructions
    
    Returns
    -------
    request object
        contains data from the resulting webpage
    '''
    base_url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query='
    return requests.get(base_url + query)

def save_data(data, save_filename, file_format = '.csv', dir_path = './data/', overwrite = False):
    '''
    Writes queried data to a file.

    Parameters
    ----------
    data: bytes
        data to be written to the file
    save_filename: string
        desired filename
    file_format: string
        '.csv' for csv
    dir_path: string
        directory where data file will be saved
    overwrite: boolean
        Flag to overwrite file if it already exists (True)
    '''
    file_path = dir_path + save_filename + file_format
    if overwrite == False and os.path.exists(file_path):
        print(f'{file_path} already exists.  Choose a different filename or set the overwrite flag to True to overwrite the existing file.')
    else:
        f = open(dir_path + save_filename + file_format, "wb")
        f.write(data)
        f.close()

if __name__ == '__main__':
    query = 'select+pl_name,discoverymethod,disc_year,disc_facility,sy_snum,sy_pnum,glat,glon,pl_orbper,pl_rade,sy_dist,pl_eqt,pl_orbeccen+from+pscomppars&format=csv'
    r = get_data(query)  # Retrieve data from exoplanet archive

    save_filename = 'distinct_planets' # Specify filename to save query data
    save_data(r.content, save_filename,overwrite=False) # Save query results in a CSV file