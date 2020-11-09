import numpy as np
import matplotlib.pyplot as plt



def g_tau(tau, par):  # ZARC1..par ---r,tau,n par = np.array( [rs, r1, tau1, n1, r2, tau2, n2,...] )

    x = (par[1::3] / (2* np.pi * tau)) * (np.sin((1- par[3::3]) * np.pi)) / (np.cosh(par[3::3]*np.log(tau/par[2::3])) - np.cos((1-par[3::3]) * np.pi))

    return x.sum(axis=1)




tau = np.logspace(-6,2,72).reshape(-1,1)


par_1 = np.array([0,
                  50, 0.01,  0.7
                    ])                        # ne treba reshape jer njih ostavim u redu jer je tau u stupcu
par_2 = np.array([0,
                  50, 0.01,  0.7,
                  50, 0.001, 0.7
                    ])

g_tau1 = g_tau(tau, par_1).reshape(-1,1)

g_tau2 = g_tau(tau, par_2).reshape(-1,1)


# ZARC1 podaci
plt.figure()
plt.plot(np.log10(tau), tau*g_tau1, 'o-')
plt.xlabel('log(τ/s)')
plt.ylabel('τg(τ) / $\Omega$')
plt.title('ZARC1')

# ZARC2 podaci
plt.figure()
plt.plot(np.log10(tau), tau*g_tau2,'o-')
plt.xlabel('log(τ/s)')
plt.ylabel('τg(τ) / $\Omega$')
plt.title('ZARC2')

plt.show()
