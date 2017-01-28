import imp
import os
modulename = 'arfcnreference'
modulepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
file, pathname, description = imp.find_module(modulename, [modulepath])
arfcnreference = imp.load_module(modulename, file, pathname, description)

class TestArfcnReference:
    def instantiate_arfcn_reference(self):
        return arfcnreference.ArfcnReference()

    def test_arfcn_reference_instantiation(self):
        assert self.instantiate_arfcn_reference()

    def test_get_by_uplink(self):
        ref = self.instantiate_arfcn_reference()
        uplink_freq = 890.2
        desired_channel = 1
        result = ref.get_for_uplink(uplink_freq)
        assert result["channel"] == desired_channel

    def test_get_by_uplink_fail(self):
        ref = self.instantiate_arfcn_reference()
        uplink_freq = 9999999999999
        desired_channel = None
        result = ref.get_for_uplink(uplink_freq)
        assert result == desired_channel

    def test_get_by_downlink(self):
        ref = self.instantiate_arfcn_reference()
        downlink_freq = 887.4
        desired_channel = 1011
        result = ref.get_for_downlink(downlink_freq)
        print ref.arfcn_by_uplink
        for x in ref.arfcn_by_downlink.items():
            print x
        assert result["channel"] == desired_channel

    def test_get_by_downlink_fail(self):
        ref = self.instantiate_arfcn_reference()
        downlink_freq = 9999999999999
        desired_channel = None
        result = ref.get_for_downlink(downlink_freq)
        assert result == desired_channel

    def test_get_channels_in_band(self):
        target_band = "GSM-850"
        ref = self.instantiate_arfcn_reference()
        results_count = 124
        results = ref.channels_in_band(target_band)
        assert len(results) == results_count

    def test_get_channels_in_band_fail(self):
        target_band = "GSM-8501"
        ref = self.instantiate_arfcn_reference()
        results = ref.channels_in_band(target_band)
        assert results is None

    def test_arfcn_for_uplink_range(self):
        ref = self.instantiate_arfcn_reference()
        val_1 = 842
        val_2 = 942
        regular = ref.arfcn_for_uplink_range(val_1, val_2)
        reverse = ref.arfcn_for_uplink_range(val_1, val_2)
        assert len(regular) == len(reverse)
        assert len(reverse) == 374

    def test_arfcn_for_uplink_range_fail(self):
        ref = self.instantiate_arfcn_reference()
        val_1 = 9999999999
        val_2 = 9999999999
        regular = ref.arfcn_for_uplink_range(val_1, val_2)
        reverse = ref.arfcn_for_uplink_range(val_1, val_2)
        assert len(regular) == len(reverse)
        assert len(reverse) == 0

    def test_arfcn_for_downlink_range(self):
        ref = self.instantiate_arfcn_reference()
        val_1 = 842
        val_2 = 942
        regular = ref.arfcn_for_downlink_range(val_1, val_2)
        reverse = ref.arfcn_for_downlink_range(val_1, val_2)
        assert len(regular) == len(reverse)
        assert len(reverse) == 374

    def test_arfcn_for_downlink_range_fail(self):
        ref = self.instantiate_arfcn_reference()
        val_1 = 9999999999
        val_2 = 9999999999
        regular = ref.arfcn_for_downlink_range(val_1, val_2)
        reverse = ref.arfcn_for_downlink_range(val_1, val_2)
        assert len(regular) == len(reverse)
        assert len(reverse) == 0
