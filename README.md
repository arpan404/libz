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

| **Field**        | **Type**                   | **Description**                                                |
| ---------------- | -------------------------- | -------------------------------------------------------------- |
| `name`           | `string`                   | Field name, must only contain alphabets.                       |
| `type`           | `string`                   | Data type, options: `date`, `text`, `number`, `boolean`.       |
| `unique` (opt.)  | `boolean` (default: False) | Ensures no duplicate values in this field.                     |
| `primary` (opt.) | `boolean` (default: False) | Specifies this field as the primary key (unique and non-null). |

Either single dictionary or list of dictionaries should be passed to 'defineSchema' method

This 'define_schema' method returns the instance of the class. So yes, it supports method chaining
