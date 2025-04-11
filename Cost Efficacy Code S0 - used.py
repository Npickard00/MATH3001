# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 19:36:35 2025

@author: Natasha Pickard
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math

# Define FEV values and mitigation contributions for both floods
#mitigation:FEV,total cost
floods = {
    "2020 Armley 2030 Upper": {
        "FEV": 3.1,  # Mm³
        "mitigations": {
            "Walls": (8.03, 75.6),
            "Calverley": (1.8, 10),
            "Rodley": (2.2, 14),
            "GRR": (0.65, 10),
            "NFM": (0.47, 4),
            "Beavers": (0.0935, 1),
            "Cononley+Holden": (4.1, 35)
        }
    },
    "2015 Armley 2030 Upper": {
        "FEV": 20.31,  # Mm³
        "mitigations": {
            "Walls": (13.24, 75.6),
            "Calverley": (1.8, 10),
            "Rodley": (2.2, 14),
            "GRR": (0.65, 10),
            "NFM": (0.47, 4),
            "Beavers": (0.0935, 1),
            "Cononley+Holden": (4.1, 35)
        }
    },
    "2020 Armley 2050 Upper": {
        "FEV": 5.16,  # Mm³
        "mitigations": {
            "Walls": (5.15353, 75.6),
            "Calverley": (1.8, 10),
            "Rodley": (2.2, 14),
            "GRR": (0.65, 10),
            "NFM": (0.47, 4),
            "Beavers": (0.0935, 1),
            "Cononley+Holden": (4.1, 35)
        }
    },
    "2015 Armley 2050 Upper": {
        "FEV": 24.49,  # Mm³
        "mitigations": {
            "Walls": (14.96, 75.6),
            "Calverley": (1.8, 10),
            "Rodley": (2.2, 14),
            "GRR": (0.65, 10),
            "NFM": (0.47, 4),
            "Beavers": (0.0935, 1),
            "Cononley+Holden": (4.1, 35)
        }
    },
    "2020 Armley 2080 Upper": {
        "FEV": 13.57,  # Mm³
        "mitigations": {
            "Walls": (12.617, 75.6),
            "Calverley": (1.8, 10),
            "Rodley": (2.2, 14),
            "GRR": (0.65, 10),
            "NFM": (0.47, 4),
            "Beavers": (0.0935, 1),
            "Cononley+Holden": (4.1, 35)
        }
    },
    "2015 Armley 2080 Upper": {
        "FEV": 38.33,  # Mm³
        "mitigations": {
            "Walls": (20, 75.6),
            "Calverley": (1.8, 10),
            "Rodley": (2.2, 14),
            "GRR": (0.65, 10),
            "NFM": (0.47, 4),
            "Beavers": (0.0935, 1),
            "Cononley+Holden": (4.1, 35)
        }
    }
}

# Enhanced version: proper axis ticks, labels, proportional layout, and title placement
def plot_square_lake_enhanced(name, fev, mitigations):
    fig, ax = plt.subplots(figsize=(8, 6))
    size = math.sqrt(fev*10**6/ 2)

    total_vol = sum(vol for vol, _ in mitigations.values())
    total_cost = sum(cost for _, cost in mitigations.values())
    total_percent = total_vol / fev * 100
    colors = plt.cm.Paired(np.linspace(0, 1, len(mitigations)))

    # Fill entire square if overcapacity
    if total_vol >= fev:
        ax.add_patch(patches.Rectangle((0, 0), size, size, color='lightblue', alpha=0.6))

    x = 0
    label_base_y = size
    label_spacing = size / (len(mitigations) + 1)

    for i, (name_m, (vol, cost)) in enumerate(mitigations.items()):
        width = vol / fev * size
        percent = vol / fev * 100
        cost_eff = cost / percent if percent != 0 else 0
        label = f"{name_m}\n{percent:.1f}%\n\u00A3{cost_eff:.1f}/%"

        if total_vol < fev:
            rect = patches.Rectangle((x, 0), width, size, color=colors[i], alpha=0.8)
            ax.add_patch(rect)

        label_y = label_base_y - (i + 1) * label_spacing
        label_x = size + 0.4
        arrow_start_x = 0 if total_vol >= fev else x
        arrow_end_x = size if total_vol >= fev else x + width
        arrow_y = label_y - 0.2

        ax.annotate('', xy=(arrow_end_x, arrow_y), xytext=(arrow_start_x, arrow_y),
                    arrowprops=dict(arrowstyle='<->', color='black'))

        ax.annotate(label,
                    xy=(label_x-(0.05*size), label_y+(0.06*size)),
                    xytext=((arrow_start_x + arrow_end_x) / 2-(0.05*size), label_y+(0.06*size)),
                    ha='left', va='center', fontsize=9)
        

        x += width
        if x >= size:
            break


    ax.set_xlim(0, size + 2)
    ax.set_ylim(0, size + 1)
    tick_interval = size / 5
    ax.set_xticks(np.arange(0, size + 0.1, tick_interval))
    ax.set_yticks(np.arange(0, size + 0.1, tick_interval))
    ax.set_xlabel("Sidelength (m)", fontsize=10)
    ax.set_ylabel("Sidelength (m)", fontsize=10)

    # Title positioned just above the centre of the square
    ax.text(size / 2, size + 0.3, f"$S_0$: FEV ≈ {size:.0f}$^2$ m$^2$ × 2m ≈ {fev:.2f}Mm$^3$",
            ha='center', va='bottom', fontsize=12)
    total_arrow_y = size + 0.05
    ax.annotate('', xy=(x, 100), xytext=(0, 100),
                arrowprops=dict(arrowstyle='<->', color='black', linewidth=1.5))
    ax.text(size / 2, 200,
            f"Total: {total_percent:.1f}% FEV mitigated, \u00A3{total_cost:.1f}M",
            ha='center', va='bottom', fontsize=10, weight='bold')

    ax.set_aspect('equal')
    ax.tick_params(axis='both', labelsize=9)
    # Bold square edges with high zorder to bring to front
    ax.plot([0, size], [0, 0], 'k-', linewidth=2, zorder=10)          # Bottom
    ax.plot([0, size], [size, size], 'k-', linewidth=2, zorder=10)    # Top
    ax.plot([0, 0], [0, size], 'k-', linewidth=2, zorder=10)          # Left
    ax.plot([size, size], [0, size], 'k-', linewidth=2, zorder=10)    # Right
    plt.tight_layout()
    plt.show()

# Render for all flood scenarios
for name, data in floods.items():
    plot_square_lake_enhanced(name, data["FEV"], data["mitigations"])
