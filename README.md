# PLP Python Week 3 Assignment: Grade Reporter & Bug Hunt

## Files

* `grade_reporter.py` — Uses a `for` loop and conditional statements to assign grades, count passes and failures, and calculate the average score.
* `bug_hunt.py` — Demonstrates debugging by fixing three bugs in a `while` loop program that calculates the sum of numbers from 1 to 5.

## Bug Hunt Reflection

The hardest bug to find was the incorrect `while` loop condition because it did not produce an error message. The program ran successfully but printed 10 instead of the expected answer, 15. I knew something was wrong by comparing the output with the correct sum of 1 + 2 + 3 + 4 + 5, and I fixed the condition by changing `< 5` to `<= 5`.
