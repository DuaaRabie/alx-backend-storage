-- task4
-- Buy buy buy

-- Create a transaction to ensure data consistency
START TRANSACTION;

-- Create the trigger
DELIMITER //
CREATE TRIGGER update_item_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_id INT;
    
    -- Get the ID of the ordered item
    SELECT order_item_id INTO item_id FROM order_items WHERE order_id = NEW.id;
    
    -- Check if the item exists in the items table
    IF EXISTS (SELECT 1 FROM items WHERE id = item_id) THEN
        UPDATE items
        SET quantity = CASE
            WHEN quantity IS NULL THEN NULL
            ELSE quantity - 1
        END
        WHERE id = item_id;
        
        -- Log the update operation
        INSERT INTO order_log (order_id, item_id, old_quantity, new_quantity)
        VALUES (NEW.id, item_id, 
               (SELECT quantity FROM items WHERE id = item_id),
               (SELECT CASE WHEN quantity IS NULL THEN NULL ELSE quantity - 1 END FROM items WHERE id = item_id));
    END IF;
END;//
DELIMITER ;

-- Commit the transaction
COMMIT;
