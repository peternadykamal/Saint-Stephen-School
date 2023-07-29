## Database fields

| Field           | description                           | attributes                                                                                                                                                   |
| --------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CharField       | for small text                        | max_length='value' required                                                                                                                                  |
| TextField       | for lard text                         | max_length='value' required                                                                                                                                  |
| BooleanField    |                                       |                                                                                                                                                              |
| IntegerField    |                                       |                                                                                                                                                              |
| FileField       |                                       | upload_to='FolderName in static folder'                                                                                                                      |
| ImageField      |                                       | upload_to='pathToFolder in static folder', default='pathToFile in static fodler'                                                                                                                                                             |
| DateTimeField   |                                       | auto_now_add=Bool                                                                                                                                            |
| UUIDField       | has to import it `import uuid`        | default=uuid.uuid4                                                                                                                                           |
|                 |                                       |                                                                                                                                                              |
| OneToOneField   | relationship puts in the Child Class  | fistAttribute=OtherClassName ("ClassName", ClassName) required,  on_delete=models.SET_NULL\|CASCADE required                                                 |
| ForeignKey      | relationship puts in the Child Class  | fistAttribute=OtherClassName ("ClassName", ClassName) required, related_name="value",  on_delete=models.SET_NULL\|CASCADE required                           |
| ManyToManyField | relationship puts in the Parent Class | fistAttribute=OtherClassName ("ClassName", ClassName) required, through='OtherCostumeTable'                                                                  |
|                 |                                       |                                                                                                                                                              |
| -               | for any field                         | default='Value', null=Bool, blank=Bool, editable=Bool, , unique=Bool, primary_key=Bool, choices=Tuple of Tuples (first value stored, second value displayed) |


## Database quarry 
```cmd
from appName.models import ClassName #Table Name
```
After that can easy to create or retrieve from database
```cmd
variable        = ClassName  . objects       . all()  
#varible that   | Modle Name | Modle Objects | Method
#holds response |            | Attribute     |
```

 | Method      | description                                                                            | Note                                                   |
 | ----------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------ |
 | `all()`     | get all records from this ClassName form database                                      | -                                                      |
 | `get() `    | get single record from this ClassName form database, and specify wanted attributes     | gets error if note found more than one or if not found |
 | `filter()`  | get specific records from this ClassName form database,  and specify wanted attributes | -                                                      |
 | `exclude()` | opposite of filter method                                                              | -                                                      |
 | first()            | get the first object in table                                                                                        |                                                        |
 | last()      | get the last object in table                                                           |                                                        |

| more Methods                                                                   | description                                            | Note                                                     |
| ------------------------------------------------------------------------------ | ------------------------------------------------------ | -------------------------------------------------------- |
| order_by('Attribute')                                                          | order by single value                                  | -                                                        |
| order_by('Attribute1','Attribute2')                                            | order by multiple values with order                    | -                                                        |
| order_by('-Attribute')                                                         | order by revered value                                 | -                                                        |
| variable = ClassName.objects.create(attribute1='value',attribute2='value',...) | create new instance                                    | -                                                        |
| variable.save()                                                                | insert or edit object hold in the variable in database | if id forced by developer already exists it will edit it |
| variable.delete()                                                                               | delete object hold in the variable in database                                                        |                                                          |

| attributes in functions        | description                                         |
| ------------------------------ | --------------------------------------------------- |
| `attribute='value'`            | equals exact value specified                        |
| `attribute__startwith='value'` | get values start with value                         |
| `attribute__contains='value'`  | get values contains a value                         |
| `attribute__icontains='value'` | get values contains a value ignoring case sensitive |
| `attribute__gt='value'`        | get values greater than value                       |
| `attribute__gte='value'`       | get values greater than or equal value              |
| `attribute__lt='value'`        | get values less than value                          |
| `attribute__lte='value'`       | get values less than or equal value                 |

| attributes with  . access    | description                     | relationship |
| ---------------------------- | ------------------------------- | ------------ |
| variable.attribute           | to access specific attributes   | Any          |
| variable.attribute_set.all() | get all children for this model | One to Many  |
| variable.relationship.all()  | get all children for this model | Many to Many |

