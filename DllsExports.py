import os
import json 
import pefile


exports_list = []

for filename in os.listdir("C:\\Windows\\System32"):
    if filename.endswith(".dll"):
        try:
            pe = pefile.PE("C:\\Windows\\System32\\" + filename)
            if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
                for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                    try:
                        exports_list.append(exp.name.decode('utf-8'))
                    except:
                        continue
        except pefile.PEFormatError:
            print(f"Error: could not process file {filename}")
            continue

exports_json = {'exports':exports_list}
open('exports.json','wt').write(json.dumps(exports_json))
