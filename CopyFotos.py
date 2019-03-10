import os
import sys
import getopt
from datetime import datetime
import pandas as pd
import collections
from shutil import copyfile


def main(argv):
    source = ''
    stNewPath = ''
    stOriginalPath = ''
    try:
        opts, args = getopt.getopt(argv, "hs:i:o:", ["source=", "ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -s <fuente> -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -s <source> -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-s", "--source"):
            source = arg
        elif opt in ("-i", "--ifile"):
            stOriginalPath = arg
        elif opt in ("-o", "--ofile"):
            stNewPath = arg
    df = pd.read_csv('C:/Users/al_be/OneDrive/Documentos/Fotos/UltimaCopia.tsv', sep='\t')
    # list(df)

    # Filtro = 'Telefono == \'' + source + '\''
    filtered_df = df.loc[df['Telefono'] == source]
    if len(filtered_df)>0:
        filtered_df = filtered_df.sort_values(by=['Fecha'], ascending=False)
        dtFecha = filtered_df['Fecha'].iloc[0]
    else:
        dtFecha = '1990/01/01'

    # stOriginalPath = "C:/Users/al_be/OneDrive/Fotos/FondoEscritorio/"
    # stNewPath = "c:/temp/Fotos"
    timelastreaded = datetime.strptime(dtFecha, '%Y/%m/%d')

    files = os.scandir(stOriginalPath)

    by_date = collections.defaultdict(list)

    for f in files:
        if f.name.endswith(".jpg"):
            if f.stat().st_mtime > timelastreaded.timestamp():
                print(f.name)
                print(f.path)
                print(datetime.fromtimestamp(f.stat().st_mtime))
                t = os.path.getmtime(f)
                mod_time = datetime.fromtimestamp(t)
                mod_date = mod_time.date().strftime('%Y%m%d')
                by_date[mod_date].append(f)
                # copyfile(f.path, stNewPath + "/" + f.name)

    for fecha, files in by_date.items():
        stPath = stNewPath + "/" + fecha
        if not os.path.isdir(stPath):
            os.mkdir(stPath)
        for file in files:
            copyfile(file.path, stPath + "/" + file.name)

    files = [f.path for f in os.scandir(stOriginalPath) if
             not (not f.name.endswith(".jpg") or not (f.stat().st_mtime > timelastreaded.timestamp()))]
    print(len(files))

    row = [source, datetime.today().strftime('%Y/%m/%d')]
    df.loc[len(df)] = row
    df.to_csv('C:/Users/al_be/OneDrive/Documentos/Fotos/UltimaCopia.tsv', sep='\t', index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
