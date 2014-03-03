#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This and the following exercise are using US Patent database.
# The patent.data file is a small excerpt of a much larger datafile
# that is available for download from US Patent website. They are pretty large ( >100 MB each).
# The data itself is in XML, however there is a problem with how it's formatted.
# Please run this script and observe the error. Then find the line that is causing the error.
# You can do that by just looking at the datafile in the web UI, or programmatically.
# For quiz purpose it does not matter, but as an exercise we suggest that you try to do it programmatically.
# The original file is ~600MB large, you might not be able to open it in a text editor.

import xml.etree.ElementTree as ET

PATENTS = 'patent.data'

def get_root(fname):

    tree = ET.parse(fname)
    return tree.getroot()


get_root(PATENTS)