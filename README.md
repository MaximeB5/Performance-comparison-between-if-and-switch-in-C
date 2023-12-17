# Performance-comparison-between-if-and-switch-in-C

- Launch main.py without command line parameter --> using default value for NUMBER_OF_CASES (10 000)
- Launch main.py with one command line parameter --> if is an int, override NUMBER_OF_CASES, else use its default value (10 000)
- ...
- The file main.py generates all .c files for each use cases.
- The use cases must be launched from command line with an integer argument provided as the data to find, if it exists in the generated dataset.
- The dataset is generated based on the variable NUMBER_OF_CASES in main.py.
- Use cases are independent. Their dataset may vary : the use case 1 uses from 0 to NUMBER_OF_CASES, but the use case 4 uses from (-1 * (NUMBER_OF_CASES / 2)) to (NUMBER_OF_CASES/2)


# Use cases available :

- Use case 1 : from 0 to max value (only positive values)
- Use case 2 : from max value to 0 (only positive values)
- Use case 3 : mix with all possible values (only positive values, including 0, but not starting at 0)
- Use case 4 : mix with all possible values, including negative values (first value is a negative one, and the second is a positive, all others are random values)


# Benchmarking :

- Unix : use time command, e.g. time ./a.out
- Other OS : add time.h dependency in .c files such as :
  clock_t begin = clock();
  /* the generated code */
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("time spent is %f", time_spent);
