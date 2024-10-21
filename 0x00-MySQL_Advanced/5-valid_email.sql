-- task5
-- Email validation to sent

DELIMITER //

CREATE TRIGGER validate_email_after_update
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF NEW.email <> OLD.email THEN
			SET NEW.valid_email = 0;
		END IF;
	END;
//
DELIMITER ;
