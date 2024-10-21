-- task7
-- Average score

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	DECLARE average_score FLOAT;

	SELECT SUM(score) / COUNT(*) INTO average_score
	FROM corrections WHERE user_id = user_id;

	UPDATE users SET average_score = average_score WHERE id = user_id;
END//	

DELIMITER ;
