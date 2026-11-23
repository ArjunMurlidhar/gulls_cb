# Primary-lens-only rates. Drop lens rows with ID != primary_ID (binary
# companions; Is_Binary == 2 in the Huston catalogs). Singles and primaries
# have ID == primary_ID and are kept. Sources are not filtered, including
# dark sources (R062 >= 99 stays in the sum).

import pandas as pd
import numpy as np
import sys

if len(sys.argv)!=5:
    print("Usage: %s <source_file> <source_solid_angle> <lens_file> <lens_solid_angle>\n" % (sys.argv[0]))
    sys.exit()


source_data = pd.read_csv(sys.argv[1],sep='\s+',usecols=['Dist','mul','mub']).sort_values('Dist',kind='mergesort')
source_area = float(sys.argv[2])
lens_columns = ['Dist','mul','mub','Mass','ID','primary_ID']
try:
    lens_data = pd.read_csv(sys.argv[3],sep='\s+',usecols=lens_columns)
except ValueError as exc:
    sys.exit("calc_rate_primary_lens.py: lens catalog must include %s (%s)" % (", ".join(lens_columns), exc))
lens_id = pd.to_numeric(lens_data['ID'], errors='coerce')
primary_id = pd.to_numeric(lens_data['primary_ID'], errors='coerce')
# Huston catalogs: Is_Binary 0 single, 1 primary, 2 companion. A single or
# primary has ID == primary_ID. Companions do not, and leave the rate sum.
keep = lens_id.notna() & primary_id.notna() & (lens_id == primary_id)
n_drop = int((~keep).sum())
if n_drop:
    sys.stderr.write(
        "calc_rate_primary_lens.py: dropped %d lens row(s) with ID != primary_ID; %d kept\n"
        % (n_drop, int(keep.sum()))
    )
lens_data = lens_data.loc[keep].sort_values('Dist',kind='mergesort')
lens_area = float(sys.argv[4])
map_spacing = 0.2 #Steps between the map tiles in deg

#print(source_data.shape)
#print(lens_data.shape)
#print(lens_data.columns.to_string())

#constants
rEsun = 2.85412
#multiply by this factor to convert from mas yr-1 to km s-1 / kpc
mAUYRSEC = 1.495978707e8 / (365.25 * 86400.0)

l_D = lens_data['Dist'].to_numpy()
l_mul = lens_data['mul'].to_numpy()
l_mub = lens_data['mub'].to_numpy()
l_M = lens_data['Mass'].to_numpy()
nlens = l_D.shape[0]


s_D = source_data['Dist'].to_numpy()
s_mul = source_data['mul'].to_numpy()
s_mub = source_data['mub'].to_numpy()
nsource = s_D.shape[0]

if nsource == 0 or nlens == 0:
    sys.exit("calc_rate_primary_lens.py: no usable stars (nsource=%d, nlens=%d)" % (nsource, nlens))

lidx = np.searchsorted(l_D,s_D,side='left')
#print(lidx)


tau = 0 #Optical depth
tEmean = 0 #Mean timescale
murelmean = 0 #Mean relative proper motion
sumtE = 0 #Mean timecale normalization
wsum = 0 #Sum of event rate weights

tauD = np.zeros(shape=s_D.shape)

for s in range(nsource):

    #Handle the case of the source being closer than the lens
    if lidx[s]==0:
        continue
    
    Ds = s_D[s]
    muls = s_mul[s]
    mubs = s_mub[s]

    x = l_D[:lidx[s]]/Ds
    rE = (rEsun*np.sqrt(Ds)) * np.sqrt(l_M[:lidx[s]] * (1-x) * x)
    thE = rE/l_D[:lidx[s]]
    murel = np.sqrt((l_mul[:lidx[s]]-muls)**2+(l_mub[:lidx[s]]-mubs)**2)
    w = 2 * thE * murel

    tauD[s] = np.sum(thE**2) * np.pi / (1000**2 * lens_area*3600**2)
    tau += tauD[s]
    wsum += np.sum(w)
    # drawsl also rejects a pair with identical proper motion. Those pairs
    # have zero weight, but 0 * (theta_E / mu_rel) is NaN and would wipe tEmean.
    moving = murel > 0
    if np.any(moving):
        tE = 365.25 * thE[moving]/murel[moving]
        tEmean += np.sum(w[moving]*tE)
        murelmean += np.sum(w[moving]*murel[moving])


#Unit conversions and constant multipliers
#tau = Sum pi thE^2/lens area averaged over sources. thE in mas, lens_area in sq deg
tau /= nsource 
if wsum == 0:
    tEmean = float('nan')
    murelmean = float('nan')
else:
    tEmean /= wsum
    murelmean /= wsum

nevents_per_tile = wsum * 1.0e-6 / (lens_area*3600**2) * (map_spacing**2/source_area)
nevents_per_source = nevents_per_tile / (map_spacing**2*nsource/source_area)
nevents_per_deg2 = nevents_per_tile/map_spacing**2
source_density = nsource/(source_area * 3600) #in arcmin**2

#print("nsource","source_area","nlens","lens_area","tau","tEmean","murelmean","nevents_per_tile","nevents_per_source","nevents_per_deg2","source_density")
print(nsource,source_area,nlens,lens_area,tau,tEmean,murelmean,nevents_per_tile,nevents_per_source,nevents_per_deg2,source_density)
kpcidx = np.searchsorted(s_D,np.arange(1,16,2))
#print(s_D[kpcidx])
#print(tauD[kpcidx])
    
    

    
    
