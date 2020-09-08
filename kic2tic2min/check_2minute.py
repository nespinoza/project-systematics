from pylab import *
from astroquery.mast import Observations
import pandas as pd

objects = pd.read_csv('KIC2TIC.csv', comment='#')
tmin_tics = np.array([])
tmin_kics = np.array([])

for i in range(len(objects['TIC'])):
    print(i,'out of about 200,000')
    TICID = objects['TIC'][i]
    obs_table = Observations.query_object('TIC'+str(TICID),radius='.02 deg')
    for j in range(len(obs_table['dataURL'])):
        if 's_lc.fits' in obs_table['dataURL'][j]:
            print('TIC', objects['TIC'][i],' KIC',objects['KIC'][i],'has 2min cadence data.')
            tmin_kics = np.append(tmin_kics,objects['KIC'][i])
            tmin_tics = np.append(tmin_tics,TICID)
fout = open('2min_tics_kics.txt','w')
fout.write('#TICID     KICID\n')
for i in range(len(tmin_tics)):
    fout.write('{0:} {1:}\n'.format(tmin_tics[i],tmin_kics[i]))
fout.close()
