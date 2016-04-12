class networkAttr(object):
    ATTR_CORE_ROWS = None
    ATTR_CORE_COLS = None
    ATTR_CORE_CORES = None
    ATTR_CORE_VCS = None

    def __init__(self, core_rows, core_cols, core_cores, core_vcs):
        networkAttr.ATTR_CORE_ROWS = int(core_rows)
        networkAttr.ATTR_CORE_COLS = int(core_cols)
        networkAttr.ATTR_CORE_CORES = int(core_cores)
        networkAttr.ATTR_CORE_VCS = int(core_vcs)
