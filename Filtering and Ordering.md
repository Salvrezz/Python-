```python
import pandas as pd
```


```python
df = pd.read_excel(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\world_population_excel_workbook.xlsx")
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
df[df['Rank'] <= 10]
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
      <th>16</th>
      <td>8</td>
      <td>BGD</td>
      <td>Bangladesh</td>
      <td>Dhaka</td>
      <td>Asia</td>
      <td>171186372</td>
      <td>167420951</td>
      <td>157830000</td>
      <td>148391139</td>
      <td>129193327</td>
      <td>107147651</td>
      <td>83929765</td>
      <td>67541860</td>
      <td>147570</td>
      <td>1160.0350</td>
      <td>1.0108</td>
      <td>2.15</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>South America</td>
      <td>215313498</td>
      <td>213196304</td>
      <td>205188205</td>
      <td>196353492</td>
      <td>175873720</td>
      <td>150706446</td>
      <td>122288383</td>
      <td>96369875</td>
      <td>8515767</td>
      <td>25.2841</td>
      <td>1.0046</td>
      <td>2.70</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1</td>
      <td>CHN</td>
      <td>China</td>
      <td>Beijing</td>
      <td>Asia</td>
      <td>1425887337</td>
      <td>1424929781</td>
      <td>1393715448</td>
      <td>1348191368</td>
      <td>1264099069</td>
      <td>1153704252</td>
      <td>982372466</td>
      <td>822534450</td>
      <td>9706961</td>
      <td>146.8933</td>
      <td>1.0000</td>
      <td>17.88</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2</td>
      <td>IND</td>
      <td>India</td>
      <td>New Delhi</td>
      <td>Asia</td>
      <td>1417173173</td>
      <td>1396387127</td>
      <td>1322866505</td>
      <td>1240613620</td>
      <td>1059633675</td>
      <td>870452165</td>
      <td>696828385</td>
      <td>557501301</td>
      <td>3287590</td>
      <td>431.0675</td>
      <td>1.0068</td>
      <td>17.77</td>
    </tr>
    <tr>
      <th>93</th>
      <td>4</td>
      <td>IDN</td>
      <td>Indonesia</td>
      <td>Jakarta</td>
      <td>Asia</td>
      <td>275501339</td>
      <td>271857970</td>
      <td>259091970</td>
      <td>244016173</td>
      <td>214072421</td>
      <td>182159874</td>
      <td>148177096</td>
      <td>115228394</td>
      <td>1904569</td>
      <td>144.6529</td>
      <td>1.0064</td>
      <td>3.45</td>
    </tr>
    <tr>
      <th>131</th>
      <td>10</td>
      <td>MEX</td>
      <td>Mexico</td>
      <td>Mexico City</td>
      <td>North America</td>
      <td>127504125</td>
      <td>125998302</td>
      <td>120149897</td>
      <td>112532401</td>
      <td>97873442</td>
      <td>81720428</td>
      <td>67705186</td>
      <td>50289306</td>
      <td>1964375</td>
      <td>64.9082</td>
      <td>1.0063</td>
      <td>1.60</td>
    </tr>
    <tr>
      <th>149</th>
      <td>6</td>
      <td>NGA</td>
      <td>Nigeria</td>
      <td>Abuja</td>
      <td>Africa</td>
      <td>218541212</td>
      <td>208327405</td>
      <td>183995785</td>
      <td>160952853</td>
      <td>122851984</td>
      <td>95214257</td>
      <td>72951439</td>
      <td>55569264</td>
      <td>923768</td>
      <td>236.5759</td>
      <td>1.0241</td>
      <td>2.74</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5</td>
      <td>PAK</td>
      <td>Pakistan</td>
      <td>Islamabad</td>
      <td>Asia</td>
      <td>235824862</td>
      <td>227196741</td>
      <td>210969298</td>
      <td>194454498</td>
      <td>154369924</td>
      <td>115414069</td>
      <td>80624057</td>
      <td>59290872</td>
      <td>881912</td>
      <td>267.4018</td>
      <td>1.0191</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>171</th>
      <td>9</td>
      <td>RUS</td>
      <td>Russia</td>
      <td>Moscow</td>
      <td>Europe</td>
      <td>144713314</td>
      <td>145617329</td>
      <td>144668389</td>
      <td>143242599</td>
      <td>146844839</td>
      <td>148005704</td>
      <td>138257420</td>
      <td>130093010</td>
      <td>17098242</td>
      <td>8.4636</td>
      <td>0.9973</td>
      <td>1.81</td>
    </tr>
    <tr>
      <th>221</th>
      <td>3</td>
      <td>USA</td>
      <td>United States</td>
      <td>Washington, D.C.</td>
      <td>North America</td>
      <td>338289857</td>
      <td>335942003</td>
      <td>324607776</td>
      <td>311182845</td>
      <td>282398554</td>
      <td>248083732</td>
      <td>223140018</td>
      <td>200328340</td>
      <td>9372610</td>
      <td>36.0935</td>
      <td>1.0038</td>
      <td>4.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
##Getting a specuific country
specific_countries = ['Bangladesh', 'Brazil']

df[df['Country'].isin(specific_countries)]
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
      <th>16</th>
      <td>8</td>
      <td>BGD</td>
      <td>Bangladesh</td>
      <td>Dhaka</td>
      <td>Asia</td>
      <td>171186372</td>
      <td>167420951</td>
      <td>157830000</td>
      <td>148391139</td>
      <td>129193327</td>
      <td>107147651</td>
      <td>83929765</td>
      <td>67541860</td>
      <td>147570</td>
      <td>1160.0350</td>
      <td>1.0108</td>
      <td>2.15</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>South America</td>
      <td>215313498</td>
      <td>213196304</td>
      <td>205188205</td>
      <td>196353492</td>
      <td>175873720</td>
      <td>150706446</td>
      <td>122288383</td>
      <td>96369875</td>
      <td>8515767</td>
      <td>25.2841</td>
      <td>1.0046</td>
      <td>2.70</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['Country'].str.contains('United')]
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
      <th>219</th>
      <td>97</td>
      <td>ARE</td>
      <td>United Arab Emirates</td>
      <td>Abu Dhabi</td>
      <td>Asia</td>
      <td>9441129</td>
      <td>9287289</td>
      <td>8916899</td>
      <td>8481771</td>
      <td>3275333</td>
      <td>1900151</td>
      <td>1014048</td>
      <td>298084</td>
      <td>83600</td>
      <td>112.9322</td>
      <td>1.0081</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>220</th>
      <td>21</td>
      <td>GBR</td>
      <td>United Kingdom</td>
      <td>London</td>
      <td>Europe</td>
      <td>67508936</td>
      <td>67059474</td>
      <td>65224364</td>
      <td>62760039</td>
      <td>58850043</td>
      <td>57210442</td>
      <td>56326328</td>
      <td>55650166</td>
      <td>242900</td>
      <td>277.9289</td>
      <td>1.0034</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>221</th>
      <td>3</td>
      <td>USA</td>
      <td>United States</td>
      <td>Washington, D.C.</td>
      <td>North America</td>
      <td>338289857</td>
      <td>335942003</td>
      <td>324607776</td>
      <td>311182845</td>
      <td>282398554</td>
      <td>248083732</td>
      <td>223140018</td>
      <td>200328340</td>
      <td>9372610</td>
      <td>36.0935</td>
      <td>1.0038</td>
      <td>4.24</td>
    </tr>
    <tr>
      <th>222</th>
      <td>200</td>
      <td>VIR</td>
      <td>United States Virgin Islands</td>
      <td>Charlotte Amalie</td>
      <td>North America</td>
      <td>99465</td>
      <td>100442</td>
      <td>102803</td>
      <td>106142</td>
      <td>108185</td>
      <td>100685</td>
      <td>96640</td>
      <td>63446</td>
      <td>347</td>
      <td>286.6427</td>
      <td>0.9937</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
##To make country an index within a table 
df2 = df.set_index('Country')
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
      <th>Rank</th>
      <th>CCA3</th>
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
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>36</td>
      <td>AFG</td>
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
      <th>Albania</th>
      <td>138</td>
      <td>ALB</td>
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
      <th>Algeria</th>
      <td>34</td>
      <td>DZA</td>
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
      <th>American Samoa</th>
      <td>213</td>
      <td>ASM</td>
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
      <th>Andorra</th>
      <td>203</td>
      <td>AND</td>
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
    </tr>
    <tr>
      <th>Wallis and Futuna</th>
      <td>226</td>
      <td>WLF</td>
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
      <th>Western Sahara</th>
      <td>172</td>
      <td>ESH</td>
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
      <th>Yemen</th>
      <td>46</td>
      <td>YEM</td>
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
      <th>Zambia</th>
      <td>63</td>
      <td>ZMB</td>
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
      <th>Zimbabwe</th>
      <td>74</td>
      <td>ZWE</td>
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
<p>234 rows × 16 columns</p>
</div>




```python
##Filtering for columns

