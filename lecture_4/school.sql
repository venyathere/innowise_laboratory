-- 1
CREATE TABLE [grades] ( 
  [id] INTEGER NOT NULL,
  [student_id] INTEGER NOT NULL,
  [subject] TEXT NOT NULL,
  [grade] INTEGER NOT NULL,
   PRIMARY KEY ([id])
);
CREATE TABLE [students] ( 
  [id] INTEGER NOT NULL,
  [full_name] TEXT NOT NULL,
  [birth_year] INTEGER NOT NULL,
   PRIMARY KEY ([id])
);
ALTER TABLE [grades] ADD FOREIGN KEY ([student_id]) REFERENCES [students] ([id]) ON DELETE CASCADE ON UPDATE CASCADE;
-- 2
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94);
-- 3
select s.full_name, g.grade 
from grades g
join students s on g.student_id = s.id
where s.full_name = 'Alice Johnson';
-- 4
select s.full_name, avg(g.grade) AS avg_grade
from grades g
join students s on g.student_id = s.id
group by s.full_name;
-- 5
select full_name 
from students
where birth_year > 2004;
-- 6
select subject, avg(grade)
from grades
group by subject;
-- 7
select s.full_name, avg(g.grade) AS avg_grade
from grades g
join students s on g.student_id = s.id
group by s.full_name
ORDER BY avg_grade desc
LIMIT 3;
-- 8
select s.full_name
from grades g
join students s on g.student_id = s.id
where g.grade > 80
group by s.full_name;
-- 9
