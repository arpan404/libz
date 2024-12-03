from libz import Libz
database = Libz("test")

database.define_schema([{
    "name": "posts",
    "fields": [
        {
            "name": "uid",
            "type": "text",
            "unique": False,
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
        "uid": "1x90",
        "postedBy": "arpan404",
        "postedOn": "12/2/2024"
    }
)


print(database.find("posts", {"uid": "Arpan"}))


database.update(collection="posts", new_data={
                "postedBy": "tarpan404"}, condition={"uid": "1x90"})

print(database.delete("posts", {
    "uid": "1x90"
}))
