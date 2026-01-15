# Django-Projects

# Student Result Management API

## Base URL
http://127.0.0.1:8000/

---

## 1. Add Student (Smart Insert)
POST /add-student/

### Request Body
{
  "name": "Ravi",
  "email": "ravi@gmail.com",
  "python_marks": 80,
  "django_marks": 70,
  "sql_marks": 75
}

### Response
{
  "status": "success",
  "total": 225,
  "percentage": 75.0,
  "grade": "A"
}

---

## 2. Students with Grade A
GET /grade-a/

---

## 3. Top 3 Students
GET /top-3/

---

## 4. Average Percentage
GET /average/

---

## 5. Pass vs Fail Count
GET /pass-fail/

---

## 6. Soft Delete Student
DELETE /students/delete/{id}/

### Response
{
  "status": "success",
  "message": "Student soft deleted"
}

---

## Notes
- Soft delete is implemented using `is_active` flag
- Deleted students are not returned in fetch APIs
