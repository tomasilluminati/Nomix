
#
#           ----------------
#           || Nomix V1.1 ||
#           ----------------
# 
#           by Tomás Illuminati
#
#           DEVELOPED IN PYTHON 3.11.0 64-bit
#           ENCODING: UTF-8
#           DATE: FEB 19 2024
#        
#           DESCRIPTION: FUNCTION THAT GENERATES NAMES AND SURNAMES IN A CUSTOMIZABLE OR RANDOM WAY.
#



import random


def get_name(data_type=str):

    data_type = data_type.upper()

#USA NAMES
    if data_type == "USA_MALE_NAME":
        USA_MALE_NAME = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas', 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth', 'Joshua', 'George', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'Nicholas', 'Eric', 'Stephen', 'Jonathan', 'Larry', 'Justin', 'Scott', 'Brandon', 'Frank', 'Benjamin', 'Samuel', 'Gregory', 'Raymond', 'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry', 'Tyler', 'Aaron', 'Jose', 'Henry', 'Douglas', 'Peter', 'Adam', 'Nathan', 'Zachary', 'Walter', 'Kyle', 'Harold', 'Carl', 'Jeremy', 'Keith', 'Roger', 'Gerald', 'Ethan', 'Arthur', 'Terry', 'Christian', 'Sean', 'Lawrence', 'Austin', 'Joe', 'Noah', 'Jesse', 'Albert', 'Bryan', 'Billy', 'Bruce', 'Willie', 'Jordan', 'Dylan', 'Alan', 'Ralph', 'Gabriel', 'Roy', 'Juan', 'Wayne', 'Eugene', 'Logan', 'Randy', 'Louis', 'Russell', 'Vincent', 'Philip', 'Bobby', 'Johnny', 'Bradley', 'Martin', 'Craig', 'Stanley', 'Leonard', 'Chester', 'Melvin', 'Lloyd', 'Theodore', 'Caleb', 'Clarence', 'Glen', 'Hector', 'Lester', 'Gavin', 'Alfred', 'Cameron', 'Chase', 'Antonio', 'Miles', 'Travis', 'Ronnie', 'Leon', 'Jeremiah', 'Cody', 'Sam', 'Seth', 'Elijah', 'Blake', 'Nathaniel', 'Adrian', 'Don', 'Jared', 'Evan', 'Franklin', 'Oscar', 'Joel', 'Mitchell', 'Jorge', 'Victor', 'Dean', 'Calvin', 'Derrick', 'Liam', 'Gordon', 'Allan', 'Garrett', 'Derek', 'Jayden', 'Luke', 'Maxwell', 'Landon', 'Leo', 'Armando', 'Clinton', 'Brett', 'Erick', 'Mason', 'Julian', 'Danny', 'Clayton', 'Harrison', 'Dwayne', 'Shaun', 'Drew', 'Preston', 'Kurt', 'Damian', 'Colin', 'Andre', 'Simon', 'Jonathon', 'Dillon', 'Fabian', 'Raul', 'Gerard', 'Nelson', 'Miguel', 'Tristan', 'Graham', 'Riley', 'Perry', 'Terrence', 'Adriel', 'Fernando', 'Wesley', 'Eli', 'Eduardo', 'Cesar', 'Javier', 'Santiago', 'Angel', 'Aiden', 'Ruben', 'Lance', 'Edwin', 'Julio', 'Avery', 'Collin', 'Trevor', 'Conner', 'Israel', 'Jake', 'Ray', 'Wade', 'Dexter', 'Felix', 'Gideon', 'Hank', 'Ian', 'Kendrick', 'Marshall', 'Nolan', 'Otis', 'Pierce', 'Quentin', 'Sawyer', 'Tobias', 'Ulises', 'Vance', 'Warren', 'Xavier', 'Yahir', 'Zane']
        return random.choice(USA_MALE_NAME)
    
    elif data_type == "USA_FEMALE_NAME":
        USA_FEMALE_NAME = ['Mary', 'Jennifer', 'Linda', 'Patricia', 'Elizabeth', 'Susan', 'Jessica', 'Sarah', 'Karen', 'Nancy', 'Lisa', 'Betty', 'Margaret', 'Emily', 'Kimberly', 'Donna', 'Michelle', 'Dorothy', 'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Laura', 'Sharon', 'Cynthia', 'Kathleen', 'Amy', 'Shirley', 'Angela', 'Helen', 'Anna', 'Brenda', 'Pamela', 'Nicole', 'Ruth', 'Katherine', 'Christine', 'Sandra', 'Emma', 'Janet', 'Carolyn', 'Virginia', 'Maria', 'Samantha', 'Debra', 'Rachel', 'Julie', 'Joan', 'Heather', 'Frances', 'Teresa', 'Christina', 'Martha', 'Catherine', 'Diane', 'Joyce', 'Evelyn', 'Kelly', 'Alice', 'Olivia', 'Judith', 'Grace', 'Janice', 'Danielle', 'Lauren', 'Marie', 'Victoria', 'Joanne', 'Megan', 'Rose', 'Wanda', 'Sara', 'Ashley', 'Natalie', 'Audrey', 'Judy', 'Theresa', 'Stacy', 'Lori', 'Denise', 'Erin', 'Vanessa', 'Sylvia', 'Diana', 'Tiffany', 'Jane', 'Bonnie', 'Amber', 'Beverly', 'Paula', 'Dawn', 'Rita', 'Christy', 'Holly', 'Brittany', 'Jacqueline', 'Marilyn', 'Lillian', 'Kristen', 'Tammy', 'Robin', 'Kathy', 'Gloria', 'Ruby', 'Rosemary', 'Tracy', 'Hannah', 'Chelsea', 'Marlene', 'Thelma', 'Lois', 'Norma', 'Peggy', 'Jill', 'Kathryn', 'Mildred', 'Colleen', 'Edna', 'Gina', 'Vivian', 'Carla', 'Yvonne', 'Michele', 'Josephine', 'Annie', 'Renee', 'Eleanor', 'Joann', 'Valerie', 'Doris', 'Darlene', 'Lucy', 'Suzanne', 'Becky', 'Ethel', 'Veronica', 'Charlene', 'Edith', 'Jean', 'Roberta', 'Anita', 'Marjorie', 'Lydia', 'Geraldine', 'Clara', 'Agnes', 'Bessie', 'Delores', 'June', 'Penny', 'Maureen', 'Maxine', 'Jan', 'Nora', 'Sherry', 'Dolores', 'Jeanne', 'Juanita', 'Yolanda', 'Gladys', 'Harriet', 'Shelia', 'Willie', 'Alma', 'Jessie', 'Janie', 'Francine', 'Hazel', 'Loretta', 'Shelly', 'Robyn', 'Laurel', 'Mandy', 'Alicia', 'Misty', 'Daisy', 'Tonya', 'Wendy', 'Melinda', 'Vicki', 'Connie', 'Lena', 'Arlene', 'Gail', 'Debbie', 'Marianne', 'Lynda', 'Jeannie', 'Leah', 'Marcella', 'Claudia', 'Kristin', 'Jenny', 'Bridget', 'Tamara', 'Sue', 'Dina', 'Christie', 'Cassandra', 'Patti', 'Desiree', 'Marsha', 'Lynette', 'Rosa', 'Kerry', 'Tina', 'Carrie', 'Margo', 'Rene', 'Dena', 'Janis', 'Leigh', 'Elaine', 'Aimee']
        return random.choice(USA_FEMALE_NAME)


#ENGLISH NAMES
    elif data_type == "ENGLISH_MALE_NAME":
        ENGLISH_MALE_NAME  = ['Aaron', 'Adam', 'Adrian', 'Alan', 'Albert', 'Alex', 'Alexander', 'Alfred', 'Andrew', 'Anthony', 'Arthur', 'Barry', 'Benjamin', 'Bernard', 'Billy', 'Bradley', 'Brian', 'Bruce', 'Carl', 'Charles', 'Christopher', 'Colin', 'Connor', 'Craig', 'Daniel', 'David', 'Dennis', 'Derek', 'Dominic', 'Donald', 'Douglas', 'Duncan', 'Edward', 'Edwin', 'Elliott', 'Eric', 'Ethan', 'Eugene', 'Evan', 'Frank', 'Frederick', 'Gabriel', 'Gary', 'George', 'Gerald', 'Graham', 'Gregory', 'Harold', 'Harry', 'Henry', 'Hugh', 'Ian', 'Isaac', 'Jack', 'Jacob', 'James', 'Jason', 'Jeffrey', 'Jeremy', 'Jerry', 'Jesse', 'Jim', 'Joe', 'John', 'Jonathan', 'Jordan', 'Joseph', 'Joshua', 'Julian', 'Justin', 'Keith', 'Kenneth', 'Kevin', 'Larry', 'Lawrence', 'Lee', 'Leonard', 'Liam', 'Louis', 'Lucas', 'Malcolm', 'Mark', 'Martin', 'Matthew', 'Max', 'Michael', 'Nathan', 'Neil', 'Nicholas', 'Oliver', 'Oscar', 'Patrick', 'Paul', 'Peter', 'Philip', 'Raymond', 'Richard', 'Robert', 'Roger', 'Ronald', 'Roy', 'Russell', 'Ryan', 'Samuel', 'Scott', 'Sean', 'Simon', 'Stephen', 'Steve', 'Steven', 'Stuart', 'Terry', 'Theodore', 'Thomas', 'Timothy', 'Toby', 'Tom', 'Tony', 'Tyler', 'Victor', 'Vincent', 'Walter', 'Wayne', 'William', 'Zachary']
        return random.choice(ENGLISH_MALE_NAME)
    
    elif data_type == "ENGLISH_FEMALE_NAME":
        ENGLISH_FEMALE_NAME = ['Abigail', 'Adelaide', 'Alexandra', 'Alice', 'Amanda', 'Amelia', 'Amy', 'Andrea', 'Angela', 'Ann', 'Anna', 'Anne', 'Annie', 'Aria', 'Ashley', 'Audrey', 'Ava', 'Barbara', 'Beatrice', 'Beth', 'Betty', 'Beverly', 'Brianna', 'Bridget', 'Brooke', 'Caitlin', 'Camila', 'Caroline', 'Catherine', 'Charlotte', 'Chloe', 'Clara', 'Claire', 'Daisy', 'Danielle', 'Diana', 'Donna', 'Dorothy', 'Edith', 'Eleanor', 'Elena', 'Elizabeth', 'Ella', 'Emily', 'Emma', 'Eva', 'Evelyn', 'Faith', 'Florence', 'Gabriella', 'Grace', 'Hannah', 'Harper', 'Hazel', 'Heather', 'Isabella', 'Isabelle', 'Jacqueline', 'Jade', 'Jane', 'Jasmine', 'Jennifer', 'Jessica', 'Joan', 'Jordan', 'Josephine', 'Joyce', 'Julia', 'Juliana', 'Juliet', 'Katherine', 'Katie', 'Kayla', 'Kimberly', 'Lily', 'Laura', 'Lauren', 'Leah', 'Lillian', 'Linda', 'Lisa', 'Lucy', 'Lydia', 'Madeline', 'Madison', 'Makayla', 'Maria', 'Mariana', 'Marilyn', 'Marissa', 'Mary', 'Maya', 'Melissa', 'Mia', 'Michelle', 'Molly', 'Natalie', 'Nicole', 'Olivia', 'Paige', 'Penelope', 'Rachel', 'Rebecca', 'Rose', 'Ruby', 'Samantha', 'Sara', 'Sarah', 'Scarlett', 'Sophia', 'Sophie', 'Stella', 'Stephanie', 'Susan', 'Teresa', 'Valerie', 'Vanessa', 'Victoria', 'Violet', 'Virginia', 'Wendy', 'Willow', 'Zoe']
        return random.choice(ENGLISH_FEMALE_NAME)


