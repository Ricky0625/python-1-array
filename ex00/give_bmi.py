def all_int_or_float(lst: list) -> bool:

    """
    all_int_of_float(lst: list) -> bool

    Return True if the list consists only int or float. bool is also
    consider as int in python so need to add additional checking
    to check if it's not a instance of bool.
    """

    return all(
        [isinstance(x, (int, float)) and not isinstance(x, bool) for x in lst]
        )


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:

    """
    give_bmi(height: list, weight: list) -> list
    NOTE: list should be list[int | float]

    Return a list of bmi value. The bmi value is calculated based on the
    given height and weight.
    """

    try:
        bmis = []

        # check the list
        if height == [] or weight == []:
            raise AssertionError('Empty list')
        if len(height) != len(weight):
            raise AssertionError('The lists are not the same size')
        if not (all_int_or_float(height) and all_int_or_float(weight)):
            raise AssertionError('The lists should contain int or float')

        # iterate through both list and calculate bmi
        for idx, item in enumerate(height):
            if (item == 0):
                raise ZeroDivisionError("Zero divsion")
            bmi_value = weight[idx] / (item ** 2)
            bmis.append(bmi_value)

        return bmis
    except Exception as e:
        print(f"[ERROR]: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    """
    apply_list(bmi: list, limit: int) -> list[bool]

    Return a list of boolean. Check if the bmi value in the list
    is above the limit.
    """

    try:
        res = []

        # check the list
        if bmi == []:
            raise AssertionError('Empty list')
        if not all_int_or_float(bmi):
            raise AssertionError('The lists should contain int or float')

        # check if bmi value is above the limit
        for value in bmi:
            res.append(True if value > limit else False)

        return res
    except Exception as e:
        print(f"[ERROR]: {e}")
        return []
