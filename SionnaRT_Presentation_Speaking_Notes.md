# Presentation speaking notes

1. Introduce the team, guides, and project: investigating Sionna RT as a foundation for ray-traced ISAC sensing.
2. Explain that received signals arrive over multiple paths, and the environment changes those paths.
3. Define ISAC briefly. State that this project completes ray tracing and channel analysis; it does not yet implement sensing.
4. Walk through the notebook pipeline, from loading the scene to exporting data and figures.
5. Point out the buildings, the fixed transmitter, receiver route, colored paths, and radio-map overlay.
6. Describe the main simulation parameters and mention that the balanced profile is an exploratory run.
7. Explain direct, reflected, transmitted, diffracted, and mixed paths. Zero scattering coefficients explain the lack of diffuse records.
8. Explain the simplified code: load the scene, update receiver position and velocity, trace paths, and extract channel responses.
9. Describe the 1.183-km route and 61 snapshots. The radio map is at a different height and is a different output from the point RSS.
10. Explain that coherent power sums complex paths first, so phase matters; incoherent power sums the individual powers.
11. Identify the strongest and weakest snapshots and explain the difference between the two power curves. Shading marks sampled NLoS positions.
12. Show the LoS and NLoS renderings. A blocked direct path does not mean all propagation paths disappear or that service necessarily fails.
13. Explain the count of 4,826 path records and how a path's delay and power can be inspected. Path counts do not equal power percentages.
14. Explain delay spread as the dispersion of path arrival delays, and Doppler spread as dispersion of path frequency shifts. Mention the velocity approximation near turns.
15. Describe the exported per-path data, snapshot summaries, numerical arrays, configuration, plots, and animation.
16. Discuss possible sensing uses, then stress that one-way path delays cannot automatically be interpreted as monostatic target ranges.
17. Acknowledge uncalibrated materials, a static scene, and no field validation. Suggest convergence tests followed by a target, waveform, estimator, and validation.
18. Conclude that the project has established the ray-tracing pipeline and its interpretable outputs, which can support future ISAC research.
