```python
import pandas as pd
```


```python
df = pd.read_csv(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\Flavors.csv")
df
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
      <th>Flavor</th>
      <th>Base Flavor</th>
      <th>Liked</th>
      <th>Flavor Rating</th>
      <th>Texture Rating</th>
      <th>Total Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mint Chocolate Chip</td>
      <td>Vanilla</td>
      <td>Yes</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chocolate</td>
      <td>Chocolate</td>
      <td>Yes</td>
      <td>8.8</td>
      <td>7.6</td>
      <td>16.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Vanilla</td>
      <td>Vanilla</td>
      <td>No</td>
      <td>4.7</td>
      <td>5.0</td>
      <td>9.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Cookie Dough</td>
      <td>Vanilla</td>
      <td>Yes</td>
      <td>6.9</td>
      <td>6.5</td>
      <td>13.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rocky Road</td>
      <td>Chocolate</td>
      <td>Yes</td>
      <td>8.2</td>
      <td>7.0</td>
      <td>15.2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Pistachio</td>
      <td>Vanilla</td>
      <td>No</td>
      <td>2.3</td>
      <td>3.4</td>
      <td>5.7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cake Batter</td>
      <td>Vanilla</td>
      <td>Yes</td>
      <td>6.5</td>
      <td>6.0</td>
      <td>12.5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Neapolitan</td>
      <td>Vanilla</td>
      <td>No</td>
      <td>3.8</td>
      <td>5.0</td>
      <td>8.8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Chocolte Fudge Brownie</td>
      <td>Chocolate</td>
      <td>Yes</td>
      <td>8.2</td>
      <td>7.1</td>
      <td>15.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating':[  'mean','sum']})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2" halign="left">Flavor Rating</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>sum</th>
    </tr>
    <tr>
      <th>Base Flavor</th>
      <th>Liked</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chocolate</th>
      <th>Yes</th>
      <td>8.4</td>
      <td>25.2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Vanilla</th>
      <th>No</th>
      <td>3.6</td>
      <td>10.8</td>
    </tr>
    <tr>
      <th>Yes</th>
      <td>7.8</td>
      <td>23.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Base Flavor').sum()
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
      <th>Flavor</th>
      <th>Liked</th>
      <th>Flavor Rating</th>
      <th>Texture Rating</th>
      <th>Total Rating</th>
    </tr>
    <tr>
      <th>Base Flavor</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chocolate</th>
      <td>ChocolateRocky RoadChocolte Fudge Brownie</td>
      <td>YesYesYes</td>
      <td>25.2</td>
      <td>21.7</td>
      <td>47.1</td>
    </tr>
    <tr>
      <th>Vanilla</th>
      <td>Mint Chocolate ChipVanillaCookie DoughPistachi...</td>
      <td>YesNoYesNoYesNo</td>
      <td>34.2</td>
      <td>33.9</td>
      <td>68.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Base Flavor').count()
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
      <th>Flavor</th>
      <th>Liked</th>
      <th>Flavor Rating</th>
      <th>Texture Rating</th>
      <th>Total Rating</th>
    </tr>
    <tr>
      <th>Base Flavor</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chocolate</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Vanilla</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Base Flavor').min()
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
      <th>Flavor</th>
      <th>Liked</th>
      <th>Flavor Rating</th>
      <th>Texture Rating</th>
      <th>Total Rating</th>
    </tr>
    <tr>
      <th>Base Flavor</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chocolate</th>
      <td>Chocolate</td>
      <td>Yes</td>
      <td>8.2</td>
      <td>7.0</td>
      <td>15.2</td>
    </tr>
    <tr>
      <th>Vanilla</th>
      <td>Cake Batter</td>
      <td>No</td>
      <td>2.3</td>
      <td>3.4</td>
      <td>5.7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Base Flavor').max()
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
      <th>Flavor</th>
      <th>Liked</th>
      <th>Flavor Rating</th>
      <th>Texture Rating</th>
      <th>Total Rating</th>
    </tr>
    <tr>
      <th>Base Flavor</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Chocolate</th>
      <td>Rocky Road</td>
      <td>Yes</td>
      <td>8.8</td>
      <td>7.6</td>
      <td>16.6</td>
    </tr>
    <tr>
      <th>Vanilla</th>
      <td>Vanilla</td>
      <td>Yes</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>18.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
