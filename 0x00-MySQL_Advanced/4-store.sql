-- task4
-- Buy buy buy

-- Create a transaction to ensure data consistency
START TRANSACTION;

-- Create the trigger
DELIMITER //
CREATE TRIGGER update_item_quantity_after_order
AFTER INSERT ON order
FOR EACH ROW
BEGIN
   UPDATE items SET quantity = quatinty - NEW.number WHERE naem = NEW.item_name
END;//
DELIMITER ;

-- Commit the transaction
COMMIT;
