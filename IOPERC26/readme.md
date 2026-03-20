# Environmental Research: Climate Paper (draft)

See call: https://iopscience.iop.org/collections/ercl-250113-756

The local parent directory must be set to one's environment in most codes supplied below.

Three-panel graphs for 2015 and 2020 River Aire (graph made/placed into a subfolder "data", relative to parent directory:
- code: QuadrantandSquarelakeCode.py without GRR; set to Armley2015 or Armley2020 data
- code with GRR rating curve: QuadrantandSquarelakeGRR.py including GRR; set to Armley2015 or Armley2020 data
- Select file, e.g. (line ~48 in first code):
`selected_file = "Armley_2015"`
or
`selected_file = "Armley_2020"`
- The code with GRR rating curve: QuadrantandSquarelakeGRR.py also creates a look-up table of the GRR-rating curve stored under subfolder data in the file "hh_qqq.txt".
- Codes run as: `python3 QuadrantandSquarelakeCode.py` in relevant dirctory; and, as `python3 QuadrantandSquarelakeGRR.py` 

The cumulative distribution function and extra data for the climate-uplift for the three preiods 2015-2039, 2040, 2069 and 2070-2125 have been generated with the code CDDFup.py (graph made/placed into a subfolder "data").
- Code runs as: `python3 CDFFup.py` with nscenario set (e.g., `nscenario=3` for 2070-2125, et cetera) set for the chosen period.

The uplifts graphs are created using the codes CCL3panel.py and/or CCL3paneGRRl.py:
- code:
- code:

The cost-effectiveness graphs are made with the codes ;






