```python
import pandas as pd
```


```python
pd.read_csv(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\countries of the world.csv")
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
      <th>Country</th>
      <th>Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>ASIA (EX. NEAR EAST)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>EASTERN EUROPE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>NORTHERN AFRICA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>OCEANIA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>WESTERN EUROPE</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>222</th>
      <td>West Bank</td>
      <td>NEAR EAST</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Western Sahara</td>
      <td>NORTHERN AFRICA</td>
    </tr>
    <tr>
      <th>224</th>
      <td>Yemen</td>
      <td>NEAR EAST</td>
    </tr>
    <tr>
      <th>225</th>
      <td>Zambia</td>
      <td>SUB-SAHARAN AFRICA</td>
    </tr>
    <tr>
      <th>226</th>
      <td>Zimbabwe</td>
      <td>SUB-SAHARAN AFRICA</td>
    </tr>
  </tbody>
</table>
<p>227 rows × 2 columns</p>
</div>




```python
pd.read_json(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\json_sample.json")
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
      <th>12 Strong</th>
      <th>A Fantastic Woman (Una Mujer Fantástica)</th>
      <th>All The Money In The World</th>
      <th>Bilal: A New Breed Of Hero</th>
      <th>Call Me By Your Name</th>
      <th>Darkest Hour</th>
      <th>Den Of Thieves</th>
      <th>Ferdinand</th>
      <th>Fifty Shades Freed</th>
      <th>Film Stars Don'T Die In Liverpool</th>
      <th>Forever My Girl</th>
      <th>Golden Exits</th>
      <th>Hostiles</th>
      <th>I, Tonya</th>
      <th>Insidious: The Last Key</th>
      <th>Jumanji: Welcome To The Jungle</th>
      <th>Mary And The Witch'S Flower</th>
      <th>Maze Runner: The Death Cure</th>
      <th>Molly'S Game</th>
      <th>Paddington 2</th>
      <th>Padmaavat</th>
      <th>Permission</th>
      <th>Peter Rabbit</th>
      <th>Phantom Thread</th>
      <th>Pitch Perfect 3</th>
      <th>Proud Mary</th>
      <th>Sanpo Suru Shinryakusha</th>
      <th>Star Wars: The Last Jedi</th>
      <th>The 15:17 To Paris</th>
      <th>The Commuter</th>
      <th>The Disaster Artist</th>
      <th>The Greatest Showman</th>
      <th>The Insult (L'Insulte)</th>
      <th>The Post</th>
      <th>The Shape Of Water</th>
      <th>Three Billboards Outside Ebbing, Missouri</th>
      <th>Till The End Of The World</th>
      <th>Winchester</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>{'Genre': 'Action', 'Gross': '$453,173', 'IMDB...</td>
      <td>{'popcornscore': 83, 'rating': 'R', 'tomatosco...</td>
      <td>{'popcornscore': 71, 'rating': 'R', 'tomatosco...</td>
      <td>{'popcornscore': 91, 'rating': 'PG13', 'tomato...</td>
      <td>{'popcornscore': 87, 'rating': 'R', 'tomatosco...</td>
      <td>{'popcornscore': 84, 'rating': 'PG13', 'tomato...</td>
      <td>{'Genre': 'Action', 'Gross': '$491,898', 'IMDB...</td>
      <td>{'popcornscore': 49, 'rating': 'PG', 'tomatosc...</td>
      <td>{'Genre': 'Drama', 'Gross': 'unknown', 'IMDB M...</td>
      <td>{'popcornscore': 69, 'rating': 'R', 'tomatosco...</td>
      <td>{'popcornscore': 91, 'rating': 'PG', 'tomatosc...</td>
      <td>{'Genre': 'Drama', 'Gross': 'unknown', 'IMDB M...</td>
      <td>{'Genre': 'Adventure', 'Gross': '$548,886', 'I...</td>
      <td>{'popcornscore': 89, 'rating': 'R', 'tomatosco...</td>
      <td>{'popcornscore': 51, 'rating': 'PG13', 'tomato...</td>
      <td>{'Genre': 'Action', 'Gross': '$760,867', 'IMDB...</td>
      <td>{'popcornscore': 78, 'rating': 'PG', 'tomatosc...</td>
      <td>{'Genre': 'Action', 'Gross': '$720,463', 'IMDB...</td>
      <td>{'popcornscore': 85, 'rating': 'R', 'tomatosco...</td>
      <td>{'Genre': 'Animation', 'Gross': '$184,414', 'I...</td>
      <td>{'popcornscore': 62, 'rating': 'NR', 'tomatosc...</td>
      <td>{'Genre': 'Comedy', 'Gross': 'unknown', 'IMDB ...</td>
      <td>{'Genre': 'Animation', 'Gross': 'unknown', 'IM...</td>
      <td>{'popcornscore': 68, 'rating': 'R', 'tomatosco...</td>
      <td>{'popcornscore': 52, 'rating': 'PG13', 'tomato...</td>
      <td>{'popcornscore': 56, 'rating': 'R', 'tomatosco...</td>
      <td>{'Genre': 'Drama', 'Gross': 'unknown', 'IMDB M...</td>
      <td>{'popcornscore': 48, 'rating': 'PG13', 'tomato...</td>
      <td>{'Genre': 'Drama', 'Gross': 'unknown', 'IMDB M...</td>
      <td>{'popcornscore': 48, 'rating': 'PG13', 'tomato...</td>
      <td>{'popcornscore': 89, 'rating': 'R', 'tomatosco...</td>
      <td>{'Genre': 'Biography', 'Gross': '$627,248', 'I...</td>
      <td>{'popcornscore': 86, 'rating': 'R', 'tomatosco...</td>
      <td>{'Genre': 'Biography', 'Gross': '$463,228', 'I...</td>
      <td>{'Genre': 'Adventure', 'Gross': '$448,287', 'I...</td>
      <td>{'popcornscore': 87, 'rating': 'R', 'tomatosco...</td>
      <td>{'popcornscore': -1, 'rating': 'NR', 'tomatosc...</td>
      <td>{'Genre': 'Biography', 'Gross': '$696,786', 'I...</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_excel(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\world_population_excel_workbook.xlsx")
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
      <th>Rank</th>
      <th>CCA3</th>
      <th>Country</th>
      <th>Capital</th>
      <th>Continent</th>
      <th>2022 Population</th>
      <th>2020 Population</th>
      <th>2015 Population</th>
      <th>2010 Population</th>
      <th>2000 Population</th>
      <th>1990 Population</th>
      <th>1980 Population</th>
      <th>1970 Population</th>
      <th>Area (kmÂ²)</th>
      <th>Density (per kmÂ²)</th>
      <th>Growth Rate</th>
      <th>World Population Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>36</td>
      <td>AFG</td>
      <td>Afghanistan</td>
      <td>Kabul</td>
      <td>Asia</td>
      <td>41128771</td>
      <td>38972230</td>
      <td>33753499</td>
      <td>28189672</td>
      <td>19542982</td>
      <td>10694796</td>
      <td>12486631</td>
      <td>10752971</td>
      <td>652230</td>
      <td>63.0587</td>
      <td>1.0257</td>
      <td>0.52</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138</td>
      <td>ALB</td>
      <td>Albania</td>
      <td>Tirana</td>
      <td>Europe</td>
      <td>2842321</td>
      <td>2866849</td>
      <td>2882481</td>
      <td>2913399</td>
      <td>3182021</td>
      <td>3295066</td>
      <td>2941651</td>
      <td>2324731</td>
      <td>28748</td>
      <td>98.8702</td>
      <td>0.9957</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>DZA</td>
      <td>Algeria</td>
      <td>Algiers</td>
      <td>Africa</td>
      <td>44903225</td>
      <td>43451666</td>
      <td>39543154</td>
      <td>35856344</td>
      <td>30774621</td>
      <td>25518074</td>
      <td>18739378</td>
      <td>13795915</td>
      <td>2381741</td>
      <td>18.8531</td>
      <td>1.0164</td>
      <td>0.56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>213</td>
      <td>ASM</td>
      <td>American Samoa</td>
      <td>Pago Pago</td>
      <td>Oceania</td>
      <td>44273</td>
      <td>46189</td>
      <td>51368</td>
      <td>54849</td>
      <td>58230</td>
      <td>47818</td>
      <td>32886</td>
      <td>27075</td>
      <td>199</td>
      <td>222.4774</td>
      <td>0.9831</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>203</td>
      <td>AND</td>
      <td>Andorra</td>
      <td>Andorra la Vella</td>
      <td>Europe</td>
      <td>79824</td>
      <td>77700</td>
      <td>71746</td>
      <td>71519</td>
      <td>66097</td>
      <td>53569</td>
      <td>35611</td>
      <td>19860</td>
      <td>468</td>
      <td>170.5641</td>
      <td>1.0100</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>229</th>
      <td>226</td>
      <td>WLF</td>
      <td>Wallis and Futuna</td>
      <td>Mata-Utu</td>
      <td>Oceania</td>
      <td>11572</td>
      <td>11655</td>
      <td>12182</td>
      <td>13142</td>
      <td>14723</td>
      <td>13454</td>
      <td>11315</td>
      <td>9377</td>
      <td>142</td>
      <td>81.4930</td>
      <td>0.9953</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>230</th>
      <td>172</td>
      <td>ESH</td>
      <td>Western Sahara</td>
      <td>El AaiÃºn</td>
      <td>Africa</td>
      <td>575986</td>
      <td>556048</td>
      <td>491824</td>
      <td>413296</td>
      <td>270375</td>
      <td>178529</td>
      <td>116775</td>
      <td>76371</td>
      <td>266000</td>
      <td>2.1654</td>
      <td>1.0184</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>231</th>
      <td>46</td>
      <td>YEM</td>
      <td>Yemen</td>
      <td>Sanaa</td>
      <td>Asia</td>
      <td>33696614</td>
      <td>32284046</td>
      <td>28516545</td>
      <td>24743946</td>
      <td>18628700</td>
      <td>13375121</td>
      <td>9204938</td>
      <td>6843607</td>
      <td>527968</td>
      <td>63.8232</td>
      <td>1.0217</td>
      <td>0.42</td>
    </tr>
    <tr>
      <th>232</th>
      <td>63</td>
      <td>ZMB</td>
      <td>Zambia</td>
      <td>Lusaka</td>
      <td>Africa</td>
      <td>20017675</td>
      <td>18927715</td>
      <td>16248230</td>
      <td>13792086</td>
      <td>9891136</td>
      <td>7686401</td>
      <td>5720438</td>
      <td>4281671</td>
      <td>752612</td>
      <td>26.5976</td>
      <td>1.0280</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>233</th>
      <td>74</td>
      <td>ZWE</td>
      <td>Zimbabwe</td>
      <td>Harare</td>
      <td>Africa</td>
      <td>16320537</td>
      <td>15669666</td>
      <td>14154937</td>
      <td>12839771</td>
      <td>11834676</td>
      <td>10113893</td>
      <td>7049926</td>
      <td>5202918</td>
      <td>390757</td>
      <td>41.7665</td>
      <td>1.0204</td>
      <td>0.20</td>
    </tr>
  </tbody>
</table>
<p>234 rows × 17 columns</p>
</div>




```python
pd.read_table(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\countries of the world.txt",sep = '\t')
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
      <th>Country</th>
      <th>Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>ASIA (EX. NEAR EAST)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>EASTERN EUROPE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>NORTHERN AFRICA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>OCEANIA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>WESTERN EUROPE</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>222</th>
      <td>West Bank</td>
      <td>NEAR EAST</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Western Sahara</td>
      <td>NORTHERN AFRICA</td>
    </tr>
    <tr>
      <th>224</th>
      <td>Yemen</td>
      <td>NEAR EAST</td>
    </tr>
    <tr>
      <th>225</th>
      <td>Zambia</td>
      <td>SUB-SAHARAN AFRICA</td>
    </tr>
    <tr>
      <th>226</th>
      <td>Zimbabwe</td>
      <td>SUB-SAHARAN AFRICA</td>
    </tr>
  </tbody>
</table>
<p>227 rows × 2 columns</p>
</div>




```python
pd.read_csv(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\countries of the world.txt", sep = '\t')
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
      <th>Country</th>
      <th>Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>ASIA (EX. NEAR EAST)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>EASTERN EUROPE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>NORTHERN AFRICA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>OCEANIA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>WESTERN EUROPE</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>222</th>
      <td>West Bank</td>
      <td>NEAR EAST</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Western Sahara</td>
      <td>NORTHERN AFRICA</td>
    </tr>
    <tr>
      <th>224</th>
      <td>Yemen</td>
      <td>NEAR EAST</td>
    </tr>
    <tr>
      <th>225</th>
      <td>Zambia</td>
      <td>SUB-SAHARAN AFRICA</td>
    </tr>
    <tr>
      <th>226</th>
      <td>Zimbabwe</td>
      <td>SUB-SAHARAN AFRICA</td>
    </tr>
  </tbody>
</table>
<p>227 rows × 2 columns</p>
</div>




```python
df = pd.read_excel(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\world_population_excel_workbook.xlsx", sheet_name = "Sheet1")
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
      <th>Rank</th>
      <th>CCA3</th>
      <th>Country</th>
      <th>Capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>36</td>
      <td>AFG</td>
      <td>Afghanistan</td>
      <td>Kabul</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138</td>
      <td>ALB</td>
      <td>Albania</td>
      <td>Tirana</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>DZA</td>
      <td>Algeria</td>
      <td>Algiers</td>
    </tr>
    <tr>
      <th>3</th>
      <td>213</td>
      <td>ASM</td>
      <td>American Samoa</td>
      <td>Pago Pago</td>
    </tr>
    <tr>
      <th>4</th>
      <td>203</td>
      <td>AND</td>
      <td>Andorra</td>
      <td>Andorra la Vella</td>
    </tr>
    <tr>
      <th>5</th>
      <td>42</td>
      <td>AGO</td>
      <td>Angola</td>
      <td>Luanda</td>
    </tr>
    <tr>
      <th>6</th>
      <td>224</td>
      <td>AIA</td>
      <td>Anguilla</td>
      <td>The Valley</td>
    </tr>
    <tr>
      <th>7</th>
      <td>201</td>
      <td>ATG</td>
      <td>Antigua and Barbuda</td>
      <td>Saint Johnâ€™s</td>
    </tr>
    <tr>
      <th>8</th>
      <td>33</td>
      <td>ARG</td>
      <td>Argentina</td>
      <td>Buenos Aires</td>
    </tr>
    <tr>
      <th>9</th>
      <td>140</td>
      <td>ARM</td>
      <td>Armenia</td>
      <td>Yerevan</td>
    </tr>
    <tr>
      <th>10</th>
      <td>198</td>
      <td>ABW</td>
      <td>Aruba</td>
      <td>Oranjestad</td>
    </tr>
    <tr>
      <th>11</th>
      <td>55</td>
      <td>AUS</td>
      <td>Australia</td>
      <td>Canberra</td>
    </tr>
    <tr>
      <th>12</th>
      <td>99</td>
      <td>AUT</td>
      <td>Austria</td>
      <td>Vienna</td>
    </tr>
    <tr>
      <th>13</th>
      <td>91</td>
      <td>AZE</td>
      <td>Azerbaijan</td>
      <td>Baku</td>
    </tr>
    <tr>
      <th>14</th>
      <td>176</td>
      <td>BHS</td>
      <td>Bahamas</td>
      <td>Nassau</td>
    </tr>
    <tr>
      <th>15</th>
      <td>154</td>
      <td>BHR</td>
      <td>Bahrain</td>
      <td>Manama</td>
    </tr>
    <tr>
      <th>16</th>
      <td>8</td>
      <td>BGD</td>
      <td>Bangladesh</td>
      <td>Dhaka</td>
    </tr>
    <tr>
      <th>17</th>
      <td>186</td>
      <td>BRB</td>
      <td>Barbados</td>
      <td>Bridgetown</td>
    </tr>
    <tr>
      <th>18</th>
      <td>96</td>
      <td>BLR</td>
      <td>Belarus</td>
      <td>Minsk</td>
    </tr>
    <tr>
      <th>19</th>
      <td>81</td>
      <td>BEL</td>
      <td>Belgium</td>
      <td>Brussels</td>
    </tr>
    <tr>
      <th>20</th>
      <td>177</td>
      <td>BLZ</td>
      <td>Belize</td>
      <td>Belmopan</td>
    </tr>
    <tr>
      <th>21</th>
      <td>77</td>
      <td>BEN</td>
      <td>Benin</td>
      <td>Porto-Novo</td>
    </tr>
    <tr>
      <th>22</th>
      <td>206</td>
      <td>BMU</td>
      <td>Bermuda</td>
      <td>Hamilton</td>
    </tr>
    <tr>
      <th>23</th>
      <td>165</td>
      <td>BTN</td>
      <td>Bhutan</td>
      <td>Thimphu</td>
    </tr>
    <tr>
      <th>24</th>
      <td>80</td>
      <td>BOL</td>
      <td>Bolivia</td>
      <td>Sucre</td>
    </tr>
    <tr>
      <th>25</th>
      <td>137</td>
      <td>BIH</td>
      <td>Bosnia and Herzegovina</td>
      <td>Sarajevo</td>
    </tr>
    <tr>
      <th>26</th>
      <td>144</td>
      <td>BWA</td>
      <td>Botswana</td>
      <td>Gaborone</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>Brasilia</td>
    </tr>
    <tr>
      <th>28</th>
      <td>221</td>
      <td>VGB</td>
      <td>British Virgin Islands</td>
      <td>Road Town</td>
    </tr>
    <tr>
      <th>29</th>
      <td>175</td>
      <td>BRN</td>
      <td>Brunei</td>
      <td>Bandar Seri Begawan</td>
    </tr>
    <tr>
      <th>30</th>
      <td>108</td>
      <td>BGR</td>
      <td>Bulgaria</td>
      <td>Sofia</td>
    </tr>
    <tr>
      <th>31</th>
      <td>58</td>
      <td>BFA</td>
      <td>Burkina Faso</td>
      <td>Ouagadougou</td>
    </tr>
    <tr>
      <th>32</th>
      <td>78</td>
      <td>BDI</td>
      <td>Burundi</td>
      <td>Bujumbura</td>
    </tr>
    <tr>
      <th>33</th>
      <td>73</td>
      <td>KHM</td>
      <td>Cambodia</td>
      <td>Phnom Penh</td>
    </tr>
    <tr>
      <th>34</th>
      <td>53</td>
      <td>CMR</td>
      <td>Cameroon</td>
      <td>Yaounde</td>
    </tr>
    <tr>
      <th>35</th>
      <td>39</td>
      <td>CAN</td>
      <td>Canada</td>
      <td>Ottawa</td>
    </tr>
    <tr>
      <th>36</th>
      <td>171</td>
      <td>CPV</td>
      <td>Cape Verde</td>
      <td>Praia</td>
    </tr>
    <tr>
      <th>37</th>
      <td>205</td>
      <td>CYM</td>
      <td>Cayman Islands</td>
      <td>George Town</td>
    </tr>
    <tr>
      <th>38</th>
      <td>117</td>
      <td>CAF</td>
      <td>Central African Republic</td>
      <td>Bangui</td>
    </tr>
    <tr>
      <th>39</th>
      <td>69</td>
      <td>TCD</td>
      <td>Chad</td>
      <td>N'Djamena</td>
    </tr>
    <tr>
      <th>40</th>
      <td>65</td>
      <td>CHL</td>
      <td>Chile</td>
      <td>Santiago</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1</td>
      <td>CHN</td>
      <td>China</td>
      <td>Beijing</td>
    </tr>
    <tr>
      <th>42</th>
      <td>28</td>
      <td>COL</td>
      <td>Colombia</td>
      <td>Bogota</td>
    </tr>
    <tr>
      <th>43</th>
      <td>163</td>
      <td>COM</td>
      <td>Comoros</td>
      <td>Moroni</td>
    </tr>
    <tr>
      <th>44</th>
      <td>223</td>
      <td>COK</td>
      <td>Cook Islands</td>
      <td>Avarua</td>
    </tr>
    <tr>
      <th>45</th>
      <td>124</td>
      <td>CRI</td>
      <td>Costa Rica</td>
      <td>San JosÃ©</td>
    </tr>
    <tr>
      <th>46</th>
      <td>130</td>
      <td>HRV</td>
      <td>Croatia</td>
      <td>Zagreb</td>
    </tr>
    <tr>
      <th>47</th>
      <td>85</td>
      <td>CUB</td>
      <td>Cuba</td>
      <td>Havana</td>
    </tr>
    <tr>
      <th>48</th>
      <td>189</td>
      <td>CUW</td>
      <td>Curacao</td>
      <td>Willemstad</td>
    </tr>
    <tr>
      <th>49</th>
      <td>158</td>
      <td>CYP</td>
      <td>Cyprus</td>
      <td>Nicosia</td>
    </tr>
    <tr>
      <th>50</th>
      <td>88</td>
      <td>CZE</td>
      <td>Czech Republic</td>
      <td>Prague</td>
    </tr>
    <tr>
      <th>51</th>
      <td>115</td>
      <td>DNK</td>
      <td>Denmark</td>
      <td>Copenhagen</td>
    </tr>
    <tr>
      <th>52</th>
      <td>160</td>
      <td>DJI</td>
      <td>Djibouti</td>
      <td>Djibouti</td>
    </tr>
    <tr>
      <th>53</th>
      <td>204</td>
      <td>DMA</td>
      <td>Dominica</td>
      <td>Roseau</td>
    </tr>
    <tr>
      <th>54</th>
      <td>84</td>
      <td>DOM</td>
      <td>Dominican Republic</td>
      <td>Santo Domingo</td>
    </tr>
    <tr>
      <th>55</th>
      <td>15</td>
      <td>COD</td>
      <td>DR Congo</td>
      <td>Kinshasa</td>
    </tr>
    <tr>
      <th>56</th>
      <td>67</td>
      <td>ECU</td>
      <td>Ecuador</td>
      <td>Quito</td>
    </tr>
    <tr>
      <th>57</th>
      <td>14</td>
      <td>EGY</td>
      <td>Egypt</td>
      <td>Cairo</td>
    </tr>
    <tr>
      <th>58</th>
      <td>112</td>
      <td>SLV</td>
      <td>El Salvador</td>
      <td>San Salvador</td>
    </tr>
    <tr>
      <th>59</th>
      <td>152</td>
      <td>GNQ</td>
      <td>Equatorial Guinea</td>
      <td>Malabo</td>
    </tr>
    <tr>
      <th>60</th>
      <td>132</td>
      <td>ERI</td>
      <td>Eritrea</td>
      <td>Asmara</td>
    </tr>
    <tr>
      <th>61</th>
      <td>156</td>
      <td>EST</td>
      <td>Estonia</td>
      <td>Tallinn</td>
    </tr>
    <tr>
      <th>62</th>
      <td>159</td>
      <td>SWZ</td>
      <td>Eswatini</td>
      <td>Mbabane</td>
    </tr>
    <tr>
      <th>63</th>
      <td>12</td>
      <td>ETH</td>
      <td>Ethiopia</td>
      <td>Addis Ababa</td>
    </tr>
    <tr>
      <th>64</th>
      <td>231</td>
      <td>FLK</td>
      <td>Falkland Islands</td>
      <td>Stanley</td>
    </tr>
    <tr>
      <th>65</th>
      <td>209</td>
      <td>FRO</td>
      <td>Faroe Islands</td>
      <td>TÃ³rshavn</td>
    </tr>
    <tr>
      <th>66</th>
      <td>162</td>
      <td>FJI</td>
      <td>Fiji</td>
      <td>Suva</td>
    </tr>
    <tr>
      <th>67</th>
      <td>118</td>
      <td>FIN</td>
      <td>Finland</td>
      <td>Helsinki</td>
    </tr>
    <tr>
      <th>68</th>
      <td>23</td>
      <td>FRA</td>
      <td>France</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>69</th>
      <td>184</td>
      <td>GUF</td>
      <td>French Guiana</td>
      <td>Cayenne</td>
    </tr>
    <tr>
      <th>70</th>
      <td>183</td>
      <td>PYF</td>
      <td>French Polynesia</td>
      <td>Papeete</td>
    </tr>
    <tr>
      <th>71</th>
      <td>146</td>
      <td>GAB</td>
      <td>Gabon</td>
      <td>Libreville</td>
    </tr>
    <tr>
      <th>72</th>
      <td>142</td>
      <td>GMB</td>
      <td>Gambia</td>
      <td>Banjul</td>
    </tr>
    <tr>
      <th>73</th>
      <td>131</td>
      <td>GEO</td>
      <td>Georgia</td>
      <td>Tbilisi</td>
    </tr>
    <tr>
      <th>74</th>
      <td>19</td>
      <td>DEU</td>
      <td>Germany</td>
      <td>Berlin</td>
    </tr>
    <tr>
      <th>75</th>
      <td>47</td>
      <td>GHA</td>
      <td>Ghana</td>
      <td>Accra</td>
    </tr>
    <tr>
      <th>76</th>
      <td>219</td>
      <td>GIB</td>
      <td>Gibraltar</td>
      <td>Gibraltar</td>
    </tr>
    <tr>
      <th>77</th>
      <td>90</td>
      <td>GRC</td>
      <td>Greece</td>
      <td>Athens</td>
    </tr>
    <tr>
      <th>78</th>
      <td>208</td>
      <td>GRL</td>
      <td>Greenland</td>
      <td>Nuuk</td>
    </tr>
    <tr>
      <th>79</th>
      <td>193</td>
      <td>GRD</td>
      <td>Grenada</td>
      <td>Saint George's</td>
    </tr>
    <tr>
      <th>80</th>
      <td>178</td>
      <td>GLP</td>
      <td>Guadeloupe</td>
      <td>Basse-Terre</td>
    </tr>
    <tr>
      <th>81</th>
      <td>191</td>
      <td>GUM</td>
      <td>Guam</td>
      <td>HagÃ¥tÃ±a</td>
    </tr>
    <tr>
      <th>82</th>
      <td>68</td>
      <td>GTM</td>
      <td>Guatemala</td>
      <td>Guatemala City</td>
    </tr>
    <tr>
      <th>83</th>
      <td>207</td>
      <td>GGY</td>
      <td>Guernsey</td>
      <td>Saint Peter Port</td>
    </tr>
    <tr>
      <th>84</th>
      <td>75</td>
      <td>GIN</td>
      <td>Guinea</td>
      <td>Conakry</td>
    </tr>
    <tr>
      <th>85</th>
      <td>149</td>
      <td>GNB</td>
      <td>Guinea-Bissau</td>
      <td>Bissau</td>
    </tr>
    <tr>
      <th>86</th>
      <td>164</td>
      <td>GUY</td>
      <td>Guyana</td>
      <td>Georgetown</td>
    </tr>
    <tr>
      <th>87</th>
      <td>82</td>
      <td>HTI</td>
      <td>Haiti</td>
      <td>Port-au-Prince</td>
    </tr>
    <tr>
      <th>88</th>
      <td>89</td>
      <td>HND</td>
      <td>Honduras</td>
      <td>Tegucigalpa</td>
    </tr>
    <tr>
      <th>89</th>
      <td>104</td>
      <td>HKG</td>
      <td>Hong Kong</td>
      <td>Hong Kong</td>
    </tr>
    <tr>
      <th>90</th>
      <td>94</td>
      <td>HUN</td>
      <td>Hungary</td>
      <td>Budapest</td>
    </tr>
    <tr>
      <th>91</th>
      <td>179</td>
      <td>ISL</td>
      <td>Iceland</td>
      <td>ReykjavÃ­k</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2</td>
      <td>IND</td>
      <td>India</td>
      <td>New Delhi</td>
    </tr>
    <tr>
      <th>93</th>
      <td>4</td>
      <td>IDN</td>
      <td>Indonesia</td>
      <td>Jakarta</td>
    </tr>
    <tr>
      <th>94</th>
      <td>17</td>
      <td>IRN</td>
      <td>Iran</td>
      <td>Tehran</td>
    </tr>
    <tr>
      <th>95</th>
      <td>35</td>
      <td>IRQ</td>
      <td>Iraq</td>
      <td>Baghdad</td>
    </tr>
    <tr>
      <th>96</th>
      <td>125</td>
      <td>IRL</td>
      <td>Ireland</td>
      <td>Dublin</td>
    </tr>
    <tr>
      <th>97</th>
      <td>202</td>
      <td>IMN</td>
      <td>Isle of Man</td>
      <td>Douglas</td>
    </tr>
    <tr>
      <th>98</th>
      <td>98</td>
      <td>ISR</td>
      <td>Israel</td>
      <td>Jerusalem</td>
    </tr>
    <tr>
      <th>99</th>
      <td>25</td>
      <td>ITA</td>
      <td>Italy</td>
      <td>Rome</td>
    </tr>
    <tr>
      <th>100</th>
      <td>52</td>
      <td>CIV</td>
      <td>Ivory Coast</td>
      <td>Yamoussoukro</td>
    </tr>
    <tr>
      <th>101</th>
      <td>139</td>
      <td>JAM</td>
      <td>Jamaica</td>
      <td>Kingston</td>
    </tr>
    <tr>
      <th>102</th>
      <td>11</td>
      <td>JPN</td>
      <td>Japan</td>
      <td>Tokyo</td>
    </tr>
    <tr>
      <th>103</th>
      <td>195</td>
      <td>JEY</td>
      <td>Jersey</td>
      <td>Saint Helier</td>
    </tr>
    <tr>
      <th>104</th>
      <td>83</td>
      <td>JOR</td>
      <td>Jordan</td>
      <td>Amman</td>
    </tr>
    <tr>
      <th>105</th>
      <td>66</td>
      <td>KAZ</td>
      <td>Kazakhstan</td>
      <td>Nursultan</td>
    </tr>
    <tr>
      <th>106</th>
      <td>27</td>
      <td>KEN</td>
      <td>Kenya</td>
      <td>Nairobi</td>
    </tr>
    <tr>
      <th>107</th>
      <td>192</td>
      <td>KIR</td>
      <td>Kiribati</td>
      <td>Tarawa</td>
    </tr>
    <tr>
      <th>108</th>
      <td>129</td>
      <td>KWT</td>
      <td>Kuwait</td>
      <td>Kuwait City</td>
    </tr>
    <tr>
      <th>109</th>
      <td>110</td>
      <td>KGZ</td>
      <td>Kyrgyzstan</td>
      <td>Bishkek</td>
    </tr>
    <tr>
      <th>110</th>
      <td>103</td>
      <td>LAO</td>
      <td>Laos</td>
      <td>Vientiane</td>
    </tr>
    <tr>
      <th>111</th>
      <td>151</td>
      <td>LVA</td>
      <td>Latvia</td>
      <td>Riga</td>
    </tr>
    <tr>
      <th>112</th>
      <td>119</td>
      <td>LBN</td>
      <td>Lebanon</td>
      <td>Beirut</td>
    </tr>
    <tr>
      <th>113</th>
      <td>147</td>
      <td>LSO</td>
      <td>Lesotho</td>
      <td>Maseru</td>
    </tr>
    <tr>
      <th>114</th>
      <td>121</td>
      <td>LBR</td>
      <td>Liberia</td>
      <td>Monrovia</td>
    </tr>
    <tr>
      <th>115</th>
      <td>107</td>
      <td>LBY</td>
      <td>Libya</td>
      <td>Tripoli</td>
    </tr>
    <tr>
      <th>116</th>
      <td>216</td>
      <td>LIE</td>
      <td>Liechtenstein</td>
      <td>Vaduz</td>
    </tr>
    <tr>
      <th>117</th>
      <td>141</td>
      <td>LTU</td>
      <td>Lithuania</td>
      <td>Vilnius</td>
    </tr>
    <tr>
      <th>118</th>
      <td>168</td>
      <td>LUX</td>
      <td>Luxembourg</td>
      <td>Luxembourg</td>
    </tr>
    <tr>
      <th>119</th>
      <td>167</td>
      <td>MAC</td>
      <td>Macau</td>
      <td>Concelho de Macau</td>
    </tr>
    <tr>
      <th>120</th>
      <td>50</td>
      <td>MDG</td>
      <td>Madagascar</td>
      <td>Antananarivo</td>
    </tr>
    <tr>
      <th>121</th>
      <td>62</td>
      <td>MWI</td>
      <td>Malawi</td>
      <td>Lilongwe</td>
    </tr>
    <tr>
      <th>122</th>
      <td>45</td>
      <td>MYS</td>
      <td>Malaysia</td>
      <td>Kuala Lumpur</td>
    </tr>
    <tr>
      <th>123</th>
      <td>174</td>
      <td>MDV</td>
      <td>Maldives</td>
      <td>MalÃ©</td>
    </tr>
    <tr>
      <th>124</th>
      <td>59</td>
      <td>MLI</td>
      <td>Mali</td>
      <td>Bamako</td>
    </tr>
    <tr>
      <th>125</th>
      <td>173</td>
      <td>MLT</td>
      <td>Malta</td>
      <td>Valletta</td>
    </tr>
    <tr>
      <th>126</th>
      <td>215</td>
      <td>MHL</td>
      <td>Marshall Islands</td>
      <td>Majuro</td>
    </tr>
    <tr>
      <th>127</th>
      <td>180</td>
      <td>MTQ</td>
      <td>Martinique</td>
      <td>Fort-de-France</td>
    </tr>
    <tr>
      <th>128</th>
      <td>126</td>
      <td>MRT</td>
      <td>Mauritania</td>
      <td>Nouakchott</td>
    </tr>
    <tr>
      <th>129</th>
      <td>157</td>
      <td>MUS</td>
      <td>Mauritius</td>
      <td>Port Louis</td>
    </tr>
    <tr>
      <th>130</th>
      <td>182</td>
      <td>MYT</td>
      <td>Mayotte</td>
      <td>Mamoudzou</td>
    </tr>
    <tr>
      <th>131</th>
      <td>10</td>
      <td>MEX</td>
      <td>Mexico</td>
      <td>Mexico City</td>
    </tr>
    <tr>
      <th>132</th>
      <td>194</td>
      <td>FSM</td>
      <td>Micronesia</td>
      <td>Palikir</td>
    </tr>
    <tr>
      <th>133</th>
      <td>135</td>
      <td>MDA</td>
      <td>Moldova</td>
      <td>Chisinau</td>
    </tr>
    <tr>
      <th>134</th>
      <td>217</td>
      <td>MCO</td>
      <td>Monaco</td>
      <td>Monaco</td>
    </tr>
    <tr>
      <th>135</th>
      <td>134</td>
      <td>MNG</td>
      <td>Mongolia</td>
      <td>Ulaanbaatar</td>
    </tr>
    <tr>
      <th>136</th>
      <td>169</td>
      <td>MNE</td>
      <td>Montenegro</td>
      <td>Podgorica</td>
    </tr>
    <tr>
      <th>137</th>
      <td>230</td>
      <td>MSR</td>
      <td>Montserrat</td>
      <td>Brades</td>
    </tr>
    <tr>
      <th>138</th>
      <td>40</td>
      <td>MAR</td>
      <td>Morocco</td>
      <td>Rabat</td>
    </tr>
    <tr>
      <th>139</th>
      <td>48</td>
      <td>MOZ</td>
      <td>Mozambique</td>
      <td>Maputo</td>
    </tr>
    <tr>
      <th>140</th>
      <td>26</td>
      <td>MMR</td>
      <td>Myanmar</td>
      <td>Nay Pyi Taw</td>
    </tr>
    <tr>
      <th>141</th>
      <td>145</td>
      <td>NAM</td>
      <td>Namibia</td>
      <td>Windhoek</td>
    </tr>
    <tr>
      <th>142</th>
      <td>225</td>
      <td>NRU</td>
      <td>Nauru</td>
      <td>Yaren</td>
    </tr>
    <tr>
      <th>143</th>
      <td>49</td>
      <td>NPL</td>
      <td>Nepal</td>
      <td>Kathmandu</td>
    </tr>
    <tr>
      <th>144</th>
      <td>71</td>
      <td>NLD</td>
      <td>Netherlands</td>
      <td>Amsterdam</td>
    </tr>
    <tr>
      <th>145</th>
      <td>185</td>
      <td>NCL</td>
      <td>New Caledonia</td>
      <td>NoumÃ©a</td>
    </tr>
    <tr>
      <th>146</th>
      <td>123</td>
      <td>NZL</td>
      <td>New Zealand</td>
      <td>Wellington</td>
    </tr>
    <tr>
      <th>147</th>
      <td>106</td>
      <td>NIC</td>
      <td>Nicaragua</td>
      <td>Managua</td>
    </tr>
    <tr>
      <th>148</th>
      <td>54</td>
      <td>NER</td>
      <td>Niger</td>
      <td>Niamey</td>
    </tr>
    <tr>
      <th>149</th>
      <td>6</td>
      <td>NGA</td>
      <td>Nigeria</td>
      <td>Abuja</td>
    </tr>
    <tr>
      <th>150</th>
      <td>232</td>
      <td>NIU</td>
      <td>Niue</td>
      <td>Alofi</td>
    </tr>
    <tr>
      <th>151</th>
      <td>56</td>
      <td>PRK</td>
      <td>North Korea</td>
      <td>Pyongyang</td>
    </tr>
    <tr>
      <th>152</th>
      <td>150</td>
      <td>MKD</td>
      <td>North Macedonia</td>
      <td>Skopje</td>
    </tr>
    <tr>
      <th>153</th>
      <td>210</td>
      <td>NFK</td>
      <td>Northern Mariana Islands</td>
      <td>Saipan</td>
    </tr>
    <tr>
      <th>154</th>
      <td>120</td>
      <td>NOR</td>
      <td>Norway</td>
      <td>Oslo</td>
    </tr>
    <tr>
      <th>155</th>
      <td>127</td>
      <td>OMN</td>
      <td>Oman</td>
      <td>Muscat</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5</td>
      <td>PAK</td>
      <td>Pakistan</td>
      <td>Islamabad</td>
    </tr>
    <tr>
      <th>157</th>
      <td>222</td>
      <td>PLW</td>
      <td>Palau</td>
      <td>Ngerulmud</td>
    </tr>
    <tr>
      <th>158</th>
      <td>122</td>
      <td>PSE</td>
      <td>Palestine</td>
      <td>Ramallah</td>
    </tr>
    <tr>
      <th>159</th>
      <td>128</td>
      <td>PAN</td>
      <td>Panama</td>
      <td>Panama City</td>
    </tr>
    <tr>
      <th>160</th>
      <td>93</td>
      <td>PNG</td>
      <td>Papua New Guinea</td>
      <td>Port Moresby</td>
    </tr>
    <tr>
      <th>161</th>
      <td>109</td>
      <td>PRY</td>
      <td>Paraguay</td>
      <td>AsunciÃ³n</td>
    </tr>
    <tr>
      <th>162</th>
      <td>44</td>
      <td>PER</td>
      <td>Peru</td>
      <td>Lima</td>
    </tr>
    <tr>
      <th>163</th>
      <td>13</td>
      <td>PHL</td>
      <td>Philippines</td>
      <td>Manila</td>
    </tr>
    <tr>
      <th>164</th>
      <td>37</td>
      <td>POL</td>
      <td>Poland</td>
      <td>Warsaw</td>
    </tr>
    <tr>
      <th>165</th>
      <td>92</td>
      <td>PRT</td>
      <td>Portugal</td>
      <td>Lisbon</td>
    </tr>
    <tr>
      <th>166</th>
      <td>136</td>
      <td>PRI</td>
      <td>Puerto Rico</td>
      <td>San Juan</td>
    </tr>
    <tr>
      <th>167</th>
      <td>143</td>
      <td>QAT</td>
      <td>Qatar</td>
      <td>Doha</td>
    </tr>
    <tr>
      <th>168</th>
      <td>114</td>
      <td>COG</td>
      <td>Republic of the Congo</td>
      <td>Brazzaville</td>
    </tr>
    <tr>
      <th>169</th>
      <td>161</td>
      <td>REU</td>
      <td>Reunion</td>
      <td>Saint-Denis</td>
    </tr>
    <tr>
      <th>170</th>
      <td>64</td>
      <td>ROU</td>
      <td>Romania</td>
      <td>Bucharest</td>
    </tr>
    <tr>
      <th>171</th>
      <td>9</td>
      <td>RUS</td>
      <td>Russia</td>
      <td>Moscow</td>
    </tr>
    <tr>
      <th>172</th>
      <td>76</td>
      <td>RWA</td>
      <td>Rwanda</td>
      <td>Kigali</td>
    </tr>
    <tr>
      <th>173</th>
      <td>228</td>
      <td>BLM</td>
      <td>Saint Barthelemy</td>
      <td>Gustavia</td>
    </tr>
    <tr>
      <th>174</th>
      <td>211</td>
      <td>KNA</td>
      <td>Saint Kitts and Nevis</td>
      <td>Basseterre</td>
    </tr>
    <tr>
      <th>175</th>
      <td>190</td>
      <td>LCA</td>
      <td>Saint Lucia</td>
      <td>Castries</td>
    </tr>
    <tr>
      <th>176</th>
      <td>220</td>
      <td>MAF</td>
      <td>Saint Martin</td>
      <td>Marigot</td>
    </tr>
    <tr>
      <th>177</th>
      <td>229</td>
      <td>SPM</td>
      <td>Saint Pierre and Miquelon</td>
      <td>Saint-Pierre</td>
    </tr>
    <tr>
      <th>178</th>
      <td>199</td>
      <td>VCT</td>
      <td>Saint Vincent and the Grenadines</td>
      <td>Kingstown</td>
    </tr>
    <tr>
      <th>179</th>
      <td>188</td>
      <td>WSM</td>
      <td>Samoa</td>
      <td>Apia</td>
    </tr>
    <tr>
      <th>180</th>
      <td>218</td>
      <td>SMR</td>
      <td>San Marino</td>
      <td>San Marino</td>
    </tr>
    <tr>
      <th>181</th>
      <td>187</td>
      <td>STP</td>
      <td>Sao Tome and Principe</td>
      <td>SÃ£o TomÃ©</td>
    </tr>
    <tr>
      <th>182</th>
      <td>41</td>
      <td>SAU</td>
      <td>Saudi Arabia</td>
      <td>Riyadh</td>
    </tr>
    <tr>
      <th>183</th>
      <td>72</td>
      <td>SEN</td>
      <td>Senegal</td>
      <td>Dakar</td>
    </tr>
    <tr>
      <th>184</th>
      <td>105</td>
      <td>SRB</td>
      <td>Serbia</td>
      <td>Belgrade</td>
    </tr>
    <tr>
      <th>185</th>
      <td>196</td>
      <td>SYC</td>
      <td>Seychelles</td>
      <td>Victoria</td>
    </tr>
    <tr>
      <th>186</th>
      <td>102</td>
      <td>SLE</td>
      <td>Sierra Leone</td>
      <td>Freetown</td>
    </tr>
    <tr>
      <th>187</th>
      <td>113</td>
      <td>SGP</td>
      <td>Singapore</td>
      <td>Singapore</td>
    </tr>
    <tr>
      <th>188</th>
      <td>214</td>
      <td>SXM</td>
      <td>Sint Maarten</td>
      <td>Philipsburg</td>
    </tr>
    <tr>
      <th>189</th>
      <td>116</td>
      <td>SVK</td>
      <td>Slovakia</td>
      <td>Bratislava</td>
    </tr>
    <tr>
      <th>190</th>
      <td>148</td>
      <td>SVN</td>
      <td>Slovenia</td>
      <td>Ljubljana</td>
    </tr>
    <tr>
      <th>191</th>
      <td>166</td>
      <td>SLB</td>
      <td>Solomon Islands</td>
      <td>Honiara</td>
    </tr>
    <tr>
      <th>192</th>
      <td>70</td>
      <td>SOM</td>
      <td>Somalia</td>
      <td>Mogadishu</td>
    </tr>
    <tr>
      <th>193</th>
      <td>24</td>
      <td>ZAF</td>
      <td>South Africa</td>
      <td>Pretoria</td>
    </tr>
    <tr>
      <th>194</th>
      <td>29</td>
      <td>KOR</td>
      <td>South Korea</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>195</th>
      <td>86</td>
      <td>SSD</td>
      <td>South Sudan</td>
      <td>Juba</td>
    </tr>
    <tr>
      <th>196</th>
      <td>30</td>
      <td>ESP</td>
      <td>Spain</td>
      <td>Madrid</td>
    </tr>
    <tr>
      <th>197</th>
      <td>61</td>
      <td>LKA</td>
      <td>Sri Lanka</td>
      <td>Colombo</td>
    </tr>
    <tr>
      <th>198</th>
      <td>32</td>
      <td>SDN</td>
      <td>Sudan</td>
      <td>Khartoum</td>
    </tr>
    <tr>
      <th>199</th>
      <td>170</td>
      <td>SUR</td>
      <td>Suriname</td>
      <td>Paramaribo</td>
    </tr>
    <tr>
      <th>200</th>
      <td>87</td>
      <td>SWE</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
    <tr>
      <th>201</th>
      <td>101</td>
      <td>CHE</td>
      <td>Switzerland</td>
      <td>Bern</td>
    </tr>
    <tr>
      <th>202</th>
      <td>60</td>
      <td>SYR</td>
      <td>Syria</td>
      <td>Damascus</td>
    </tr>
    <tr>
      <th>203</th>
      <td>57</td>
      <td>TWN</td>
      <td>Taiwan</td>
      <td>Taipei</td>
    </tr>
    <tr>
      <th>204</th>
      <td>95</td>
      <td>TJK</td>
      <td>Tajikistan</td>
      <td>Dushanbe</td>
    </tr>
    <tr>
      <th>205</th>
      <td>22</td>
      <td>TZA</td>
      <td>Tanzania</td>
      <td>Dodoma</td>
    </tr>
    <tr>
      <th>206</th>
      <td>20</td>
      <td>THA</td>
      <td>Thailand</td>
      <td>Bangkok</td>
    </tr>
    <tr>
      <th>207</th>
      <td>155</td>
      <td>TLS</td>
      <td>Timor-Leste</td>
      <td>Dili</td>
    </tr>
    <tr>
      <th>208</th>
      <td>100</td>
      <td>TGO</td>
      <td>Togo</td>
      <td>LomÃ©</td>
    </tr>
    <tr>
      <th>209</th>
      <td>233</td>
      <td>TKL</td>
      <td>Tokelau</td>
      <td>Nukunonu</td>
    </tr>
    <tr>
      <th>210</th>
      <td>197</td>
      <td>TON</td>
      <td>Tonga</td>
      <td>Nukuâ€˜alofa</td>
    </tr>
    <tr>
      <th>211</th>
      <td>153</td>
      <td>TTO</td>
      <td>Trinidad and Tobago</td>
      <td>Port-of-Spain</td>
    </tr>
    <tr>
      <th>212</th>
      <td>79</td>
      <td>TUN</td>
      <td>Tunisia</td>
      <td>Tunis</td>
    </tr>
    <tr>
      <th>213</th>
      <td>18</td>
      <td>TUR</td>
      <td>Turkey</td>
      <td>Ankara</td>
    </tr>
    <tr>
      <th>214</th>
      <td>111</td>
      <td>TKM</td>
      <td>Turkmenistan</td>
      <td>Ashgabat</td>
    </tr>
    <tr>
      <th>215</th>
      <td>212</td>
      <td>TCA</td>
      <td>Turks and Caicos Islands</td>
      <td>Cockburn Town</td>
    </tr>
    <tr>
      <th>216</th>
      <td>227</td>
      <td>TUV</td>
      <td>Tuvalu</td>
      <td>Funafuti</td>
    </tr>
    <tr>
      <th>217</th>
      <td>31</td>
      <td>UGA</td>
      <td>Uganda</td>
      <td>Kampala</td>
    </tr>
    <tr>
      <th>218</th>
      <td>38</td>
      <td>UKR</td>
      <td>Ukraine</td>
      <td>Kiev</td>
    </tr>
    <tr>
      <th>219</th>
      <td>97</td>
      <td>ARE</td>
      <td>United Arab Emirates</td>
      <td>Abu Dhabi</td>
    </tr>
    <tr>
      <th>220</th>
      <td>21</td>
      <td>GBR</td>
      <td>United Kingdom</td>
      <td>London</td>
    </tr>
    <tr>
      <th>221</th>
      <td>3</td>
      <td>USA</td>
      <td>United States</td>
      <td>Washington, D.C.</td>
    </tr>
    <tr>
      <th>222</th>
      <td>200</td>
      <td>VIR</td>
      <td>United States Virgin Islands</td>
      <td>Charlotte Amalie</td>
    </tr>
    <tr>
      <th>223</th>
      <td>133</td>
      <td>URY</td>
      <td>Uruguay</td>
      <td>Montevideo</td>
    </tr>
    <tr>
      <th>224</th>
      <td>43</td>
      <td>UZB</td>
      <td>Uzbekistan</td>
      <td>Tashkent</td>
    </tr>
    <tr>
      <th>225</th>
      <td>181</td>
      <td>VUT</td>
      <td>Vanuatu</td>
      <td>Port-Vila</td>
    </tr>
    <tr>
      <th>226</th>
      <td>234</td>
      <td>VAT</td>
      <td>Vatican City</td>
      <td>Vatican City</td>
    </tr>
    <tr>
      <th>227</th>
      <td>51</td>
      <td>VEN</td>
      <td>Venezuela</td>
      <td>Caracas</td>
    </tr>
    <tr>
      <th>228</th>
      <td>16</td>
      <td>VNM</td>
      <td>Vietnam</td>
      <td>Hanoi</td>
    </tr>
    <tr>
      <th>229</th>
      <td>226</td>
      <td>WLF</td>
      <td>Wallis and Futuna</td>
      <td>Mata-Utu</td>
    </tr>
    <tr>
      <th>230</th>
      <td>172</td>
      <td>ESH</td>
      <td>Western Sahara</td>
      <td>El AaiÃºn</td>
    </tr>
    <tr>
      <th>231</th>
      <td>46</td>
      <td>YEM</td>
      <td>Yemen</td>
      <td>Sanaa</td>
    </tr>
    <tr>
      <th>232</th>
      <td>63</td>
      <td>ZMB</td>
      <td>Zambia</td>
      <td>Lusaka</td>
    </tr>
    <tr>
      <th>233</th>
      <td>74</td>
      <td>ZWE</td>
      <td>Zimbabwe</td>
      <td>Harare</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option('display.max.row',234)
pd.set_option('display.max.column',38)
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 234 entries, 0 to 233
    Data columns (total 4 columns):
     #   Column   Non-Null Count  Dtype 
    ---  ------   --------------  ----- 
     0   Rank     234 non-null    int64 
     1   CCA3     234 non-null    object
     2   Country  234 non-null    object
     3   Capital  234 non-null    object
    dtypes: int64(1), object(3)
    memory usage: 7.4+ KB
    


```python
df.shape
```




    (234, 4)




```python
df.head(10)
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
      <th>Rank</th>
      <th>CCA3</th>
      <th>Country</th>
      <th>Capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>36</td>
      <td>AFG</td>
      <td>Afghanistan</td>
      <td>Kabul</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138</td>
      <td>ALB</td>
      <td>Albania</td>
      <td>Tirana</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>DZA</td>
      <td>Algeria</td>
      <td>Algiers</td>
    </tr>
    <tr>
      <th>3</th>
      <td>213</td>
      <td>ASM</td>
      <td>American Samoa</td>
      <td>Pago Pago</td>
    </tr>
    <tr>
      <th>4</th>
      <td>203</td>
      <td>AND</td>
      <td>Andorra</td>
      <td>Andorra la Vella</td>
    </tr>
    <tr>
      <th>5</th>
      <td>42</td>
      <td>AGO</td>
      <td>Angola</td>
      <td>Luanda</td>
    </tr>
    <tr>
      <th>6</th>
      <td>224</td>
      <td>AIA</td>
      <td>Anguilla</td>
      <td>The Valley</td>
    </tr>
    <tr>
      <th>7</th>
      <td>201</td>
      <td>ATG</td>
      <td>Antigua and Barbuda</td>
      <td>Saint Johnâ€™s</td>
    </tr>
    <tr>
      <th>8</th>
      <td>33</td>
      <td>ARG</td>
      <td>Argentina</td>
      <td>Buenos Aires</td>
    </tr>
    <tr>
      <th>9</th>
      <td>140</td>
      <td>ARM</td>
      <td>Armenia</td>
      <td>Yerevan</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(10)
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
      <th>Rank</th>
      <th>CCA3</th>
      <th>Country</th>
      <th>Capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>224</th>
      <td>43</td>
      <td>UZB</td>
      <td>Uzbekistan</td>
      <td>Tashkent</td>
    </tr>
    <tr>
      <th>225</th>
      <td>181</td>
      <td>VUT</td>
      <td>Vanuatu</td>
      <td>Port-Vila</td>
    </tr>
    <tr>
      <th>226</th>
      <td>234</td>
      <td>VAT</td>
      <td>Vatican City</td>
      <td>Vatican City</td>
    </tr>
    <tr>
      <th>227</th>
      <td>51</td>
      <td>VEN</td>
      <td>Venezuela</td>
      <td>Caracas</td>
    </tr>
    <tr>
      <th>228</th>
      <td>16</td>
      <td>VNM</td>
      <td>Vietnam</td>
      <td>Hanoi</td>
    </tr>
    <tr>
      <th>229</th>
      <td>226</td>
      <td>WLF</td>
      <td>Wallis and Futuna</td>
      <td>Mata-Utu</td>
    </tr>
    <tr>
      <th>230</th>
      <td>172</td>
      <td>ESH</td>
      <td>Western Sahara</td>
      <td>El AaiÃºn</td>
    </tr>
    <tr>
      <th>231</th>
      <td>46</td>
      <td>YEM</td>
      <td>Yemen</td>
      <td>Sanaa</td>
    </tr>
    <tr>
      <th>232</th>
      <td>63</td>
      <td>ZMB</td>
      <td>Zambia</td>
      <td>Lusaka</td>
    </tr>
    <tr>
      <th>233</th>
      <td>74</td>
      <td>ZWE</td>
      <td>Zimbabwe</td>
      <td>Harare</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[225]
```




    Rank             181
    CCA3             VUT
    Country      Vanuatu
    Capital    Port-Vila
    Name: 225, dtype: object




```python
df.loc[225]
```




    Rank             181
    CCA3             VUT
    Country      Vanuatu
    Capital    Port-Vila
    Name: 225, dtype: object




```python

```
