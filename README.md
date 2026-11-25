<h1 align="center">Split MEG file [ctf]</h1>

<p align="center">
  Splits a CTF MEG recording into two time segments (for example test and retest) with MNE-Python and saves each as a .fif file.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.536"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.536-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Splits a CTF MEG recording into two time segments (for example test and retest) with MNE-Python and saves each as a .fif file.**

Reads the CTF .ds recording with mne.io.read_raw_ctf and saves two cropped copies: t1min-t1max to the test output and t2min-t2max to the retest output. Use it to cut one recording into two parts for test-retest analyses.

| | |
|---|---|
| **Inputs** | `neuro/meg/ctf` |
| **Outputs** | `neuro/meg/fif` ×2 |
| **Container** | `brainlife/mne:0.23dev` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.536](https://doi.org/10.25663/brainlife.app.536) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif file` | `neuro/meg/ctf` | yes | CTF MEG recording (.ds) with BIDS sidecars. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir1` | `neuro/meg/fif` | First segment (t1min to t1max) as meg.fif. |
| `out_dir2` | `neuro/meg/fif` | Second segment (t2min to t2max) as meg.fif. |

<details>
<summary><b>Parameters</b> (4)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `t1min` | number | `0` | Start time of the first segment. (s) |
| `t1max` | string |  | End time of the first segment. (s) |
| `t2min` | number |  | Start time of the second segment. (s) |
| `t2max` | number |  | End time of the second segment. (s) |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.536](https://doi.org/10.25663/brainlife.app.536), choose `neuro/meg/ctf` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meg/fif`, `neuro/meg/fif`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:0.23dev`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "ds": "/path/to/fif file/ds",
       "headshape": "/path/to/fif file/headshape",
       "channels": "/path/to/fif file/channels",
       "coordsystem": "/path/to/fif file/coordsystem",
       "events": "/path/to/fif file/events",
       "events_json": "/path/to/fif file/events_json",
       "t1min": 0,
       "t1max": "",
       "t2min": "<number>",
       "t2max": "<number>"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Split MEG file [ctf]. brainlife.io App. [doi:10.25663/brainlife.app.536](https://doi.org/10.25663/brainlife.app.536)
- Gramfort et al. MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience* 7 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Guiomar Niso

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
