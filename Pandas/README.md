

```python
# David Hui
# Dec 9th 2017


import pandas as pd
```


```python
# District Summary
```


```python
schools = 'raw_data/schools_complete.csv'
students = 'raw_data/students_complete.csv'
```


```python
schools_df = pd.read_csv(schools, encoding="iso-8859-1",low_memory=False)
schools_df.rename(columns={"name":"school"}, inplace=True)
schools_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
schools_type_df = pd.DataFrame(schools_df.groupby(["school","type"]).count())

del schools_type_df["School ID"]
del schools_type_df["size"]
del schools_type_df["budget"]

schools_type_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th>school</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <th>District</th>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <th>Charter</th>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <th>District</th>
    </tr>
    <tr>
      <th>Ford High School</th>
      <th>District</th>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <th>Charter</th>
    </tr>
  </tbody>
</table>
</div>




```python
students_df = pd.read_csv(students, encoding="iso-8859-1",low_memory=False)
students_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_schools = len(schools_df.index)
# print("Total Schools = " + str(total_schools))
```


```python
total_students = len(students_df.index)
# print("Total Students = " + str(total_students))
```


```python
total_budget = sum(schools_df["budget"])
# print("Total Budget = " + str(total_budget))
```


```python
avg_math_score = sum(students_df["math_score"]) / total_students
# print("Average Math Score = " + str(avg_math_score))
```


```python
avg_reading_score = sum(students_df["reading_score"]) / total_students
# print("Average Reading Score = " + str(avg_reading_score))
```


```python
#################################################################
#
#  District Summary
#
#################################################################
```


```python

# print ((FailedMath / total_students)*100)

PassedMath = students_df["math_score"].loc[students_df["math_score"] >= 65].count()
percentPassingMath = (PassedMath / total_students)*100
print ("% Passing Math = " + str(percentPassingMath))
```

    % Passing Math = 84.7281082461
    


```python
PassedReading = students_df["reading_score"].loc[students_df["reading_score"] >= 65].count()
percentPassingReading = (PassedReading / total_students)*100
# print ("% Passing Reading = " + str((percentPassingReading)) )
```


```python
avg_passing_rate = (percentPassingMath + percentPassingReading) / 2
# print("Overall Passing Rate = " + str(avg_passing_rate))
```


```python
District_Summary_df = pd.DataFrame({"Total Schools":[total_schools], 
                                 "Total Students":[total_students], 
                                 "Total Budget":[total_budget],
                                 "Average Math Score":[avg_math_score],
                                 "Average Reading Score":[avg_reading_score],
                                 "% Passing Math":[percentPassingMath],
                                 "% Passing Reading":[percentPassingReading],
                                 "Overall Passing Rate":[avg_passing_rate]
                                })

Organized_District_Summary_df = District_Summary_df[["Total Schools",
                                               "Total Students",
                                              "Total Budget",
                                              "Average Math Score",
                                              "Average Reading Score",
                                              "% Passing Math",
                                              "% Passing Reading",
                                              "Overall Passing Rate"
                                              ]]

Organized_District_Summary_df["Average Math Score"] = Organized_District_Summary_df["Average Math Score"].map("{0:,.2f}%".format)
Organized_District_Summary_df["Average Reading Score"] = Organized_District_Summary_df["Average Reading Score"].map("{0:,.2f}%".format)
Organized_District_Summary_df["% Passing Math"] = Organized_District_Summary_df["% Passing Math"].map("{0:,.2f}%".format)
Organized_District_Summary_df["% Passing Reading"] = Organized_District_Summary_df["% Passing Reading"].map("{0:,.2f}%".format)
Organized_District_Summary_df["Overall Passing Rate"] = Organized_District_Summary_df["Overall Passing Rate"].map("{0:,.2f}%".format)

Organized_District_Summary_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.99%</td>
      <td>81.88%</td>
      <td>84.73%</td>
      <td>96.20%</td>
      <td>90.46%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################################################################
