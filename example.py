from libz import Libz
database = Libz("test")

database.define_schema([{
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
}])

database.define_schema({
    "name": "videos",
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

database.insert(
    "posts", {
        "uid": "Arpan",
        "postedBy": "ab",
        "postedOn": "12/2/2024"
    }
)

print(database.find("posts", {"uid": "Arpan"}))
