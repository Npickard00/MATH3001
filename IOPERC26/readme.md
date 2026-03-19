# Environmental Research: Climate Paper (draft)

See call: https://iopscience.iop.org/collections/ercl-250113-756

The local parent directory must be set to one's environment in most codes supplied below.

Three-panel graphs for 2015 and 2020 River Aire (made/placed into a subfolder "data", relative to parent directory:
- code: QuadrantandSquarelakeCode.py without GRR; set to Armley2015 or Armley2020 data
- code with GRR rating curve: QuadrantandSquarelakeGRR.py including GRR; set to Armley2015 or Armley2020 data
- Select file, e.g. (line ~48 in first code):
`selected_file = "Armley_2015"`
or
`selected_file = "Armley_2020"`

The cumulative distribution function and extra data for the climate-uplift for 2070-2125 have been generated with the code CDDFup.py (made/placed into a subfolder "data").