#
# School Summary
#
#################################################################
```


```python
#schools_df.rename(columns={"name":"school"},inplace=True)
schools_df
budget_school_df = pd.DataFrame(schools_df.groupby(["school"]).sum())
#budget_school_df.rename(columns={"name":"school"},inplace=True)

budget_school_df.index.names =["school"] 
budget_school_df.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>size</th>
      <th>budget</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>7</td>
      <td>4976</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>6</td>
      <td>1858</td>
      <td>1081356</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>1</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>13</td>
      <td>2739</td>
      <td>1763916</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>4</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
studentAvgBySchool_df = pd.DataFrame(students_df.groupby(["school"]).sum())
#studentAvgBySchool_df
```


```python
studentAvgBySchool_df.reset_index(inplace=True)
budget_school_df.reset_index(inplace=True)

merged_df = pd.merge(studentAvgBySchool_df,budget_school_df, on="school")
#merged_df.head()
```


```python

merged_df['Avg Math Score']=merged_df["math_score"]/merged_df["size"]
merged_df['Avg Reading Score']=merged_df["reading_score"]/merged_df["size"]
#merged_df.head()
```


```python
PassedReadingBySchool= students_df[(students_df["reading_score"] >= 65)]
PassedMathBySchool= students_df[(students_df["math_score"] >= 65)]
#PassedReadingBySchool
```


```python
PassedMathBySchool=pd.DataFrame(PassedMathBySchool.groupby(["school"])["math_score"].count())
PassedMathBySchool.rename(columns={"math_score":"Total # of Students Pass Math"}, inplace=True)

PassedReadingBySchool_df=pd.DataFrame(PassedReadingBySchool.groupby(["school"])["reading_score"].count())
PassedReadingBySchool_df.rename(columns={"reading_score":"Total # of Students Pass Reading"}, inplace=True)
```


```python

PassedMathBySchool.reset_index(inplace=True)
PassedReadingBySchool_df.reset_index(inplace=True)

merged_df.reset_index(inplace=True)
merged_df = pd.merge(merged_df, PassedReadingBySchool_df, on="school")

merged_df.reset_index(inplace=True)
merged_df = pd.merge(merged_df, PassedMathBySchool, on="school")
merged_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>level_0</th>
      <th>index</th>
      <th>school</th>
      <th>Student ID</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>School ID</th>
      <th>size</th>
      <th>budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>Total # of Students Pass Reading</th>
      <th>Total # of Students Pass Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>Bailey High School</td>
      <td>101303896</td>
      <td>403225</td>
      <td>383393</td>
      <td>7</td>
      <td>4976</td>
      <td>3124928</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>4705</td>
      <td>3877</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>Cabrera High School</td>
      <td>31477307</td>
      <td>156027</td>
      <td>154329</td>
      <td>6</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>1858</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>Figueroa High School</td>
      <td>12949059</td>
      <td>239335</td>
      <td>226223</td>
      <td>1</td>
      <td>2949</td>
      <td>1884411</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>2788</td>
      <td>2276</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>3</td>
      <td>Ford High School</td>
      <td>99055935</td>
      <td>221164</td>
      <td>211184</td>
      <td>13</td>
      <td>2739</td>
      <td>1763916</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>2571</td>
      <td>2142</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>Griffin High School</td>
      <td>19077394</td>
      <td>123043</td>
      <td>122360</td>
      <td>4</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>1468</td>
      <td>1468</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_df["% Passing Reading"] = (merged_df["Total # of Students Pass Reading"] / merged_df["size"]) * 100
merged_df["% Passing Math"] = (merged_df["Total # of Students Pass Math"] / merged_df["size"]) * 100

merged_df.rename(columns={"budget":"Total School Budget"}, inplace=True)
merged_df["Per Student Budget"] = merged_df["Total School Budget"] / merged_df["size"]

