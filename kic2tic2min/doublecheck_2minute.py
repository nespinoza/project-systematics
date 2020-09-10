from pylab import *
from astroquery.mast import Observations
import pandas as pd

tic,kic = np.loadtxt('2min_tics_kics.txt',unpack=True)
fout = open('2min_tics_kicsFINAL.txt','w')
fout.write('#TICID     KICID\n')
for i in range(3314,len(tic)):
    print(i,tic[i])
    TICID = int(tic[i])
    obs_table = Observations.query_object('TIC'+str(TICID),radius='.02 deg')
    ok = False
    for j in range(len(obs_table['dataURL'])):
        if 's_lc.fits' in obs_table['dataURL'][j]:
            v = obs_table['dataURL'][j].split('-')
            if int(v[-3]) == int(tic[i]):
                ok = True
    if ok:
        fout.write('{0:} {1:}\n'.format(int(tic[i]),int(kic[i])))
#fout = open('2min_tics_kics.txt','w')
#fout.write('#TICID     KICID\n')
#for i in range(len(tmin_tics)):
#    fout.write('{0:} {1:}\n'.format(tmin_tics[i],tmin_kics[i]))
#fout.close()
