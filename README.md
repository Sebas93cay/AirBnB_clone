# AirBnB_clone

This project is a copy of Airbnb web page.

During the development phase we created the console where we can create, modify and destroy objects of different classes.

## Console



### Created Classes

- BaseModel: All other classes inherits from BaseModel
- User
- City
- Amenity
- Place
- Review
- State



### How to Use Console

#### Run the console

```bash
./console.py
```

#### Exit the console

```
(hbtn) quit
or
(hbtn) EOF
```



### Commands to use:

#### Create

```
create <class>
```

#### Show

```
show <class> <id>
or
<class>.show(<id>)
```

#### Destroy

```
destroy <class> <id>
or
<class>.destroy(<id>)
```

#### All

```
all
or
all <class>
or
<class>.all()
```

#### Count

```
count <class>
or 
<class>.count()
```

#### Update

```
update <class> <id> <attribute name> "<attribute value>"
or
<class>.update(<id>, <attribute name>, <attribute value>)
or
<class>.update(<id>, <dictionary_with_attributes>)
```

### Console Storage

Each object created with the console is saved in file.json with JSON format for now :)