del merged_df["index"]
del merged_df["Student ID"]
del merged_df["School ID"]

schools_type_df.reset_index(inplace=True)
merged_df.reset_index(inplace=True)

school_summary_df = pd.merge(merged_df,schools_type_df, on="school")

# School Summary Result Below
del school_summary_df["index"]
del school_summary_df["level_0"]


school_summary_df.rename(columns={"school":"School Name","type":"School Type","size":"Total Students"}, inplace=True)
school_summary_df = school_summary_df[["School Name","School Type","Total Students","Total School Budget","Per Student Budget","Avg Math Score","Avg Reading Score","% Passing Math","% Passing Reading"]]
school_summary_df["Overall Passing Rate"] = (school_summary_df["% Passing Math"] + school_summary_df["% Passing Reading"] ) /2

school_summary_df["Avg Math Score"] = school_summary_df["Avg Math Score"].map("{0:,.2f}%".format)
school_summary_df["Avg Reading Score"] = school_summary_df["Avg Reading Score"].map("{0:,.2f}%".format)
school_summary_df["% Passing Math"] = school_summary_df["% Passing Math"].map("{0:,.2f}%".format)
school_summary_df["% Passing Reading"] = school_summary_df["% Passing Reading"].map("{0:,.2f}%".format)
school_summary_df["Overall Passing Rate"] = school_summary_df["Overall Passing Rate"].map("{0:,.2f}%".format)


school_summary_df.head()
#list(school_summary_df)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.05%</td>
      <td>81.03%</td>
      <td>77.91%</td>
      <td>94.55%</td>
      <td>86.23%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.06%</td>
      <td>83.98%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.71%</td>
      <td>81.16%</td>
      <td>77.18%</td>
      <td>94.54%</td>
      <td>85.86%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.10%</td>
      <td>80.75%</td>
      <td>78.20%</td>
      <td>93.87%</td>
      <td>86.04%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.35%</td>
      <td>83.82%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################################################################
#
#  Top 5 Performing Schools (By Passing Rate)
#
#################################################################
```


```python
# Top 5 Performing Schools (By Passing Rate)

sorted_Top5_df = school_summary_df.sort_values("Overall Passing Rate", ascending=False)

schools_type_df.reset_index(inplace=True)

sorted_Top5_df.reset_index(inplace=True)
sorted_Top5_df.rename(columns={"School Name":"school"}, inplace=True)

sorted_Top5_df = pd.merge(sorted_Top5_df,schools_type_df, on="school")
sorted_Top5_df.rename(columns={"school":"School Name","type":"School Type"}, inplace=True)

sorted_Top5_df = sorted_Top5_df[["School Name","School Type","Total Students","Total School Budget","Per Student Budget","Avg Math Score","Avg Reading Score","% Passing Math","% Passing Reading","Overall Passing Rate"]]

#del sorted_Top5_df["index_x"]
#del sorted_Top5_df["index_y"]

sorted_Top5_df.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.84%</td>
      <td>80.74%</td>
      <td>77.94%</td>
      <td>94.62%</td>
      <td>86.28%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.05%</td>
      <td>81.03%</td>
      <td>77.91%</td>
      <td>94.55%</td>
      <td>86.23%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.07%</td>
      <td>80.97%</td>
      <td>77.97%</td>
      <td>94.48%</td>
      <td>86.22%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.29%</td>
      <td>80.93%</td>
      <td>77.73%</td>
      <td>94.61%</td>
      <td>86.17%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.63%</td>
      <td>81.18%</td>
      <td>77.72%</td>
      <td>94.48%</td>
      <td>86.10%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################################################################
#
#  Bottom 5 Performing Schools (By Passing Rate)
#
#################################################################
```


```python
# Bottom 5 Performing Schools (By Passing Rate)

sorted_bottom5_df = school_summary_df.sort_values('Overall Passing Rate', ascending=True)

schools_type_df.reset_index(inplace=True)

