from quickImpt import *

ds = xr.open_dataset('d14cabio.nc',decode_times=False)

aved14c = [ds.D14Cabio.isel(time=t,lev=-1).mean() for t in np.arange(0,len(ds.time),1)]
aved14c = xr.concat(aved14c, 'time')
aved14c['time'] = aved14c.time/365
fig = plt.figure(figsize=(8,4.5))
ax = fig.add_subplot(1,1,1)

aved14c.plot(ax=ax)

plt.title('surface d14c variation')
plt.xlabel('year')

ds2 = xr.open_dataset('d14cocn.nc',decode_times=False)
aved14cocn = [ds2.ABIO_D14Cocn.isel(time=t,z_t=0).mean() for t in np.arange(0, len(ds2.time), 1)]
aved14cocn = xr.concat(aved14cocn, 'time')
aved14cocn['time'] = (aved14cocn.time - 365)/365
aved14cocn.plot(ax=ax,color='r')

plt.savefig('d14c-variation.pdf')
