# libz

### Simple DBMS (not a relational one) that stores data in a folder with different file.

##### Coded a lot in C++ and Typescript in last few weeks, so coded this to recall python for exam

> Python Version: 3.12.4

## Creating a database

```python
database = Libz("users")
```

## Defining a schema

```python
database.define_schema({
    "name": "posts",
    "fields":[
        {
            "name:"uid",
            "type": "text",
            "unique":True,
            "primary": True
        },
        {
            "name" : "postedBy",
            "type":"text"
            "unique": False,
        },
        {
            "name":"postedOn",
            "type": "date"
        }
    ]
})
```

```
name: string - should only be alphabets
types: string - options [date, text, number, boolean]
unique : boolean - optional [default to False ]
primary : boolean - optional [default to False ]


Either single dictionary or list of dictionaries should be passed to 'defineSchema' method

This 'define_schema' method returns the instance of the class. So yes, it supports method chaining


```
