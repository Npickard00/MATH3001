# Environmental Research: Climate Paper (draft)

See call: https://iopscience.iop.org/collections/ercl-250113-756

The local parent directory must be set to one's environment in most codes supplied, and discussed below.

## Section on 2015 and 2020T floods and FEV.
Three-panel graphs for 2015 and 2020 River Aire (graph made/placed into a subfolder "data", relative to parent directory:
- code: QuadrantandSquarelakeCode.py without GRR; set to Armley2015 or Armley2020 data
- code with GRR rating curve: QuadrantandSquarelakeGRR.py including GRR; set to Armley2015 or Armley2020 data
- Select file, e.g. (line ~48 in first code):
`selected_file = "Armley_2015"`
or
`selected_file = "Armley_2020"`
- The code with GRR rating curve: QuadrantandSquarelakeGRR.py also creates a look-up table of the GRR-rating curve stored under subfolder data in the file "hh_qqq.txt".
- Codes run as: `python3 QuadrantandSquarelakeCode.py` in relevant dirctory; and, as `python3 QuadrantandSquarelakeGRR.py` 

## Section with uplift factors and its table
The cumulative distribution function and extra data for the climate-uplift for the three preiods 2015-2039, 2040, 2069 and 2070-2125 have been generated with the code CDDFup.py (graph made/placed into a subfolder "data").
- Code runs as: `python3 CDFFup.py` with nscenario set (e.g., `nscenario=3` for 2070-2125, et cetera) set for the chosen period.
- The 5th and 30th percentile values added in the Table are created by running through nscenerio=1, 2, 3.

## Section with uplifted three-panel graphs
The uplifts graphs are created using the codes CCL3panel.py and/or CCL3paneGRRl.py:
- choose input file (circa line 47), uplift factor, rating curve error, thresholds, scenario (central, higher central, upper end, at circa line 56) and river-uplift period (set year=2080, e.g., or 2030 or 2050, at circa line 52);
- code CCL3panel.py creates uplift three-panel graph without GRR curve, set figure name near bottom of file (circa line 559);
- code CCL3paneGRRl.py creates uplift three-panel graph with GRR curve and prints various outputs (set figure name near bottom of file at circa line 647);
- code CCL3paneGRRl.py creates printed output for FEV, FEVGRR, plus error bars and such;
- by playing with thresholds in code CCL3paneGRRl.py, several investigations can be made for the cost-effectiveness analyses: see indications on circa lines 66 and 70 .

## Section on respective mitigation measures and cost-effectivness
Next we select the Armley-2015 data set. For the cost-effectiveness graphs, the respective measures have to be quantified, for which two main codes are used.

For giving-room-to-the-river (GRR):
- case S0, printed output of FEV_GRR=V_{e,GRR} follows from QuadrantandSquarelakeGRR.py at ht=3.9; S0-GRR contribution then follows by subtraction as V_e-V^{(0)}_{e,GRR}
- case S1,  printed output of FEV_GRR follows from CCL3paneGRRl.py at ht=3.9; S1-GRR contribution then follows by subtraction as V_e-V^{(1)}_{e,GRR}.

For higher walls (HW), for S0:
- Threshold \hat{Q}_GRR found for S0 by hand-shooting with code QuadrantandSquarelakeGRR.py set varying ht such that remainder FEV is found. 
- Two look-up tables created, normal and GRR one, made with  QuadrantandSquarelakeGRR.py named hh_qqqrtnormal.txt and hh_qqqrtGRR.txt
- Used QuadrantandSquarelakeGRR.py by changing ht circa line 56; 14.5% is (0.66+0.7)/9.33 = 10.6%; 20.5% is (0.66+1.26)/9.33 = 20.6%

For S1 now use CCL3paneGRRl.py with ht set at 5.02.


 

The cost-effectiveness graphs are  with the codes 






