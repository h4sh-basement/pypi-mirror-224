MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.









# 基础数据类型的使用

有时间，字典，列表，数值，字符串，元组等。

```
pip install basic-type-operations
```

## 常用的关于时间的方法

## 判断闰年

```python
from basic_type_operations.date_operation import DateOperation

print(DateOperation.determine_leap_year(2021))
# False
print(DateOperation.determine_leap_year(2008))
# True
```

## 今天开始到现在共多少秒

```python
from basic_type_operations.date_operation import DateOperation

print(DateOperation.today_top_now_second())
# 73591
```

## 整形转时间

```python
from basic_type_operations.date_operation import DateOperation

print(DateOperation.TimeStampToTime(1479264792))
# 2016-11-16 10:53:12
```



## 获取格林威治时间

```python
from basic_type_operations.date_operation import DateOperation

print(DateOperation.UTCISOTime())
# 2022-03-22T06:00:44.000000Z
```

## 格林威治时间-转-北京时间

```python

from basic_type_operations.date_operation import DateOperation

print(DateOperation.UTC2BJS('2022-03-22T06:00:44.528Z'))
# 2016-11-16 10:53:12
```

## 北京时间-转 格林威治时间

```python
from basic_type_operations.date_operation import DateOperation

print(DateOperation.BJS2UTC('2022-03-22 14:00:44'))
# 2022-03-22T06:00:44.000000Z
```



## 某年的开始和结束

```python
from basic_type_operations.date_operation import DateOperation
import datetime

# 获取当年的开始和结束
print(DateOperation.year_top_tail())
# ('2023-01-01', '2023-12-31')
# 获取输入年份的开始和结束
print(DateOperation.year_top_tail(2021))
# ('2021-01-01', '2021-12-31')
# 输入时间获取年份的开始和结束时间
date = datetime.datetime.now()
print(DateOperation.year_top_tail(date))
# ('2023-01-01', '2023-12-31')
```

## 月份所在季度以及季度的开始和结束

```python
from basic_type_operations.date_operation import DateOperation
import datetime
# 获取当前季度的开始和结束
print(DateOperation.quarter_top_tail())
#('2023-07-01', '2023-09-30')
# 输入时间获取季度的开始和结束时间
date = datetime.datetime.now()
print(DateOperation.quarter_top_tail(date))
#('2023-07-01', '2023-09-30')
```

## 某月开始和结束日期

```python
from basic_type_operations.date_operation import DateOperation
import datetime

# 获取当前月的开始和结束
print(DateOperation.month_top_tail())
# (datetime.date(2023, 8, 1), datetime.date(2023, 8, 31))
# 输入时间获取月的开始和结束时间
date = datetime.datetime.now()
print(DateOperation.month_top_tail(date))
# (datetime.date(2023, 8, 1), datetime.date(2023, 8, 31))
```

## 某周开始和结束日期

```python
from basic_type_operations.date_operation import DateOperation
import datetime

# 获取当前周的开始和结束
print(DateOperation.week_top_tail())
# ('2023-08-07', '2023-08-13')
# 输入时间获取周的开始和结束时间
date = datetime.datetime.now()
print(DateOperation.week_top_tail(date))
# ('2023-08-07', '2023-08-13')
```

## 某天开始和结束日期

```python
from basic_type_operations.date_operation import DateOperation
import datetime

# 获取当前天的开始和结束
print(DateOperation.day_top_tail())
# (datetime.datetime(2023, 8, 10, 0, 0), datetime.datetime(2023, 8, 10, 23, 59, 59))
# 输入时间获取天的开始和结束时间
date = datetime.datetime.now()
print(DateOperation.day_top_tail(date))
# (datetime.datetime(2023, 8, 10, 0, 0), datetime.datetime(2023, 8, 10, 23, 59, 59))

```

更多方法请看模块date_operation，或者联系作者一起探讨。

