# Problem

The Central City Fire Department collaborates with the transportation department
to maintain maps that reflect the current status of city streets. On any given
day, several streets are closed for repairs or construction. Firefighters need
to be able to select routes from their stations to fires that avoid closed
streets.

Central City is divided into non-overlapping fire districts, each containing a
single fire station. When a fire is reported, a central dispatcher alerts the
fire station of the district where the fire is located and sends them a list of
possible routes from the fire station to the fire. You must write a program that
the central dispatcher can use to generate these routes.

## Input

The city maintains a separate map for each fire district. The street corners on
each map are identified by positive integers less than 21, with the fire station
always on corner 1.

The input consists of a single test case as follows:

-   The first line contains a single integer identifying the street corner where
    the fire is located.
-   The remaining lines consist of space-separated pairs of integers that
    represent street corners connected by an open street. (For example, if the
    input contains the line `1 2`, then there is an open street between corners
    1 and 2.)

### Sample input

```
6
1 2
1 3
3 4
3 5
4 6
5 6
2 3
2 4
```

## Output

Output a list of routes from the fire station to the fire. Each route should be
on a separate line and enumerate the street corners that the route passes
through. Include only routes that do not pass through any corner more than once
(for obvious reasons, the fire department doesn't want its trucks driving around
in circles.)

### Sample output

```
1 2 3 4 6
1 2 3 5 6
1 2 4 3 5 6
1 2 4 6
1 3 2 4 6
1 3 4 6
1 3 5 6
```
