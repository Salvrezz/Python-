```python
import pandas as pd
```


```python
df1 = pd.read_csv(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\LOTR.csv")
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Skills</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.read_csv(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\LOTR 2.csv")
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006</td>
      <td>Legolas</td>
      <td>2931</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>Elrond</td>
      <td>6520</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1008</td>
      <td>Barromir</td>
      <td>51</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.merge(df2, how = 'inner', on = 'FellowshipID')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName_x</th>
      <th>Skills</th>
      <th>FirstName_y</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>Frodo</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>Samwise</td>
      <td>39</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.merge(df2, how = 'outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Skills</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1006</td>
      <td>Legolas</td>
      <td>NaN</td>
      <td>2931.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1007</td>
      <td>Elrond</td>
      <td>NaN</td>
      <td>6520.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1008</td>
      <td>Barromir</td>
      <td>NaN</td>
      <td>51.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.merge(df2, how = 'left')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Skills</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.merge(df2, how = 'right')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Skills</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006</td>
      <td>Legolas</td>
      <td>NaN</td>
      <td>2931</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>Elrond</td>
      <td>NaN</td>
      <td>6520</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1008</td>
      <td>Barromir</td>
      <td>NaN</td>
      <td>51</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.merge(df2, how = 'cross')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID_x</th>
      <th>FirstName_x</th>
      <th>Skills</th>
      <th>FellowshipID_y</th>
      <th>FirstName_y</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>1001</td>
      <td>Frodo</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>1002</td>
      <td>Samwise</td>
      <td>39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>1006</td>
      <td>Legolas</td>
      <td>2931</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>1007</td>
      <td>Elrond</td>
      <td>6520</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>1008</td>
      <td>Barromir</td>
      <td>51</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>1001</td>
      <td>Frodo</td>
      <td>50</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>1002</td>
      <td>Samwise</td>
      <td>39</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>1006</td>
      <td>Legolas</td>
      <td>2931</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>1007</td>
      <td>Elrond</td>
      <td>6520</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>1008</td>
      <td>Barromir</td>
      <td>51</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>1001</td>
      <td>Frodo</td>
      <td>50</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>1002</td>
      <td>Samwise</td>
      <td>39</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>1006</td>
      <td>Legolas</td>
      <td>2931</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>1007</td>
      <td>Elrond</td>
      <td>6520</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>1008</td>
      <td>Barromir</td>
      <td>51</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>1001</td>
      <td>Frodo</td>
      <td>50</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>1002</td>
      <td>Samwise</td>
      <td>39</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>1006</td>
      <td>Legolas</td>
      <td>2931</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>1007</td>
      <td>Elrond</td>
      <td>6520</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>1008</td>
      <td>Barromir</td>
      <td>51</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_left', rsuffix = '_right', how = 'outer')
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FirstName_left</th>
      <th>Skills</th>
      <th>FirstName_right</th>
      <th>Age</th>
    </tr>
    <tr>
      <th>FellowshipID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1001</th>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>Frodo</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1002</th>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>Samwise</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>1003</th>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1004</th>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1006</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Legolas</td>
      <td>2931.0</td>
    </tr>
    <tr>
      <th>1007</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Elrond</td>
      <td>6520.0</td>
    </tr>
    <tr>
      <th>1008</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Barromir</td>
      <td>51.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1,df2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Skills</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>NaN</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>NaN</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006</td>
      <td>Legolas</td>
      <td>NaN</td>
      <td>2931.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>Elrond</td>
      <td>NaN</td>
      <td>6520.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1008</td>
      <td>Barromir</td>
      <td>NaN</td>
      <td>51.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1,df2], join = 'inner')

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>Gandalf</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>Pippin</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006</td>
      <td>Legolas</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>Elrond</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1008</td>
      <td>Barromir</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1,df2], join = 'outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Skills</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>NaN</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>NaN</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006</td>
      <td>Legolas</td>
      <td>NaN</td>
      <td>2931.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>Elrond</td>
      <td>NaN</td>
      <td>6520.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1008</td>
      <td>Barromir</td>
      <td>NaN</td>
      <td>51.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1,df2], join = 'inner',axis = 1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Skills</th>
      <th>FellowshipID</th>
      <th>FirstName</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>Frodo</td>
      <td>Hiding</td>
      <td>1001</td>
      <td>Frodo</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>Samwise</td>
      <td>Gardening</td>
      <td>1002</td>
      <td>Samwise</td>
      <td>39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>Gandalf</td>
      <td>Spells</td>
      <td>1006</td>
      <td>Legolas</td>
      <td>2931</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>Pippin</td>
      <td>Fireworks</td>
      <td>1007</td>
      <td>Elrond</td>
      <td>6520</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