sorted_bottom5_df.reset_index(inplace=True)
sorted_bottom5_df.rename(columns={"School Name":"school"}, inplace=True)
sorted_bottom5_df = pd.merge(sorted_bottom5_df,schools_type_df, on="school")

del sorted_bottom5_df["index_x"]
del sorted_bottom5_df["index_y"]
del sorted_bottom5_df["level_0"]

sorted_bottom5_df.rename(columns={"school":"School Name","type":"School Type"}, inplace=True)

sorted_bottom5_df = sorted_bottom5_df[["School Name","School Type","Total Students","Total School Budget","Per Student Budget","Avg Math Score","Avg Reading Score","% Passing Math","% Passing Reading","Overall Passing Rate"]]

sorted_bottom5_df.head()
#bottom5_df.reset_index()
#bottom5_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.06%</td>
      <td>83.98%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.35%</td>
      <td>83.82%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.80%</td>
      <td>83.81%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.84%</td>
      <td>84.04%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.36%</td>
      <td>83.73%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################################################################
#
# Math Scores by Grade
#
#################################################################
```


```python
# Math Scores by Grade

# get sum of the math score per grade

MathScoreByGrade_df= pd.DataFrame(students_df.groupby(["school","grade"])["math_score"].sum())
MathScoreByGrade_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>math_score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>95399</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>96972</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>78634</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>112388</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <th>10th</th>
      <td>38750</td>
    </tr>
  </tbody>
</table>
</div>




```python
StudentCountByGrade_df=pd.DataFrame(students_df.groupby(["school","grade"]).count())
del StudentCountByGrade_df["name"]
del StudentCountByGrade_df["gender"]
del StudentCountByGrade_df["math_score"]
del StudentCountByGrade_df["reading_score"]
StudentCountByGrade_df.rename(columns={"Student ID":"Student Count"},inplace=True)
StudentCountByGrade_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Student Count</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>1239</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>1251</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>1028</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>1458</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <th>10th</th>
      <td>466</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge Math score per grade info with Student count
#MathScoreByGrade_df.reset_index(drop=True,inplace=True)
#StudentCountByGrade_df.reset_index(drop=True,inplace=True)

MathScoreByGrade_df.reset_index(inplace=True)
StudentCountByGrade_df.reset_index(inplace=True)

merged_math_score_df = pd.merge(StudentCountByGrade_df,MathScoreByGrade_df, on=["school","grade"])

#merged_math_score_df.drop("grade_y", axis=1, inplace=True)
#merged_math_score_df.rename(columns={"grade_x":"Grade"}, inplace=True)
#merged_math_score_df.rename(columns={"name":"Student Count"}, inplace=True)

merged_math_score_df["Avg Math Score Per Grade"] = merged_math_score_df["math_score"] /  merged_math_score_df["Student Count"]
merged_math_score_df["Avg Math Score Per Grade"] = merged_math_score_df["Avg Math Score Per Grade"].map("{0:,.2f}%".format)
#merged_math_score_df.reset_index()
```


```python
merged_math_score_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>grade</th>
      <th>Student Count</th>
      <th>math_score</th>
      <th>Avg Math Score Per Grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>10th</td>
      <td>1239</td>
      <td>95399</td>
      <td>76.996772</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bailey High School</td>
      <td>11th</td>
      <td>1251</td>
      <td>96972</td>
      <td>77.515588</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bailey High School</td>
      <td>12th</td>
      <td>1028</td>
      <td>78634</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bailey High School</td>
      <td>9th</td>
      <td>1458</td>
      <td>112388</td>
      <td>77.083676</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cabrera High School</td>
      <td>10th</td>
      <td>466</td>
      <td>38750</td>
      <td>83.154506</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################################################################
#
# Reading Scores by Grade
#
#################################################################
```


