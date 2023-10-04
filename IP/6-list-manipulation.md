# 04/10/23 

```py
a = 5 
b = 6
c = a + b 
print(c)  # 11
```

Similarly, 

```py
a = 5 
a = 3 
b = 2 
c = a+b 
print(c)  #  5 
```

But for this case, the replaced variable gets deleted. This is the problem of python

- Storage also becomes difficult with huge number of variables. 

List solves that problem 

```py
     0  1  2  3  4  5
E = [50,60,70,80,90,100]
M = [50,60,70,80,90,100]
```

The numbers above are called index value or address.  
They always start from zero. 

```py
print(E[0])  # 50 
print(E[5])  # 100 
```
> The above shows index numbers are used to locate values within a list. 

- **Index value**:
    1. Positive Index Value 
    2. Negative Index Value

- Negative Index value ends with -1 

```python
B = [50,60,70,80,90]
     -5 -4 -3 -2 -1 
```

> It works like a number line. 

## Types of Lists 

```py
a = [1,2,,3,4,5] # Integer list  
b = [1.6,2.3,3.9,4.4,5.6] # Floating-point list  
c = ['W','O','R','L','D'] # Character list  
d = ['so','sehr','schon']  # Word List  
e = [1, 3.5, -2, 'Sekai','L'] # Mixed list   
```

- For calculations, only pure list of one type is applicable. 

## Creating an Empty List 

Q = List[]

- Sequence is also a kind of list 

`a = (1,2,3,4,5) # This is a sequence`

- List follows index values but sequences do not. 

### Converting Sequence to a list 

```py 
a = (1,2,3,4,5)
b = List[a]

print(b) # [1,2,3,4,5]
print(a) # (1,2,,3,4,5)

```

- Sequence can be converted into list but not vice versa. 


