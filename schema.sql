
CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
	username TEXT UNIQUE,
	password TEXT,
	admin BOOLEAN,
	visible BOOLEAN,
	created_at TIMESTAMP
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
	name TEXT UNIQUE,
	description TEXT,
	visible BOOLEAN,
	address TEXT
);

CREATE TABLE receipts (
    id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants,
	user_id INTEGER REFERENCES users,
	dishes TEXT,
	price INTEGER,
	additional_info TEXT,
	created_at TIMESTAMP
);

CREATE TABLE dishes (
    id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants,
	dish_name TEXT,
	visible BOOLEAN,
	price INTEGER
);

CREATE TABLE receiptdishes (
	receipt_id INTEGER REFERENCES receipts,
	dish_id INTEGER REFERENCES dishes
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	restaurant_id INTEGER REFERENCES restaurants,
	stars INTEGER,
	review TEXT,
	visible BOOLEAN,
	created_at TIMESTAMP
);
