DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(255) UNIQUE NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS publicaciones;

CREATE TABLE IF NOT EXISTS publicaciones (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    url_imagen VARCHAR(255),
    id_usuario INT REFERENCES usuarios (id) ON DELETE CASCADE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS comentarios;

CREATE TABLE IF NOT EXISTS comentarios (
    comentario VARCHAR(255) NOT NULL,
    id_publicacion INT REFERENCES publicaciones (id),
    id_usuario INT REFERENCES usuarios (id) ON DELETE SET NULL,
    fecha_creacion timestamptz NOT NULL
);


INSERT INTO usuarios (usuario, nombre, email, password, fecha_creacion) VALUES
    ('maria_gomez', 'María Gómez', 'maria.gomez@email.com', 'maria123', NOW()),
    ('luis_fernandez', 'Luis Fernández', 'luis.fernandez@email.com', 'luis123', NOW()),
    ('ana_torres', 'Ana Torres', 'ana.torres@email.com', 'ana456', NOW());

INSERT INTO publicaciones (id_usuario, titulo, contenido, url_imagen, fecha_creacion) VALUES
    (1, 'El poder de la rutina matutina: Cómo empezar tu día con intención',
    'Descubre cómo una rutina matutina puede mejorar tu enfoque y bienestar. Desde meditar hasta evitar el celular, cada hábito suma para empezar mejor tu día.',
    'https://example.com/img/rutina-matutina.jpg', NOW()),

    (2, '5 hábitos para mejorar tu energía durante el día',
    'Dormir bien es solo el comienzo. Aprende cómo pequeños cambios como la hidratación y el movimiento matutino pueden marcar una gran diferencia.',
    'https://example.com/img/energia-habitos.jpg', NOW()),

    (3, 'Cómo evitar distracciones digitales desde la mañana',
    'Las notificaciones pueden arruinar tu enfoque desde temprano. Te mostramos estrategias para proteger tu tiempo y tu mente.',
    'https://example.com/img/sin-celular.jpg', NOW());

INSERT INTO comentarios (comentario, id_publicacion, id_usuario, fecha_creacion) VALUES
    ('¡Muy buen artículo! Ya empecé a dejar el celular al despertar y me siento más enfocada.', 1, 3, NOW()),
    ('No sabía que el agua en ayunas tenía tanto impacto. Gracias por el tip.', 1, 2, NOW()),
    ('¿Podrías recomendar una app para meditar por la mañana?', 2, 1, NOW()),
    ('Totalmente de acuerdo, las redes sociales son una trampa desde temprano.', 3, 3, NOW());