#FRENCH NAMES
    elif data_type == "FRENCH_MALE_NAME":
        FRENCH_MALE_NAME =  ['Louis', 'Paul', 'Antoine', 'Jean', 'Pierre', 'Jacques', 'François', 'Vincent', 'Charles', 'Guillaume', 'Alexandre', 'Michel', 'Thierry', 'Philippe', 'Mathieu', 'Lucas', 'Julien', 'Sébastien', 'Damien', 'Romain', 'Gérard', 'Hugo', 'David', 'Yves', 'Sylvain', 'Olivier', 'Étienne', 'Maxime', 'Bruno', 'Georges', 'Nicolas', 'Marc', 'Cédric', 'Fabien', 'Léo', 'Benoît', 'Yannick', 'Victor', 'Grégoire', 'Alexis', 'Maurice', 'Fabrice', 'Adrien', 'Cyril', 'Samuel', 'René', 'Jérôme', 'Gilles', 'Rémi', 'Franck', 'Jean-Pierre', 'Ludovic', 'Denis', 'Serge', 'Jules', 'Arnaud', 'Léon', 'Patrice', 'Yvan', 'Thomas', 'Christophe', 'Michaël', 'Thibault', 'Quentin', 'Laurent', 'Didier', 'Alain', 'Éric', 'Gilbert', 'Emmanuel', 'Benjamin', 'François-Xavier', 'Stéphane', 'Nathan', 'Christian', 'Hervé', 'Renaud', 'Alex', 'Frédéric', 'Bertrand', 'Kévin', 'Pascal', 'Raphaël', 'Gaston', 'Gaëtan', 'Hugues', 'Alban', 'Simon', 'Anthony', 'Adrian', 'Valentin', 'Patrick', 'Matthieu', 'Maxence', 'Daniel', 'Dominique', 'Claude', 'Rémy', 'Alphonse', 'Luc', 'Régis', 'Sacha', 'Yann', 'Lionel', 'Yvon', 'André', 'Jérémy', 'Jean-Claude', 'Eddy', 'Gustave', 'Tristan', 'Florian', 'Léopold', 'Roger', 'Édouard', 'Noël', 'Émile', 'Marcel', 'Félix', 'Théo', 'Lucien', 'Arthur', 'Baptiste', 'Robin']
        return random.choice(FRENCH_MALE_NAME)

    elif data_type == "FRENCH_FEMALE_NAME":
        FRENCH_FEMALE_NAME = ['Sophie', 'Camille', 'Marie', 'Lucie', 'Claire', 'Charlotte', 'Julie', 'Emilie', 'Alice', 'Laura', 'Nathalie', 'Sandrine', 'Céline', 'Aurélie', 'Elise', 'Manon', 'Valérie', 'Isabelle', 'Caroline', 'Chloé', 'Léa', 'Laetitia', 'Mathilde', 'Marion', 'Mélanie', 'Pauline', 'Anne', 'Cécile', 'Aude', 'Audrey', 'Hélène', 'Valentine', 'Elodie', 'Lola', 'Christine', 'Marine', 'Christelle', 'Claudine', 'Catherine', 'Vanessa', 'Juliette', 'Fanny', 'Emmanuelle', 'Amandine', 'Émilie', 'Marianne', 'Danielle', 'Monique', 'Coralie', 'Nina', 'Olivia', 'Elsa', 'Béatrice', 'Florence', 'Laurine', 'Odette', 'Maëlle', 'Isabella', 'Nadia', 'Mireille', 'Rosalie', 'Amélie', 'Éloïse', 'Clémence', 'Cassandra', 'Sylvie', 'Élise', 'Héloïse', 'Gabrielle', 'Sandra', 'Morgane', 'Carole', 'Colette', 'Angélique', 'Inès', 'Yvonne', 'Natalie', 'Yvette', 'Jacqueline', 'Liliane', 'Léonie', 'Lorraine', 'Nicole', 'Jeanne', 'Aline', 'Océane', 'Joëlle', 'Flavie', 'Élizabeth', 'Chantal', 'Claudia', 'Louise', 'Anne-Marie', 'Léonore', 'Diane', 'Alicia', 'Suzanne', 'Amalia', 'Estelle', 'Rose', 'Victoria', 'Bérénice', 'Noémie', 'Sylviane', 'Lucienne', 'Margot', 'Renée', 'Véronique', 'Marcelle', 'Ségolène', 'Maïlys', 'Édith', 'Yolande', 'Josette', 'Simone', 'Justine', 'Célestine', 'Lysiane', 'Floriane', 'Capucine', 'Thérèse', 'Violette', 'Priscilla', 'Eugénie', 'Roxane', 'Léontine', 'Honorine', 'Mélodie', 'Antoinette', 'Lilou', 'Faustine', 'Alexandra', 'Flore', 'Gisèle', 'Giselle', 'Irène', 'Ludmila', 'Maïté', 'Olympe', 'Romaine', 'Victoire', 'Albertine', 'Annette', 'Bernadette', 'Ghislaine', 'Claudie', 'Jeannine', 'Lucette', 'Roseline', 'Angele', 'Christiane', 'Lili', 'Michèle', 'Noëlle', 'Stéphanie', 'Émilienne', 'Clementine', 'Corinne', 'Francine', 'Jocelyne', 'Solange', 'Anne-Laure']
        return random.choice(FRENCH_FEMALE_NAME)
    

#SPANISH NAMES
    elif data_type == "SPANISH_MALE_NAME":
        SPAIN_MALE_NAME = ['Juan', 'Antonio', 'José', 'Manuel', 'Francisco', 'David', 'Javier', 'José Antonio', 'Daniel', 'Francisco Javier', 'José Luis', 'Francisco José', 'Ángel', 'Miguel', 'José Manuel', 'Alejandro', 'Rafael', 'Pedro', 'Juan Carlos', 'Luis', 'Fernando', 'Pablo', 'Sergio', 'Carlos', 'Andrés', 'Ignacio', 'Jorge', 'Roberto', 'José María', 'Mariano', 'Adrián', 'Óscar', 'Diego', 'Enrique', 'Víctor', 'Mario', 'Emilio', 'Eduardo', 'Rubén', 'Héctor', 'Alberto', 'Joaquín', 'Ricardo', 'Gonzalo', 'Marcos', 'Agustín', 'Jaime', 'Juan José', 'Ramón', 'Tomás', 'Ismael', 'Nicolás', 'Jesús', 'Manolo', 'Lorenzo', 'Salvador', 'Julián', 'Felipe', 'Guillermo', 'Armando', 'Alfonso', 'Eugenio', 'Esteban', 'Marcelo', 'Israel', 'Samuel', 'Alex', 'Germán', 'Eloy', 'Martín', 'Bruno', 'Raul', 'Teodoro', 'Aitor', 'Alonso', 'Cristian', 'Xavier', 'Mateo', 'Nacho', 'Félix', 'Xavi', 'Hugo', 'Óliver', 'Gerardo', 'Pascual', 'Borja', 'Iván', 'Juan Manuel', 'César', 'Cristóbal', 'Antón', 'Domingo', 'Luis Miguel', 'Gustavo', 'Moisés', 'Gabriel', 'Josué', 'Marc', 'Adrià', 'Pau', 'Joan', 'Biel', 'Albert', 'Iker', 'Alvaro', 'Jon', 'Raúl', 'Hector', 'Asier', 'Ivan', 'Julen', 'Eneko', 'Mikel', 'Ander', 'Unai', 'Beñat', 'Gorka', 'Ibai', 'Markel', 'Aimar', 'Igor', 'Edu', 'Txema', 'Ion', 'Aritz', 'Xabier', 'Telmo', 'Iñaki', 'Oier', 'Ekain', 'Xuban', 'Izan', 'Iñigo', 'Marco', 'Lucas', 'Elio', 'Benjamín', 'Gael', 'Valentín', 'Sebastián', 'Damián', 'Matías', 'Valentino', 'Santiago', 'Maximiliano', 'Dante', 'Ian', 'Leandro', 'Luciano', 'Axel', 'Ramiro', 'Facundo', 'Bautista', 'Benicio', 'Jeremías', 'Simón', 'Valentin', 'Rodrigo']
        return random.choice(SPAIN_MALE_NAME)

    elif data_type == "SPANISH_FEMALE_NAME":
        SPAIN_FEMALE_NAME = ['María', 'Carmen', 'Ana', 'Isabel', 'Laura', 'Marta', 'Elena', 'Sara', 'Raquel', 'Lucía', 'Cristina', 'Pilar', 'Natalia', 'Lourdes', 'Patricia', 'Silvia', 'Rosa', 'Alicia', 'Luisa', 'Beatriz', 'Mónica', 'Victoria', 'Inés', 'Lorena', 'Noelia', 'Paula', 'Concepción', 'Adela', 'Andrea', 'Clara', 'Celia', 'Verónica', 'Diana', 'Eva', 'Gemma', 'Begoña', 'Mercedes', 'Carolina', 'Sandra', 'Alba', 'Ángela', 'Marina', 'Cecilia', 'Olga', 'Montserrat', 'Margarita', 'Lidia', 'Esther', 'Nerea', 'Gloria', 'Rocío', 'Aurora', 'Miriam', 'Juana', 'Eloísa', 'Lola', 'Esperanza', 'Cayetana', 'Candela', 'Elvira', 'África', 'Berta', 'Amelia', 'Belén', 'Soledad', 'Maribel', 'Eulalia', 'Irene', 'Elisa', 'Manuela', 'Eugenia', 'Sofía', 'Elsa', 'Gabriela', 'Irma', 'Daniela', 'Guadalupe', 'Abril', 'Yolanda', 'Emilia', 'Julia', 'Nuria', 'Ruth', 'Amparo', 'Leonor', 'Angélica', 'Anabel', 'Aitana', 'Carlota', 'Ariadna', 'Violeta', 'Olivia', 'Emma', 'Martina', 'Valeria', 'Carla', 'Claudia', 'Adriana', 'Isabella', 'Ainhoa', 'Jimena', 'Alejandra', 'Nora', 'Lara', 'Lia', 'Camila', 'Valentina', 'Noa', 'Júlia', 'Aroa', 'Mireia', 'Naiara', 'Alma', 'Iris', 'Ona', 'Leire', 'Mara']
        return random.choice(SPAIN_FEMALE_NAME)
    

