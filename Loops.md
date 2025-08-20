```python
List = [1,2,3,4,5]
```


```python
for age in List:
    print(age)
```

    1
    2
    3
    4
    5
    


```python
List = [1,2,3,4,5]
```


```python
for age in List:
    print(age+age)
```

    2
    4
    6
    8
    10
    


```python
List = [1,2,3,4,5]

for age in List:
    print(age * 2)
```

    2
    4
    6
    8
    10
    


```python
List = [1,2,3,4,5]

for age in List:
    print('yelp!')
```

    yelp!
    yelp!
    yelp!
    yelp!
    yelp!
    


```python
Player_Team = {'name':'Rooney', 'age':28, 'position':['ST','CM']}

for Player in Player_Team.values():
    print(Player)
```

    Rooney
    28
    ['ST', 'CM']
    


```python
for Player in Player_Team.keys():
    print(Player)
```

    name
    age
    position
    


```python
for key,value in Player_Team.items():
    print(key,'->',value)
```

    name -> Rooney
    age -> 28
    position -> ['ST', 'CM']
    


```python
flavours =['orange','chocolate','vanilla']
toppings =['oreos','icy','sprinkle']
for one in flavours:
    for two in toppings:
        print(one, 'topped with',two)
```

    orange topped with oreos
    orange topped with icy
    orange topped with sprinkle
    chocolate topped with oreos
    chocolate topped with icy
    chocolate topped with sprinkle
    vanilla topped with oreos
    vanilla topped with icy
    vanilla topped with sprinkle
    


```python

```


```python
number=0
```


```python
while number <5:
    print(number)
    number = number + 1
```

    0
    1
    2
    3
    4
    


```python
number = 0

while number <5:
    print(number)
    if number == 5:
        break
    number = number + 1
else:
    print('No longer < 5')
```

    0
    1
    2
    3
    4
    No longer < 5
    


```python

```


```python

```


```python

```


```python

```


```python

```
