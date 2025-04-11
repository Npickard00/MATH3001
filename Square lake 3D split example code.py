# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 22:28:21 2025

@author: Natasha Pickard
"""


# 3D cuboids aligned like "lake depth" visualization
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D

def draw_cuboid(ax, origin, size, color='lightblue', edge='k', alpha=0.3):
    x, y, z = origin
    dx, dy, dz = size
    vertices = [
        [x, y, z],
        [x + dx, y, z],
        [x + dx, y + dy, z],
        [x, y + dy, z],
        [x, y, z + dz],
        [x + dx, y, z + dz],
        [x + dx, y + dy, z + dz],
        [x, y + dy, z + dz]
    ]
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[0], vertices[3], vertices[7], vertices[4]]
    ]
    cuboid = Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors=edge, alpha=alpha)
    ax.add_collection3d(cuboid)

# === Setup figure ===
fig = plt.figure(figsize=(14, 8))  # Larger canvas
ax = fig.add_subplot(111, projection='3d')

# Stretch the box aspect so the cubes fill the scene more naturally
ax.set_box_aspect([6, 3, 1])  # x:y:z ratio (tweak as needed)

# Remove whitespace around the plot
plt.subplots_adjust(left=0, right=0.2, top=0.2, bottom=0)

# === Define cuboid sizes ===
sizes = [
    (2, 0.1, 0.2),      # l1
    (2, 0.4, 0.2),      # l2
    (2, 0.4, 0.2),      # l3
    (2, 0.8, 0.2)       # l4
]
colors = [ 'darkgreen','forestgreen','mediumseagreen', 'lightgreen']
labels = ['l₄','l₃','l₂','l₁']

cuboids = []
y_pos = 0
gap = 0.3

# === Draw cuboids ===
for size, color in zip(sizes, colors):
    origin = (0, y_pos, 0)
    cuboids.append((origin, size, color))
    draw_cuboid(ax, origin, size, color=color)
    y_pos += size[1] + gap

# === Add labels and double-headed arrows along Y direction ===
for (origin, size, _), label in zip(cuboids, labels):
    x = (origin[0] + size[0] / 2)-1.1  # center in x
    y = origin[1] + size[1] / 2  # center in y
    z = origin[2]          # a little below the cube

    # Label centered below the arrow
    ax.text(x-0.2, y, z - 0.01, label, fontsize=20, ha='center')

    # Arrow span based on actual cube width (size[1])
    y0 = origin[1]
    y1 = origin[1] + size[1]
    arrow_z = z

    # Arrow from bottom to top
    ax.quiver(x, y0, arrow_z, 0, size[1], 0,
              color='black', arrow_length_ratio=0.1, linewidth=1)

    # Arrow from top to bottom
    ax.quiver(x, y1, arrow_z, 0, -size[1], 0,
              color='black', arrow_length_ratio=0.1, linewidth=1)
    
# === View and layout settings ===
ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 1.8)
ax.set_zlim(0, 0.4)
ax.set_axis_off()
ax.view_init(elev=10, azim=180)

plt.tight_layout()
plt.show()