```python
# Reading Scores by Grade

# get sum of the reading score per grade

ReadingScoreByGrade_df= pd.DataFrame(students_df.groupby(["school","grade"])["reading_score"].sum())
ReadingScoreByGrade_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>reading_score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>100244</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>101263</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83178</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>118540</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <th>10th</th>
      <td>39262</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge reading score per grade info with Student count

#StudentCountByGrade_df.reset_index(drop=True,inplace=True)

ReadingScoreByGrade_df.reset_index(inplace=True)
StudentCountByGrade_df.reset_index(inplace=True)

merged_reading_score_df = pd.merge(StudentCountByGrade_df,ReadingScoreByGrade_df, on=["school","grade"])

merged_reading_score_df["Avg Reading Score Per Grade"] = merged_reading_score_df["reading_score"] /  merged_reading_score_df["Student Count"]
merged_reading_score_df["Avg Reading Score Per Grade"] = merged_reading_score_df["Avg Reading Score Per Grade"].map("{0:,.2f}%".format)

merged_reading_score_df.reset_index()
del merged_reading_score_df["index"]
merged_reading_score_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>grade</th>
      <th>Student Count</th>
      <th>reading_score</th>
      <th>Avg Reading Score Per Grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>10th</td>
      <td>1239</td>
      <td>100244</td>
      <td>80.91%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bailey High School</td>
      <td>11th</td>
      <td>1251</td>
      <td>101263</td>
      <td>80.95%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bailey High School</td>
      <td>12th</td>
      <td>1028</td>
      <td>83178</td>
      <td>80.91%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bailey High School</td>
      <td>9th</td>
      <td>1458</td>
      <td>118540</td>
      <td>81.30%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cabrera High School</td>
      <td>10th</td>
      <td>466</td>
      <td>39262</td>
      <td>84.25%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################################################################
#
# Scores by School Spending
#
#################################################################
```


```python

bins = [550, 580, 610, 640, 670]
group_names = ['Low', 'Okay', 'Good', 'Great']
Category = pd.cut(school_summary_df['Per Student Budget'], bins, labels=group_names)

school_summary_df['Category'] = pd.cut(school_summary_df['Per Student Budget'], bins, labels=group_names)
school_summary_df = school_summary_df[["School Name","School Type","Total Students","Total School Budget","Per Student Budget","Category","Avg Math Score","Avg Reading Score","% Passing Math","% Passing Reading","Overall Passing Rate"]]

school_summary_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Category</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>Good</td>
      <td>77.05%</td>
      <td>81.03%</td>
      <td>77.91%</td>
      <td>94.55%</td>
      <td>86.23%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>Okay</td>
      <td>83.06%</td>
      <td>83.98%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>Good</td>
      <td>76.71%</td>
      <td>81.16%</td>
      <td>77.18%</td>
      <td>94.54%</td>
      <td>85.86%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>Great</td>
      <td>77.10%</td>
      <td>80.75%</td>
      <td>78.20%</td>
      <td>93.87%</td>
      <td>86.04%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>Good</td>
      <td>83.35%</td>
      <td>83.82%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>Great</td>
      <td>77.29%</td>
      <td>80.93%</td>
      <td>77.73%</td>
      <td>94.61%</td>
      <td>86.17%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>Okay</td>
      <td>83.80%</td>
      <td>83.81%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>Great</td>
      <td>76.63%</td>
      <td>81.18%</td>
      <td>77.72%</td>
      <td>94.48%</td>
      <td>86.10%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>Great</td>
      <td>77.07%</td>
      <td>80.97%</td>
      <td>77.97%</td>
      <td>94.48%</td>
      <td>86.22%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>Okay</td>
      <td>83.84%</td>
      <td>84.04%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>Good</td>
      <td>76.84%</td>
      <td>80.74%</td>
      <td>77.94%</td>
      <td>94.62%</td>
      <td>86.28%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>Okay</td>
      <td>83.36%</td>
      <td>83.73%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>Good</td>
      <td>83.42%</td>
      <td>83.85%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>Low</td>
      <td>83.27%</td>
      <td>83.99%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>Okay</td>
      <td>83.68%</td>
      <td>83.95%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################################################################
#
# Scores by School Size
#
#################################################################
```


