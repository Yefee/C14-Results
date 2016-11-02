from quickImpt import *




def plotsurf(dset,var,case):
	fig = plt.figure(figsize=(8,5))
	ax = fig.add_subplot(1,1,1)
	dset[var].mean(dim='time').plot(ax=ax)
	plt.savefig('plots/'+case+var+'.pdf')
	
case = ['PI', 'LGM']
var2d = ['ABIO_ALK_SURF','ABIO_CO2STAR','ABIO_CO2_ATM_PRESS','ABIO_CO2_IFRAC','ABIO_CO2_PV','ABIO_CO2_SCHMIDT','ABIO_CO2_XKW','ABIO_D14Catm','ABIO_DCO2STAR','ABIO_DIC14_SURF','ABIO_DIC_SURF','ABIO_DpCO2','ABIO_pCO2','ABIO_pCO2SURF','FG_ABIO_DIC','FG_ABIO_DIC14','FvICE_ABIO_DIC','FvICE_ABIO_DIC14','FvPER_ABIO_DIC','FvPER_ABIO_DIC14']

var3d = ['ABIO_D14Cocn','ABIO_DIC','ABIO_DIC14']


for cs in case:
	ds = xr.open_dataset('c14_coupling_'+cs+'.nc', decode_times=False)
	for var in var2d:
		plotsurf(ds,var,case):
	
	
