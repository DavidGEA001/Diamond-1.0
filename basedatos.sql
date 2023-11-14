CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
    id_usuarios int(25) auto_increment not null,
    nombre varchar(250) ,
    apellido varchar(250) ,
    email varchar(250) not null,
    password varchar(250) not null,
    fecha date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id_usuarios),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE = InnoDB;

CREATE TABLE productos(
    id_productos int(25) auto_increment not null,
    id_usuarios int(25) not null,
    titulo varchar(250) not null,
    descripcion text,
    fecha date not null,
    CONSTRAINT pk_productos PRIMARY KEY(id_productos),
    CONSTRAINT fk_productos_usuarios FOREIGN KEY(id_usuarios) REFERENCES usuarios(id_usuarios)
) ENGINE = InnoDB;