#RUSSIAN NAMES
    elif data_type == "RUSSIAN_MALE_NAME":
        RUSSIAN_MALE_NAME = ['Alexander', 'Andrei', 'Anton', 'Arkady', 'Artem', 'Boris', 'Dmitri', 'Evgeni', 'Fedor', 'Gennady', 'Georgi', 'Igor', 'Ilya', 'Ivan', 'Konstantin', 'Leonid', 'Maksim', 'Mikhail', 'Nikita', 'Nikolai', 'Oleg', 'Pavel', 'Petr', 'Roman', 'Sergei', 'Stanislav', 'Vadim', 'Valeri', 'Vasili', 'Viktor', 'Vladimir', 'Yuri', 'Yaroslav', 'Yevgeny', 'Zakhar', 'Alexey', 'Anatoly', 'Daniil', 'Denis', 'Egor', 'Gleb', 'Kirill', 'Matvei', 'Nikolay', 'Ruslan', 'Semyon', 'Timofei', 'Yegor', 'Aleksandr', 'Andrey', 'Arkadiy', 'Dmitriy', 'Evgeniy', 'Gennadiy', 'Georgiy', 'Sergey', 'Valeriy', 'Vasiliy', 'Yevgeniy', 'Anatoliy', 'Matvey', 'Timofey']

        return random.choice(RUSSIAN_MALE_NAME)

    elif data_type == "RUSSIAN_FEMALE_NAME":
        RUSSIAN_FEMALE_NAME = ['Alexandra', 'Alina', 'Anastasia', 'Angelina', 'Anna', 'Antonina', 'Arina', 'Daria', 'Diana', 'Ekaterina', 'Elena', 'Elizaveta', 'Eva', 'Galina', 'Inna', 'Irina', 'Karina', 'Ksenia', 'Larisa', 'Lilia', 'Ludmila', 'Lyubov', 'Maria', 'Marina', 'Nadezhda', 'Natalia', 'Nina', 'Olga', 'Polina', 'Svetlana', 'Tatiana', 'Valentina', 'Valeria', 'Varvara', 'Vera', 'Veronika', 'Victoria', 'Yana', 'Yelena', 'Yulia', 'Yevgeniya', 'Zoya', 'Aleksandra', 'Anastasiya', 'Darya', 'Yekaterina', 'Yelizaveta', 'Yeva', 'Kseniya', 'Liliya', 'Lyudmila', 'Mariya', 'Nataliya', 'Tatyana', 'Valeriya', 'Viktoria', 'Yuliya']

        return random.choice(RUSSIAN_FEMALE_NAME)


#GERMAN NAMES
    elif data_type == "GERMAN_MALE_NAME":
        GERMAN_MALE_NAME = ['Alexander', 'Andreas', 'Anton', 'Armin', 'Axel', 'Benjamin', 'Bernd', 'Bernhard', 'Christian', 'Christoph', 'Daniel', 'David', 'Dieter', 'Dominik', 'Eduard', 'Elias', 'Emil', 'Fabian', 'Felix', 'Florian', 'Franz', 'Frederik', 'Friedrich', 'Georg', 'Gerhard', 'Gregor', 'Hans', 'Heinrich', 'Helmut', 'Henrik', 'Herbert', 'Holger', 'Horst', 'Jan', 'Jens', 'Johann', 'Johannes', 'Jonas', 'Jörg', 'Josef', 'Julian', 'Jürgen', 'Karl', 'Karsten', 'Klaus', 'Konrad', 'Lars', 'Lennart', 'Ludwig', 'Manuel', 'Marco', 'Marcus', 'Mario', 'Markus', 'Martin', 'Matthias', 'Max', 'Michael', 'Moritz', 'Nico', 'Niklas', 'Olaf', 'Oliver', 'Patrick', 'Paul', 'Peter', 'Philipp', 'Ralf', 'Raphael', 'Reinhard', 'René', 'Richard', 'Robert', 'Roland', 'Rolf', 'Sebastian', 'Simon', 'Stefan', 'Stephan', 'Sven', 'Thomas', 'Thorsten', 'Tim', 'Tobias', 'Udo', 'Ulrich', 'Uwe', 'Volker', 'Walter', 'Werner', 'Wilhelm', 'Wolfgang', 'Albert', 'Alfred', 'Alwin', 'Ansgar', 'Arthur', 'August', 'Bernard', 'Carl', 'Caspar', 'Detlef', 'Edgar', 'Edwin', 'Egon', 'Ernst', 'Ewald', 'Franz-Josef', 'Friedhelm', 'Fritz', 'Gerd', 'Gustav', 'Hartmut', 'Heinz', 'Hermann', 'Hubert', 'Jochen', 'Joel', 'Jonathan', 'Julius', 'Justus', 'Karl-Heinz', 'Klemens', 'Kurt', 'Leopold', 'Lothar', 'Ludger', 'Lukas', 'Malte', 'Marcel', 'Mathias', 'Matthäus', 'Maurice', 'Maximilian', 'Moses', 'Nikolaus', 'Norbert', 'Oskar', 'Otto', 'Pascal', 'Rainer', 'Roman', 'Ronald', 'Silas', 'Theo', 'Till', 'Valentin', 'Vincent', 'Willi']
        return random.choice(GERMAN_MALE_NAME)
    
    elif data_type == "GERMAN_FEMALE_NAME":
        GERMAN_FEMALE_NAME = ['Alexandra', 'Alice', 'Alina', 'Amelie', 'Anastasia', 'Angelika', 'Anna', 'Annika', 'Antonia', 'Astrid', 'Barbara', 'Beatrix', 'Bianca', 'Birgit', 'Carina', 'Caroline', 'Christina', 'Claudia', 'Dagmar', 'Daniela', 'Diana', 'Elena', 'Elsa', 'Emma', 'Erika', 'Esther', 'Frida', 'Gabriela', 'Hanna', 'Helena', 'Ines', 'Ingrid', 'Isabel', 'Isabella', 'Jana', 'Jennifer', 'Jessica', 'Johanna', 'Julia', 'Juliane', 'Karin', 'Katja', 'Katharina', 'Kerstin', 'Laura', 'Lea', 'Lena', 'Linda', 'Lisa', 'Luisa', 'Maja', 'Maria', 'Marie', 'Marina', 'Marlene', 'Martina', 'Melanie', 'Monika', 'Nadine', 'Natalie', 'Nicole', 'Nina', 'Olga', 'Patricia', 'Paula', 'Petra', 'Renate', 'Sabine', 'Sandra', 'Sarah', 'Simone', 'Sophia', 'Stefanie', 'Sylvia', 'Tanja', 'Tatjana', 'Teresa', 'Ursula', 'Vanessa', 'Verena', 'Veronica', 'Victoria', 'Yvonne', 'Zoe', 'Ada', 'Adelheid', 'Agnes', 'Alberta', 'Alma', 'Alva', 'Amalia', 'Amira', 'Anneliese', 'Annette', 'Antje', 'Aurelia', 'Ava', 'Beate', 'Berta', 'Bettina', 'Bianka', 'Brigitte', 'Carla', 'Carmen', 'Charlotte', 'Cora', 'Dorothea', 'Edith', 'Elisa', 'Ella', 'Elvira', 'Emilia', 'Emmeline', 'Eva', 'Fiona', 'Franziska', 'Frederike', 'Gabriele', 'Gerda', 'Gisela', 'Hannelore', 'Hedwig', 'Heidi', 'Helga', 'Hilda', 'Ida']
        return random.choice(GERMAN_FEMALE_NAME)
    

