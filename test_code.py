import numpy as np
import matplotlib.pyplot as plt

from sionna.rt import (
    load_scene,
    Transmitter,
    Receiver,
    PlanarArray,
    PathSolver,
    RadioMapSolver,
    Camera
)


# ============================================================
# LOAD SCENE
# ============================================================

scene = load_scene("test_scene/test_scene.xml")


# ============================================================
# PRINT RADIO MATERIALS
# ============================================================

for i, obj in enumerate(scene.objects.values()):

    print(f"{obj.name}: {obj.radio_material.name}")

    if i >= 10:
        break


# ============================================================
# TRANSMITTER ARRAY
# ============================================================

scene.tx_array = PlanarArray(
    num_rows=4,
    num_cols=4,
    vertical_spacing=0.5,
    horizontal_spacing=0.5,
    pattern="tr38901",
    polarization="V"
)


# ============================================================
# RECEIVER ARRAY
# ============================================================

scene.rx_array = PlanarArray(
    num_rows=1,
    num_cols=1,
    vertical_spacing=0.5,
    horizontal_spacing=0.5,
    pattern="iso",
    polarization="V"
)


# ============================================================
# TRANSMITTER
# ============================================================

tx = Transmitter(
    name="tx",
    position=[-107, 43, 10],
    orientation=[0.0, 0.0, 0.0]
)

scene.add(tx)


# ============================================================
# RECEIVER
# ============================================================

rx = Receiver(
    name="rx",
    position=[160, -74, 2],
    orientation=[0.0, 0.0, 0.0]
)


scene.add(rx)


# ============================================================
# FREQUENCY
# ============================================================

scene.frequency = 3.5e9


# ============================================================
# RADIO MAP
# ============================================================

rm_solver = RadioMapSolver()

rm = rm_solver(
    scene,
    max_depth=5,
    samples_per_tx=1_000_000,
    cell_size=(2.0, 2.0),
    center=[0, 0, 1.5],
    size=[200, 200],
    orientation=[0, 0, 0]
)


print()
print("Radio map computed!")
print("Path gain shape:")
print(rm.path_gain.shape)


# ============================================================
# PREVIEW RADIO MAP
# ============================================================

scene.preview(
    radio_map=rm,
    rm_metric="path_gain",
    rm_db_scale=True
)


# ============================================================
# RAY TRACING
# ============================================================

path_solver = PathSolver()

paths = path_solver(
    scene,
    max_depth=5,
    los=True,
    specular_reflection=True,
    diffuse_reflection=False,
    refraction=False,
    diffraction=False
)


print()
print("Ray tracing completed.")


# ============================================================
# CONVERT PATHS TO CIR
# ============================================================

a, tau = paths.cir(
    normalize_delays=False
)


print()
print("CIR computed.")

print("Coefficient shape:")
print(a.shape)

print("Delay shape:")
print(tau.shape)


# ============================================================
# PLOT CIR
# ============================================================

a_np = a[0].numpy()
tau_np = tau.numpy()

plt.figure(figsize=(10, 5))

plt.stem(
    tau_np[0, 0, :] * 1e9,
    np.abs(a_np[0, 0, 0, 0, :, 0])
)

plt.xlabel("Delay [ns]")
plt.ylabel(r"$|a|$")
plt.title("Sionna RT Channel Impulse Response")

plt.grid(True)

plt.show()


# ============================================================
# PREVIEW RAY PATHS
# ============================================================

scene.preview(
    paths=paths,
    radio_map=rm,
    rm_metric="path_gain",
    rm_db_scale=True
)


# ============================================================
# OPTIONAL: SAVE RENDER
# ============================================================

camera = Camera(
    position=[32, -12, 2],
    look_at=[0, 0, 5]
)

scene.render_to_file(
    camera=camera,
    filename="sionna_rt_result.png",
    paths=paths,
    radio_map=rm,
    rm_metric="path_gain",
    rm_db_scale=True,
    resolution=[1600, 1000],
    num_samples=128,
    show_devices=True,
    show_orientations=False
)

print()
print("==========================================")
print("SIMULATION COMPLETE")
print("==========================================")

print("Output:")
print("sionna_rt_result.png")