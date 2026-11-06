# SionnaRT_Kinematics_ISAC

## Investigation of Sionna RT for Ray-Traced ISAC-Based Sensing

This project investigates how Sionna RT can model radio propagation in a 3D scene and produce interpretable channel data for a moving receiver. A fixed transmitter operates at 3.5 GHz while the receiver follows a waypoint route. At each sampled position, the notebook traces propagation paths and exports their geometry, complex coefficients, delays, Doppler shifts, angles, and interaction types.

The implemented work covers **ray tracing and channel analysis**. The results can support future integrated sensing and communication (ISAC) experiments, but the current project does not implement a sensing waveform, target detection, range–Doppler processing, or sensing accuracy evaluation.

## Project contents

| Path | Description |
| --- | --- |
| `mobility_channel_study.ipynb` | Main simulation, analysis, exports, plots, and optional animation |
| `test_scene/test_scene.xml` and `test_scene/meshes/` | Scene definition and 3D geometry |
| `outputs/mobility_20261104_235027/` | Saved run used in the report and presentation |
| `MOBILITY_CHANNEL_STUDY_DOCUMENTATION.md` | Detailed notebook workflow, data dictionaries, and limitations; its worked results refer to the older `mobility_20260918_004212` run |
| `IEEE_SionnaRT_ISAC_Report.tex` and `.pdf` | IEEE-style project report and compiled PDF |
| `SionnaRT_ISAC_Presentation.tex` and `.pdf` | Beamer presentation and compiled PDF |
| `SionnaRT_Presentation_Speaking_Notes.md` | Slide-by-slide speaking notes |
| `*_Overleaf.zip` | Self-contained report and presentation source packages |
| `test.ipynb`, `test_code.py` | Earlier single-link scene exploration |

## Setup

The saved run records Python 3.13.0, Sionna 2.1.0, and NumPy 2.4.6. The pinned packages are listed in `requirements.txt`; the simulation also requires a compatible Mitsuba/Dr.Jit backend and a Jupyter frontend. Rendering and ray tracing can be computationally demanding.

From the project root, create a virtual environment and install the dependencies. For example, in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Open `mobility_channel_study.ipynb` in a Jupyter-compatible editor and select this environment as its kernel. If your editor does not provide Jupyter and a kernel, install them in the environment:

```powershell
python -m pip install jupyterlab ipykernel
python -m ipykernel install --user --name siona-rt --display-name "Python (Sionna RT)"
jupyter lab
```

## Run the study

1. Open the main notebook from the project root so its relative paths resolve correctly.
2. In the configuration cell, select `RUN_PROFILE = "quick"`, `"balanced"`, or `"publication"`. The quick profile is useful for checking the setup first.
3. For a faster initial run, set `CREATE_SCENE_GIF = False` and, if an interactive viewer is unavailable, `OPEN_INTERACTIVE_PREVIEW = False`.
4. Run the cells in order. The configuration cell creates a timestamped directory under `outputs/`.
5. Inspect that directory's `RUN_SUMMARY.md`, `run_config.json`, and CSV files. Re-running export cells without re-running the configuration cell can overwrite files in the current run directory.

The notebook offers three profiles:

| Profile | Snapshots | Path depth | Path samples per source |
| --- | ---: | ---: | ---: |
| `quick` | 21 | 2 | 20,000 |
| `balanced` | 61 | 3 | 100,000 |
| `publication` | 181 | 5 | 1,000,000 |

A higher profile increases computation and does not by itself establish physical accuracy or solver convergence.

## Saved results

The report and slides use the **balanced** run `outputs/mobility_20261104_235027`. Its receiver follows a 1,183.45 m route over 118.35 s at a nominal 10 m/s. It contains 61 snapshots and 4,826 valid path records. Coherent received power ranges from −70.92 to −13.87 dBm. The direct line-of-sight path appears in 39 snapshots and is absent in 22; every snapshot has at least one valid traced path. These figures describe this specific simulated configuration, not field measurements or a practical service-outage test.

Each run may contain:

- `snapshot_summary.csv`: position, path count, received power, delay/Doppler spread, and other snapshot metrics.
- `path_data.csv`: one row per valid path, including coefficients, delays, Doppler, angles, and interaction data.
- `channel_arrays.npz`: padded channel arrays; use the `valid` mask when analyzing them.
- `run_config.json`, `RUN_SUMMARY.md`, and `DATA_DICTIONARY.md`: configuration, overview, and field definitions.
- `figures/`, `scene_frames/`, and a GIF: visualizations when the relevant notebook cells are enabled.

The `.gitignore` keeps the saved run used by the documents available for version control, while excluding its generated GIF and most animation frames, other run directories, and local build/cache files. Ignored files remain on disk; the notebook can regenerate them. The two frames used by the presentation are retained.

## Build the report and presentation

The LaTeX files use the saved run's figures through relative paths, so compile them from the project root. With a TeX distribution containing `IEEEtran` and Beamer:

```powershell
pdflatex IEEE_SionnaRT_ISAC_Report.tex
pdflatex IEEE_SionnaRT_ISAC_Report.tex
pdflatex SionnaRT_ISAC_Presentation.tex
pdflatex SionnaRT_ISAC_Presentation.tex
```

Alternatively, upload `IEEE_SionnaRT_ISAC_Report_Overleaf.zip` or `SionnaRT_Beamer_Overleaf.zip` to Overleaf; each archive includes its required source and figures.

## Interpretation and limitations

- The scene, materials, transmitter, and environment are static; the receiver moves between independently traced snapshots. Path indices should not be assumed to track the same physical path across snapshots.
- The ITU-style materials are not calibrated to measurements. Although diffuse reflection is enabled, the saved materials have zero scattering coefficients.
- Coherent RSS is a narrowband, reference-frequency calculation. The reported SNR uses thermal noise only and does not include interference or receiver noise figure.
- Receiver velocity is estimated from chords between sampled points. At sharp turns this can underestimate the nominal speed and affect Doppler.
- The radio map is computed at 1.5 m while the receiver is at 2 m; a map cell is not the same quantity as the snapshot's coherent RSS.
- A missing direct path does not imply service outage. The current model does not define a receiver sensitivity or SNR threshold.

## Team

- Nandish Chauhan — 202451040@iiitvadodara.ac.in
- Aahan Poddar — 202451184@iiitvadodara.ac.in

Under the guidance of Dr. Bhupendra Kumar — bhupendra_kumar@iiitvadodara.ac.in.
