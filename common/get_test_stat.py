def get_stat(stat: list) -> int:
    if stat is None:
        return 0
    if isinstance(stat, int):
        return stat
    res = len([s for s in stat if s.when == "call"])
    return res