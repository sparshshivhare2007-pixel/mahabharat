RANKS = {

    1: "warrior",
    5: "soldier",
    10: "champion",
    20: "hero",
    40: "legend",
    80: "pandava",
    100: "maharathi"
}


def get_rank(level):

    current = "warrior"

    for lvl, rank in RANKS.items():

        if level >= lvl:
            current = rank

    return current
