# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import tabula
from glob import glob

def process_command_line():
    parser = ArgumentParser(description="Importar dados BDF.")
    parser.add_argument("--input_folder", type=str, required=True,  help="Caminho para a pasta de entrada.")
    return parser.parse_args()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args=process_command_line()
    fnames = glob(f'{args.input_folder}\*.pdf')
    for fname in fnames:
        dfl = tabula.read_pdf(fname, pages='all', multiple_tables=False, lattice=True)
        dfl[0].to_csv(fname.replace('.pdf','.csv'))
        print(f'File {fname} converted.')


