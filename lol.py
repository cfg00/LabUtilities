import glob,os,numpy as np,sys
#merfish11: /mnt/merfish11/20230908_D106Luo/DNA/
#merfish10: 
fls_dapi = glob.glob(r'/mnt/merfish11/20230908_D106Luo/DNA/AnalysisDeconvolveCG/*')
#fl_targ = r'Q:\Carlos_Analysis\AnalysisDeconvolveCG'

import shutil
from tqdm import tqdm
for fl_dapi in tqdm(fls_dapi):
    #
    fl_targ = fl_dapi.replace(r'mnt/merfish11/20230908_D106Luo/DNA',r'/mnt/merfish8v1/Carlos_Analysis')
    #print(fl_targ)
    if not os.path.exists(fl_targ):
        try:
            print("transfering" +str(fl_targ))
            shutil.copy2(fl_dapi,fl_targ)
        except:
            print("some stuff going on w... "+str(fl_targ))