```python
bins = [400, 2000, 3600, 5200]
group_names = ['Small', 'Medium', 'Large']
Size = pd.cut(school_summary_df['Total Students'], bins, labels=group_names)

school_summary_df['Size'] = pd.cut(school_summary_df['Total Students'], bins, labels=group_names)
school_summary_df = school_summary_df[["Size","School Type","School Name","Avg Math Score","Avg Reading Score","% Passing Math","% Passing Reading","Overall Passing Rate"]]

school_summary_df['Overall Passing Rate'] = school_summary_df['Overall Passing Rate'].replace('%','',regex=True).astype('float')/100
school_summary_df['% Passing Reading'] = school_summary_df['% Passing Reading'].replace('%','',regex=True).astype('float')/100
school_summary_df['% Passing Math'] = school_summary_df['% Passing Math'].replace('%','',regex=True).astype('float')/100
school_summary_df['Avg Reading Score'] = school_summary_df['Avg Reading Score'].replace('%','',regex=True).astype('float')/100
school_summary_df['Avg Math Score'] = school_summary_df['Avg Math Score'].replace('%','',regex=True).astype('float')/100

school_summary_df.groupby("Size").count()

smallCount = school_summary_df["Avg Math Score"].loc[school_summary_df["Size"] == "Small"].count()
mediumCount = school_summary_df["Avg Math Score"].loc[school_summary_df["Size"] == "Medium"].count()
largeCount = school_summary_df["Avg Math Score"].loc[school_summary_df["Size"] == "Large"].count()

final_df = pd.DataFrame(school_summary_df[["Size",
                                                 "Avg Math Score",
                                                 "Avg Reading Score",
                                                 "% Passing Math",
                                                 "% Passing Reading",
                                                 "Overall Passing Rate"]])

final_df = pd.DataFrame(school_summary_df.groupby(["Size"]).sum())

smallAvgMathScore = (school_summary_df["Avg Math Score"].loc[school_summary_df["Size"] == "Small"].sum() /smallCount) * 100
final_df.loc["Small","Avg Math Score"] = smallAvgMathScore


smallAvgReadingScore = (school_summary_df["Avg Reading Score"].loc[school_summary_df["Size"] == "Small"].sum() / smallCount) * 100
final_df.loc["Small","Avg Reading Score"] = smallAvgReadingScore


smallPertMathScore = (school_summary_df["% Passing Math"].loc[school_summary_df["Size"] == "Small"].sum() / smallCount) * 100
final_df.loc["Small","% Passing Math"] = smallPertMathScore


smallrPertReadingScore = (school_summary_df["% Passing Reading"].loc[school_summary_df["Size"] == "Small"].sum() / smallCount) * 100
final_df.loc["Small","% Passing Reading"] = smallrPertReadingScore

smallOverAllScore = (school_summary_df["Overall Passing Rate"].loc[school_summary_df["Size"] == "Small"].sum() / smallCount) * 100
final_df.loc["Small","Overall Passing Rate"] = smallOverAllScore


# Medium

mediumAvgMathScore = (school_summary_df["Avg Math Score"].loc[school_summary_df["Size"] == "Medium"].sum() / mediumCount) * 100
final_df.loc["Medium","Avg Math Score"] = mediumAvgMathScore


mediumAvgReadingScore = (school_summary_df["Avg Reading Score"].loc[school_summary_df["Size"] == "Medium"].sum() / mediumCount) * 100
final_df.loc["Medium","Avg Reading Score"] = mediumAvgReadingScore


mediumPertMathScore = (school_summary_df["% Passing Math"].loc[school_summary_df["Size"] == "Medium"].sum() / mediumCount) * 100
final_df.loc["Medium","% Passing Math"] = mediumPertMathScore


mediumPertReadingScore = (school_summary_df["% Passing Reading"].loc[school_summary_df["Size"] == "Medium"].sum() / mediumCount) * 100
final_df.loc["Medium","% Passing Reading"] = mediumPertReadingScore

mediumOverAllScore = (school_summary_df["Overall Passing Rate"].loc[school_summary_df["Size"] == "Medium"].sum() / mediumCount) * 100
final_df.loc["Medium","Overall Passing Rate"] = mediumOverAllScore

# LargeScore

largeAvgMathScore = (school_summary_df["Avg Math Score"].loc[school_summary_df["Size"] == "Medium"].sum() / largeCount) * 100
final_df.loc["Large","Avg Math Score"] = largeAvgMathScore


largeAvgReadingScore = (school_summary_df["Avg Reading Score"].loc[school_summary_df["Size"] == "Medium"].sum() / largeCount) * 100
final_df.loc["Large","Avg Reading Score"] = largeAvgReadingScore


largePertMathScore = (school_summary_df["% Passing Math"].loc[school_summary_df["Size"] == "Medium"].sum() / largeCount) * 100
final_df.loc["Large","% Passing Math"] = largePertMathScore


largePertReadingScore = (school_summary_df["% Passing Reading"].loc[school_summary_df["Size"] == "Medium"].sum() / largeCount) * 100
final_df.loc["Large","% Passing Reading"] = largePertReadingScore

largeOverAllScore = (school_summary_df["Overall Passing Rate"].loc[school_summary_df["Size"] == "Medium"].sum() / largeCount) * 100
final_df.loc["Large","Overall Passing Rate"] = largeOverAllScore

final_df["Avg Math Score"] = final_df["Avg Math Score"].map("{0:,.2f}%".format)
final_df["Avg Reading Score"] = final_df["Avg Reading Score"].map("{0:,.2f}%".format)
final_df["% Passing Math"] = final_df["% Passing Math"].map("{0:,.2f}%".format)
final_df["% Passing Reading"] = final_df["% Passing Reading"].map("{0:,.2f}%".format)
final_df["Overall Passing Rate"] = final_df["Overall Passing Rate"].map("{0:,.2f}%".format)

#final_df.head()
```

    C:\Users\MH\Anaconda3\lib\site-packages\ipykernel_launcher.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    C:\Users\MH\Anaconda3\lib\site-packages\ipykernel_launcher.py:9: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      if __name__ == '__main__':
    C:\Users\MH\Anaconda3\lib\site-packages\ipykernel_launcher.py:10: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      # Remove the CWD from sys.path while we load stuff.
    C:\Users\MH\Anaconda3\lib\site-packages\ipykernel_launcher.py:11: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      # This is added back by InteractiveShellApp.init_path()
    C:\Users\MH\Anaconda3\lib\site-packages\ipykernel_launcher.py:12: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      if sys.path[0] == '':
    


