from random import randint


def dice_input(cube):
    if not isinstance(cube, str):
        return "Wrong input!"
    elif 'D' not in cube:
        return "Wrong input!"
    else:
        dices_nuber, rest_code = cube.split('D')
        cube_type = 0
        additional_number = 0
        character = 0
        if "+" in rest_code:
            character = '+'
            cube_type, additional_number = rest_code.split('+')
        elif "-" in rest_code:
            character = '-'
            cube_type, additional_number = rest_code.split('-')
        else:
            cube_type = rest_code
        try:
            result = [int(dices_nuber), int(cube_type), int(additional_number), character]
            return result
        except ValueError:
            return "Wrong input!"


def dice_simulator(dice):
    dice_parameters = dice_input(dice)
    if not isinstance(dice_parameters, list):
        return "Wrong input"
    nuber_of_dice_roll = dice_parameters[0]
    cube_type = dice_parameters[1]
    additional_modifier = dice_parameters[2]
    modify_variable = dice_parameters[3]
    result_of_all_dice_roll = 0
    for i in range(nuber_of_dice_roll):
        number = randint(1, cube_type)
        result_of_all_dice_roll += number
    if modify_variable == 0:
        result = result_of_all_dice_roll
    elif modify_variable == '+':
        result = result_of_all_dice_roll + additional_modifier
    else:
        result = result_of_all_dice_roll - additional_modifier
    return result


if __name__ == '__main__':
    print(dice_simulator('2D20+1'))
    print(dice_simulator(123))
    print(dice_simulator('2D+1'))
    print(dice_simulator('2D100'))
    print(dice_simulator('2D6-10'))
