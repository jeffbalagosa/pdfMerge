from PyPDF2 import PdfMerger
import os

input_folder = 'input'
# prompt user for output file name use _merged.pdf as default
output_file_name = input(
    'Enter output file name (_merged.pdf by default): ') or '_merged.pdf'

# merge all pdf files in the /input folder
merger = PdfMerger()
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        merger.append(f'{input_folder}/' + filename)

merger.write(f'output/{output_file_name}')
merger.close()

# ask if user wants to delete the files in the /input folder
delete_files = input('Permanently delete files in input folder? (y/n): ')
if delete_files.lower() == 'y':
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            os.remove(f'{input_folder}/' + filename)
