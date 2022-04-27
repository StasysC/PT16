from duombaze import db, Query

all_message = Query.query.all()
print(all_message)