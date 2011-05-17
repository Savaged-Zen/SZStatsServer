from szstats.utils.string import parse_modversion


def test_parse_modversion():
    rc = parse_modversion("CyanogenMod-7.0.0-RC2-N1")
    rc_four = parse_modversion("CyanogenMod-7.0.2.3-RC3-N1")
    stable = parse_modversion("CyanogenMod-7.0.0-N1")
    stable_four = parse_modversion("CyanogenMod-7.0.2.1-Supersonic")
    nightly = parse_modversion("CyanogenMod-7-01012011-NIGHTLY-N1")
    kang1 = parse_modversion("CyanogenMod-7.0.0-RC2-N1-KANG")
    kang2 = parse_modversion("CyanogenMod-7-Negro90-V.3.1-MAGLDR")

    assert rc == "7.0.0-RC2"
    assert rc_four == "7.0.2.3-RC3"
    assert stable == "7.0.0"
    assert stable_four == "7.0.2.1"
    assert nightly == "Nightly"
    assert kang1 == None
    assert kang2 == None
