CREATE TABLE IF NOT EXISTS manufacturers(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
name VARCHAR
);
CREATE TABLE IF NOT EXISTS models(
id INT GENERATED ALWAYS AS IDENTITY (START WITH 1000) PRIMARY KEY, 
model_name VARCHAR,
manufacturer_id INT,

CONSTRAINT fk_manufacturers_models
FOREIGN KEY (manufacturer_id)
REFERENCES manufacturers(id)
);
CREATE TABLE IF NOT EXISTS production_years(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
established_on DATE,
manufacturer_id INT,

CONSTRAINT fk_manufacturers_production_years
FOREIGN KEY (manufacturer_id)
REFERENCES manufacturers(id)
);
INSERT INTO manufacturers(name)
VALUES ('BMW'),
		('Tesla'),
		('Lada')
;
INSERT INTO models(model_name, manufacturer_id)
VALUES ('X1', 1),
		('i6', 1),
		('Model S', 2),
		('Model X', 2),
		('Model 3', 2),
		('Nova', 3)
;
INSERT INTO production_years(established_on, manufacturer_id)
VALUES	('1916-03-01', 1),
		('2003-01-01', 2),
		('1966-05-01', 3)
;