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