periodic_table = {
    1: {'name': 'Hydrogen', 'symbol': 'H', 'atomic_mass': 1.008},
    2: {'name': 'Helium', 'symbol': 'He', 'atomic_mass': 4.0026},
    3: {'name': 'Lithium', 'symbol': 'Li', 'atomic_mass': 6.94},
    4: {'name': 'Beryllium', 'symbol': 'Be', 'atomic_mass': 9.0122},
    5: {'name': 'Boron', 'symbol': 'B', 'atomic_mass': 10.81},
    6: {'name': 'Carbon', 'symbol': 'C', 'atomic_mass': 12.011},
    7: {'name': 'Nitrogen', 'symbol': 'N', 'atomic_mass': 14.007},
    8: {'name': 'Oxygen', 'symbol': 'O', 'atomic_mass': 15.999},
    9: {'name': 'Fluorine', 'symbol': 'F', 'atomic_mass': 18.998},
    10: {'name': 'Neon', 'symbol': 'Ne', 'atomic_mass': 20.180},
    11: {'name': 'Sodium', 'symbol': 'Na', 'atomic_mass': 22.990},
    12: {'name': 'Magnesium', 'symbol': 'Mg', 'atomic_mass': 24.305},
    13: {'name': 'Aluminum', 'symbol': 'Al', 'atomic_mass': 26.982},
    14: {'name': 'Silicon', 'symbol': 'Si', 'atomic_mass': 28.085},
    15: {'name': 'Phosphorus', 'symbol': 'P', 'atomic_mass': 30.974},
    16: {'name': 'Sulfur', 'symbol': 'S', 'atomic_mass': 32.06},
    17: {'name': 'Chlorine', 'symbol': 'Cl', 'atomic_mass': 35.45},
    18: {'name': 'Argon', 'symbol': 'Ar', 'atomic_mass': 39.948},
    19: {'name': 'Potassium', 'symbol': 'K', 'atomic_mass': 39.098},
    20: {'name': 'Calcium', 'symbol': 'Ca', 'atomic_mass': 40.078},
    21: {'name': 'Scandium', 'symbol': 'Sc', 'atomic_mass': 44.956},
    22: {'name': 'Titanium', 'symbol': 'Ti', 'atomic_mass': 47.867},
    23: {'name': 'Vanadium', 'symbol': 'V', 'atomic_mass': 50.942},
    24: {'name': 'Chromium', 'symbol': 'Cr', 'atomic_mass': 51.996},
    25: {'name': 'Manganese', 'symbol': 'Mn', 'atomic_mass': 54.938},
    26: {'name': 'Iron', 'symbol': 'Fe', 'atomic_mass': 55.845},
    27: {'name': 'Cobalt', 'symbol': 'Co', 'atomic_mass': 58.933},
    28: {'name': 'Nickel', 'symbol': 'Ni', 'atomic_mass': 58.693},
    29: {'name': 'Copper', 'symbol': 'Cu', 'atomic_mass': 63.546},
    30: {'name': 'Zinc', 'symbol': 'Zn', 'atomic_mass': 65.38},
    31: {'name': 'Gallium', 'symbol': 'Ga', 'atomic_mass': 69.723},
    32: {'name': 'Germanium', 'symbol': 'Ge', 'atomic_mass': 72.64},
    33: {'name': 'Arsenic', 'symbol': 'As', 'atomic_mass': 74.922},
    34: {'name': 'Selenium', 'symbol': 'Se', 'atomic_mass': 78.96},
    35: {'name': 'Bromine', 'symbol': 'Br', 'atomic_mass': 79.904},
    36: {'name': 'Krypton', 'symbol': 'Kr', 'atomic_mass': 83.798},
    37: {'name': 'Rubidium', 'symbol': 'Rb', 'atomic_mass': 85.468},
    38: {'name': 'Strontium', 'symbol': 'Sr', 'atomic_mass': 87.62},
    39: {'name': 'Yttrium', 'symbol': 'Y', 'atomic_mass': 88.906},
    40: {'name': 'Zirconium', 'symbol': 'Zr', 'atomic_mass': 91.224},
    41: {'name': 'Niobium', 'symbol': 'Nb', 'atomic_mass': 92.906},
    42: {'name': 'Molybdenum', 'symbol': 'Mo', 'atomic_mass': 95.94},
    43: {'name': 'Technetium', 'symbol': 'Tc', 'atomic_mass': 98},
    44: {'name': 'Ruthenium', 'symbol': 'Ru', 'atomic_mass': 101.07},
    45: {'name': 'Rhodium', 'symbol': 'Rh', 'atomic_mass': 102.91},
    46: {'name': 'Palladium', 'symbol': 'Pd', 'atomic_mass': 106.42},
    47: {'name': 'Silver', 'symbol': 'Ag', 'atomic_mass': 107.87},
    48: {'name': 'Cadmium', 'symbol': 'Cd', 'atomic_mass': 112.41},
    49: {'name': 'Indium', 'symbol': 'In', 'atomic_mass': 114.82},
    50: {'name': 'Tin', 'symbol': 'Sn', 'atomic_mass': 118.71},
    51: {'name': 'Antimony', 'symbol': 'Sb', 'atomic_mass': 121.76},
    52: {'name': 'Tellurium', 'symbol': 'Te', 'atomic_mass': 127.60},
    53: {'name': 'Iodine', 'symbol': 'I', 'atomic_mass': 126.90},
    54: {'name': 'Xenon', 'symbol': 'Xe', 'atomic_mass': 131.29},
    55: {'name': 'Cesium', 'symbol': 'Cs', 'atomic_mass': 132.91},
    56: {'name': 'Barium', 'symbol': 'Ba', 'atomic_mass': 137.33},
    57: {'name': 'Lanthanum', 'symbol': 'La', 'atomic_mass': 138.91},
    58: {'name': 'Cerium', 'symbol': 'Ce', 'atomic_mass': 140.12},
    59: {'name': 'Praseodymium', 'symbol': 'Pr', 'atomic_mass': 140.91},
    60: {'name': 'Neodymium', 'symbol': 'Nd', 'atomic_mass': 144.24},
    61: {'name': 'Promethium', 'symbol': 'Pm', 'atomic_mass': 145},
    62: {'name': 'Samarium', 'symbol': 'Sm', 'atomic_mass': 150.36},
    63: {'name': 'Europium', 'symbol': 'Eu', 'atomic_mass': 151.96},
    64: {'name': 'Gadolinium', 'symbol': 'Gd', 'atomic_mass': 157.25},
    65: {'name': 'Terbium', 'symbol': 'Tb', 'atomic_mass': 158.93},
    66: {'name': 'Dysprosium', 'symbol': 'Dy', 'atomic_mass': 162.50},
    67: {'name': 'Holmium', 'symbol': 'Ho', 'atomic_mass': 164.93},
    68: {'name': 'Erbium', 'symbol': 'Er', 'atomic_mass': 167.26},
    69: {'name': 'Thulium', 'symbol': 'Tm', 'atomic_mass': 168.93},
    70: {'name': 'Ytterbium', 'symbol': 'Yb', 'atomic_mass': 173.04},
    71: {'name': 'Lutetium', 'symbol': 'Lu', 'atomic_mass': 174.97},
    72: {'name': 'Hafnium', 'symbol': 'Hf', 'atomic_mass': 178.49},
    73: {'name': 'Tantalum', 'symbol': 'Ta', 'atomic_mass': 180.95},
    74: {'name': 'Tungsten', 'symbol': 'W', 'atomic_mass': 183.84},
    75: {'name': 'Rhenium', 'symbol': 'Re', 'atomic_mass': 186.21},
    76: {'name': 'Osmium', 'symbol': 'Os', 'atomic_mass': 190.23},
    77: {'name': 'Iridium', 'symbol': 'Ir', 'atomic_mass': 192.22},
    78: {'name': 'Platinum', 'symbol': 'Pt', 'atomic_mass': 195.08},
    79: {'name': 'Gold', 'symbol': 'Au', 'atomic_mass': 196.97},
    80: {'name': 'Mercury', 'symbol': 'Hg', 'atomic_mass': 200.59},
    81: {'name': 'Thallium', 'symbol': 'Tl', 'atomic_mass': 204.38},
    82: {'name': 'Lead', 'symbol': 'Pb', 'atomic_mass': 207.2},
    83: {'name': 'Bismuth', 'symbol': 'Bi', 'atomic_mass': 208.98},
    84: {'name': 'Polonium', 'symbol': 'Po', 'atomic_mass': 209},
    85: {'name': 'Astatine', 'symbol': 'At', 'atomic_mass': 210},
    86: {'name': 'Radon', 'symbol': 'Rn', 'atomic_mass': 222},
    87: {'name': 'Francium', 'symbol': 'Fr', 'atomic_mass': 223},
    88: {'name': 'Radium', 'symbol': 'Ra', 'atomic_mass': 226},
    89: {'name': 'Actinium', 'symbol': 'Ac', 'atomic_mass': 227},
    90: {'name': 'Thorium', 'symbol': 'Th', 'atomic_mass': 232.04},
    91: {'name': 'Protactinium', 'symbol': 'Pa', 'atomic_mass': 231.04},
    92: {'name': 'Uranium', 'symbol': 'U', 'atomic_mass': 238.03},
    93: {'name': 'Neptunium', 'symbol': 'Np', 'atomic_mass': 237},
    94: {'name': 'Americium', 'symbol': 'Am', 'atomic_mass': 243},
    95: {'name': 'Curium', 'symbol': 'Cm', 'atomic_mass': 247},
    96: {'name': 'Berkelium', 'symbol': 'Bk', 'atomic_mass': 247},
    97: {'name': 'Californium', 'symbol': 'Cf', 'atomic_mass': 251},
    98: {'name': 'Einsteinium', 'symbol': 'Es', 'atomic_mass': 252},
    99: {'name': 'Fermium', 'symbol': 'Fm', 'atomic_mass': 253},
    100: {'name': 'Mendelevium', 'symbol': 'Md', 'atomic_mass': 256},
    101: {'name': 'Nobelium', 'symbol': 'No', 'atomic_mass': 257},
    102: {'name': 'Lawrencium', 'symbol': 'Lr', 'atomic_mass': 258},
    103: {'name': 'Rutherfordium', 'symbol': 'Rf', 'atomic_mass': 259},
    104: {'name': 'Dubnium', 'symbol': 'Db', 'atomic_mass': 260},
    105: {'name': 'Seaborgium', 'symbol': 'Sg', 'atomic_mass': 261},
    106: {'name': 'Bohrium', 'symbol': 'Bh', 'atomic_mass': 262},
    107: {'name': 'Hassium', 'symbol': 'Hs', 'atomic_mass': 263},
    108: {'name': 'Meitnerium', 'symbol': 'Mt', 'atomic_mass': 268},
    109: {'name': 'Darmstadtium', 'symbol': 'Ds', 'atomic_mass': 271},
    110: {'name': 'Roentgenium', 'symbol': 'Rg', 'atomic_mass': 272},
    111: {'name': 'Copernicium', 'symbol': 'Cn', 'atomic_mass': 285},
    112: {'name': 'Nihonium', 'symbol': 'Nh', 'atomic_mass': 286},
    113: {'name': 'Flerovium', 'symbol': 'Fl', 'atomic_mass': 289},
    114: {'name': 'Moscovium', 'symbol': 'Mc', 'atomic_mass': 290},
    115: {'name': 'Livermorium', 'symbol': 'Lv', 'atomic_mass': 293},
    116: {'name': 'Tennessine', 'symbol': 'Ts', 'atomic_mass': 294},
    117: {'name': 'Oganesson', 'symbol': 'Og', 'atomic_mass': 294},
    118: {'name': 'Copernicium', 'symbol': 'Cn', 'atomic_mass': 285},
}
def search_periodic_table(query, search_type='name'):
    """Searches the periodic table based on the query and search type.
    Args:
        query: The search term (string or number).
        search_type: The type of search to perform ('name', 'symbol', 'atomic_number', 'atomic_mass').
    Returns:
        A dictionary containing the element information, or None if not found.
    """
    query = str(query).lower()
    if search_type == 'name':
        for atomic_number, element_data in periodic_table.items():
            if element_data['name'].lower() == query:
                return {**element_data, 'atomic_number': atomic_number}
    elif search_type == 'symbol':
        for atomic_number, element_data in periodic_table.items():
            if element_data['symbol'].lower() == query:
                return {**element_data, 'atomic_number': atomic_number}
    elif search_type == 'atomic_number':
        try:
            atomic_number = int(query)
            if atomic_number in periodic_table:
                return {**periodic_table[atomic_number], 'atomic_number': atomic_number}
        except ValueError:
            return None
    elif search_type == 'atomic_mass':
        try:
            atomic_mass = float(query)
            for atomic_number, element_data in periodic_table.items():
                if abs(element_data['atomic_mass'] - atomic_mass) < 0.001:
                    return {**element_data, 'atomic_number': atomic_number}
        except ValueError:
            return None
    return None

while True:
    print("\nSearch the Periodic Table:")
    print("1. Search by Name")
    print("2. Search by Symbol")
    print("3. Search by Atomic Number")
    print("4. Search by Atomic Mass")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        result = search_periodic_table(input("Enter element name: "), 'name')
    elif choice == '2':
        result = search_periodic_table(input("Enter element symbol: "), 'symbol')
    elif choice == '3':
        result = search_periodic_table(input("Enter atomic number: "), 'atomic_number')
    elif choice == '4':
        result = search_periodic_table(input("Enter atomic mass: "), 'atomic_mass')
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    if result:
        print("\nElement Found:")
        for key, value in result.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    else:
        print("Element not found.")