#CHINESE NAMES
    elif data_type == "CHINESE_MALE_NAME":
        CHINESE_MALE_NAME = ['Bo', 'Chen', 'Da', 'Dong', 'Fang', 'Feng', 'Fu', 'Gang', 'Guo', 'Hai', 'Han', 'Hao', 'He', 'Hong', 'Hua', 'Huang', 'Hui', 'Jian', 'Jiang', 'Jie', 'Jin', 'Jun', 'Lei', 'Li', 'Liang', 'Lin', 'Ming', 'Nan', 'Peng', 'Qiang', 'Qiu', 'Rui', 'Sen', 'Shan', 'Sheng', 'Shi', 'Tao', 'Wei', 'Wen', 'Xiang', 'Xiao', 'Xing', 'Xu', 'Yan', 'Yang', 'Yi', 'Yong', 'Yu', 'Yuan', 'Yun', 'Zhan', 'Zhang', 'Zhao', 'Zheng', 'Zhi', 'Zhong', 'Zhu', 'Zi', 'Aiguo', 'Bao', 'Bin', 'Cai', 'Chao', 'Cheng', 'Cong', 'Deshi', 'Dewei', 'Dexin', 'Donghai', 'Fengge', 'Fenfang', 'Fuqiang', 'Guan', 'Guang', 'Guangli', 'Guoqing', 'Haibin', 'Hailong', 'Haiqing', 'Heng', 'Hongliang', 'Huiliang', 'Jianguo', 'Jianhua', 'Jianjun', 'Jing', 'Jinhua', 'Jiwei', 'Junjie', 'Kai', 'Kang', 'Ling', 'Qing', 'Ren', 'Shuai', 'Song', 'Xiaobo', 'Xiaodong', 'Xiaogang', 'Xiaohong', 'Xiaojun', 'Xiaoliang', 'Xiaoming', 'Xiaowei', 'Xiaoqing', 'Xin', 'Xiong', 'Xue', 'Zeng', 'Zhigang', 'Zhilong', 'Zhimin', 'Zhiping', 'Zhou']
        return random.choice(CHINESE_MALE_NAME)

    elif data_type == "CHINESE_FEMALE_NAME":
        CHINESE_FEMALE_NAME = ['Ai', 'Aiguo', 'Aihua', 'An', 'Bao', 'Bei', 'Bi', 'Bing', 'Bo', 'Cai', 'Chen', 'Cheng', 'Chun', 'Cui', 'Dan', 'Di', 'Dong', 'Fang', 'Fei', 'Fen', 'Feng', 'Fu', 'Gang', 'Ge', 'Gui', 'Guifang', 'Hai', 'Hong', 'Hua', 'Huang', 'Hui', 'Jia', 'Jian', 'Jiang', 'Jiao', 'Jie', 'Jing', 'Juan', 'Jun', 'Li', 'Lian', 'Liwei', 'Liu', 'Man', 'Mei', 'Min', 'Ming', 'Na', 'Nan', 'Ning', 'Ping', 'Qian', 'Qiang', 'Qing', 'Qiu', 'Rong', 'Ru', 'Rui', 'Shan', 'Sheng', 'Shu', 'Shuang', 'Shuyan', 'Su', 'Sufen', 'Suhua', 'Suyin', 'Ting', 'Wei', 'Wen', 'Xia', 'Xian', 'Xiao', 'Xiaoli', 'Xiaoling', 'Xiaomei', 'Xiaoyan', 'Xiaoying', 'Xin', 'Xing', 'Xiu', 'Xue', 'Yan', 'Yi', 'Ying', 'Yong', 'Yu', 'Yuan', 'Yue', 'Yun', 'Zha', 'Zhan', 'Zhen', 'Zheng', 'Zhi', 'Zhirong', 'Zhixia', 'Zhong', 'Zhu', 'Zhuo', 'Zi', 'Zong', 'Ling']
        return random.choice(CHINESE_FEMALE_NAME)


#GREEK NAMES
    elif data_type == "GREEK_MALE_NAME":
        GREEK_MALE_NAME = ['Alexander', 'Andreas', 'Antonis', 'Christos', 'Dimitris', 'Efthimis', 'George', 'Gregory', 'Ioannis', 'Kostas', 'Manolis', 'Michalis', 'Nikolas', 'Panagiotis', 'Stavros', 'Theodoros', 'Vasilis', 'Yiannis', 'Zacharias', 'Achilles', 'Agamemnon', 'Anastasios', 'Artemis', 'Christoforos', 'Eleftherios', 'Marios', 'Michail', 'Panayiotis', 'Stefanos', 'Vasileios', 'Yannis', 'Alexandros', 'Aristotelis', 'Demetrios', 'Elias', 'Haris', 'Iason', 'Konstantinos', 'Leandros', 'Lefteris', 'Miltiadis', 'Nikiforos', 'Panos', 'Petros', 'Sotiris', 'Thanasis', 'Thomas', 'Xenophon', 'Yorgos', 'Zisis', 'Adonis', 'Alexios', 'Andonis', 'Apostolos', 'Argyris', 'Charalampos', 'Chariton', 'Christodoulos', 'Dimitri', 'Emmanouil', 'Evangelos', 'Filippos', 'Fotios', 'Giorgos', 'Grigoris', 'Ioannidis', 'Kleanthis', 'Kleon', 'Kyriakos', 'Lykourgos', 'Nektarios', 'Nikitas', 'Panagis', 'Panayotis', 'Pavlos', 'Polycarpos', 'Polykarpos', 'Savvas', 'Simeon', 'Spiros', 'Stratos', 'Stylianos', 'Tasos', 'Theofilos', 'Theophilos', 'Vangelis', 'Xenofon']

        return random.choice(GREEK_MALE_NAME)
    
    elif data_type == "GREEK_FEMALE_NAME":
        GREEK_FEMALE_NAME = ['Alexandra', 'Anastasia', 'Angeliki', 'Anna', 'Anthi', 'Antonia', 'Areti', 'Athina', 'Despina', 'Dimitra', 'Eirini', 'Eleftheria', 'Elisavet', 'Elli', 'Eva', 'Georgia', 'Ioanna', 'Katerina', 'Kyriaki', 'Maria', 'Marina', 'Natalia', 'Niki', 'Nikoletta', 'Panagiota', 'Sofia', 'Stavroula', 'Theodora', 'Vasiliki', 'Xanthi', 'Zoi']

        return random.choice(GREEK_FEMALE_NAME)


#JAPANESE NAMES
    elif data_type == "JAPANESE_MALE_NAME":
        JAPANESE_MALE_NAME = ['Hiroto', 'Haruto', 'Sota', 'Yuma', 'Haruna', 'Yamato', 'Naoto', 'Yuto', 'Kentaro', 'Shuntaro', 'Takuma', 'Shohei', 'Kotaro', 'Tomoya', 'Yuga', 'Kaito', 'Ren', 'Ryo', 'Riku', 'Takumi', 'Yuki', 'Sora', 'Ryota', 'Hiroki', 'Kazuki', 'Yusuke', 'Sho', 'Kota', 'Shota', 'Daiki', 'Ryoma', 'Keita', 'Koki', 'Sosuke', 'Hayato', 'Shin', 'Taiki', 'Hikaru', 'Kazuya', 'Kento', 'Rui', 'Tatsuya', 'Yosuke', 'Yoshiki', 'Ryuki', 'Ryosuke', 'Yukihiro', 'Yoshito', 'Shogo', 'Takeru', 'Shu', 'Jun', 'Shunsuke', 'Toshiro', 'Toma', 'Shinji', 'Shinichi', 'Shoma', 'Kosuke', 'Haruki', 'Kazuma', 'Ryusei', 'Satoshi', 'Takashi', 'Yusei', 'Haru', 'Hiroshi', 'Issei', 'Yasuhiro', 'Takahiro', 'Taichi', 'Kohei', 'Haruma', 'Masato', 'Daichi', 'Takayuki', 'Yudai', 'Hayate', 'Takuya', 'Toshiyuki', 'Yuji', 'Junpei', 'Ryuta', 'Shun', 'Kenta', 'Hiroaki', 'Kensuke', 'Yusaku', 'Tomohiro', 'Yoshihiro', 'Takeshi', 'Yugo', 'Yasuo', 'Tadashi', 'Hajime', 'Tomoki', 'Makoto', 'Mitsuru', 'Noboru', 'Tsuyoshi', 'Tetsuya', 'Shigeki', 'Jiro', 'Koji', 'Akira', 'Hideo', 'Masashi', 'Kazuo', 'Kenji', 'Taro', 'Ichiro', 'Toshio', 'Susumu', 'Hideki', 'Yukio', 'Hisashi', 'Akio', 'Ryoichi', 'Minoru', 'Toshiaki', 'Kazuhiko', 'Yoshiaki', 'Akihiro', 'Shuichi', 'Kojiro', 'Masaaki', 'Takao', 'Tadao', 'Tetsuji', 'Haruhiko', 'Yasushi']

        return random.choice(JAPANESE_MALE_NAME)
    
    elif data_type == "JAPANESE_FEMALE_NAME":
        JAPANESE_FEMALE_NAME = ['Hina', 'Sakura', 'Yui', 'Yuna', 'Aoi', 'Riko', 'Kokoro', 'Miu', 'Yua', 'Sora', 'Hana', 'Rina', 'Akari', 'Miyu', 'Rio', 'Yuka', 'Yume', 'Koharu', 'Mana', 'Yuzu', 'Ayaka', 'Himari', 'Risa', 'Nana', 'Yuki', 'Haruka', 'Kana', 'Moka', 'Ichika', 'Rin', 'Momo', 'Kotone', 'Misaki', 'Noa', 'Hinata', 'Rika', 'Saki', 'Mai', 'Airi', 'Aika', 'Yukino', 'Kaede', 'Ayane', 'Mao', 'Nao', 'Mio', 'Asuka', 'Saya', 'Kaho', 'Kanon', 'Yura', 'Erika', 'Mizuki', 'Yuriko', 'Nagisa', 'Ayumi', 'Mina', 'Miki', 'Karin', 'Ayano', 'Asumi', 'Kokona', 'Mei', 'Shiori', 'Hikari', 'Emi', 'Yuri', 'Mayu', 'Marina', 'Haruna', 'Yuzuki', 'Miyuki', 'Miku', 'Yurika', 'Kokoa', 'Nanami', 'Aya', 'Akane', 'Nozomi', 'Koh']

        return random.choice(JAPANESE_FEMALE_NAME)
    

