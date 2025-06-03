import pandas as pd
import warnings
import os

# DtypeWarning in eine Exception umwandeln
warnings.simplefilter('error', pd.errors.DtypeWarning)

def find_problem_csvs(folder_path):
    problematic_files = []
    
    for filename in os.listdir(folder_path):
        if not filename.endswith('.csv'):
            continue
            
        filepath = os.path.join(folder_path, filename)
        try:
            # Wichtig: low_memory=True (Standard) beibehalten
            pd.read_csv(filepath, low_memory=True)
        except pd.errors.DtypeWarning as e:
            problematic_files.append(filename)
        except Exception:
            # Andere Fehler ignorieren
            pass
            
    return problematic_files

# Verwendung:
problem_files = find_problem_csvs('data')
print("Problematische Dateien:", problem_files)


