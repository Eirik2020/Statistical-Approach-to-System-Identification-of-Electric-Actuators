import numpy as np
import matplotlib.pyplot as plt

## reset defaults
plt.rcdefaults()

## Set up LaTeX fonts
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
    })

## Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots(figsize=(4.5,3))

ax.plot(t, s, linewidth=3)

ax.set(xlabel=r'time $\tau_p$ [$\mu$s]', ylabel=r'voltage (mV)')
ax.set(title=r'$ E = m c^2 $')

#fig.savefig("test600.png", format="png", dpi=600, bbox_inches="tight")
fig.savefig("test1200t.eps", format="eps", dpi=1200, bbox_inches="tight", transparent=True)
#fig.savefig("test1200t.pdf", format="pdf", dpi=1200, bbox_inches="tight", transparent=True)

plt.show()