import sys

import numpy as np
import pytest

from pyaerocom.io.ebas_nasa_ames import EbasColDef, EbasFlagCol, EbasNasaAmesFile, NasaAmesHeader
from tests.fixtures.ebas import loaded_nasa_ames_example as filedata


@pytest.fixture(scope="module")
def head():
    return NasaAmesHeader


def test_EbasFlagCol():
    fc = EbasFlagCol(np.asarray([0, 0.66, 0.456, 0.999, 0.999100, 0.999100456]))
    assert (fc.valid == np.asarray([True, True, False, False, True, True])).all()


@pytest.mark.parametrize(
    "raw_data,decoded",
    [
        (np.asarray([0]), np.asarray([[0, 0, 0]])),
        (np.asarray([0.10045666]), np.asarray([[100, 456, 660]])),
        (np.asarray([0.10045666, 0]), np.asarray([[100, 456, 660], [0, 0, 0]])),
        (np.asarray([0.10045666, 0.12]), np.asarray([[100, 456, 660], [120, 0, 0]])),
        (np.asarray([0.10045666, 0.1234]), np.asarray([[100, 456, 660], [123, 400, 0]])),
    ],
)
def test_EbasFlagCol_decoded(raw_data, decoded):
    fc = EbasFlagCol(raw_data, False)
    assert fc._decoded is None
    dc = fc.decoded
    assert fc._decoded is dc
    assert decoded.ndim == 2
    assert (dc == decoded).all()


def test_NasaAmesHeader_NUM_FIXLINES(head):
    assert head._NUM_FIXLINES == 13


def test_NasaAmesHeader_CONV_STR(head):
    assert head.CONV_STR("bla ") == "bla"


def test_NasaAmesHeader_CONV_PI(head):
    assert head.CONV_PI("bla;blub") == "bla; blub"


def test_EbasNasaAmesFile_instance(filedata):
    assert isinstance(filedata, NasaAmesHeader)
    assert isinstance(filedata, EbasNasaAmesFile)


def test_EbasNasaAmesFile_head_fix(filedata):
    HEAD_FIX = dict(
        num_head_lines=93,
        num_head_fmt=1001,
        data_originator="Brem, Benjamin; Baltensperger, Urs",
        sponsor_organisation="CH02L, Paul Scherrer Institut, PSI, Laboratory of Atmospheric Chemistry (LAC), OFLB, , 5232, Villigen PSI, Switzerland",
        submitter="Brem, Benjamin",
        project_association="ACTRIS CREATE EMEP GAW-WDCA",
        vol_num=1,
        vol_totnum=1,
        ref_date=np.datetime64("2019-01-01T00:00:00"),
        revision_date=np.datetime64("2021-05-28T00:00:00"),
        freq=0.041667,
        descr_time_unit="days from file reference point",
        num_cols_dependent=23,
        mul_factors=[1.0] * 23,
        vals_invalid=[999.999999, 9999.99, 999.99, 9999.99]
        + [99.99999999] * 9
        + [999.99999999] * 9
        + [9.999999],
        descr_first_col="end_time of measurement, days from the file reference point",
    )
    assert isinstance(filedata.head_fix, dict)
    assert filedata.head_fix == HEAD_FIX


def test_EbasNasaAmesFile_head_fix_error(filedata):
    with pytest.raises(AttributeError) as e:
        filedata.head_fix = "Blaaaaaaaaaaaaaaa"
    if sys.version_info < (3, 11):
        assert str(e.value).startswith("can't set attribute")
    else:
        assert str(e.value).endswith("object has no setter")


def test_EbasNasaAmesFile_data(filedata):
    assert isinstance(filedata.data, np.ndarray)
    assert filedata.data.ndim == 2


def test_EbasNasaAmesFile_shape(filedata):
    assert filedata.shape == (8760, 24)


def test_EbasNasaAmesFile_col_num(filedata):
    assert filedata.col_num == 24


def test_EbasNasaAmesFile_col_names(filedata):
    COLUMN_NAMES = (
        ["starttime", "endtime", "pressure", "relative_humidity", "temperature"]
        + ["aerosol_light_backscattering_coefficient"] * 9
        + ["aerosol_light_scattering_coefficient"] * 9
        + ["numflag"]
    )
    assert filedata.col_names == COLUMN_NAMES


def test_EbasNasaAmesFile_get_time_gaps_meas(filedata):
    gaps = filedata.get_time_gaps_meas()
    assert len(gaps) == 8759
    assert np.unique(gaps).sum() == 0


def test_EbasNasaAmesFile_get_dt_meas(filedata):
    dt = filedata.get_dt_meas()
    assert len(dt) == 8759
    assert list(np.unique(dt)) == [3599.0, 3600.0, 3601.0]


@pytest.mark.parametrize("update", [{"bla": 42}, {"vol_num": 42}])
def test_EbasNasaAmesFile_update(filedata: EbasNasaAmesFile, update: dict):
    data = EbasNasaAmesFile(filedata.file)
    data.update(**update)
    for key, val in update.items():
        if key in filedata._head_fix:
            assert data._head_fix[key] == val
        else:
            assert data._meta[key] == val


def test_EbasNasaAmesFile___str__(filedata):
    assert isinstance(filedata.__str__(), str)


@pytest.mark.parametrize(
    "colnum,value",
    [
        (5, 450),
        (8, 550),
    ],
)
def test_EbasColDef_get_wavelength_nm(filedata, colnum, value):
    coldef = filedata.var_defs[colnum]
    assert isinstance(coldef, EbasColDef)
    assert coldef.get_wavelength_nm() == value


def test_EbasColDef_get_wavelength_nm_error(filedata):
    with pytest.raises(KeyError) as e:
        filedata.var_defs[0].get_wavelength_nm()
    assert str(e.value) == "'Column variable starttime does not contain wavelength information'"
