SELECT "student_students"."USN","student_students"."Name", "student_students"."Department", "student_students"."Email", "student_students"."Phone" 
FROM "student_students" 
WHERE "student_students"."USN" 
LIKE 117 ESCAPE '\'