#KOREAN NAMES
    elif data_type == "KOREAN_MALE_NAME":
        KOREAN_MALE_NAME = ['Jihoon', 'Minjoon', 'Joonho', 'Seojin', 'Jaehyun', 'Jisung', 'Sungmin', 'Jiwon', 'Seungwoo', 'Haeun', 'Younghoon', 'Minseok', 'Junho', 'Hyunwoo', 'Seungmin', 'Kyungsoo', 'Taehyun', 'Hyungjoon', 'Jonghyun', 'Dongwook', 'Hoon', 'Woojin', 'Yoonseok', 'Taeyong', 'Jaehee', 'Siwoo', 'Sungwoo', 'Jinwoo', 'Seunghoon', 'Jungwoo', 'Minho', 'Hyunjoon', 'Donghyun', 'Junseok', 'Taemin', 'Hyeonu', 'Hwan', 'Eunseo', 'Yujin']

        return random.choice(KOREAN_MALE_NAME)
    
    elif data_type == "KOREAN_FEMALE_NAME":
        KOREAN_FEMALE_NAME = ['Jiyeon', 'Minji', 'Jisoo', 'Seojin', 'Jiyoung', 'Hyerin', 'Soomin', 'Yuna', 'Jiwon', 'Seungyeon', 'Jiwoo', 'Yerim', 'Haeun', 'Seoyeon', 'Eunji', 'Hyerim', 'Hae']
        return random.choice(KOREAN_FEMALE_NAME)


#Hindi Names
    elif data_type == "HINDI_MALE_NAME":
        HINDI_MALE_NAME = ['Arjun', 'Mohan', 'Rajesh', 'Nitin', 'Vikram', 'Rahul', 'Deepak', 'Manish', 'Vijay', 'Ravi', 'Amit', 'Arun', 'Anil', 'Ajay', 'Rakesh', 'Sanjay', 'Sandeep', 'Pradeep', 'Sunil', 'Vinod', 'Ankit', 'Vishal', 'Prakash', 'Pawan', 'Alok', 'Amar', 'Anand', 'Rajendra', 'Satish', 'Navin', 'Dinesh', 'Rajiv', 'Vivek', 'Suresh', 'Mahesh', 'Kamal', 'Rajeev', 'Ashish', 'Aryan', 'Gopal', 'Praveen', 'Hari', 'Jitendra', 'Sachin', 'Subhash', 'Naveen', 'Shivam', 'Krishna', 'Vimal', 'Rohit', 'Rajkumar', 'Ranjan', 'Nikhil', 'Ramesh', 'Prashant', 'Avinash', 'Harish', 'Harsh', 'Suman', 'Raj', 'Rajan', 'Pramod', 'Raju', 'Ganesh', 'Arvind', 'Ajeet', 'Mukesh', 'Devendra', 'Kishan', 'Santosh', 'Rajat', 'Vikas', 'Saurabh', 'Ashok', 'Manoj']

        return random.choice(HINDI_MALE_NAME)
    
    elif data_type == "HINDI_FEMALE_NAME":
        HINDI_FEMALE_NAME = ['Aarti', 'Monika', 'Swati', 'Neeta', 'Vidya', 'Ritu', 'Pooja', 'Sonia', 'Priya', 'Anita', 'Jyoti', 'Anjali', 'Meena', 'Rani', 'Shweta', 'Smita', 'Radha', 'Neha', 'Renu', 'Sapna', 'Kavita', 'Poonam', 'Manisha', 'Sangeeta', 'Arti', 'Shilpa', 'Rashi', 'Indira', 'Kiran', 'Preeti', 'Sarita', 'Geeta', 'Rekha', 'Sunita', 'Rina', 'Madhu', 'Mamta', 'Nisha', 'Sarika', 'Anjana', 'Suman', 'Nidhi', 'Anamika', 'Anu', 'Deepika', 'Sweta', 'Kusum', 'Sushma', 'Jaya', 'Nitu', 'Reena', 'Anshu', 'Manju', 'Nandini', 'Sakshi', 'Sonam', 'Anju', 'Shobha', 'Sadhana', 'Madhuri', 'Rakhi', 'Priyanka', 'Kajal', 'Neetu', 'Rashmi', 'Sheetal', 'Seema', 'Meenakshi']

        return random.choice(HINDI_FEMALE_NAME)


#Italian Names
    elif data_type == "ITALIAN_MALE_NAME":
        ITALIAN_MALE_NAME = ['Alessandro', 'Andrea', 'Antonio', 'Alessio', 'Alberto', 'Angelo', 'Amedeo', 'Armando', 'Bruno', 'Bernardo', 'Carlo', 'Cristiano', 'Claudio', 'Davide', 'Daniele', 'Diego', 'Emanuele', 'Enrico', 'Fabio', 'Filippo', 'Francesco', 'Federico', 'Giovanni', 'Giuseppe', 'Guido', 'Gabriele', 'Giacomo', 'Giorgio', 'Giulio', 'Ignazio', 'Ivan', 'Luca', 'Leonardo', 'Lorenzo', 'Matteo', 'Marco', 'Massimo', 'Michele', 'Mauro', 'Nicola', 'Nicolò', 'Pietro', 'Paolo', 'Roberto', 'Riccardo', 'Stefano', 'Salvatore', 'Simone', 'Tommaso', 'Umberto', 'Valerio', 'Vittorio', 'Vincenzo', 'Dario', 'Domenico', 'Edoardo', 'Emilio', 'Ettore', 'Fabrizio', 'Fulvio', 'Giancarlo', 'Gianluca', 'Gianmarco', 'Gianpaolo', 'Giuliano', 'Guglielmo', 'Gino', 'Gaspare', 'Isacco', 'Leandro', 'Ludovico', 'Mario', 'Nico']

        return random.choice(ITALIAN_MALE_NAME)
    
    elif data_type == "ITALIAN_FEMALE_NAME":
        ITALIAN_FEMALE_NAME = ['Alessandra', 'Anna', 'Antonia', 'Alice', 'Beatrice', 'Bianca', 'Chiara', 'Cristina', 'Daniela', 'Donatella', 'Elena', 'Elisa', 'Francesca', 'Federica', 'Giulia', 'Giovanna', 'Graziella', 'Isabella', 'Laura', 'Luisa', 'Lucia', 'Marta', 'Maria', 'Matilde', 'Michela', 'Monica', 'Natalia', 'Nicoletta', 'Paola', 'Patrizia', 'Rosa', 'Roberta', 'Sara', 'Silvia', 'Simona', 'Stefania', 'Valentina', 'Vanessa', 'Veronica', 'Vittoria', 'Adriana', 'Alessia', 'Angelica', 'Arianna', 'Aurora', 'Camilla', 'Carlotta', 'Caterina', 'Claudia', 'Debora', 'Eleonora', 'Erika', 'Filomena', 'Gabriella', 'Giorgia', 'Giusy', 'Ilaria', 'Jessica', 'Lara', 'Livia', 'Manuela', 'Marcella', 'Milena', 'Miriam', 'Nicole', 'Noemi', 'Renata', 'Rita', 'Serena', 'Susanna', 'Teresa', 'Valeria', 'Viola', 'Viviana', 'Ylenia', 'Yolanda', 'Zoe']

        return random.choice(ITALIAN_FEMALE_NAME)


#African Names
    elif data_type == "AFRICAN_MALE_NAME":
        AFRICAN_MALE_NAME = ['Kwame', 'Kwaku', 'Kwasi', 'Kweku', 'Kofi', 'Kwadwo', 'Kwabena', 'Jabari', 'Tariq', 'Ayo', 'Azibo', 'Chidi', 'Simba', 'Idris', 'Kato', 'Obasi', 'Omari', 'Sekou', 'Zaire', 'Diallo', 'Amara', 'Jengo', 'Kamau', 'Nuru', 'Ade', 'Abimbola', 'Ayodele', 'Olabisi', 'Adisa', 'Afolabi', 'Adeyemi', 'Oba', 'Babatunde', 'Okeke', 'Osaze', 'Nwabudike', 'Odion', 'Emeka', 'Eze', 'Chukwu', 'Ugo', 'Nnamdi', 'Chima', 'Onyeka', 'Jabulani', 'Zulu', 'Lerato', 'Thabo', 'Bakari', 'Rashidi']

        return random.choice(AFRICAN_MALE_NAME)
    
    elif data_type == "AFRICAN_FEMALE_NAME":
        AFRICAN_FEMALE_NAME = ['Ama', 'Akosua', 'Adwoa', 'Abena', 'Afia', 'Amara', 'Ayana', 'Fatima', 'Halima', 'Layla', 'Nia', 'Zara', 'Ayisha', 'Kadija', 'Khadija', 'Laila', 'Aisha', 'Safiya', 'Najwa', 'Samira']

        return random.choice(AFRICAN_FEMALE_NAME)


#Portuguese Names
    elif data_type == "PORTUGUESE_MALE_NAME":
        PORTUGUESE_MALE_NAME = ['Adriano', 'Alexandre', 'André', 'António', 'Artur', 'Augusto', 'Aurélio', 'Bernardo', 'Bruno', 'Carlos', 'César', 'Cristiano', 'Daniel', 'David', 'Diogo', 'Duarte', 'Eduardo', 'Fábio', 'Fernando', 'Filipe', 'Francisco', 'Gabriel', 'Gilberto', 'Gonçalo', 'Guilherme', 'Gustavo', 'Hélder', 'Hugo', 'Igor', 'Isaac', 'Jaime', 'João', 'Jorge', 'José', 'Júlio', 'Leandro', 'Leonardo', 'Luís', 'Manuel', 'Marco', 'Mário', 'Miguel', 'Nelson', 'Nuno', 'Paulo', 'Pedro', 'Rafael', 'Ricardo', 'Roberto', 'Rodrigo', 'Rui', 'Samuel', 'Sandro', 'Sérgio', 'Tiago', 'Tomás', 'Valter', 'Vasco', 'Victor', 'Vítor']


        return random.choice(PORTUGUESE_MALE_NAME)


    elif data_type == "PORTUGUESE_FEMALE_NAME":
        PORTUGUESE_FEMALE_NAME = ['Adriana', 'Alexandra', 'Alice', 'Amélia', 'Ana', 'Andreia', 'Angélica', 'Antónia', 'Aurora', 'Beatriz', 'Carla', 'Carolina', 'Catarina', 'Clara', 'Cristina', 'Daniela', 'Diana', 'Eduarda', 'Elena', 'Elisa', 'Elsa', 'Emília', 'Fabiana', 'Filipa', 'Francisca', 'Gabriela', 'Helena', 'Inês', 'Isabel', 'Jéssica', 'Joana', 'Júlia', 'Laura', 'Lara', 'Leonor', 'Letícia', 'Lídia', 'Liliana', 'Luana', 'Lúcia', 'Lurdes', 'Mafalda', 'Mara', 'Margarida', 'Maria', 'Mariana', 'Marisa', 'Marta', 'Matilde', 'Melissa', 'Mónica', 'Natália', 'Nádia', 'Nicole', 'Olívia', 'Patrícia', 'Paula', 'Raquel', 'Renata', 'Rita', 'Rosa', 'Sandra', 'Sara', 'Sofia', 'Soraia', 'Tatiana', 'Teresa', 'Vanessa', 'Vera', 'Verónica', 'Vitória']



        return random.choice(PORTUGUESE_FEMALE_NAME)






    else:
        print("ERROR, INVALID RandomNames.get_name OPTION!!!")
      
