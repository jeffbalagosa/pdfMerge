from PyPDF2 import PdfMerger
import os

input_folder = 'input'
output_file_name = '0_merged_output.pdf'

# merge all pdf files in the /input folder
merger = PdfMerger()
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        merger.append(f'{input_folder}/' + filename)

merger.write(f'output/{output_file_name}')
merger.close()
