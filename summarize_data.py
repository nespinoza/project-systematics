import lightkurve as lk
import numpy as np
import pandas as pd


cat = pd.read_csv(
    'tics_kics_mcq_rot.txt',
    names=['tic_id', 'kic_id', 'prot'],
    delim_whitespace=True
)

n_quarters = []
kepler_long = []
kepler_short = []
n_sectors = []
tess_ffi = []
tess_short = []

for i, row in cat.iterrows():
    kic_id = f'KIC{row.kic_id:.0f}'
    tic_id = f'TIC{row.tic_id:.0f}'
    print(i, kic_id, tic_id)

    # Searches
    sr_keplerlong = lk.search_targetpixelfile(
        kic_id, mission='Kepler', cadence='long'
    )
    sr_keplershort = lk.search_targetpixelfile(
        kic_id, mission='Kepler', cadence='short'
    )
    sr_tessffi = lk.search_tesscut(tic_id)
    sr_tessshort = lk.search_targetpixelfile(tic_id, mission='TESS')
    if len(sr_tessshort):
        # (Having some trouble with TIC IDs)
        idx_good = np.where(sr_tessshort.target_name == str(row.tic_id))
        sr_tessshort = sr_tessshort[idx_good]

    # Record results
    n_quarters.append(len(sr_keplerlong))
    kepler_long.append(bool(len(sr_keplerlong)))
    kepler_short.append(bool(len(sr_keplershort)))
    n_sectors.append(len(sr_tessffi))
    tess_ffi.append(bool(len(sr_tessffi)))
    tess_short.append(bool(len(sr_tessshort)))

df = pd.DataFrame({
    'kic_id': cat.kic_id,
    'tic_id': cat.tic_id,
    'n_quarters': n_quarters,
    'kepler_long': kepler_long,
    'kepler_short': kepler_short,
    'n_sectors': n_sectors,
    'tess_ffi': tess_ffi,
    'tess_short': tess_short
})
df.to_csv('data_summary.csv', index=False)
