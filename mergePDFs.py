# Import the modules you need
from PyPDF2 import PdfFileMerger
from os import listdir

# Set input directory to where you have the files saved. Remember to use '/' not '\'
 input_dir = "C:/GLO/someCores/McFaddinDocs/McFaddinDocs/"

# Initialize count variable at 1
count = 1

# While count is less than or equal to 31 the loop will run. 
while count <= 31:

    # declares empty list after count is incremented
    merge_list = []
    # For each file in the directory
    for x in listdir(input_dir):
        if count < 10:
            if x.startswith('15-0' + str(count)):
                merge_list.append(input_dir + x)
        else:
            if x.startswith('15-' + str(count)):
                merge_list.append(input_dir + x)


    # Merges pdf's using the pyPDF2 module
    merger = PdfFileMerger()

    for pdf in merge_list:
        merger.append(pdf)
    if count < 10:
        merger.write(f"C:/GLO/someCores/McFaddinDocs/Merged/JCVC-15-0{str(count)}.pdf")
    else: 
        merger.write(f"C:/GLO/someCores/McFaddinDocs/Merged/JCVC-15-{str(count)}.pdf")
    merger.close()
    count += 1