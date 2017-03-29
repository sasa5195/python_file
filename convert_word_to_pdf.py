from os import chdir, getcwd, listdir, path
from time import strftime
from win32com import client

def count_files(filetype):
    ''' (str) -> int
    Returns the number of files given a specified file type.
    >>> count_files(".docx")
    11
    '''
    count_files = 0
    for files in listdir(folder):
        if files.endswith(filetype):
            count_files += 1
    return count_files


def check_path(prompt):
    abs_path = raw_input(prompt)
    while path.exists(abs_path) != True:
        print "\nThe specified path does not exist.\n"
        abs_path = raw_input(prompt)
    return abs_path    
    
print "\n"

folder = check_path("Provide absolute path for the folder: ")

chdir(folder)

num_docx = count_files(".docx")
num_doc = count_files(".doc")


if num_docx + num_doc == 0:
    print "\nThe specified folder does not contain docx or docs files.\n"
    print strftime("%H:%M:%S"), "There are no files to convert. BYE, BYE!."
    exit()
else:
    print "\nNumber of doc and docx files: ", num_docx + num_doc, "\n"
    print strftime("%H:%M:%S"), "Starting to convert files ...\n"


try:
    word = client.DispatchEx("Word.Application")
    for files in listdir(getcwd()):
        if files.endswith(".docx"):
            new_name = files.replace(".docx", r".pdf")
            in_file = path.abspath(folder + "\\" + files)
            new_file = path.abspath(folder + "\\" + new_name)
            doc = word.Documents.Open(in_file)
            print strftime("%H:%M:%S"), " docx -> pdf ", path.relpath(new_file)
            doc.SaveAs(new_file, FileFormat = 17)
            doc.Close()
        if files.endswith(".doc"):
            new_name = files.replace(".doc", r".pdf")
            in_file = path.abspath(folder + "\\" + files)
            new_file = path.abspath(folder + "\\" + new_name)
            doc = word.Documents.Open(in_file)
            print strftime("%H:%M:%S"), " doc  -> pdf ", path.relpath(new_file)
            doc.SaveAs(new_file, FileFormat = 17)
            doc.Close()
except Exception, e:
    print e
finally:
    word.Quit()
