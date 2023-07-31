user <=> profile (one to one relation)

tag have many privileges and privilege have many tags
tag have many profiles and profile have many tags

---

user
username (id code)
email
first name
last name
password

talmza level
id
level number
level name
no of years
next level id

school level
id
level number
level name
no of years
next level id

profile
id
name (unique)
birthdate
talmza level (foreign key)
current talmza level year
school level (foreign key)
current school level yaer
job
profile image path
gender
phone number
mother phone number
father phone number
confession father
church
Deaconess (رسامة)

address (one to one relationship with profile)
building
street
Branches from
floor
Apartment number
Residential Complexes
district
Additional Details

Expenses
id
year
amount of money payed
"created for" profile id (foreign key)
total number of Expenses (not as a proprty in the table but an constant stored in a spearte table or as .env file in backend)

profile form log
"created for" profile id (foreign key)
log date
"created by" profile id (foreign key)
category action
action
