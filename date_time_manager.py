from datetime import date
from msilib.schema import Directory
import os 
import glob 
import pathlib
import shutil
from khayyam import JalaliDate
from rtl import rtl
def get_persian_date():
    date = JalaliDate.today().strftime('%A-%d-%B-%Y')
    return date


def create_folder(  ):
    directory_list = folders_names()
    date=get_persian_date()
    parent_dir = os.path.dirname(__file__)
    
    try:
        os.mkdir(parent_dir +"\\"+ date)
    except:
        print('folder as name of %s is already exist' %(date))
    
    
    for directory in directory_list:
        
        path = os.path.join(parent_dir+"\\"+date, directory)
        
        
        try:
            os.mkdir(path)
        except:
            print('folder as name of %s is already exist' %(directory))
        else:
            pass
    
    
    
    
def folders_names():
    dir_path = os.path.dirname(__file__)
    file_names = []
    
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            file_names.append(path)
    
    
    suffixs = []
    for item in file_names:
        file_extention = get_file_extention(item)
        
        suffixs.append(file_extention)
    final_suffixs = []
    for item in suffixs:
        if item  not in final_suffixs:
            final_suffixs.append(item)
            
    
    return final_suffixs 




def get_file_extention(text):
    
    result=str()

    for item in text[::-1]:
        
    
        if item == '.' or item=="\\":
    
            break
    
        result += item
    
    return(result[::-1])




    

def find_all_file_directory():
    parent_directory = os.path.dirname(__file__)
    
    dir_path = parent_directory+'\*.*'
    
    res = glob.glob(dir_path)
    
    return(res)

 
def find_all_root_directory():
    directory_list = []
    date = get_persian_date()
    rootdir = os.path.dirname(__file__)
    rootdir += "\\" + date
    
    for file in os.listdir(rootdir):
    
        d = os.path.join(rootdir, file)
    
        if os.path.isdir(d):
    
            directory_list.append(d) 
    
    return directory_list
        
def move_files():
     source_list = find_all_file_directory()
     destination_list = find_all_root_directory()
     date = get_persian_date()
     
     
     for source in source_list:
     
        for destination in destination_list:
     
            if get_file_extention(source) == get_file_extention(destination):
     
                 shutil.move(source,destination)
    
    

create_folder()

move_files()

