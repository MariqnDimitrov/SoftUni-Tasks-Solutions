CREATE VIEW view_addresses
AS 
SELECT
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	e.department_id,
	CONCAT(a.number,' ', a.street) as address
FROM 
	employees AS e
JOIN
	addresses AS a
ON 
	a.id = e.address_id;