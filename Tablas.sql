CREATE DATABASE Tienda_Juegos;
use Tienda_Juegos;

create table Rol(
	id_rol int auto_increment primary key,
	nombre_rol varchar(50)
);
insert into Rol (nombre_rol) values ('usuario');
insert into Rol (nombre_rol) values ('desarrollador');
insert into Rol (nombre_rol) values ('administrador');


create table Usuario(
	id_usuario int auto_increment primary key,
	id_rol int,
    foreign key (id_rol) references Rol(id_rol),
	usuario varchar(50),
    password varchar(50),
    email varchar(50),
    
    -- bloqueo de cuenta
    estado enum ('activo','bloqueado') default 'activo'
);
SELECT * FROM Usuario;
create table Juego(
	id_juego int auto_increment primary key,
	id_desarrollador int,
    foreign key (id_desarrollador) references Usuario(id_usuario),
	titulo varchar(50),
    precio decimal(10,2),
    fecha_lanzamiento date,
    descripcion varchar(500)
);

create table Biblioteca_Personal(
	id_biblioteca int auto_increment primary key,
	id_usuario int,
	foreign key (id_usuario) references Usuario(id_usuario),
	id_juego int,
    foreign key (id_juego) references Juego(id_juego)
);

create table Compra(
	id_compra int auto_increment primary key,
	id_usuario int,
	foreign key (id_usuario) references Usuario(id_usuario),
	fecha_compra datetime,
    total_pagado decimal(10,2),
    metodo_pago varchar(50)
);

create table Categoria_Genero(
	id_categoria int auto_increment primary key,
	descripcion varchar(500)
);

