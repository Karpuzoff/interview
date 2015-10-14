
__author__ = "Valery Karpuzoff"
__copyright__ = "Copyright (C) 2015 Valery Karpuzoff"

import re


def _create_at_end(string):
    length = len(string)

    def at_end(index):
        return index >= length

    return at_end


def _parse_one_summand(text, start_index):
    text_from_start_index = text[start_index:]
    m = re.match(r'^([\-\+]?)(\d*)('+x+'?)(\^(\d+)?)?', text_from_start_index)

    base = 1
    if m.group(1):
        base = {'-': -1, '+': +1}.get(m.group(1))
    if m.group(2):
        base *= int(m.group(2))

    exponent = 0
    if m.group(3):
        exponent = 1
        if m.group(5):
            exponent = int(m.group(5))
    elif m.group(4):
        base **= int(m.group(5))

    return {exponent: base}, start_index + m.end()


def _power(base, exponent):
    assert len(exponent) == 1
    assert next(iter(exponent)) == 0
    power_const = exponent[next(iter(exponent))]

    # TODO: make this optimal:
    result = base
    for i in range(1, power_const):
        result = _multiply(result, base)

    return result


def _multiply(factors1, factors2):
    result = dict()
    for (exponent1, base1) in factors1.items():
        for (exponent2, base2) in factors2.items():
            key = exponent1 + exponent2
            if key in result:
                result[key] += base1 * base2
            else:
                result[key] = base1 * base2
            if result[key] == 0:
                del result[key]
    return result


def _add(summands1, summands2):
    if not summands1:
        return dict(summands2)
    if not summands2:
        return dict(summands1)
    result = dict(summands2)
    for (exponent, base) in summands1.items():
        if exponent in result:
            result[exponent] += base
        else:
            result[exponent] = base
        if result[exponent] == 0:
            del result[exponent]
    return result


def _parse_factor(text, i):
    summands = dict()

    first = text[i]

    end_symbol = ')' if text[i] == '(' else "*)"

    if text[i] in "(*^":
        i += 1

    while (not _at_end(i)) and (text[i] not in end_symbol):

        summand, i = _parse_one_summand(text, i)

        if first == '^' and text[i] != '(':
            return summand, i + 1

        while (not _at_end(i)) and (text[i] not in "+-)"):
            inner, new_i = _parse_factor(text, i)
            if not inner:
                raise ValueError(" (Empty brackets)")
            if text[i] == '^':
                summand = _power(summand, inner)
            else:
                summand = _multiply(summand, inner)
            i = new_i

        summands = _add(summands, summand)

    return summands, i + 1


def _parse_polynom(text):
    summands, i = _parse_factor(text, 0)
    if not _at_end(i):
        raise ValueError(" (Missed '(')")
    return summands


def _polynom_to_string(summands):
    string = ""
    for key in sorted(summands.keys(), reverse=True):
        base, exponent = summands[key], key
        if base > 0:
            if len(string) != 0:
                string += '+'
        elif base == -1 and exponent > 0:
            string += '-'
        if abs(base) > 1 or exponent == 0:
            string += str(base)
        if exponent > 0:
            string += x
            if exponent > 1:
                string += '^'
                string += str(exponent)
    return string


def simplify(input_polynom):
    input_polynom = "".join(input_polynom.split())  # remove all spaces

    if not input_polynom:
        return ""

    global x
    x = 'x'
    m = re.search(r'[a-zA-Z]', input_polynom)
    if m:
        x = m.group()[0]

    if input_polynom.find(x + x) != -1:
        raise ValueError(" (Instead 'xx' you must use 'x^2')")

    if re.search(r'[a-zA-Z]', input_polynom.replace(x, '')):
        raise ValueError(" (One variable supported only)")

    if not re.fullmatch(r'([\-\+\d'+x+'\(][\-\+\*\d'+x+'\^\(\)]*)?['+x+'\d\)]', input_polynom):
        raise ValueError(" (Incorrect polynom)")

    m = re.search(r'[\-\+\*\^][\-\+\*\^]', input_polynom)
    if m:
        raise ValueError(" (Nonexisting operand between '" + m.group() + "')")

    m = re.search(r'[\-\+\*\^]\)', input_polynom)
    if m:
        raise ValueError(" (Uncompleted operation '" + m.group() + "')")

    input_polynom = '(' + input_polynom + ')'
    global _at_end
    _at_end = _create_at_end(input_polynom)

    polynom = _parse_polynom(input_polynom)
    return _polynom_to_string(polynom)


###############################################################################


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: polynom <polynom with '+', '-', '*', '^', '(', ')' and 'x'>")
        exit(0)

    try:
        input_polynom = "".join(sys.argv[1:])  # join all parts in one string
        print(simplify(input_polynom))
    except ValueError as error:
        print("Error: Invalid expression." + error.args[0])
        print("Abort")
    except Exception as error:
        print("Unexpected error: " + error.args[0])
        print("Abort")
