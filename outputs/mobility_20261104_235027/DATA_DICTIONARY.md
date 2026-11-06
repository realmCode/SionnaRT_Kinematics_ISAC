# Mobility Channel Study — Data Dictionary

## Files
- `path_data.csv`: one row for each valid path at each trajectory snapshot.
- `snapshot_summary.csv`: aggregate channel and kinematic metrics for each snapshot.
- `channel_arrays.npz`: padded raw numerical tensors. Use the `valid` mask before analysis.
- `run_config.json`: complete run configuration, versions, assumptions, and material audit.

## Important definitions
- `path_gain_linear = |a_i|^2`; `path_gain_db = 10 log10(path_gain_linear)`.
- `path_loss_db = -path_gain_db`.
- `received_power_w = transmit_power_w * path_gain_linear`.
- `rss_w` uses coherent path summation: `Pt * |sum_i a_i|^2`.
- `incoherent_rss_w` uses `Pt * sum_i |a_i|^2` and excludes inter-path interference.
- Delay spread and Doppler spread are power-weighted RMS values.
- `category=mixed` means a path contains more than one propagation-interaction type.
- Vertices, object IDs, primitive IDs, and interactions are indexed by path depth.

## Physical limitations
Results depend on mesh accuracy and radio-material calibration. Refraction uses Sionna RT's thin-slab model. Diffraction is first-order. Diffuse scattering requires nonzero calibrated scattering coefficients. Atmospheric, vegetation, vehicle, and hardware losses are absent unless explicitly modeled.
