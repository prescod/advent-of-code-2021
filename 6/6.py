from typing import NamedTuple


class FishCohort(NamedTuple):
    countdown: int
    size: int

    def __repr__(self):
        return f"<{self.countdown} {self.juvenile} {self.size}>"


def advance(cohort):
    return FishCohort(cohort.countdown - 1, cohort.size)


def tick(cohorts: tuple):
    fish = tuple(advance(cohort) for cohort in cohorts)
    cohorts_in_heat = tuple(cohort for cohort in fish if (cohort.countdown == -1))
    regular_cohorts = tuple(cohort for cohort in fish if (cohort.countdown >= 0))
    num_fish_in_heat = sum(cohort.size for cohort in cohorts_in_heat)
    children = FishCohort(8, num_fish_in_heat)
    postpartum_cohorts = FishCohort(6, num_fish_in_heat)
    return (*regular_cohorts, children, postpartum_cohorts)


def eval(runtime, data):
    individuals = tuple(int(d) for d in data.strip().split(","))
    cohorts = [FishCohort(i, individuals.count(i)) for i in range(0, 6)]
    for i in range(runtime):
        cohorts = tick(cohorts)
        print(i, sum(cohort.size for cohort in cohorts))


def test():
    eval(80, "3,4,3,1,2")
    eval(256, "3,4,3,1,2")


def real():
    testdata = "4,1,1,1,5,1,3,1,5,3,4,3,3,1,3,3,1,5,3,2,4,4,3,4,1,4,2,2,1,3,5,1,1,3,2,5,1,1,4,2,5,4,3,2,5,3,3,4,5,4,3,5,4,2,5,5,2,2,2,3,5,5,4,2,1,1,5,1,4,3,2,2,1,2,1,5,3,3,3,5,1,5,4,2,2,2,1,4,2,5,2,3,3,2,3,4,4,1,4,4,3,1,1,1,1,1,4,4,5,4,2,5,1,5,4,4,5,2,3,5,4,1,4,5,2,1,1,2,5,4,5,5,1,1,1,1,1,4,5,3,1,3,4,3,3,1,5,4,2,1,4,4,4,1,1,3,1,3,5,3,1,4,5,3,5,1,1,2,2,4,4,1,4,1,3,1,1,3,1,3,3,5,4,2,1,1,2,1,2,3,3,5,4,1,1,2,1,2,5,3,1,5,4,3,1,5,2,3,4,4,3,1,1,1,2,1,1,2,1,5,4,2,2,1,4,3,1,1,1,1,3,1,5,2,4,1,3,2,3,4,3,4,2,1,2,1,2,4,2,1,5,2,2,5,5,1,1,2,3,1,1,1,3,5,1,3,5,1,3,3,2,4,5,5,3,1,4,1,5,2,4,5,5,5,2,4,2,2,5,2,4,1,3,2,1,1,4,4,1,5"
    eval(80, testdata)
    eval(256, testdata)


test()
real()
