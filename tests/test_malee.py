from malee import *
import pytest
from pytest import approx


class TestMalee:
    @pytest.fixture
    def numbers(self):
        """All of the values necessary for tests"""
        vi, vf, t, i, y, i0, pe = 100, 140, 1, 0.05, 2, 40000, 1000
        Rt, Rtw = 1030, 0.3662
        Rn = [5000, 8000, 12000, 30000]
        rors = [0.1, -0.05, 0.07]  # rate of returns
        return {
            "vi": vi,
            "vf": vf,
            "t": t,
            "i": i,
            "y": y,
            "i0": i0,
            "pe": pe,
            "Rt": Rt,
            "rors": rors,
            "Rtw": Rtw,
            "Rn": Rn,
        }

    @pytest.mark.ror
    def test_ar(self, numbers):
        """Tests the functionality of `ar` function"""
        assert ar(numbers["vi"], numbers["vf"]) == approx(0.4), "Incorrect Result!"

    @pytest.mark.ror
    def test_lr(self, numbers):
        """Tests the functionality of `lr` function"""
        assert lr(numbers["vi"], numbers["vf"], numbers["t"]) == approx(
            0.3364722366212129
        ), "Incorrect Result!"

    @pytest.mark.ror
    def test_aar(self, numbers):
        """Tests the functionality of `aar` function"""
        assert aar(numbers["rors"]) == approx(0.04), "Incorrect Result!"

    @pytest.mark.ror
    def test_twr(self, numbers):
        """Tests the functionality of `twr` function"""
        assert twr(numbers["rors"]) == approx(0.11814999999999998), "Incorrect Result!"

    @pytest.mark.ror
    def test_an(self, numbers):
        """Tests the functionality of `an` function"""
        assert an(numbers["Rtw"], numbers["y"]) == approx(
            0.1688455843266894
        ), "Incorrect Result!"

    @pytest.mark.pv
    def test_pv(self, numbers):
        """Tests the functionality of `pv` function"""
        assert pv(numbers["Rt"], numbers["i"], numbers["t"]) == approx(
            980.952380952381
        ), "Incorrect Result!"

    @pytest.mark.pv
    def test_npv(self, numbers):
        """Tests the functionality of `npv` function"""
        assert npv(numbers["Rn"], numbers["i"], numbers["i0"]) == approx(
            7065.266015703324
        ), "Incorrect Result!"
        assert npv(numbers["Rn"], numbers["i"], numbers["i0"], numbers["pe"]) == approx(
            13206.894246738753
        ), "Incorrect Result!"

    @pytest.mark.mean
    def test_gm(self, numbers):
        """Tests the functionality of `gm` function"""
        assert gm(numbers["rors"]) == approx(0.03792671274950532), "Incorrect Result!"
