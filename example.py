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

database.insert("posts", {
    "uid": "Arpaaaan",
    "postedBy": "Assrpan",
    "postedOn": "Heallo"
})