df2.filter(items = ['Continent','CCA3','Growth Rate'])
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
      <th>Continent</th>
      <th>CCA3</th>
      <th>Growth Rate</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>Asia</td>
      <td>AFG</td>
      <td>1.0257</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>Europe</td>
      <td>ALB</td>
      <td>0.9957</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>Africa</td>
      <td>DZA</td>
      <td>1.0164</td>
    </tr>
    <tr>
      <th>American Samoa</th>
      <td>Oceania</td>
      <td>ASM</td>
      <td>0.9831</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>Europe</td>
      <td>AND</td>
      <td>1.0100</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Wallis and Futuna</th>
      <td>Oceania</td>
      <td>WLF</td>
      <td>0.9953</td>
    </tr>
    <tr>
      <th>Western Sahara</th>
      <td>Africa</td>
      <td>ESH</td>
      <td>1.0184</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>Asia</td>
      <td>YEM</td>
      <td>1.0217</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>Africa</td>
      <td>ZMB</td>
      <td>1.0280</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>Africa</td>
      <td>ZWE</td>
      <td>1.0204</td>
    </tr>
  </tbody>
</table>
<p>234 rows × 3 columns</p>
</div>




```python
df2.filter(items = ['Zambia'], axis = 0)
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
      <th>Zambia</th>
      <td>63</td>
      <td>ZMB</td>
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
      <td>1.028</td>
      <td>0.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.filter(like = 'United', axis = 0)
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
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>United Arab Emirates</th>
      <td>97</td>
      <td>ARE</td>
      <td>Abu Dhabi</td>
      <td>Asia</td>
      <td>9441129</td>
      <td>9287289</td>
      <td>8916899</td>
      <td>8481771</td>
      <td>3275333</td>
      <td>1900151</td>
      <td>1014048</td>
      <td>298084</td>
      <td>83600</td>
      <td>112.9322</td>
      <td>1.0081</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td>21</td>
      <td>GBR</td>
      <td>London</td>
      <td>Europe</td>
      <td>67508936</td>
      <td>67059474</td>
      <td>65224364</td>
      <td>62760039</td>
      <td>58850043</td>
      <td>57210442</td>
      <td>56326328</td>
      <td>55650166</td>
      <td>242900</td>
      <td>277.9289</td>
      <td>1.0034</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>3</td>
      <td>USA</td>
      <td>Washington, D.C.</td>
      <td>North America</td>
      <td>338289857</td>
      <td>335942003</td>
      <td>324607776</td>
      <td>311182845</td>
      <td>282398554</td>
      <td>248083732</td>
      <td>223140018</td>
      <td>200328340</td>
      <td>9372610</td>
      <td>36.0935</td>
      <td>1.0038</td>
      <td>4.24</td>
    </tr>
    <tr>
      <th>United States Virgin Islands</th>
      <td>200</td>
      <td>VIR</td>
      <td>Charlotte Amalie</td>
      <td>North America</td>
      <td>99465</td>
      <td>100442</td>
      <td>102803</td>
      <td>106142</td>
      <td>108185</td>
      <td>100685</td>
      <td>96640</td>
      <td>63446</td>
      <td>347</td>
      <td>286.6427</td>
      <td>0.9937</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc['United States']
```




    Rank                                          3
    CCA3                                        USA
    Capital                        Washington, D.C.
    Continent                         North America
    2022 Population                       338289857
    2020 Population                       335942003
    2015 Population                       324607776
    2010 Population                       311182845
    2000 Population                       282398554
    1990 Population                       248083732
    1980 Population                       223140018
    1970 Population                       200328340
    Area (kmÂ²)                             9372610
    Density (per kmÂ²)                      36.0935
    Growth Rate                              1.0038
    World Population Percentage                4.24
    Name: United States, dtype: object




