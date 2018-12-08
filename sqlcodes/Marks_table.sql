CREATE TABLE "student_marks" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
							  "USN_id" integer NOT NULL UNIQUE REFERENCES "student_students" ("USN") DEFERRABLE INITIALLY DEFERRED,
							  "CED" integer NULL, 
							  "CHE" integer NULL, 
							  "CIV" integer NULL, 
							  "ELN" integer NULL, 
							  "MAT" integer NULL, 
							  "PCD" integer NULL);