```python
#################################################################
#
# Scores by School Type
#
#################################################################
```


```python
School_Type_df = pd.DataFrame(school_summary_df[["School Type",
                                                 "Avg Math Score",
                                                 "Avg Reading Score",
                                                 "% Passing Math",
                                                 "% Passing Reading",
                                                 "Overall Passing Rate"]])


School_Type_df['Overall Passing Rate'] = School_Type_df['Overall Passing Rate'].replace('%','',regex=True).astype('float')/100
School_Type_df['% Passing Reading'] = School_Type_df['% Passing Reading'].replace('%','',regex=True).astype('float')/100
School_Type_df['% Passing Math'] = School_Type_df['% Passing Math'].replace('%','',regex=True).astype('float')/100
School_Type_df['Avg Reading Score'] = School_Type_df['Avg Reading Score'].replace('%','',regex=True).astype('float')/100
School_Type_df['Avg Math Score'] = School_Type_df['Avg Math Score'].replace('%','',regex=True).astype('float')/100

School_Type_df.groupby("School Type").count()

charterCount = School_Type_df["Avg Math Score"].loc[School_Type_df["School Type"] == "Charter"].count()
districtCount = School_Type_df["Avg Math Score"].loc[School_Type_df["School Type"] == "District"].count()

final_df = pd.DataFrame(School_Type_df[["School Type",
                                                 "Avg Math Score",
                                                 "Avg Reading Score",
                                                 "% Passing Math",
                                                 "% Passing Reading",
                                                 "Overall Passing Rate"]])

final_df = pd.DataFrame(School_Type_df.groupby(["School Type"]).sum())

charterAvgMathScore = (School_Type_df["Avg Math Score"].loc[School_Type_df["School Type"] == "Charter"].sum() / charterCount) * 100
final_df.loc["Charter","Avg Math Score"] = charterAvgMathScore


charterAvgReadingScore = (School_Type_df["Avg Reading Score"].loc[School_Type_df["School Type"] == "Charter"].sum() / charterCount) * 100
final_df.loc["Charter","Avg Reading Score"] = charterAvgReadingScore


charterPertMathScore = (School_Type_df["% Passing Math"].loc[School_Type_df["School Type"] == "Charter"].sum() / charterCount) * 100
final_df.loc["Charter","% Passing Math"] = charterPertMathScore


charterPertReadingScore = (School_Type_df["% Passing Reading"].loc[School_Type_df["School Type"] == "Charter"].sum() / charterCount) * 100
final_df.loc["Charter","% Passing Reading"] = charterPertReadingScore


charterOverAllScore = (School_Type_df["Overall Passing Rate"].loc[School_Type_df["School Type"] == "Charter"].sum() / charterCount) * 100
final_df.loc["Charter","Overall Passing Rate"] = charterOverAllScore



districtAvgMathScore = (School_Type_df["Avg Math Score"].loc[School_Type_df["School Type"] == "District"].sum() / charterCount) * 100
final_df.loc["District","Avg Math Score"] = districtAvgMathScore 


districtAvgReadingScore = (School_Type_df["Avg Reading Score"].loc[School_Type_df["School Type"] == "District"].sum() / charterCount) * 100
final_df.loc["District","Avg Reading Score"] = districtAvgReadingScore 


districtPertMathScore = (School_Type_df["% Passing Math"].loc[School_Type_df["School Type"] == "District"].sum() / charterCount) * 100
final_df.loc["District","% Passing Math"] = districtPertMathScore 


districtPertReadingScore = (School_Type_df["% Passing Reading"].loc[School_Type_df["School Type"] == "District"].sum() / charterCount) * 100
final_df.loc["District","% Passing Reading"] = districtPertReadingScore 


districtOverAllScore = (School_Type_df["Overall Passing Rate"].loc[School_Type_df["School Type"] == "District"].sum() / charterCount) * 100
final_df.loc["District","Overall Passing Rate"] = districtOverAllScore

final_df["Avg Math Score"] = (final_df["Avg Math Score"]*100).map("{0:,.2f}%".format)
final_df["Avg Reading Score"] = (final_df["Avg Reading Score"]*100).map("{0:,.2f}%".format)
final_df["% Passing Math"] = (final_df["% Passing Math"]*100).map("{0:,.2f}%".format)
final_df["% Passing Reading"] = (final_df["% Passing Reading"]*100).map("{0:,.2f}%".format)
final_df["Overall Passing Rate"] = (final_df["Overall Passing Rate"]*100).map("{0:,.2f}%".format)

final_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.47%</td>
      <td>83.90%</td>
      <td>100.00%</td>
      <td>100.00%</td>
      <td>100.00%</td>
    </tr>
    <tr>
      <th>District</th>
      <td>67.34%</td>
      <td>70.84%</td>
      <td>68.08%</td>
      <td>82.64%</td>
      <td>75.36%</td>
    </tr>
  </tbody>
</table>
</div>


