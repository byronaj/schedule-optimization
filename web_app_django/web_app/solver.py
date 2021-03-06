from datetime import date, timedelta

from ortools.sat.python import cp_model


def negated_bounded_span(workers, start, length):
    # this blocks multiple shifts in a day
    # https://tinyurl.com/ykvk74h7 explanation
    sequence = []

    # Left border (start of workers, or workers[start - 1])
    if start > 0:
        sequence.append(workers[start - 1])

    for i in range(length):
        sequence.append(workers[start + i].Not())

    # Right border (end of workers or workers[start + length])
    if start + length < len(workers):
        sequence.append(workers[start + length])

    return sequence


def add_soft_sequence_constraint(model, workers, hard_min, soft_min, min_cost, soft_max, hard_max, max_cost, prefix):
    # see OR documentation if questions arise
    cost_literals = []
    cost_coefficients = []

    # Forbid sequences that are too short.
    for length in range(1, hard_min):
        for start in range(len(workers) - length + 1):
            model.AddBoolOr(negated_bounded_span(workers, start, length))

    # Penalize sequences that are below the soft limit.
    if min_cost > 0:
        for length in range(hard_min, soft_min):
            for start in range(len(workers) - length + 1):
                span = negated_bounded_span(workers, start, length)
                name = ': under_span(start=%i, length=%i)' % (start, length)
                lit = model.NewBoolVar(prefix + name)
                span.append(lit)
                model.AddBoolOr(span)
                cost_literals.append(lit)
                # We filter exactly the sequence with a short length.
                # The penalty is proportional to the delta with soft_min.
                cost_coefficients.append(min_cost * (soft_min - length))

    # Penalize sequences that are above the soft limit.
    if max_cost > 0:
        for length in range(soft_max + 1, hard_max + 1):
            for start in range(len(workers) - length + 1):
                span = negated_bounded_span(workers, start, length)
                name = ': over_span(start=%i, length=%i)' % (start, length)
                lit = model.NewBoolVar(prefix + name)
                span.append(lit)
                model.AddBoolOr(span)
                cost_literals.append(lit)
                # Cost paid is max_cost * excess length.
                cost_coefficients.append(max_cost * (length - soft_max))

    # Just forbid any sequence of true variables with length hard_max + 1
    for start in range(len(workers) - hard_max):
        model.AddBoolOr([workers[i].Not() for i in range(start, start + hard_max + 1)])

    return cost_literals, cost_coefficients


def add_soft_sum_constraint(model, workers, hard_min, soft_min, min_cost, soft_max, hard_max, max_cost, prefix):
    cost_variables = []
    cost_coefficients = []
    sum_var = model.NewIntVar(hard_min, hard_max, '')
    # This adds the hard constraints on the sum.
    model.Add(sum_var == sum(workers))

    # Penalize sums below the soft_min target.
    # delta is distance to soft min if it is negative min has been exceeded and penalty is 0
    # excess is distance from soft min used to remove delta, this is multiplied by min_cost
    if soft_min > hard_min and min_cost > 0:
        delta = model.NewIntVar(-len(workers), len(workers), '')
        model.Add(delta == soft_min - sum_var)
        excess = model.NewIntVar(0, 7, prefix + ': under_sum')
        model.AddMaxEquality(excess, [delta, 0])
        cost_variables.append(excess)
        cost_coefficients.append(min_cost)

    # Penalize sums above the soft_max target.
    if soft_max < hard_max and max_cost > 0:
        delta = model.NewIntVar(-7, 7, '')
        model.Add(delta == sum_var - soft_max)
        excess = model.NewIntVar(0, 7, prefix + ': over_sum')
        model.AddMaxEquality(excess, [delta, 0])
        cost_variables.append(excess)
        cost_coefficients.append(max_cost)

    # see https://tinyurl.com/2rawh9nw for explanation
    return cost_variables, cost_coefficients


