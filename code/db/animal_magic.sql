DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    phone VARCHAR
);

CREATE TABLE animals ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    species VARCHAR,
    dob VARCHAR,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    note_text TEXT,
    appt_date VARCHAR,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);