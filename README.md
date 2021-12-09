# sta308final
STA 308 final (fall 2021)
| Functionality                               | In R               | In Python                      |
|---------------------------------------------|--------------------|--------------------------------|
|Import Downloaded Csv files                  | read.csv           | pandas.read.csv                |
|Change columns (variables) names             | rename()           | data.rename(columns=[])        |
|merge two data sets together by a varaible   | merge (_ by.x,by.y)| data.merge(_on=)               |
|Change data frame to contain specified var   | select()           | data.loc(:,[])                 |
|Groups data in DF together by commonality var| group_by()         | data.groupby()                 |
|created VOF variable name and added to DF    | summarize()        | data.assign()                  |
| caculates the mean                          | mean()             | .mean()                        |
| calculates standard deviation               | sd()               | .std()                         |
| assignment opperator                        | <-                 | =                              |
| Removes an observation                      | filter().          | data['column'] != "Observation"|





1. The Coefficient of Variation is the ratio of the standard deviation to the mean. In essence, in essence, the value represents the extent of variability in relation to the mean of the population. So, to compute CoV, you take your standard deviation and devide it by the mean (sd/mean). Hence, the lower the value, the better. You can multiple tha value by 100* to get a percentage.
2. When looking at CoV values, the region with the lowers is the Northeast, with a value of .1850450, and the South with the highest COV value, which is .4933262 (or 49.33%). As I stated in the previous question, we prefer to have a lower COV value, but that does not inherently tell us much about the population data. Even the Northeast has the lowers COV value, they have the highest mean age adjusted rate, but have a smaller standard deviation. This shows that COV tells us about the varation in the data, but is difficult to make insights about the data with only that value. The Region with the lowest Mean AAr is West, with a value of 18.13846, with a similair standard deviation as the Northeast (around 5) and cotains a COV value of .2776581 (or 27.76%)
3. It is difficult to figure out exactly what my favorite part of the class (I know its not functions though :) ) but I would say that I enjoyed the data cleaning steps, both in R and Python. I don't know exactly why this is, but I do find it fun to take large data samples (single or multiple) and adjusting and minimzing it and producing values of interest. It does sound boring, and maybe when I do it enough times, it will be for me. But for this semester, and  with this final assignment, I found it fun and challenging to complete the task, and in the end when it all started to work, I felt rewarded. I know that I can provide a skill to employers in the future that not many other majors can do. It was a bumpy ride this semester, but I feel like I learned alot and challenged myself, even if my grade is not totally indicative of that. 
