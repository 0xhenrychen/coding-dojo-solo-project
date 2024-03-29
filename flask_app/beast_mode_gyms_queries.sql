SELECT * FROM users;
SELECT * FROM classes;
SELECT * FROM joined_classes;
SELECT * FROM comments;

SET FOREIGN_KEY_CHECKS = 0;
                    DELETE FROM classes
                    WHERE ID = 20;
                    SET FOREIGN_KEY_CHECKS = 1;
                    

 SELECT * FROM comments
                    JOIN users ON users.id = comments.user_id
                    WHERE comments.class_id = 1
                    ORDER BY comments.created_at ASC;


SELECT * FROM classes
                    WHERE classes.id = 18
DELETE FROM classes
                    WHERE class.ID = 18;
            
DELETE FROM classes
            WHERE ID = 1;

SELECT * FROM classes C
                    JOIN users TE ON TE.id = C.trainee_id
                    JOIN users TR ON TR.id = C.trainer_id
                    WHERE C.trainee_id != 2 OR C.trainee_id IS NULL
                    ORDER BY class_date ASC, class_time ASC;

SELECT * FROM classes
                    WHERE classes.trainee_id != 2 OR classes.trainee_id IS NULL
                    ORDER BY class_date ASC, class_time ASC;
                    
SELECT * FROM classes
WHERE trainer_id = 5;

UPDATE classes
                    JOIN users ON users.id = classes.trainee_id
                    SET trainee_id = NULL
                    WHERE classes.id = 5 AND users.id = 2;
                    
INSERT INTO joined_classes (user_id, class_id)
                    VALUES (2, 1);

SELECT * from joined_classes
JOIN classes ON classes.id = joined_classes.class_id
JOIN users ON users.id = joined_classes.user_id
WHERE users.id = 2;

DELETE FROM joined_classes
WHERE class_id = 7 AND user_id = 2;

SELECT * FROM classes C
JOIN joined_classes JCC ON JCC.class_id = C.id
JOIN joined_classes JCU ON JCU.user_id = 2
WHERE C.id != JCC.class_id
ORDER BY class_date ASC, class_time ASC;

SELECT * from classes
                    JOIN joined_classes
                    JOIN users
                    WHERE joined_classes.user_id = !3
                    ORDER BY class_date ASC, class_time ASC;

SELECT * from classes
                    LEFT JOIN joined_classes ON classes.id = joined_classes.class_id
                    WHERE joined_classes.user_id IS NULL OR joined_classes.user_id != 3;

SELECT * from joined_classes
                    JOIN classes ON classes.id = joined_classes.class_id
                    JOIN users ON users.id = joined_classes.user_id
                    JOIN users TR ON TR.id = classes.trainer_id 
                    WHERE users.id = 3
                    ORDER BY classes.class_date ASC, classes.class_time ASC;

SELECT * from classes
                    LEFT JOIN joined_classes ON classes.id = joined_classes.class_id
                    JOIN users TR ON TR.id = classes.trainer_id
                    WHERE joined_classes.user_id IS NULL OR joined_classes.user_id != 2
                    ORDER BY class_date ASC, class_time ASC;
                    
                    SELECT * from classes
                    JOIN joined_classes ON classes.id = joined_classes.class_id
                    JOIN users TR ON TR.id = classes.trainer_id
                    WHERE joined_classes.user_id != 2 AND (classes.id != joined_classes.class_id AND joined_classes.user_id != 2)
                    ORDER BY classes.class_date ASC, classes.class_time ASC;
                    
                    
                    
SELECT * FROM joined_classes
                    JOIN users ON users.id = joined_classes.user_id
                    JOIN classes ON classes.id = joined_classes.class_id
                    WHERE classes.id = 1;
                    
SELECT * FROM classes
LEFT JOIN users ON users.id = classes.trainer_id
WHERE classes.id NOT IN (SELECT class_id FROM joined_classes WHERE user_id = 2);

INSERT INTO comments (class_comment, class_id, user_id)
                    VALUES ("hey world 123", 1, 2);
                    
SELECT * FROM comments
LEFT JOIN users ON users.id = comments.user_id
WHERE comments.class_id = 2;

SELECT * FROM classes
                    JOIN users ON users.id = classes.trainer_id
                    WHERE classes.trainer_id = 1
                    FORMAT classes.class_time("19:30:10", "%h %i %s %p")
                    ORDER BY class_date ASC, class_time ASC;