def solve_shift_scheduling(
        emp_ids,
        num_employees,
        num_weeks,
        shifts,
        shift_constraints,
        weekly_sum_constraints,
        penalized_transitions,
        weekly_cover_demands
):
    """Solves the shift scheduling problem."""

    # Penalty for exceeding the cover constraint per shift type.
    excess_cover_penalties = (0, 0, 0)  # all set to forbidden
    # excess_cover_penalties = (3, 3, 6)  # lower penalty for first and second, higher for third

    num_days = num_weeks * 7
    num_shifts = len(shifts)

    model = cp_model.CpModel()

    work = {}
    for e in range(num_employees):
        for s in range(num_shifts):
            for d in range(num_days):
                work[e, s, d] = model.NewBoolVar('work%i_%i_%i' % (e, s, d))

    # Linear terms of the objective in a minimization context.
    obj_int_vars = []
    obj_int_coeffs = []
    obj_bool_vars = []
    obj_bool_coeffs = []

    # Exactly one shift per day.
    for e in range(num_employees):
        for d in range(num_days):
            model.Add(sum(work[e, s, d] for s in range(num_shifts)) == 1)

    # Shift constraints
    for ct in shift_constraints:
        shift, hard_min, soft_min, min_cost, soft_max, hard_max, max_cost = ct

        for e in range(num_employees):
            workers = [work[e, shift, d] for d in range(num_days)]

            variables, coeffs = add_soft_sequence_constraint(
                model,
                workers,
                hard_min,
                soft_min,
                min_cost,
                soft_max,
                hard_max,
                max_cost,
                'shift_constraint(employee %i, shift %i)' % (e, shift)
            )

            obj_bool_vars.extend(variables)
            obj_bool_coeffs.extend(coeffs)

    # Weekly sum constraints
    for ct in weekly_sum_constraints:
        shift, hard_min, soft_min, min_cost, soft_max, hard_max, max_cost = ct

        for e in range(num_employees):

            for w in range(num_weeks):
                workers = [work[e, shift, d + w * 7] for d in range(7)]

                variables, coeffs = add_soft_sum_constraint(
                    model,
                    workers,
                    hard_min,
                    soft_min,
                    min_cost,
                    soft_max,
                    hard_max,
                    max_cost,
                    'weekly_sum_constraint(employee %i, shift %i, week %i)' % (e, shift, w)
                )

                obj_int_vars.extend(variables)
                obj_int_coeffs.extend(coeffs)

    # Penalized transitions
    for previous_shift, next_shift, cost in penalized_transitions:
        for e in range(num_employees):

            for d in range(num_days - 1):
                transition = [work[e, previous_shift, d].Not(), work[e, next_shift, d + 1].Not()]

                if cost == 0:
                    model.AddBoolOr(transition)
                else:
                    trans_var = model.NewBoolVar('transition (employee=%i, day=%i)' % (e, d))
                    transition.append(trans_var)
                    model.AddBoolOr(transition)
                    obj_bool_vars.append(trans_var)
                    obj_bool_coeffs.append(cost)

    # Cover constraints
    for s in range(1, num_shifts):
        for w in range(num_weeks):
            for d in range(7):
                workers = [work[e, s, w * 7 + d] for e in range(num_employees)]

                # Ignore Off shift.
                min_demand = weekly_cover_demands[d][s - 1]
                worked = model.NewIntVar(min_demand, num_employees, '')
                model.Add(worked == sum(workers))
                over_penalty = excess_cover_penalties[s - 1]

                if over_penalty > 0:
                    name = 'excess_demand(shift=%i, week=%i, day=%i)' % (s, w, d)
                    excess = model.NewIntVar(0, num_employees - min_demand, name)
                    model.Add(excess == worked - min_demand)
                    obj_int_vars.append(excess)
                    obj_int_coeffs.append(over_penalty)

    # Objective
    model.Minimize(
        sum(obj_bool_vars[i] * obj_bool_coeffs[i] for i in range(len(obj_bool_vars)))
        + sum(obj_int_vars[i] * obj_int_coeffs[i] for i in range(len(obj_int_vars)))
    )

    # Solve the model.
    solver = cp_model.CpSolver()
    solution_printer = cp_model.ObjectiveSolutionPrinter()
    status = solver.Solve(model, solution_printer)

    # Print solution, employees as rows and days as columns
    # schedule2d is the array to return employee schedule
    schedule2d = []
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print()
        header = '          '

        for w in range(num_weeks):
            header += 'M  T  W  Th F  Sa Su '

        print(header)

        schedule2d = [['V' for _ in range(num_days)] for _ in range(num_employees)]

        for e in range(num_employees):
            schedule = ''

            for d in range(num_days):
                for s in range(num_shifts):
                    if solver.BooleanValue(work[e, s, d]):
                        schedule += shifts[s] + '  '
                        schedule2d[e][d] = shifts[s]

            print('worker %i: %s' % (e, schedule))

        # --------------------------------------------------------------------------------------------------------------
        # Output Formatting
        # --------------------------------------------------------------------------------------------------------------
        # Get the nearest date (after current date) that is a Monday
        next_monday = date.today() + timedelta(days=(0 - date.today().weekday() - 1) % 7 + 1)

        # List of n dates starting from next Monday
        schedule_dates = [next_monday + timedelta(days=i) for i in range(num_days)]

        # Attach dates and format for output
        schedule2d = [
            {
                'employee': int(e),
                'shift_assignments': [
                    {
                        'shift_date': d,
                        'assignment': int(s)
                    }
                    for d, s in zip(schedule_dates, shift_list)
                ]
            }
            for e, shift_list in zip(emp_ids, schedule2d)
        ]
        # --------------------------------------------------------------------------------------------------------------

        print('Penalties:')
        for i, var in enumerate(obj_bool_vars):
            if solver.BooleanValue(var):
                penalty = obj_bool_coeffs[i]
                if penalty > 0:
                    print('  %s violated, penalty=%i' % (var.Name(), penalty))
                else:
                    print('  %s fulfilled, gain=%i' % (var.Name(), -penalty))

        for i, var in enumerate(obj_int_vars):
            if solver.Value(var) > 0:
                print('  %s violated by %i, linear penalty=%i' % (var.Name(), solver.Value(var), obj_int_coeffs[i]))

    print()
    print('Statistics')
    print('  - status          : %s' % solver.StatusName(status))
    print('  - conflicts       : %i' % solver.NumConflicts())
    print('  - branches        : %i' % solver.NumBranches())
    print('  - wall time       : %f s' % solver.WallTime())

    return schedule2d
