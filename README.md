## Unit Testing Assignment

[![Build Status](https://travis-ci.com/Champ2k/unittesting-Champ2k.svg?branch=master)](https://travis-ci.com/Champ2k/unittesting-Champ2k)

by Wikrom Chanthakhun.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| what other test case?  |  what result?       |
| only an integers       |  TypeError          |
| not a list             |  NameError          |
| only a string          |  list with 1 item of a alphabet  |


## Test Cases for Fraction
| Test case              |  Expected Result    |
|------------------------|---------------------|
| test string            |  string of the fraction|
| test add               |  object 1 + object 2|
| 1/2 == 1/2             |  True               |
| test sub               |  object 1 - object 2|
| 1/2 > 1/3              |  True               |
| test mul               |  object 1 * object 2|
| 1/0 + 1/0              |  0/0                |
| 0/0 + 0/0              |  0/0                |
| 1/0 - (-1/0)           |  0/0                |
| 0/0 - 0/0              |  0/0                |
| 1/0 == -1/0            |  True               |
| 0/0 == 0               |  False              |
| 0/0 == 1/0 or -1/0     |  False              |
| Not a integer          |  TypeError          |

