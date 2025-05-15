-- Active: 1743529530148@@127.0.0.1@3306@biblioteca_digital_personal
DROP DATABASE IF EXISTS biblioteca_digital_personal;
CREATE DATABASE biblioteca_digital_personal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE biblioteca_digital_personal;

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role_id INT,
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE libro_personal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150),
    autor VARCHAR(100),
    genero VARCHAR(50),
    anio_publicacion INT,
    url VARCHAR(255),
    notas TEXT,
    etiquetas VARCHAR(255),
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES users(id)  
);




INSERT INTO roles (name) VALUES ('Admin'), ('Moderador'), ('Lector'); 

SHOW TABLES

SELECT * FROM libro_personal
