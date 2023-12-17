# Performance-comparison-between-if-and-switch-in-C

- The file main.py generates all .c files for each use cases.
- The use cases must be launched from command line with an integer argument provided as the data to find, if it exists in the generated dataset.
- The dataset is generated based on the variable NUMBER_OF_CASES in main.py.
- Use cases are independent. Their dataset may vary : the use case 1 uses from 0 to NUMBER_OF_CASES, but the use case 4 uses from (-1 * (NUMBER_OF_CASES / 2)) to (NUMBER_OF_CASES/2)


# Use cases available :

- Use case 1 : from 0 to max value (only positive values)
- Use case 2 : from max value to 0 (only positive values)
- Use case 3 : mix with all possible values (only positive values, including 0, but not starting at 0)
- Use case 4 : mix with all possible values, including negative values (first value is a negative one, and the second is a positive, all others are random values)
