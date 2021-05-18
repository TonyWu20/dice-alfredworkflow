import json
from sys import argv, stdout
import dice


def makeItem(query, roll_result, roll_sum):
    '''
    Format for alfred json
    Args:
        query: Input quest
        roll_result: separated results of dice(s)
        roll_sum: sum of roll
    '''
    icon = "CCC09FC5-7F21-4A11-9199-5D2B42CA0D19.png"
    item = {
        'uid': roll_result,
        'title': query,
        'subtitle': f"Each dice: {roll_result}, sum: {roll_sum}",
        'arg': roll_result,
        'autocomplete': query,
        'icon': {
            'path': icon
        }
    }
    return item


def makeReturn(items: list):
    '''
    Organize list
    Args:
        items : list
    '''
    out = {'items': items}
    return out


def roll_dice(roll_set: str) -> list:
    """
    roll dice
    Args:
        dice (str): ndn
    """
    dice_set = dice.roll(roll_set)
    result: list = dice_set.do_roll()
    return result


def main():
    '''
    main functions
    '''
    roll_quest = argv[1]
    roll_set = argv[2]
    roll_result = roll_dice(roll_set)
    roll_str = ", ".join([str(i) for i in roll_result])
    roll_sum = sum(roll_result)
    item = [makeItem(roll_quest, roll_str, str(roll_sum))]
    out = makeReturn(item)
    result = json.dumps(out, indent=4) + '\n'
    stdout.write(result)


if __name__ == "__main__":
    main()
