# Nomix v1.0
![License](https://img.shields.io/badge/license-MIT-red.svg)
![Version](https://img.shields.io/badge/version-1.0-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11-blue)


![logo](https://github.com/tomasilluminati/Nomix/blob/main/logo/logo.png)

## Overview
This Python module generates random names based on parameters such as gender and nationality. It provides functions to retrieve random names and last names from various cultures.

## Table of Contents
- [Installation](#installation)
- [Functions](#functions)
  - [get_name](#get_name)
  - [get_name_random](#get_name_random)
  - [get_lastname](#get_lastname)
  - [get_lastname_random](#get_lastname_random)
  - [get_fullname](#get_fullname)
  - [get_fullname_random](#get_fullname_random)
- [Contributing](#contributing)
- [License](#license)

## Installation
Clone the repository:

```bash
git clone https://github.com/tomasilluminati/Nomix
```
Or use the pip command:

```bash
pip install nomix 
```

## Usage
Import the module in your project

```python
import nomix 
```

## Functions

### get_name()
Returns a random name based on the specified data type. Available data types include:

- "USA_MALE_NAME"
- "USA_FEMALE_NAME"
- "ENGLISH_MALE_NAME"
- "ENGLISH_FEMALE_NAME"
- "FRENCH_MALE_NAME"
- "FRENCH_FEMALE_NAME"
- "SPANISH_MALE_NAME"
- "SPANISH_FEMALE_NAME"
- "RUSSIAN_MALE_NAME"
- "RUSSIAN_FEMALE_NAME"
- "GERMAN_MALE_NAME"
- "GERMAN_FEMALE_NAME"
- "CHINESE_MALE_NAME"
- "CHINESE_FEMALE_NAME"
- "GREEK_MALE_NAME"
- "GREEK_FEMALE_NAME"
- "JAPANESE_MALE_NAME"
- "JAPANESE_FEMALE_NAME"
- "KOREAN_MALE_NAME"
- "KOREAN_FEMALE_NAME"
- "HINDI_MALE_NAME"
- "HINDI_FEMALE_NAME"
- "ITALIAN_MALE_NAME"
- "ITALIAN_FEMALE_NAME"
- "AFRICAN_MALE_NAME"
- "AFRICAN_FEMALE_NAME"
- "PORTUGUESE_MALE_NAME"
- "PORTUGUESE_FEMALE_NAME"

#### Example:

```python
import nomix 

name = nomix.get_name("USA_MALE_NAME")
print(name)

#Output: Maxwell 
```

------

### get_name_random()
Returns a random name from any available nationality and gender (No required parameters).

#### Example:

```python
import nomix 

name = nomix.get_name_random()
print(name)

#Output: Yulia
```

-----
### get_lastname()
Returns a random last name based on the specified data type. Available data types include:

- "USA_LASTNAME"
- "ENGLISH_LASTNAME"
- "FRENCH_LASTNAME"
- "SPANISH_LASTNAME"
- "RUSSIAN_LASTNAME"
- "GERMAN_LASTNAME"
- "CHINESE_LASTNAME"
- "GREEK_LASTNAME"
- "JAPANESE_LASTNAME"
- "KOREAN_LASTNAME"
- "HINDI_LASTNAME"
- "ITALIAN_LASTNAME"
- "AFRICAN_LASTNAME"
- "PORTUGUESE_LASTNAME"

#### Example:

```python
import nomix 

lastname = nomix.get_lastname("JAPANESE_LASTNAME")
print(lastname)

#Output: Matsui 
```

-----
### get_lastname_random()
Returns a random last name from any available nationality (No required parameters).

#### Example:

```python
import nomix 

lastname = nomix.get_lastname_random()
print(lastname)

#Output: Sander 
```

----
### get_fullname()
Returns a full name based on the specified genre (male/female) and nationality. If genre or nationality is not provided, it randomly selects them.

#### Parameters

`genre`: (Optional) The gender of the name. It can be "MALE" for male or "FEMALE" for female.

`nationality`: (Optional) The nationality of the name. It must be one of the following options:

- "USA"
- "ENGLISH"
- FRENCH"
- "SPANISH"
- "RUSSIAN"
- "GERMAN"
- "CHINESE"
- "GREEK"
- "JAPANESE"
- "KOREAN"
- "HINDI"
- "ITALIAN"
- "AFRICAN"
- "PORTUGUESE".


#### Example:

```python
import nomix 

full_name = nomix.get_fullname("MALE", "KOREAN")
print(full_name)

#Output: Younghoon Seol
```

-----
### get_fullname_random()
Returns a random full name from any available nationality and gender (No required parameters).

#### Example:

```python
import nomix 

full_name = nomix.get_fullname_random()
print(full_name)

#Output: Anatoliy Afanasiev
```

## Contributing
Contributions are welcome! Please feel free to open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Copyright
Copyright (c) 2024 Tomas Illuminati
