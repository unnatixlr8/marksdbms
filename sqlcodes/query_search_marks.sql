SELECT "student_marks"."id", "student_marks"."USN_id", "student_marks"."MAT", "student_marks"."CHE", "student_marks"."PCD", "student_marks"."CED", "student_marks"."ELN", "student_marks"."CIV" 
FROM "student_marks" 
WHERE "student_marks"."USN_id" 
LIKE 117 ESCAPE '\'