def get_name_random():

    origin_list = ["USA_MALE_NAME", "USA_FEMALE_NAME", "ENGLISH_MALE_NAME", "ENGLISH_FEMALE_NAME",
                   "FRENCH_MALE_NAME", "FRENCH_FEMALE_NAME", "SPANISH_MALE_NAME", "SPANISH_FEMALE_NAME",
                   "RUSSIAN_MALE_NAME", "RUSSIAN_FEMALE_NAME", "GERMAN_MALE_NAME", "GERMAN_FEMALE_NAME",
                   "CHINESE_MALE_NAME", "CHINESE_FEMALE_NAME", "GREEK_MALE_NAME", "GREEK_FEMALE_NAME",
                   "JAPANESE_MALE_NAME", "JAPANESE_FEMALE_NAME", "KOREAN_MALE_NAME", "KOREAN_FEMALE_NAME",
                   "HINDI_MALE_NAME", "HINDI_FEMALE_NAME", "ITALIAN_MALE_NAME", "ITALIAN_FEMALE_NAME",
                   "AFRICAN_MALE_NAME", "AFRICAN_FEMALE_NAME", "PORTUGUESE_MALE_NAME", "PORTUGUESE_FEMALE_NAME"]
    
    name = get_name(random.choice(origin_list))

    return name

def get_lastname(data_type=str):
    data_type = data_type.upper()

#USA & ENGLISH LASTNAMES
    if data_type == "USA_LASTNAME" or data_type == "ENGLISH_LASTNAME":
        USA_LASTNAME = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson', 'White', 'Lopez', 'Lee', 'Gonzalez', 'Harris', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright', 'Scott', 'Green', 'Adams', 'Baker', 'Nelson', 'Hill', 'Ramirez', 'Campbell', 'Mitchell', 'Roberts', 'Carter', 'Phillips', 'Evans', 'Turner', 'Torres', 'Parker', 'Collins', 'Edwards', 'Stewart', 'Flores', 'Morris', 'Nguyen', 'Murphy', 'Rivera', 'Cook', 'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed', 'Bailey', 'Bell', 'Gomez', 'Kelly', 'Howard', 'Ward', 'Cox', 'Diaz', 'Richardson', 'Wood', 'Watson', 'Brooks', 'Bennett', 'Gray', 'James', 'Reyes', 'Cruz', 'Hughes', 'Price', 'Myers', 'Long', 'Foster', 'Sanders', 'Ross', 'Morales', 'Powell', 'Sullivan', 'Russell', 'Ortiz', 'Jenkins', 'Gutierrez', 'Perry', 'Butler', 'Barnes', 'Fisher', 'Henderson', 'Coleman', 'Simmons', 'Patterson', 'Jordan', 'Reynolds', 'Hamilton', 'Graham', 'Kim', 'Gonzales', 'Alexander', 'Ramos', 'Wallace', 'Griffin', 'West', 'Cole', 'Hayes', 'Chavez', 'Gibson', 'Bryant', 'Ellis', 'Stevens', 'Murray', 'Ford', 'Marshall', 'Owens', 'Mcdonald', 'Harrison', 'Ruiz', 'Kennedy', 'Wells', 'Alvarez', 'Woods', 'Mendoza', 'Castillo', 'Olson', 'Webb', 'Washington', 'Tucker', 'Freeman', 'Burns', 'Henry', 'Vasquez', 'Snyder', 'Simpson', 'Crawford', 'Jimenez', 'Porter', 'Mason', 'Shaw', 'Gordon', 'Wagner', 'Hunter', 'Romero', 'Hicks', 'Dixon', 'Hunt', 'Palmer', 'Robertson', 'Black', 'Holmes', 'Stone', 'Meyer', 'Boyd', 'Mills', 'Warren', 'Fox', 'Rose', 'Rice', 'Moreno', 'Schmidt', 'Patel', 'Ferguson', 'Nichols', 'Herrera', 'Medina', 'Ryan', 'Fernandez', 'Weaver', 'Daniels', 'Stephens', 'Gardner', 'Payne', 'Kelley', 'Dunn', 'Pierce', 'Arnold', 'Tran', 'Spencer', 'Peters', 'Hawkins', 'Grant', 'Hansen', 'Castro', 'Hoffman', 'Hart', 'Elliott', 'Cunningham', 'Knight', 'Bradley', 'Carroll', 'Hudson', 'Duncan', 'Armstrong', 'Berry', 'Andrews', 'Johnston', 'Ray', 'Lane', 'Riley', 'Carpenter', 'Perkins', 'Aguilar', 'Silva', 'Richards', 'Willis', 'Matthews', 'Chapman', 'Lawrence', 'Garza', 'Vargas', 'Watkins', 'Wheeler', 'Larson', 'Carlson', 'Harper', 'George', 'Greene', 'Burke', 'Guzman', 'Morrison', 'Munoz', 'Jacobs', 'Obrien', 'Lawson', 'Franklin', 'Lynch', 'Bishop', 'Carr', 'Salazar', 'Austin', 'Mendez', 'Gilbert', 'Jensen', 'Williamson', 'Montgomery', 'Harvey', 'Oliver', 'Howell', 'Dean', 'Hanson', 'Weber', 'Garrett', 'Sims', 'Burton', 'Fullton']

        return random.choice(USA_LASTNAME)
    
#FRENCH LASTNAMES
    elif data_type == "FRENCH_LASTNAME":
        FRENCH_LASTNAME = ['Martin', 'Bernard', 'Thomas', 'Petit', 'Robert', 'Richard', 'Durand', 'Dubois', 'Moreau', 'Simon', 'Laurent', 'Lefebvre', 'Michel', 'Garcia', 'David', 'Bertrand', 'Roux', 'Vincent', 'Fournier', 'Morel', 'Girard', 'Andre', 'Lefevre', 'Mercier', 'Dupont', 'Lambert', 'Bonnet', 'Francois', 'Martinez', 'Legrand', 'Garnier', 'Faure', 'Rousseau', 'Blanc', 'Guerin', 'Muller', 'Henry', 'Roussel', 'Nicolas', 'Perrin', 'Morin', 'Mathieu', 'Clement', 'Gauthier', 'Dumont', 'Lemoine', 'Picard', 'Gaillard', 'Dupuis', 'Lemaire', 'Lucas', 'Meunier', 'Fontaine', 'Masson', 'Chevalier', 'Robin', 'Marchand', 'Marie', 'Da Silva', 'Gonzalez', 'Pierre', 'Dufour', 'Brun', 'Renaud', 'Blanchard', 'Benoit', 'Leclerc', 'Payet', 'Huet', 'Barbier', 'Jacquet', 'Dupuy', 'Guillaume', 'Louis', 'Hubert', 'Charles', 'Jacques', 'Caron', 'Colin', 'Vidal', 'Renard', 'Aubert', 'Le Gall', 'Berger', 'Lefort', 'Lecomte', 'Prevost', 'Pelletier', 'Remy', 'Le Roux', 'Mallet', 'Brunet', 'Baron', 'Paris', 'Lacroix', 'Leblanc', 'Adam', 'Vasseur', 'Lejeune', 'Boucher', 'Herve', 'Fleury', 'Schmitt', 'Perrot', 'Julien', 'Lebrun', 'Marchal', 'Menard', 'Leclercq', 'Renault', 'Dumas', 'Leroy', 'Meyer', 'Jacquot', 'Bouvet', 'Guillot', 'Delorme', 'Giraud', 'Fernandez', 'Lambin', 'Poulain', 'Charpentier', 'Seguin', 'Joly', 'Prevot', 'Delaunay', 'Maillard', 'Carre', 'Laporte', 'Barre', 'Pons', 'Gillet', 'Collet', 'Dupre', 'Leduc', 'Besson', 'Bertin', 'Lamy', 'Lesage', 'Beauvais', 'Rodriguez', 'Gaudin', 'Cordier', 'Fabre', 'Schneider', 'Gay', 'Pineau', 'Dauphin', 'Royer', 'Boulanger', 'Buisson', 'Riviere', 'Bailly', 'Peltier', 'Laurin', 'Loiseau', 'Delage', 'Dupond', 'Gerard', 'Bruneau', 'Bourgeois', 'Lenoir', 'Ferrand', 'Joubert', 'Brunel', 'Olivier', 'Pasquier', 'Langlois', 'Roche', 'Mahe', 'Arnaud', 'Bocquet', 'Berthelot', 'Faivre', 'Fouquet', 'Leveque', 'Lelievre', 'Bonhomme', 'Poirier', 'Reynaud', 'Girault']


        return random.choice(FRENCH_LASTNAME)

