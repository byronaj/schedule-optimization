import unittest
import re
from web_app.solver import solve_shift_scheduling

workers = 8  # workers
num_shifts = 4
weeks = 1  # weeks
stats = [[0] * (num_shifts * 2) for _ in range(workers)]
sCount = [[0] * num_shifts for _ in range(weeks * 7)]
result = [[0] * weeks * 7 for _ in range(workers)]


def set_stats(result):
    # set streak to one for all days
    for i in range(workers):
        stats[i][1] = 1
        stats[i][3] = 1
        stats[i][5] = 1
        stats[i][7] = 1
    streak = 1
    for i in range(workers):
        for j in range(weeks * 7):
            shift = result[i][j]
            if j > 0:
                previous_shift = result[i][j - 1]
            else:
                previous_shift = 'V'

            if shift == '0':
                stats[i][0] = stats[i][0] + 1
                sCount[j][0] = sCount[j][0] + 1
                if shift == previous_shift:
                    streak += 1
                    if stats[i][1] <= streak:
                        stats[i][1] = streak
                else:
                    streak = 1
            elif shift == '1':
                stats[i][2] = stats[i][2] + 1
                sCount[j][1] = sCount[j][1] + 1
                if shift == previous_shift:
                    streak += 1
                    if stats[i][3] <= streak:
                        stats[i][3] = streak
                else:
                    streak = 1
            elif shift == '2':
                stats[i][4] = stats[i][4] + 1
                sCount[j][2] = sCount[j][2] + 1
                if shift == previous_shift:
                    streak += 1
                    if stats[i][5] <= streak:
                        stats[i][5] = streak
                else:
                    streak = 1
            elif shift == '3':
                stats[i][6] = stats[i][6] + 1
                sCount[j][3] = sCount[j][3] + 1
                if shift == previous_shift:
                    streak += 1
                    if stats[i][7] <= streak:
                        stats[i][7] = streak
                else:
                    streak = 1


