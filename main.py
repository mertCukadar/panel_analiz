from functions.Data_colletors import Data_colletors
import pandas as pd

if __name__ == '__main__':

    data_collector = Data_colletors
    folders = data_collector.collect_folder_names(data_collector.data_folder_G7)
    

    xlsx_files_G7 = []
    for folder in folders:
        xls_files = data_collector.scan_folder_collect_xls(data_collector.data_folder_G7 + '/' + folder)
        try:
            xlsx_files_G7.extend(xls_files)
        except TypeError:
            pass

    #scan all xlsx files set dataframes
    for xls_files in xlsx_files_G7:
        df = pd.read_excel(xls_files)
        df1 = df.iloc[:, :]
        try:
            df2 = pd.concat([df2, df1], axis=1)
        except NameError:
            df2 = df1    
    

    print(df2)
    # desc_e7 = df2.describe()
    # #save described dataframes to a new xlsx file
    # desc_e7.to_excel(data_collector.data_folder_E7 + '/' + 'desc_e7.xlsx')
    df2.to_csv('g7.csv')


