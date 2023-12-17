#
# This python file generates use cases in order to monitor the time spent between :
#   - if/if/if/...
#   - if/else if/else
#   - switch/cases
#

import sys
from random import shuffle

# Number of if/if/if/... - if/else if/else - switch/cases to benchmark
NUMBER_OF_CASES = 10000


def file_write_new_line(f, param):
    f.write(param + "\n")
    pass


def write_top_c_file(f):
    file_write_new_line(f, '#include <stdio.h>')
    file_write_new_line(f, 'int main(int argc, char* argv[])')
    file_write_new_line(f, '{')
    file_write_new_line(f, 'if( argc != 2 ) { printf("One argument of type int is expected."); return -1; }')
    file_write_new_line(f, 'volatile int user_input = argv[1]; /* No check done on the user input, it must be an int */')
    file_write_new_line(f, 'printf("input received : <%d>", user_input);')
    pass


def write_bottom_c_file(f):
    file_write_new_line(f, 'return 0;')
    file_write_new_line(f, '}')
    pass


def write_if_if_if_case_in_file_from_list(f, integers):
    for x in integers:
        statement = 'if (user_input == ' + str(x) + ') { return 1; }'
        file_write_new_line(f, statement)
    pass


def write_if_else_if_else_case_in_file_from_list(f, integers):
    # if
    statement = 'if (user_input == ' + str(integers[0]) + ') { return 1; }'
    file_write_new_line(f, statement)

    # else if
    for x in integers[1:-1]:
        statement = 'else if (user_input == ' + str(x) + ') { return 1; }'
        file_write_new_line(f, statement)

    # else
    statement = 'else { return 2; }'
    file_write_new_line(f, statement)
    pass


def write_switch_cases_in_file_from_list(f, integers):
    # switch - start
    file_write_new_line(f, 'switch (user_input)')
    file_write_new_line(f, '{')

    # cases
    for x in integers:
        statement = 'case ' + str(x) + ': { return 1; }'
        file_write_new_line(f, statement)

    # switch - end
    file_write_new_line(f, 'default: { return 2; }')
    file_write_new_line(f, '}')
    pass


def generate_use_case_1():
    # This use case is a regular one with increment order from 0 to max value (only positive values)
    # TODO FYI - 1. Generate if/if/if/...
    # TODO FYI - 2. Generate if/else if/else
    # TODO FYI - 3. Generate switch/cases

    integers = list(range(NUMBER_OF_CASES))  # list [x, y, z, ...] from 0 to NUMBER_OF_CASES

    with open('use_case_1_if_if_if.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a regular one with increment order from 0 to max value (only positive values) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_if_if_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_1_if_else_if_else.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a regular one with increment order from 0 to max value (only positive values) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_else_if_else_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_1_switch_cases.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a regular one with increment order from 0 to max value (only positive values) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_switch_cases_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)
    pass


def generate_use_case_2():
    # This use case is a regular one with decrement order from max value to 0 (only positive values)
    # TODO FYI - 1. Generate if/if/if/...
    # TODO FYI - 2. Generate if/else if/else
    # TODO FYI - 3. Generate switch/cases

    integers = list(range(NUMBER_OF_CASES))  # list [x, y, z, ...] from 0 to NUMBER_OF_CASES
    integers = list(reversed(integers))  # list [x, y, z, ...] from NUMBER_OF_CASES to 0

    with open('use_case_2_if_if_if.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a regular one with decrement order from max value to 0 (only positive values) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_if_if_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_2_if_else_if_else.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a regular one with decrement order from max value to 0 (only positive values) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_else_if_else_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_2_switch_cases.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a regular one with decrement order from max value to 0 (only positive values) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_switch_cases_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)
    pass


def generate_use_case_3():
    # This use case is a mix with all possible values (only positive values, including 0, but not starting at 0)
    # TODO FYI - 1. Generate if/if/if/...
    # TODO FYI - 2. Generate if/else if/else
    # TODO FYI - 3. Generate switch/cases

    integers = list(range(NUMBER_OF_CASES))  # list [x, y, z, ...] from 0 to NUMBER_OF_CASES

    safety_counter = 0
    while integers[0] == 0:
        shuffle(integers)
        safety_counter += 1
        if safety_counter > 50:
            print("ERROR generate_use_case_3 > shuffle while loop")
            break

    with open('use_case_3_if_if_if.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a mix with all possible values (only positive values, including 0, but not starting at 0) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_if_if_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_3_if_else_if_else.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a mix with all possible values (only positive values, including 0, but not starting at 0) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_else_if_else_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_3_switch_cases.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a mix with all possible values (only positive values, including 0, but not starting at 0) */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_switch_cases_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)
    pass


def generate_use_case_4():
    # This use case is a mix with all possible values, including negative values
    # The first value is a negative one, and the second is a positive, all others are random values
    # TODO FYI - 1. Generate if/if/if/...
    # TODO FYI - 2. Generate if/else if/else
    # TODO FYI - 3. Generate switch/cases

    max_value = int((NUMBER_OF_CASES / 2))
    min_value = int(max_value * - 1)
    integers = list(range(min_value, max_value))  # list [x, y, z, ...] from min_value to max_value

    safety_counter = 0
    while (integers[0] > 0) or (integers[1] < 0):
        shuffle(integers)
        safety_counter += 1
        if safety_counter > 50:
            print("ERROR generate_use_case_4 > shuffle while loop")
            break

    with open('use_case_4_if_if_if.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a mix with all possible values, including negative values */')
        file_write_new_line(f, '/* The first value is a negative one, and the second is a positive, all others are random values */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_if_if_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_4_if_else_if_else.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a mix with all possible values, including negative values */')
        file_write_new_line(f, '/* The first value is a negative one, and the second is a positive, all others are random values */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_if_else_if_else_case_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)

    with open('use_case_4_switch_cases.c', 'w') as f:
        file_write_new_line(f, '/* This use case is a mix with all possible values, including negative values */')
        file_write_new_line(f, '/* The first value is a negative one, and the second is a positive, all others are random values */')
        write_top_c_file(f)
        # TODO FYI - Use Case [Start]
        write_switch_cases_in_file_from_list(f, integers)
        # TODO FYI - Use Case [End]
        write_bottom_c_file(f)
    pass


def main():
    print("... Start file generation.")
    generate_use_case_1()
    generate_use_case_2()
    generate_use_case_3()
    generate_use_case_4()
    print("... Generation has finished.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg.isdigit():
            NUMBER_OF_CASES = int(arg)
            print("... Override NUMBER_OF_CASES status : OK.\n    New value is :" + str(NUMBER_OF_CASES))
        else:
            print("(!) ERROR ! NUMBER_OF_CASES cannot be overriden.\n    Value received is not an int : " + str(arg))
            print("(!) Using default value for NUMBER_OF_CASES, value is : " + str(NUMBER_OF_CASES))
    else:
        print("... Using default value for NUMBER_OF_CASES, value is : " + str(NUMBER_OF_CASES))

    main()