class test_solver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # if any constraint is changed make sure to change the associated test parameters
        # or tests will not give valid feedback
        emp_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # need same number of id's as employees
        shifts = [0, 1, 2, 3]  # shifts
        shift_constraints = [(0, 1, 1, 0, 2, 2, 0),  # off at least one day but no more than 2 in a row
                             (3, 1, 2, 20, 3, 4,
                              5)]  # third shift at one day preferably 2 days in a row but no more than 4
        weekly_sum_constraints = [(0, 1, 2, 7, 2, 3, 4),  # one or two days off but no more than 3 in a week
                                  (3, 0, 1, 3, 4, 4, 0)]  # third shift 0 two 4 times a week
        penalized_transitions = [(1, 2, 4), (2, 3, 4), (3, 1, 0)]  # penalize back to back and forbid night to morning
        # shift b2b
        weekly_cover_demands = [
            (2, 3, 1),  # Monday
            (2, 3, 1),  # Tuesday
            (2, 2, 2),  # Wednesday
            (2, 3, 1),  # Thursday
            (2, 2, 2),  # Friday
            (1, 2, 3),  # Saturday
            (1, 3, 1),  # Sunday
        ]
        resultu = solve_shift_scheduling(
            emp_ids,
            workers,
            weeks,
            shifts,
            shift_constraints,
            weekly_sum_constraints,
            penalized_transitions,
            weekly_cover_demands
        )
        for i in range(len(resultu)):
            for key in (resultu[i]):
                if key == 'shift_assignments':
                    # this gets a list of all info for each employee
                    info = str(resultu[i][key])
                    # this is regex that finds the number after the word assignment to get shift info
                    m = re.findall("'assignment': (\d+)", info)
                    num = m
                    for x in range(len(num)):
                        result[i][x] = num[x]

        set_stats(result)

    def test_shift_constraint(self):
        for i in range(workers):
            # shift 0
            # check if off day falls between 1 and 2 days in a row for each employee
            self.assertTrue(0 < stats[i][1] < 3,
                            msg='worker {0} has {1} days off in a row which is not between 1 and 2'.format(i,
                                                                                                           stats[i][1]))

            # shift 3
            # check if night shift falls between 0 and 4 days in a row for each employee
            self.assertTrue(0 <= stats[i][7] < 5,
                            msg='worker {0} has {1} days off in a row which is not between 0 and 4'.format(i,
                                                                                                           stats[i][1]))

    def test_week_constraint(self):
        for i in range(weeks * 7):
            # shift 0
            # check that each employee has between one and 3 days off each week
            self.assertTrue(0 < stats[i][0] < 4,
                            msg='worker {0} has {1} days off which is not between 1 and 4'.format(i, stats[i][0]))

            # shift 3
            # check that each employee has less than 5 night shifts a week
            self.assertTrue(0 <= stats[i][6] < 5,
                            msg='worker {0} has {1} days off which is not less than 5'.format(i, stats[i][0]))

    def test_cover_constraints(self):
        for i in range(weeks * 7):
            for j in range(num_shifts):
                # repetitive code just make sure each day's coverage matches requirements or more
                # 'monday coverage tests'
                self.assertTrue(sCount[0][1] >= 2,
                                msg='Monday shift 1 coverage is {0} which is not > 1'.format(sCount[0][1]))
                self.assertTrue(sCount[0][2] >= 3,
                                msg='Monday shift 2 coverage is {0} which is not > 2'.format(sCount[0][2]))
                self.assertTrue(sCount[0][3] >= 1,
                                msg='Monday shift 3 coverage is {0} which is not > 0'.format(sCount[0][3]))
                # 'tuesday coverage tests'
                self.assertTrue(sCount[1][1] >= 2,
                                msg='Tuesday shift 1 coverage is {0} which is not > 1'.format(sCount[1][1]))
                self.assertTrue(sCount[1][2] >= 3,
                                msg='Tuesday shift 2 coverage is {0} which is not > 2'.format(sCount[1][2]))
                self.assertTrue(sCount[1][3] >= 1,
                                msg='Tuesday shift 3 coverage is {0} which is not > 0'.format(sCount[1][3]))
                # 'wednesday coverage tests'
                self.assertTrue(sCount[2][1] >= 2,
                                msg='Wednesday shift 1 coverage is {0} which is not > 1'.format(sCount[2][1]))
                self.assertTrue(sCount[2][2] >= 2,
                                msg='Wednesday shift 2 coverage is {0} which is not > 1'.format(sCount[2][2]))
                self.assertTrue(sCount[2][3] >= 2,
                                msg='Wednesday shift 3 coverage is {0} which is not > 1'.format(sCount[2][3]))
                # 'thursday coverage tests'
                self.assertTrue(sCount[3][1] >= 2,
                                msg='Thursday shift 1 coverage is {0} which is not > 1'.format(sCount[3][1]))
                self.assertTrue(sCount[3][2] >= 3,
                                msg='Thursday shift 2 coverage is {0} which is not > 2'.format(sCount[3][2]))
                self.assertTrue(sCount[3][3] >= 1,
                                msg='Thursday shift 3 coverage is {0} which is not > 0'.format(sCount[3][3]))
                # 'friday coverage tests'
                self.assertTrue(sCount[4][1] >= 2,
                                msg='Friday shift 1 coverage is {0} which is not > 1'.format(sCount[4][1]))
                self.assertTrue(sCount[4][2] >= 2,
                                msg='Friday shift 2 coverage is {0} which is not > 1'.format(sCount[4][2]))
                self.assertTrue(sCount[4][3] >= 2,
                                msg='Friday shift 3 coverage is {0} which is not > 1'.format(sCount[4][3]))
                # 'saturday coverage tests'
                self.assertTrue(sCount[5][1] >= 1,
                                msg='Saturday shift 1 coverage is {0} which is not > 0'.format(sCount[5][1]))
                self.assertTrue(sCount[5][2] >= 2,
                                msg='Saturday shift 2 coverage is {0} which is not > 1'.format(sCount[5][2]))
                self.assertTrue(sCount[5][3] >= 3,
                                msg='Saturday shift 3 coverage is {0} which is not > 2'.format(sCount[5][3]))
                # 'sunday coverage tests'
                self.assertTrue(sCount[6][1] >= 1,
                                msg='Sunday shift 1 coverage is {0} which is not > 0'.format(sCount[6][1]))
                self.assertTrue(sCount[6][2] >= 3,
                                msg='Sunday shift 2 coverage is {0} which is not > 2'.format(sCount[6][2]))
                self.assertTrue(sCount[6][3] >= 1,
                                msg='Sunday shift 3 coverage is {0} which is not > 0'.format(sCount[6][3]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
