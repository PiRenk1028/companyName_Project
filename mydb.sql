-- CREATE DATABASE companyName;
USE companyName;

DROP TABLE IF EXISTS General;
CREATE TABLE General(
	id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(30) NOT NULL,
    middleName VARCHAR(30),
    lastName VARCHAR(30) NOT NULL,
    dateOfBirth DATE DEFAULT '2000-01-01',
    email VARCHAR(255)
);

INSERT INTO General(firstName, middleName, lastName,email)
VALUES ("Lorem",NULL,"Ipsum",NULL),
	   ("Daniel",NULL,"Stone",NULL),
       ("Max",NULL,"Scherzer",NULL);
       
SELECT *
FROM General;



