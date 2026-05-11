data = [
    '   Harish,25,Hyderabad  ',
    'anil, ,Bangalore',
    'Ravi,30, ',
    ' ,22,chennai',
    'Sita,28,Delhi'
]

cleaned_data = []
for record in data:
    parts = [k.strip() for k in record.split(",")]
    
    if len(parts) != 3:
        continue
    
    name,age,city = parts
    
    if not name or not age or not city:
        continue
    
    cleaned_data.append({
        "name":name,
        "age":age,
        "city":city
    })   
    
    
print(cleaned_data) 