#SPANISH LASTNAMES
    elif data_type == "SPANISH_LASTNAME":
        SPANISH_LASTNAME =  ['García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sánchez', 'Pérez', 'Gómez', 'Martín', 'Jiménez', 'Hernández', 'Díaz', 'Moreno', 'Álvarez', 'Romero', 'Navarro', 'Torres', 'Domínguez', 'Vargas', 'Ramos', 'Castro', 'Serrano', 'Ortega', 'Silva', 'Ortiz', 'Rubio', 'Molina', 'Delgado', 'Morales', 'Ramírez', 'Marín', 'Suárez', 'Medina', 'Cruz', 'León', 'Herrera', 'Flores', 'Campos', 'Vega', 'Camacho', 'Herrero', 'Peña', 'Vidal', 'Cabrera', 'Reyes', 'Cortés', 'Mendoza', 'Guerrero', 'Soto', 'Cano', 'Méndez', 'Nieto', 'Lozano', 'Pardo', 'Calvo', 'Ríos', 'Vicente', 'Iglesias', 'Carrasco', 'Acosta', 'Núñez', 'Fuentes', 'Salas', 'Esteban', 'Garrido', 'Ferrer', 'Santos', 'Rojas', 'Valle', 'Santana', 'Blanco', 'Aguilar', 'Crespo', 'Castaño', 'Guillén', 'Benítez', 'Peralta', 'Giménez', 'Hurtado', 'Lara', 'Salazar', 'Montes', 'Arias', 'Carmona', 'Cordero', 'Aguilera', 'Olivares', 'Pastor', 'Lorenzo', 'Bernal', 'Gallego', 'Tejada', 'Montoya', 'Rey', 'Alonso', 'Quintana', 'Guzmán', 'Barrios', 'De la Cruz', 'Bermúdez', 'Rosales', 'Vázquez', 'Morán', 'Pulido', 'Toledo', 'Otero', 'Salvador', 'Castillo', 'Mora', 'Hernando', 'Prieto', 'Ponce', 'Alcaraz', 'Bravo', 'Manzano', 'Moya', 'Paredes', 'Valverde', 'De la Rosa', 'Aguayo', 'Galán', 'Montero', 'Cámara', 'Puga', 'Soria', 'Del Río', 'Gil', 'Mesa', 'Perea', 'Cobo', 'Sastre', 'Palma', 'Vera', 'Villar', 'De la Fuente', 'Muñiz', 'Jurado', 'San José', 'Sancho', 'Valero', 'Ruiz', 'Gimeno', 'Aparicio', 'Martos', 'Del Campo', 'Solano', 'San Martín', 'Sotelo', 'Pinto', 'Beltrán', 'Vila', 'Bañuelos', 'Alcalá', 'Roldán', 'Gallegos', 'Ledesma', 'Trujillo', 'Luque', 'Melero', 'Solís', 'Chaves', 'Caro', 'Vela', 'Zapata', 'Galindo', 'Bautista', 'Girón', 'Aranda', 'Reina', 'Escudero', 'Nevado', 'Alvarado', 'Lobo', 'Sotomayor', 'Mendizábal', 'Carranza', 'Rubiales', 'Muñoz']


        return random.choice(SPANISH_LASTNAME)

#RUSSIAN LASATNAMES
    elif data_type == "RUSSIAN_LASTNAME":
        RUSSIAN_LASTNAME = ['Ivanov', 'Smirnov', 'Kuznetsov', 'Popov', 'Sokolov', 'Lebedev', 'Kozlov', 'Novikov', 'Morozov', 'Petrov', 'Volkov', 'Solovyov', 'Vasiliev', 'Zaitsev', 'Golubev', 'Vinogradov', 'Bogdanov', 'Vorobiev', 'Tarasov', 'Pavlov', 'Sidorov', 'Mikhailov', 'Fedorov', 'Lazarev', 'Titov', 'Ponomarev', 'Alexeev', 'Kharitonov', 'Grigoriev', 'Zakharov', 'Romanov', 'Belyakov', 'Sergeev', 'Nikitin', 'Golovin', 'Kuzmin', 'Zimin', 'Dmitriev', 'Frolov', 'Rozhkov', 'Vorontsov', 'Kalinin', 'Alekseev', 'Filippov', 'Mironov', 'Makarov', 'Nikolaev', 'Nesterov', 'Karpov', 'Melnikov', 'Orlov', 'Afanasiev', 'Davydov', 'Kovalev', 'Andreev', 'Bondarev', 'Gusev', 'Konovalov', 'Kostin', 'Meshkov', 'Efimov', 'Ilyin', 'Sobolev', 'Tikhonov', 'Osipov', 'Leontiev', 'Savin', 'Timofeev', 'Belov', 'Pankov', 'Demidov', 'Egorov', 'Sviridov', 'Polyakov', 'Shirokov', 'Afinogenov', 'Klimov', 'Golikov', 'Biryukov', 'Zubkov', 'Lisov', 'Kudryavtsev', 'Semenov', 'Fokin', 'Davyd']

        return random.choice(RUSSIAN_LASTNAME)
    
#GERMAN LASTNAMES
    elif data_type == "GERMAN_LASTNAME":
        GERMAN_LASTNAME = ['Müller', 'Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Wagner', 'Becker', 'Schulz', 'Hoffmann', 'Schäfer', 'Koch', 'Bauer', 'Richter', 'Klein', 'Wolf', 'Schröder', 'Neumann', 'Schwarz', 'Zimmermann', 'Braun', 'Krüger', 'Hofmann', 'Hartmann', 'Lange', 'Schmitt', 'Werner', 'Schmitz', 'Krause', 'Meier', 'Lehmann', 'Schmid', 'Schulze', 'Maier', 'Köhler', 'Herrmann', 'König', 'Walter', 'Mayer', 'Huber', 'Kaiser', 'Fuchs', 'Peters', 'Lang', 'Scholz', 'Möller', 'Weiß', 'Jung', 'Hahn', 'Schubert', 'Vogel', 'Friedrich', 'Keller', 'Günther', 'Frank', 'Berger', 'Roth', 'Beck', 'Lorenz', 'Baumann', 'Franke', 'Albrecht', 'Schuster', 'Simon', 'Ludwig', 'Böhm', 'Winter', 'Kraus', 'Martin', 'Schumacher', 'Krämer', 'Vogt', 'Stein', 'Jäger', 'Otto', 'Sommer', 'Groß', 'Seidel', 'Heinrich', 'Brandt', 'Haas', 'Schreiber', 'Graf', 'Schulte', 'Dietrich', 'Ziegler', 'Kuhn', 'Pohl', 'Engel', 'Horn', 'Bergmann', 'Voigt', 'Busch', 'Bender', 'Seifert', 'Hermann', 'Kraft', 'Kühn', 'Hansen', 'Winkler', 'Lutz', 'Ritter', 'Adam', 'Maurer', 'Wolff', 'Pfeiffer', 'Schütz', 'Arndt', 'Bachmann', 'Voß', 'Kunz', 'Heller', 'Sauer', 'Arnold', 'Schreiner', 'Wittmann', 'Zimmer', 'Kruse', 'Lechner', 'Böhme', 'Ernst', 'Lindner', 'Thiel', 'Frey', 'Geiger', 'Freitag', 'Friedl', 'Bach', 'Kirsch', 'Weiss', 'Mayr', 'Röder', 'Steiner', 'Krug', 'Brauer', 'Haase', 'Herzog', 'Krauss', 'Hennig', 'Schröter', 'Krebs', 'Sander', 'Hein', 'Henn', 'Gruber', 'Berndt', 'Kirschbaum', 'Kopp', 'Reichert', 'Hagen', 'Geißler', 'Bühler', 'Stoll', 'Renner', 'Förster', 'Stumpf', 'Lemke', 'Seitz', 'Wegner', 'Klemm', 'Eckert', 'Heß', 'Strauß', 'Dörr', 'Rudolph', 'Kiefer', 'Schott', 'Kugler', 'Krauß', 'Weis', 'Langner', 'Heine', 'Schüler', 'Römer', 'Schütte', 'Wegener', 'Hesse', 'Thoma', 'Schwab', 'Reiter', 'Wolter', 'Neubauer', 'Greiner', 'Merkel', 'Gebhardt', 'Bertram', 'Schober', 'Schütt', 'Scheffler', 'Held', 'Feldmann', 'Keil', 'Schenk', 'Kleber', 'Koller', 'Wiedemann', 'Hess', 'Schlüter', 'Bernhardt', 'Scharf', 'Franz', 'Scheel', 'Kremer', 'Holtz', 'Thieme', 'Morgenstern', 'Hirsch', 'Wehner', 'Decker', 'Heilmann', 'Mertens', 'Schröer', 'Haupt', 'Brendel', 'Buchholz', 'Eckardt', 'Schürmann', 'Seemann', 'Friedrichs', 'Eberhardt', 'Steffen', 'Häusler', 'Stern', 'Schuhmann', 'Schütze', 'Pfeffer', 'Siegert', 'Schell', 'Kämmerer', 'Hauptmann', 'Tietz', 'Grau', 'Schultheiß', 'Gericke', 'Henning', 'Schaaf', 'Rosenberg', 'Diehl', 'Gebauer', 'Schuh', 'Seidl', 'Haber', 'Mangold', 'Steinbach', 'Löwe', 'Schnell', 'Schwarze', 'Baumgartner', 'Tiedemann', 'Althaus', 'Kellermann', 'Jahnke', 'Diekmann', 'Kolb', 'Gebhart', 'Herz', 'Höfer', 'Hinrichs', 'Strobel', 'Meissner', 'Stamm', 'Kappel', 'Schweitzer', 'Heuser', 'Claus', 'Böttcher', 'Herr', 'Bischoff', 'Baumgart', 'Jahn', 'Gerhard', 'Stange', 'Heil', 'Hollmann']


        return random.choice(GERMAN_LASTNAME)

#CHINESE LASTNAME
    elif data_type == "CHINESE_LASTNAME":
        CHINESE_LASTNAME = ['Li', 'Wang', 'Zhang', 'Liu', 'Chen', 'Yang', 'Zhao', 'Huang', 'Zhou', 'Wu', 'Xu', 'Sun', 'Ma', 'Guo', 'Hu', 'Luo', 'He', 'Gao', 'Lin', 'Wei', 'Xie', 'Deng', 'Yu', 'Shi', 'Tang', 'Zheng', 'Xiao', 'Song']


        return random.choice(CHINESE_LASTNAME)