```python
df2.iloc[200]
```




    Rank                                  87
    CCA3                                 SWE
    Capital                        Stockholm
    Continent                         Europe
    2022 Population                 10549347
    2020 Population                 10368969
    2015 Population                  9849349
    2010 Population                  9381729
    2000 Population                  8871043
    1990 Population                  8548406
    1980 Population                  8311763
    1970 Population                  8027702
    Area (kmÂ²)                       450295
    Density (per kmÂ²)               23.4276
    Growth Rate                       1.0079
    World Population Percentage         0.13
    Name: Sweden, dtype: object




```python
##To Order/Sorting by Rank and Country
df[df['Rank'] < 10].sort_values(by=['Rank','Country'],ascending=True)
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
      <th>41</th>
      <td>1</td>
      <td>CHN</td>
      <td>China</td>
      <td>Beijing</td>
      <td>Asia</td>
      <td>1425887337</td>
      <td>1424929781</td>
      <td>1393715448</td>
      <td>1348191368</td>
      <td>1264099069</td>
      <td>1153704252</td>
      <td>982372466</td>
      <td>822534450</td>
      <td>9706961</td>
      <td>146.8933</td>
      <td>1.0000</td>
      <td>17.88</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2</td>
      <td>IND</td>
      <td>India</td>
      <td>New Delhi</td>
      <td>Asia</td>
      <td>1417173173</td>
      <td>1396387127</td>
      <td>1322866505</td>
      <td>1240613620</td>
      <td>1059633675</td>
      <td>870452165</td>
      <td>696828385</td>
      <td>557501301</td>
      <td>3287590</td>
      <td>431.0675</td>
      <td>1.0068</td>
      <td>17.77</td>
    </tr>
    <tr>
      <th>221</th>
      <td>3</td>
      <td>USA</td>
      <td>United States</td>
      <td>Washington, D.C.</td>
      <td>North America</td>
      <td>338289857</td>
      <td>335942003</td>
      <td>324607776</td>
      <td>311182845</td>
      <td>282398554</td>
      <td>248083732</td>
      <td>223140018</td>
      <td>200328340</td>
      <td>9372610</td>
      <td>36.0935</td>
      <td>1.0038</td>
      <td>4.24</td>
    </tr>
    <tr>
      <th>93</th>
      <td>4</td>
      <td>IDN</td>
      <td>Indonesia</td>
      <td>Jakarta</td>
      <td>Asia</td>
      <td>275501339</td>
      <td>271857970</td>
      <td>259091970</td>
      <td>244016173</td>
      <td>214072421</td>
      <td>182159874</td>
      <td>148177096</td>
      <td>115228394</td>
      <td>1904569</td>
      <td>144.6529</td>
      <td>1.0064</td>
      <td>3.45</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5</td>
      <td>PAK</td>
      <td>Pakistan</td>
      <td>Islamabad</td>
      <td>Asia</td>
      <td>235824862</td>
      <td>227196741</td>
      <td>210969298</td>
      <td>194454498</td>
      <td>154369924</td>
      <td>115414069</td>
      <td>80624057</td>
      <td>59290872</td>
      <td>881912</td>
      <td>267.4018</td>
      <td>1.0191</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>149</th>
      <td>6</td>
      <td>NGA</td>
      <td>Nigeria</td>
      <td>Abuja</td>
      <td>Africa</td>
      <td>218541212</td>
      <td>208327405</td>
      <td>183995785</td>
      <td>160952853</td>
      <td>122851984</td>
      <td>95214257</td>
      <td>72951439</td>
      <td>55569264</td>
      <td>923768</td>
      <td>236.5759</td>
      <td>1.0241</td>
      <td>2.74</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>South America</td>
      <td>215313498</td>
      <td>213196304</td>
      <td>205188205</td>
      <td>196353492</td>
      <td>175873720</td>
      <td>150706446</td>
      <td>122288383</td>
      <td>96369875</td>
      <td>8515767</td>
      <td>25.2841</td>
      <td>1.0046</td>
      <td>2.70</td>
    </tr>
    <tr>
      <th>16</th>
      <td>8</td>
      <td>BGD</td>
      <td>Bangladesh</td>
      <td>Dhaka</td>
      <td>Asia</td>
      <td>171186372</td>
      <td>167420951</td>
      <td>157830000</td>
      <td>148391139</td>
      <td>129193327</td>
      <td>107147651</td>
      <td>83929765</td>
      <td>67541860</td>
      <td>147570</td>
      <td>1160.0350</td>
      <td>1.0108</td>
      <td>2.15</td>
    </tr>
    <tr>
      <th>171</th>
      <td>9</td>
      <td>RUS</td>
      <td>Russia</td>
      <td>Moscow</td>
      <td>Europe</td>
      <td>144713314</td>
      <td>145617329</td>
      <td>144668389</td>
      <td>143242599</td>
      <td>146844839</td>
      <td>148005704</td>
      <td>138257420</td>
      <td>130093010</td>
      <td>17098242</td>
      <td>8.4636</td>
      <td>0.9973</td>
      <td>1.81</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['Rank'] < 10].sort_values(by=['Rank','Country'],ascending=False)
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
      <th>171</th>
      <td>9</td>
      <td>RUS</td>
      <td>Russia</td>
      <td>Moscow</td>
      <td>Europe</td>
      <td>144713314</td>
      <td>145617329</td>
      <td>144668389</td>
      <td>143242599</td>
      <td>146844839</td>
      <td>148005704</td>
      <td>138257420</td>
      <td>130093010</td>
      <td>17098242</td>
      <td>8.4636</td>
      <td>0.9973</td>
      <td>1.81</td>
    </tr>
    <tr>
      <th>16</th>
      <td>8</td>
      <td>BGD</td>
      <td>Bangladesh</td>
      <td>Dhaka</td>
      <td>Asia</td>
      <td>171186372</td>
      <td>167420951</td>
      <td>157830000</td>
      <td>148391139</td>
      <td>129193327</td>
      <td>107147651</td>
      <td>83929765</td>
      <td>67541860</td>
      <td>147570</td>
      <td>1160.0350</td>
      <td>1.0108</td>
      <td>2.15</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>South America</td>
      <td>215313498</td>
      <td>213196304</td>
      <td>205188205</td>
      <td>196353492</td>
      <td>175873720</td>
      <td>150706446</td>
      <td>122288383</td>
      <td>96369875</td>
      <td>8515767</td>
      <td>25.2841</td>
      <td>1.0046</td>
      <td>2.70</td>
    </tr>
    <tr>
      <th>149</th>
      <td>6</td>
      <td>NGA</td>
      <td>Nigeria</td>
      <td>Abuja</td>
      <td>Africa</td>
      <td>218541212</td>
      <td>208327405</td>
      <td>183995785</td>
      <td>160952853</td>
      <td>122851984</td>
      <td>95214257</td>
      <td>72951439</td>
      <td>55569264</td>
      <td>923768</td>
      <td>236.5759</td>
      <td>1.0241</td>
      <td>2.74</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5</td>
      <td>PAK</td>
      <td>Pakistan</td>
      <td>Islamabad</td>
      <td>Asia</td>
      <td>235824862</td>
      <td>227196741</td>
      <td>210969298</td>
      <td>194454498</td>
      <td>154369924</td>
      <td>115414069</td>
      <td>80624057</td>
      <td>59290872</td>
      <td>881912</td>
      <td>267.4018</td>
      <td>1.0191</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>93</th>
      <td>4</td>
      <td>IDN</td>
      <td>Indonesia</td>
      <td>Jakarta</td>
      <td>Asia</td>
      <td>275501339</td>
      <td>271857970</td>
      <td>259091970</td>
      <td>244016173</td>
      <td>214072421</td>
      <td>182159874</td>
      <td>148177096</td>
      <td>115228394</td>
      <td>1904569</td>
      <td>144.6529</td>
      <td>1.0064</td>
      <td>3.45</td>
    </tr>
    <tr>
      <th>221</th>
      <td>3</td>
      <td>USA</td>
      <td>United States</td>
      <td>Washington, D.C.</td>
      <td>North America</td>
      <td>338289857</td>
      <td>335942003</td>
      <td>324607776</td>
      <td>311182845</td>
      <td>282398554</td>
      <td>248083732</td>
      <td>223140018</td>
      <td>200328340</td>
      <td>9372610</td>
      <td>36.0935</td>
      <td>1.0038</td>
      <td>4.24</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2</td>
      <td>IND</td>
      <td>India</td>
      <td>New Delhi</td>
      <td>Asia</td>
      <td>1417173173</td>
      <td>1396387127</td>
      <td>1322866505</td>
      <td>1240613620</td>
      <td>1059633675</td>
      <td>870452165</td>
      <td>696828385</td>
      <td>557501301</td>
      <td>3287590</td>
      <td>431.0675</td>
      <td>1.0068</td>
      <td>17.77</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1</td>
      <td>CHN</td>
      <td>China</td>
      <td>Beijing</td>
      <td>Asia</td>
      <td>1425887337</td>
      <td>1424929781</td>
      <td>1393715448</td>
      <td>1348191368</td>
      <td>1264099069</td>
      <td>1153704252</td>
      <td>982372466</td>
      <td>822534450</td>
      <td>9706961</td>
      <td>146.8933</td>
      <td>1.0000</td>
      <td>17.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['Rank'] < 10].sort_values(by=['Country','Rank'],ascending=[True,True])
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
      <th>16</th>
      <td>8</td>
      <td>BGD</td>
      <td>Bangladesh</td>
      <td>Dhaka</td>
      <td>Asia</td>
      <td>171186372</td>
      <td>167420951</td>
      <td>157830000</td>
      <td>148391139</td>
      <td>129193327</td>
      <td>107147651</td>
      <td>83929765</td>
      <td>67541860</td>
      <td>147570</td>
      <td>1160.0350</td>
      <td>1.0108</td>
      <td>2.15</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>South America</td>
      <td>215313498</td>
      <td>213196304</td>
      <td>205188205</td>
      <td>196353492</td>
      <td>175873720</td>
      <td>150706446</td>
      <td>122288383</td>
      <td>96369875</td>
      <td>8515767</td>
      <td>25.2841</td>
      <td>1.0046</td>
      <td>2.70</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1</td>
      <td>CHN</td>
      <td>China</td>
      <td>Beijing</td>
      <td>Asia</td>
      <td>1425887337</td>
      <td>1424929781</td>
      <td>1393715448</td>
      <td>1348191368</td>
      <td>1264099069</td>
      <td>1153704252</td>
      <td>982372466</td>
      <td>822534450</td>
      <td>9706961</td>
      <td>146.8933</td>
      <td>1.0000</td>
      <td>17.88</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2</td>
      <td>IND</td>
      <td>India</td>
      <td>New Delhi</td>
      <td>Asia</td>
      <td>1417173173</td>
      <td>1396387127</td>
      <td>1322866505</td>
      <td>1240613620</td>
      <td>1059633675</td>
      <td>870452165</td>
      <td>696828385</td>
      <td>557501301</td>
      <td>3287590</td>
      <td>431.0675</td>
      <td>1.0068</td>
      <td>17.77</td>
    </tr>
    <tr>
      <th>93</th>
      <td>4</td>
      <td>IDN</td>
      <td>Indonesia</td>
      <td>Jakarta</td>
      <td>Asia</td>
      <td>275501339</td>
      <td>271857970</td>
      <td>259091970</td>
      <td>244016173</td>
      <td>214072421</td>
      <td>182159874</td>
      <td>148177096</td>
      <td>115228394</td>
      <td>1904569</td>
      <td>144.6529</td>
      <td>1.0064</td>
      <td>3.45</td>
    </tr>
    <tr>
      <th>149</th>
      <td>6</td>
      <td>NGA</td>
      <td>Nigeria</td>
      <td>Abuja</td>
      <td>Africa</td>
      <td>218541212</td>
      <td>208327405</td>
      <td>183995785</td>
      <td>160952853</td>
      <td>122851984</td>
      <td>95214257</td>
      <td>72951439</td>
      <td>55569264</td>
      <td>923768</td>
      <td>236.5759</td>
      <td>1.0241</td>
      <td>2.74</td>
    </tr>
    <tr>
      <th>156</th>
      <td>5</td>
      <td>PAK</td>
      <td>Pakistan</td>
      <td>Islamabad</td>
      <td>Asia</td>
      <td>235824862</td>
      <td>227196741</td>
      <td>210969298</td>
      <td>194454498</td>
      <td>154369924</td>
      <td>115414069</td>
      <td>80624057</td>
      <td>59290872</td>
      <td>881912</td>
      <td>267.4018</td>
      <td>1.0191</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>171</th>
      <td>9</td>
      <td>RUS</td>
      <td>Russia</td>
      <td>Moscow</td>
      <td>Europe</td>
      <td>144713314</td>
      <td>145617329</td>
      <td>144668389</td>
      <td>143242599</td>
      <td>146844839</td>
      <td>148005704</td>
      <td>138257420</td>
      <td>130093010</td>
      <td>17098242</td>
      <td>8.4636</td>
      <td>0.9973</td>
      <td>1.81</td>
    </tr>
    <tr>
      <th>221</th>
      <td>3</td>
      <td>USA</td>
      <td>United States</td>
      <td>Washington, D.C.</td>
      <td>North America</td>
      <td>338289857</td>
      <td>335942003</td>
      <td>324607776</td>
      <td>311182845</td>
      <td>282398554</td>
      <td>248083732</td>
      <td>223140018</td>
      <td>200328340</td>
      <td>9372610</td>
      <td>36.0935</td>
      <td>1.0038</td>
      <td>4.24</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
