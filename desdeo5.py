from scipy.optimize import minimize,rosen, rosen_der
import numpy as np
newt_stats = {'fun':[], 'x':[], 'nfev':[]}
bfgs_stats = {'fun':[], 'x':[], 'nfev':[]}
for _ in range(100):
    x0 = np.random.uniform(low=1, high=10, size=10) # Random starting point from typical range of [-5, 10]
    res_newt = minimize(rosen, x0, options={'disp':False}, jac=rosen_der, method='Newton-CG')
    res_bfgs = minimize(rosen, x0, options={'disp':False}, jac=rosen_der, method='BFGS')

    newt_stats['fun'].append(res_newt.fun)
    newt_stats['x'].append(res_newt.x)
    newt_stats['nfev'].append(res_newt.nfev)

    bfgs_stats['fun'].append(res_bfgs.fun)
    bfgs_stats['x'].append(res_bfgs.x)
    bfgs_stats['nfev'].append(res_bfgs.nfev)

print("Result for Newton-CG:")
print("Mean error: " +str(res_newt.fun))
print("x: " +str(res_newt.x))
print(f"Mean gradient evaluations {np.mean(newt_stats['nfev'])}, \n median gradient evaluations {np.median(newt_stats['nfev'])}, \n maximum value {np.max(newt_stats['nfev'])}, \n minimum value {np.min(newt_stats['nfev'])}")
print("\n")


print("Result for BFGS:")
print("Mean error: " +str(res_bfgs.fun))
print("x: " +str(res_bfgs.x))
print(f"Mean gradient evaluations {np.mean(bfgs_stats['nfev'])}, \n median gradient evaluations {np.median(bfgs_stats['nfev'])}, \n maximum value {np.max(bfgs_stats['nfev'])}, \n minimum value {np.min(bfgs_stats['nfev'])}")
