CREATE DATABASE Groupbuy;
USE Groupbuy;

CREATE TABLE Group_buying_merchant(
	merchant_userid VARCHAR(255) NOT NULL,
	store_name VARCHAR(255),
	store_id VARCHAR(255),
	address VARCHAR(255),
	business_hours VARCHAR(255),
	CONSTRAINT Group_buying_merchant_PK  PRIMARY KEY(store_id),
	UNIQUE(store_id)
);

CREATE TABLE Customer(
	userid VARCHAR(255) NOT NULL,
 	store_id VARCHAR(255) NOT NULL,
	user_name VARCHAR(5),
	phone VARCHAR(10) DEFAULT NULL,
	blacklist TINYINT DEFAULT 0,
	CONSTRAINT Customer_PK PRIMARY KEY(userid, store_id)
);

CREATE TABLE Product(
	product_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	store_id VARCHAR(255) NOT NULL,
	price INT,
	unit VARCHAR(255),
	product_describe TEXT,
	supplier_name VARCHAR(255),
	product_name VARCHAR(255),
	product_picture BLOB,
	CONSTRAINT Product_FK FOREIGN KEY(store_id) REFERENCES Group_buying_merchant(store_id)
);

CREATE TABLE Group_buying_product(
	group_buying_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	purchase_quantity INT,
	launch_date DATETIME,
	statement_date DATETIME,
	arrival_date DATETIME,
	due_days TINYINT,
	inventory INT,
	income DOUBLE,
	cost DOUBLE,
	product_id BIGINT UNSIGNED,
	CONSTRAINT Group_buying_product_FK FOREIGN KEY(product_id) REFERENCES Product(product_id)
);

CREATE TABLE `Order`(
	order_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	userid VARCHAR(255) NOT NULL,
	group_buying_id BIGINT UNSIGNED NOT NULL ,
	quantity INT,
	receive_status Boolean DEFAULT FALSE,
	CONSTRAINT Order_FK1 FOREIGN KEY(userid) REFERENCES Customer(userid),
	CONSTRAINT Order_FK2 FOREIGN KEY(group_buying_id) REFERENCES Group_buying_product(group_buying_id)
);
