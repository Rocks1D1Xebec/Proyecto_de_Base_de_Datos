CREATE DATABASE Tienda_Juegos;
use Tienda_Juegos;

create table Rol(
	id_rol int auto_increment,
	nombre_rol varchar(50)
);

create table Usuario(
	id_usuario int auto_increment,
    id_rol int,
	usuario varchar(50),
    password varchar(50),
    email varchar(50)
);

create table Juego(
	id_juego int auto_increment,
    id_desarrollador int,
	titulo varchar(50),
    precio decimal(10,2),
    fecha_lanzamiento date,
    descripcion varchar(500)
);

create table Biblioteca_Personal(
	id_biblioteca int,
	id_usuario int,
    id_juego int
);

create table Compra(
	id_compra int,
    id_usuario int,
	fecha_compra datetime,
    total_pagado decimal(10,2),
    metodo_pago varchar(50)
);

create table Categoria_Genero(
	id_categoria int,
	descripcion varchar(500)
);

