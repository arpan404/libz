# libz

### Simple DBMS (not a relational one) that stores data in a folder with different file.

##### Coded a lot in C++ and Typescript in last few weeks, so coded this to recall python for exam

> Python Version: 3.12.4

## Creating a database

```python
from libz import Libz
database = Libz("users")
```

## Defining a schema

```python

database.define_schema({
    "name": "posts",
    "fields": [
        {
            "name": "uid",
            "type": "text",
            "unique": True,
            "primary": True
        },
        {
            "name": "postedBy",
            "type": "text",
            "unique": False
        },
        {
            "name": "postedOn",
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

The provided schema will be saved and used throughout the current program.

> Redefining a schema is not allowed.

For example, following code will throw and error:

```python

database.define_schema({
    "name": "posts",
    "fields": [
        {
            "name": "uid",
            "type": "text",
            "unique": True,
            "primary": True
        },
        {
            "name": "userName",
            "type": "text",
            "unique": False
        },
    ]
})
```

## Inserting data

```python

database.insert("posts", {
"uid":"1x09",
"postedBy":"@arpan404",
"postedOn":"2024-12-02"
})

```

> `insert` method takes two arguments, first one is the collection name (name provided when defining a schema) and the dictory with same all keys and value pair which were defined in the schema.
> Passing any other data type or dictionary with different keys and values will throw an error.
> Passing duplicate value to the unique field will also throw an error.

## Finding Data

> Currently only finding exact data is supported, using certain field

```python
database.find("posts", {
    "uid":"1x09"
})
```

> `find` method returns the all the available data which matches provided condition. It takes two arguments: `collection_name` and `condition`

## Deleting Data

```python
database.delete("posts", {
    "uid":"1x099"
})
```

> `delete` methods taks two arguments `collection` and `condition`. It returns True if the data is deleted successfully; raise Error otherwise.

## Updating Data

```python
database.update("posts",
    {
        "postedBy":"thearpan404"
    },
    {
        "uid":"1x099"
    })

```

> `update` methods take three argument `collection`, `new_data` and `condition`. It returns True if the data is updated successfully; raise Error otherwise.

### This is a fun project (not made for large scale use or production), if you wanna use it go ahead.

> I recommend using it only for simple projects, where you need to save and retrive data simply (like simple college projects).

#### You can modify and use the code accordingy to your needs as there will be no future update from myside unless I go to coding mood.

> I believe good code doesn’t need comments to explain itself, so I haven’t added any comments to the code.