#GREEK LASTNAME   
    elif data_type == "GREEK_LASTNAME":
        GREEK_LASTNAME = ['Papadopoulos', 'Georgiou', 'Papadakis', 'Ioannou', 'Constantinou', 'Andreadis', 'Demetriou', 'Sotiriou', 'Papadimitriou', 'Vlachos', 'Mavromatis', 'Karamanlis', 'Panagiotopoulos', 'Nikolaou', 'Papageorgiou', 'Adamopoulos', 'Pavlou', 'Christodoulou', 'Papadopoulou', 'Michalopoulos', 'Kouros', 'Papandreou', 'Zervos', 'Papantonis', 'Karagiannis', 'Kontopoulos', 'Katsoulis', 'Ioannidis', 'Pappas', 'Papathanasiou', 'Papademetriou', 'Papoutsis', 'Galanis', 'Koutris', 'Samaras', 'Zafiris', 'Stavros', 'Koutoumanos', 'Kostopoulos', 'Zervas', 'Makris', 'Papagiannis', 'Papadaki']


        return random.choice(GREEK_LASTNAME)
    
#JAPANESE LASTNAME
    elif data_type == "JAPANESE_LASTNAME":
        JAPANESE_LASTNAME = ['Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Yamamoto', 'Nakamura', 'Kobayashi', 'Kato', 'Yoshida', 'Yamada', 'Sasaki', 'Yamaguchi', 'Matsumoto', 'Inoue', 'Kimura', 'Hayashi', 'Shimizu', 'Yamazaki', 'Mori', 'Abe', 'Ikeda', 'Hashimoto', 'Ogawa', 'Kondo', 'Hasegawa', 'Okada', 'Murakami', 'Fujita', 'Ota', 'Miura', 'Nishimura', 'Koyama', 'Fujiwara', 'Maeda', 'Nakajima', 'Saito', 'Sakamoto', 'Nakagawa', 'Nakano', 'Harada', 'Yokoyama', 'Matsuda', 'Ishikawa', 'Endo', 'Aoki', 'Fujii', 'Nakayama', 'Sakai', 'Kikuchi', 'Ono', 'Ishii', 'Yano', 'Tamura', 'Nishi', 'Sugawara', 'Miyamoto', 'Ueda', 'Takeda', 'Matsui', 'Fujimoto', 'Kojima', 'Otsuka']


        return random.choice(JAPANESE_LASTNAME)

#KOREAN LASTNAME
    elif data_type == "KOREAN_LASTNAME":
        KOREAN_LASTNAME = ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Kang', 'Cho', 'Yoon', 'Han', 'Lim', 'Jang', 'Oh', 'Seo', 'Yoo', 'Shin', 'Song', 'Bae', 'Kwon', 'Hong', 'Jeon', 'Ko', 'Ha', 'Nam', 'Sim', 'Hwang', 'Baek', 'Moon', 'Jeong', 'Im', 'Sohn', 'An', 'Chung', 'Gwak', 'Yu', 'Won', 'Yun', 'Ahn', 'Go', 'No', 'Jo', 'Sin', 'Seong', 'Huh', 'Yim', 'Do', 'Yang', 'Seol', 'Maeng']


        return random.choice(KOREAN_LASTNAME)

#HINDI LASTNAME
    elif data_type == "HINDI_LASTNAME":
        HINDI_LASTNAME = ['Kumar', 'Sharma', 'Verma', 'Singh', 'Gupta', 'Agarwal', 'Goyal', 'Mehra', 'Chopra', 'Malhotra', 'Khanna', 'Bhatia', 'Chaudhary', 'Shah', 'Patel', 'Joshi', 'Gandhi', 'Shrivastava', 'Pandey', 'Nair', 'Rao', 'Chatterjee', 'Das', 'Iyer', 'Reddy', 'Roy', 'Mukherjee', 'Dutta', 'Biswas', 'Choudhury']


        return random.choice(HINDI_LASTNAME)

#ITALIAN LASTNAME  
    elif data_type == "ITALIAN_LASTNAME":
        ITALIAN_LASTNAME = ['Rossi', 'Russo', 'Ferrari', 'Esposito', 'Bianchi', 'Romano', 'Colombo', 'Ricci', 'Marino', 'Greco', 'Bruno', 'Gallo', 'Conti', 'De Luca', 'Mancini', 'Costa', 'Giordano', 'Rizzo', 'Lombardi', 'Moretti', 'Barbieri', 'Fontana', 'Santoro', 'Mariani', 'Rinaldi', 'Caruso', 'Ferrara', 'Galli', 'Martini', 'Leone', 'Longo', 'Gentile', 'Villa', 'Lombardo', 'Serra', 'Cattaneo', 'Ferraro', 'Sala', 'Ferri', 'Silvestri', 'Riva', 'Bernardi', 'Pellegrini', 'Palumbo', 'Santini', 'Parisi', 'Vitali', 'Amato', 'Mazza', 'Gatti', 'Fabbri', 'Benedetti', 'Bellini', 'Rossetti', 'Grasso', 'Testa', 'Palmieri', 'Ruggiero', "D'Angelo", 'Poli', 'Donati', 'Marini', 'Sorrentino', 'Rizzi', 'Monti', 'Vitale', 'Marchetti', 'Caputo', 'Ricciardi', "D'Amico", 'Giuliani', 'Valentini', 'Barone', 'Battaglia', 'Farina', 'Bianco', 'De Santis', 'Pagano', 'Messina', 'Orlando', 'Montanari', 'Conte']


        return random.choice(ITALIAN_LASTNAME)

#AFRICAN LASTNAME
    elif data_type == "AFRICAN_LASTNAME":
        AFRICAN_LASTNAME = ['Adebayo', 'Ajayi', 'Akintola', 'Amadi', 'Anyanwu', 'Asante', 'Banda', 'Chukwu', 'Diallo', 'Ekwueme', 'Fofana', 'Gebre', 'Ghana', 'Ifeanyi', 'Jammeh', 'Kamara', 'Kanu', 'Lamin', 'Mbeki', 'Mohammed', 'Nkrumah', 'Nwachukwu', 'Nwosu', 'Obi', 'Okafor', 'Okeke', 'Osei', 'Osman', 'Ouattara', 'Ouedraogo', 'Rashid', 'Sankoh', 'Sissoko', 'Sow', 'Toure', 'Umar', 'Wangari', 'Yamamoto', 'Zuma']


        return random.choice(AFRICAN_LASTNAME)

#PORTUGUESE LASTNAME
    elif data_type == "PORTUGUESE_LASTNAME":
        PORTUGUESE_LASTNAME = ['Abreu', 'Albuquerque', 'Almeida', 'Alves', 'Amaral', 'Andrade', 'Antunes', 'Araújo', 'Barbosa', 'Barros', 'Batista', 'Borges', 'Branco', 'Cardoso', 'Carneiro', 'Carvalho', 'Castro', 'Cavalcanti', 'Coelho', 'Correia', 'Costa', 'Cruz', 'Cunha', 'Dias', 'Domingues', 'Esteves', 'Fernandes', 'Ferreira', 'Figueiredo', 'Freitas', 'Garcia', 'Gomes', 'Gonçalves', 'Guedes', 'Lima', 'Lopes', 'Machado', 'Magalhães', 'Marques', 'Martins', 'Melo', 'Mendes', 'Moraes', 'Morais', 'Moreira', 'Nascimento', 'Neves', 'Nunes', 'Oliveira', 'Pereira', 'Pinto', 'Reis', 'Ribeiro', 'Rocha', 'Rodrigues', 'Santos', 'Silva', 'Sousa', 'Soares', 'Teixeira', 'Vieira']



        return random.choice(PORTUGUESE_LASTNAME)
    
def get_lastname_random():

    origin_list = ["USA_LASTNAME",  "ENGLISH_LASTNAME", 
                   "FRENCH_LASTNAME", "SPANISH_LASTNAME", 
                   "RUSSIAN_LASTNAME",  "GERMAN_LASTNAME", 
                   "CHINESE_LASTNAME",  "GREEK_LASTNAME", 
                   "JAPANESE_LASTNAME", "KOREAN_LASTNAME", 
                   "HINDI_LASTNAME",  "ITALIAN_LASTNAME", 
                   "AFRICAN_LASTNAME", "PORTUGUESE_LASTNAME"]
    
    name = get_lastname(random.choice(origin_list))

    return name

def get_fullname(genre=None, nationality=None):

    origin_list = ["USA",  "ENGLISH", 
                   "FRENCH", "SPANISH", 
                   "RUSSIAN",  "GERMAN", 
                   "CHINESE",  "GREEK", 
                   "JAPANESE", "KOREAN", 
                   "HINDI",  "ITALIAN", 
                   "AFRICAN", "PORTUGUESE"]
    
    genre_list = ["MALE", "FEMALE"]    

    if genre != None and nationality != None:
        name = f"{get_name(F'{nationality}_{genre}_NAME')} {get_lastname(F'{nationality}_LASTNAME')}"
    elif genre != None and nationality == None:
        nationality = random.choice(origin_list)
        name = f"{get_name(F'{nationality}_{genre}_NAME')} {get_lastname(F'{nationality}_LASTNAME')}"
    elif genre == None and nationality != None:
        genre = random.choice(genre_list)
        name = f"{get_name(F'{nationality}_{genre}_NAME')} {get_lastname(F'{nationality}_LASTNAME')}"
    else:
        name = "No information provided, use get_fullname_random in this case"
    return name

def get_fullname_random():

    origin_list = ["USA",  "ENGLISH", 
                   "FRENCH", "SPANISH", 
                   "RUSSIAN",  "GERMAN", 
                   "CHINESE",  "GREEK", 
                   "JAPANESE", "KOREAN", 
                   "HINDI",  "ITALIAN", 
                   "AFRICAN", "PORTUGUESE"]
    
    genre_list = ["MALE", "FEMALE"]
    
    nationality = random.choice(origin_list)
    genre = random.choice(genre_list)

    name = f"{get_name(f'{nationality}_{genre}_NAME')} {get_lastname(f'{nationality}_LASTNAME')}"

    return name

