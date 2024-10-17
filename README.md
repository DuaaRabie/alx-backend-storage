# 0x00. MySQL advanced
### Creating Tables with Constraints

To create tables with constraints in MySQL, you can use the `CREATE TABLE` statement along with various constraint keywords. Here's an example:

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    salary DECIMAL(10,2),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

Key points:
- `PRIMARY KEY`: Ensures uniqueness and not null
- `NOT NULL`: Prevents null values
- `UNIQUE`: Ensures all values in a column are different
- `FOREIGN KEY`: Establishes a relationship between tables

### Optimizing Queries by Adding Indexes

Indexes can significantly improve query performance. To add an index:

```sql
CREATE INDEX idx_name ON table_name (column_name);
```

Or add multiple columns:

```sql
CREATE INDEX idx_multi_columns ON table_name (column1, column2);
```

Key points:
- Indexes speed up WHERE clause searches
- They also improve JOIN operations
- Be cautious with too many indexes as they slow down insert/update operations

### Implementing Stored Procedures and Functions

Stored procedures and functions allow you to encapsulate complex logic within the database:

```sql
DELIMITER //

CREATE PROCEDURE getEmployeeDetails(IN employeeId INT)
BEGIN
    SELECT * FROM employees WHERE id = employeeId;
END //

DELIMITER ;

-- Call the procedure
CALL getEmployeeDetails(1);

-- Create a function
DELIMITER //
CREATE FUNCTION calculateSalaryBonus(salary DECIMAL(10,2)) RETURNS DECIMAL(10,2)
BEGIN
    RETURN salary * 0.05;
END //
DELIMITER ;

-- Use the function
SELECT calculateSalaryBonus(50000);
```

Key points:
- Procedures can accept parameters and execute multiple statements
- Functions return a single value
- Both improve code reusability and maintainability

### Implementing Views

Views provide a simplified way to access data from one or more tables:

```sql
CREATE VIEW employee_summary AS
SELECT e.id, e.name, d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.id;

-- Query the view
SELECT * FROM employee_summary;
```

Key points:
- Views can simplify complex queries
- They don't store data but provide a virtual table
- Useful for security by limiting access to certain data

### Implementing Triggers

Triggers automatically execute a set of actions when a specific event occurs:

```sql
CREATE TRIGGER update_log_trigger
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, old_value, new_value, timestamp)
    VALUES ('employees', OLD.name, NEW.name, NOW());
END;
```

Key points:
- Triggers run automatically on specific events (INSERT, UPDATE, DELETE)
- They can perform validation checks
- Useful for maintaining audit trails or cascading effects

These features allow you to create more complex, efficient, and maintainable database structures and operations in MySQL. Remember to use these tools judiciously based on your specific needs and performance requirements.

Citations:
[1] https://dev.mysql.com/doc/mysql/en/create-table.html
[2] https://stackoverflow.com/questions/3002605/how-do-i-add-indexes-to-mysql-tables
[3] https://dev.mysql.com/doc/en/create-index.html
[4] https://www.digitalocean.com/community/tutorials/how-to-use-stored-procedures-in-mysql
[5] https://dev.mysql.com/doc/refman/8.2/en/create-table-check-constraints.html
[6] https://www.quora.com/What-should-be-considered-before-adding-an-index-on-a-MySQL-table-Can-it-negatively-impact-performance
[7] https://www.geeksforgeeks.org/mysql-create-index-statement/
[8] https://www.informit.com/articles/article.aspx?p=377652
[9] https://www.linkedin.com/advice/3/what-best-practices-using-indexes-triggers
[10] https://www.digitalocean.com/community/tutorials/how-to-use-indexes-in-mysql
