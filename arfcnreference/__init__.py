from reference_obj import reference


__author__ = "Ash Wilson"
__version__ = "0.1"

class ArfcnReference(object):
    def __init__(self):
        self.arfcn_channel = reference
        self.arfcn_by_uplink = self.build_for_uplink()
        self.arfcn_by_downlink = self.build_for_downlink()
        self.arfcn_for_band = self.build_for_band()

    def build_for_uplink(self):
        result = {}
        for channel, meta in self.arfcn_channel.items():
            result[str(meta["uplink"])] = {"channel": channel,
                                           "band": meta["band"],
                                           "downlink": meta["downlink"]}
        return result

    def build_for_downlink(self):
        result = {}
        for channel, meta in self.arfcn_channel.items():
            result[str(meta["uplink"])] = {"channel": channel,
                                           "band": meta["band"],
                                           "uplink": meta["uplink"]}
        return result

    def build_for_band(self):
        result = {}
        for arfcn, meta in self.arfcn_channel.items():
            if not meta["band"] in result:
                result[meta["band"]] = []
            result[meta["band"]].append({"channel": arfcn, "uplink": meta["uplink"],
                                         "downlink": meta["downlink"]})
        return result

    def get_for_channel(self, channel):
        """Returns all metadata for channnel"""
        try:
            retval = self.arfcn_channel[int(channel)]
        except KeyError:
            print("Unable to locate ARFCN data for channel %s" % str(channel))
            retval = None
        return retval

    def get_for_uplink(self, uplink):
        """Returns metadata for uplink freq."""
        try:
            retval = self.arfcn_by_uplink[str(uplink)]
        except KeyError:
            print("Unable to locate ARFCN data for uplink %sMHz" % str(uplink))
            retval = None
        return retval

    def get_for_downlink(self, dnlink):
        """Returns metadata for downlink freq."""
        try:
            retval = self.arfcn_by_downlink[str(dnlink)]
        except KeyError:
            print("Unable to locate ARFCN data for dnlink %sMHz" % str(dnlink))
            retval = None
        return retval

    def channels_in_band(self, band):
        """Returns a list of ARFCN metadata objects for a band."""
        try:
            retval = self.arfcn_for_band[band]
        except KeyError:
            print("Unrecognized band designation: %s" % band)
            retval = None
        return retval

    def arfcn_for_uplink_range(self, starting_mhz, ending_mhz):
        """Returns a list of ARFCNs for a range of uplink frequencies."""
        retval = []
        if float(starting_mhz) >= float(ending_mhz):
            high = float(starting_mhz)
            low = float(ending_mhz)
        else:
            low = float(starting_mhz)
            high = float(ending_mhz)
        for channel in self.arfcn_by_uplink.items():
            if low <= float(channel[0]) and float(channel[0]) >= high:
                retval.append({channel[0]: channel[1]})
        return retval

    def arfcn_for_downlink_range(self, starting_mhz, ending_mhz):
        """Returns a list of ARFCNs for a range of uplink frequencies."""
        retval = []
        if float(starting_mhz) >= float(ending_mhz):
            high = float(starting_mhz)
            low = float(ending_mhz)
        else:
            low = float(starting_mhz)
            high = float(ending_mhz)
        for channel in self.arfcn_by_downlink.items():
            if low <= float(channel[0]) and float(channel[0]) >= high:
                retval.append({channel[0]: channel[1]})
        return retval
