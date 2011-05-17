import re

def parse_kernelversion(kernelversion):
 # Ignore KANG versions.
    if "KANG" in kernelversion:
        return None

def parse_modversion(modversion):
    # Ignore KANG versions.
    if "KANG" in modversion:
        return None

    # Determine RC Version
    match_rc = re.match(r"^SavagedZenMOD-RC(\d+)-(\d\.\d\.\d\.?\d?)-.*$", modversion)
    match_stable = re.match(r"^SavagedZenMOD-(\d\.\d\.\d\.?\d?)-.*$", modversion)
    match_nightly = re.match(r"^SavagedZenMOD-(\d)-\d{8}-Rendition-.*$", modversion)

    if match_rc:
        return "%s-RC%s" % (match_rc.group(1), match_rc.group(2))

    elif match_nightly:
        return "Nightly"

    elif match_stable:
        return match_stable.group(1)
