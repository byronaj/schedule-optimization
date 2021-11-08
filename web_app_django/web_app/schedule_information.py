class ScheduleInformation:
    def __init__(
            self,
            num_employees,
            num_weeks,
            shifts,
            shift_constraints,
            weekly_sum_constraints,
            penalized_transitions
    ):
        self.__num_employees = int(num_employees)
        self.__num_weeks = int(num_weeks)
        self.__shifts = shifts
        self.__shift_constraints = shift_constraints
        self.__weekly_sum_constraints = weekly_sum_constraints
        self.__penalized_transitions = penalized_transitions

    def employees(self):
        return self.__num_employees

    def weeks(self):
        return self.__num_weeks

    def shifts(self):
        return self.__shifts

    def shift_constraints(self):
        return self.__shift_constraints

    def weekly_constraints(self):
        return self.__weekly_sum_constraints

    def penalized_transitions(self):
        return self.__penalized_transitions
