import os
import pandas as pd

class Data_colletors:
    data_folder_E7 = 'datas/E7' # ensure that the folder is created before running the code
    data_folder_G7 = 'datas/G7' # ensure that the folder is created before running the code

    @staticmethod
    def collect_folder_names(data_folder):
        return os.listdir(data_folder)
    
    @staticmethod
    def scan_folder_collect_xls(folder_name):
        if os.path.isdir(folder_name):
            dirs = os.listdir(folder_name)
            xls_file_paths = []
            for file in dirs:
                if file.endswith('.xlsx'):
                    xls_file_paths.append(folder_name + '/' + file)
            return xls_file_paths
        else:
            pass
    
    @staticmethod
    def collect_xlsx_files(data_folder):
        folders = Data_colletors.collect_folder_names(data_folder)
        xlsx_files = []
        for folder in folders:
            xls_files = Data_colletors.scan_folder_collect_xls(data_folder + '/' + folder)
            try:
                xlsx_files.extend(xls_files)
            except TypeError:
                pass
        return xlsx_files

    @staticmethod
    def process_xlsx_files(xlsx_files):
        for xls_file in xlsx_files:
            df = pd.read_excel(xls_file)
            df1 = df.iloc[:, 2]  # Save only the 2nd column
            try:
                df2 = pd.concat([df2, df1], axis=1)
            except NameError:
                df2 = df1    
        return df2

    @staticmethod
    def save_descriptive_statistics(df, output_path):
        desc = df.describe()
        desc.to_excel(output_path)
