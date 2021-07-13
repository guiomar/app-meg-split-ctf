# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# Required libraries
# pip install mne-bids coloredlogs tqdm pandas scikit-learn json_tricks fire

# set up environment
#import mne-study-template
import os
import json
import mne
import mne_bids
import shutil

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)


fname = config['ds']
t1min = config['t1min'] # in seconds
t1max = config['t1max']
t2min = config['t2min']
t2max = config['t2max']


# Rename ds folder so internal files match
# FIND A TEMPORAL FOLDER
# mne_bids.copyfiles.copyfile_ctf(fname, 'meg.ds')
fname1 = fname[:-6]+'raw_meg.ds'
if os.path.exists(fname1):
  shutil.rmtree(fname1)
mne_bids.copyfiles.copyfile_ctf(fname, fname1)



raw = mne.io.read_raw_ctf(fname1)

# save the first seconds of MEG data in FIF file
raw.save(os.path.join('out_dir1','meg.fif'), tmin=t1min, tmax=t1max)
# save the rest in a second FIF file
raw.save(os.path.join('out_dir2','meg.fif'), tmin=t2min, tmax=t2max)

if os.path.exists(fname1):
  shutil.rmtree(fname1)