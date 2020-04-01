CREATE TABLE Login
(
   id          INT            NOT NULL AUTO_INCREMENT,
   aws       VARCHAR(255),
   firstName  VARCHAR(255),
   lastName   VARCHAR(255),
   password    VARCHAR(255),
   userId  VARCHAR(255),
   PRIMARY KEY (id)
);

INSERT INTO user_details(email,first_Name,last_Name,password) VALUES ('admin@admin.com','admin','admin','admin');

INSERT INTO user_details(email,first_Name,last_Name,password) VALUES ('john@gmail.com','john','doe','johndoe');
INSERT INTO user_details(email,first_Name,last_Name,password) VALUES ('sham@yahoo.com','sham','tis','shamtis');