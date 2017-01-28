arfcnreference
---------------

.. image:: https://travis-ci.org/sitch-io/arfcn-reference.svg?branch=master
    :target: https://travis-ci.org/sitch-io/arfcn-reference
.. image:: https://codeclimate.com/github/sitch-io/arfcn-reference/badges/coverage.svg
    :target: https://codeclimate.com/github/sitch-io/arfcn-reference/coverage
    :alt: Test Coverage
.. image:: https://codeclimate.com/github/sitch-io/arfcn-reference/badges/gpa.svg
   :target: https://codeclimate.com/github/sitch-io/arfcn-reference
   :alt: Code Climate
.. image:: https://codeclimate.com/github/sitch-io/arfcn-reference/badges/issue_count.svg
   :target: https://codeclimate.com/github/sitch-io/arfcn-reference
   :alt: Issue Count


ARFCN reference Python module
=============================

This Python module contains a reference for all GSM channels by ARFCN.

Installation:
_____________

pip install arfcnreference

Usage:
______

Get a channel by uplink frequency:

::

    >>> import arfcnreference
    >>> arf_ref = arfcnreference.ArfcnReference()
    >>> arf_ref.get_for_uplink(890.2)
    {'band': 'GSM-900', 'downlink': 935.2, 'channel': 1}
    >>> arf_ref.get_for_downlink(887.4)
    {'band': 'EGSM-900', 'uplink': 887.4, 'channel': 1011}



Frequencies are returned in MHz.

Getting channels for a range of frequencies:

::

    >>> for x in arf_ref.arfcn_for_downlink_range(842, 942):
    ...     print x
    ...
    {'1853': {'band': 'GSM-1900', 'uplink': 1853, 'channel': 526}}
    {'1867': {'band': 'GSM-1900', 'uplink': 1867, 'channel': 596}}
    {'1855': {'band': 'GSM-1900', 'uplink': 1855, 'channel': 536}}
    {'1868': {'band': 'GSM-1900', 'uplink': 1868, 'channel': 601}}
    (and so on)


Getting all channels in a band:


::

    >>> for x in arf_ref.channels_in_band("GSM-850"):
    ...     print x
    ...
    {'downlink': 869.2, 'uplink': 824.2, 'channel': 128}
    {'downlink': 869.4, 'uplink': 824.4, 'channel': 129}
    {'downlink': 869.6, 'uplink': 824.6, 'channel': 130}
    {'downlink': 869.8, 'uplink': 824.8, 'channel': 131}
    {'downlink': 870, 'uplink': 825, 'channel': 132}
    (and so on)


Testing:
________

run `py.test` from the root of this repo.

Special thanks:
_______________

The reference information was lifted, with gratitude, from http://gnuradio.org/redmine/attachments/115/all_gsm_channels_arfcn.txt
