from matplotlib import pyplot

from pyioflash import SimulationData, SimulationPlot

# Experimental Data
x = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]
z = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]
w_S2 = [0.00, 5.20, 12.50, 13.20, 14.45, 12.80, 10.40, 7.50, 4.30, 1.30, -2.90, -5.30, -9.00, -11.70, -14.20, -14.70, -14.00, -11.60, -10.10, -3.90, 0.00]
u_S2 = [0.00, -5.50, -11.70, -12.20, -12.80, -12.65, -10.80, -8.70, -5.50, -3.20, -0.80, 2.20, 5.00, 9.00, 11.50, 13.50, 14.00, 11.50, 10.00, 3.00, 0.00]
w_S1 = [0.00, 20.00, 40.50, 40.00, 37.00, 31.50, 24.50, 19.00, 14.00, 8.50, 2.80, -3.50, -9.50, -15.50, -22.50, -31.00, -37.00, -39.50, -40.00, -19.00, 0.00]
u_S1 = [0.00, -2.50, -13.00, -14.70, -17.50, -17.20, -15.00, -12.30, -8.50, -4.30, 0.30, 4.70, 8.50, 12.00, 14.50, 17.00, 17.70, 17.50, 17.30, 8.00, 0.00]
w_S7 = [0.00, 16.00, 30.00, 28.00, 25.00, 19.00, 10.00, 5.00, 0.00, -5.00, -15.00, -25.00, -37.00, -50.00, -67.00, -86.00, -100.00, -105.00, -105.00, -50.00, 0.00]
u_S7 = [0.00, -19.00, -77.00, -78.00, -75.00, -69.00, -56.00, -42.00, -26.00, -10.00, 6.00, 22.00, 36.00, 50.00, 61.00, 68.00, 71.00, 70.00, 69.00, 33.00, 0.00]

scale = 19/0.1

#data = SimulationData.from_list([681], path='../../../amr/', header='INS_LidDr_Cavity_hdf5_plt_cnt_')
#data = SimulationData.from_list(range(5), path='../../../qual2/', header='INS_Rayleigh_Benard_hdf5_plt_cnt_')
data = SimulationData.from_list([2], path='../../../qual2/', header='INS_Rayleigh_Benard_hdf5_chk_', form='chk')


visual = SimulationPlot(data, fig_options={'title': f'Rayleigh Benard Convection'})
visual.plot(axis='x', cut=0.5, field='temp')
fig1, ax1 = visual.plot(axis='x', cut=0.5, field='fcz2', line='z', cutlines=[0.5], scale=scale)
ax1.plot(x[::-1], w_S2, '.b')
ax1.plot(x[::-1], w_S1, '.r')
ax1.plot(x[::-1], w_S7, '.g')

fig2, ax2 = visual.plot(axis='x', cut=0.5, field='fcy2', line='y', cutlines=[0.5], scale=scale)
ax2.plot(z[::-1], u_S2, '.b')
ax2.plot(z[::-1], u_S1, '.r')
ax2.plot(z[::-1], u_S7, '.g')

visual.show()


#pyplot.show()




