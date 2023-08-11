# LeetQuery

[![PyPI version](https://badge.fury.io/py/leetquery.svg)](https://badge.fury.io/py/leetquery) ![Test](https://github.com/ShuYuHuang/leetquery/actions/workflows/python-app.yml/badge.svg)  [![Downloads](https://static.pepy.tech/badge/leetquery)](https://pepy.tech/project/leetquery)

A library for retriving Human Resource information from Leetcode.

## Install
``` shell
    pip install leetquery
```
## Usage
### Retrieving User Submissions
Just enter user name and limit of query!
``` python
from leetquery.user import get_submissions

submissions = get_submissions(username="syhaung", limit=12)
```
return value:
```
["question1", "question2", ...]
```

### For Problems
#### Retrieving Problem Discription
Just enter probelm nameSlug and get the problem discription in HTML~~
``` python
from leetquery.problem import get_discription

submissions = get_discription(problemname="two-sum")
```
return value:
``` html
<p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>
...
```
#### Retrieving Problem Statistics
Get the statistics for the problem in a JSON format, help you quantize difficulties
``` python
from leetquery.problem import get_stats
stat = get_stats("two-sum")
assert isinstance(stat, dict) and \
    list(stat.keys()) == ['totalAccepted', 'totalSubmission', 'totalAcceptedRaw', 'totalSubmissionRaw', 'acRate']
```
return value:
``` json
{
    'totalAccepted': '10.4M',
    'totalSubmission': '20.6M',
    ...
}
```