import numpy as np

import libcasm.xtal as xtal


def test_make_structure(example_structure_1):
    structure = example_structure_1

    assert structure.lattice().column_vector_matrix().shape == (3, 3)
    assert structure.atom_coordinate_frac().shape == (3, 4)
    assert structure.atom_coordinate_cart().shape == (3, 4)
    assert len(structure.atom_type()) == 4

    assert len(structure.atom_properties()) == 1
    assert "disp" in structure.atom_properties()
    assert structure.atom_properties()["disp"].shape == (3, 4)

    assert len(structure.mol_properties()) == 0

    assert len(structure.global_properties()) == 1
    assert "Hstrain" in structure.global_properties()
    assert structure.global_properties()["Hstrain"].shape == (6, 1)


def test_make_structure_within():
    # Lattice vectors
    lattice = xtal.Lattice(
        np.array(
            [
                [1.0, 0.0, 0.0],  # a
                [0.0, 1.0, 0.0],  # a
                [0.0, 0.0, 1.0],  # c
            ]
        ).transpose()
    )
    atom_coordinate_cart = np.array(
        [
            [0.0, 0.0, 1.1],
        ]
    ).transpose()

    init_structure = xtal.Structure(
        lattice=lattice,
        atom_coordinate_frac=xtal.fractional_to_cartesian(
            lattice, atom_coordinate_cart
        ),
        atom_type=["A"],
    )

    structure = xtal.make_structure_within(init_structure)
    expected_atom_coordinate_cart = np.array(
        [
            [0.0, 0.0, 0.1],
        ]
    ).transpose()
    assert np.allclose(structure.atom_coordinate_cart(), expected_atom_coordinate_cart)

    structure = xtal.make_within(init_structure)
    assert np.allclose(structure.atom_coordinate_cart(), expected_atom_coordinate_cart)


def test_structure_to_dict(example_structure_1):
    structure = example_structure_1
    data = structure.to_dict()

    assert "lattice_vectors" in data
    assert "coordinate_mode" in data
    assert "atom_coords" in data
    assert "atom_properties" in data
    assert len(data["atom_properties"]) == 1
    assert "disp" in data["atom_properties"]
    assert len(data["global_properties"]) == 1
    assert "Hstrain" in data["global_properties"]

    assert isinstance(xtal.pretty_json(data), str)


def test_structure_from_dict():
    data = {
        "atom_coords": [
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.5],
            [0.0, 0.0, 1.0],
            [0.5, 0.5, 1.5],
        ],
        "atom_properties": {
            "disp": {
                "value": [
                    [0.1, 0.0, 0.0],
                    [0.1, 0.0, 0.1],
                    [0.1, 0.1, 0.0],
                    [0.1, 0.2, 0.3],
                ]
            }
        },
        "atom_type": ["A", "A", "B", "B"],
        "coordinate_mode": "Cartesian",
        "global_properties": {
            "Hstrain": {"value": [0.009950330853168087, 0.0, 0.0, 0.0, 0.0, 0.0]}
        },
        "lattice_vectors": [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 2.0]],
        "mol_coords": [],
        "mol_type": [],
    }
    structure = xtal.Structure.from_dict(data)

    assert structure.lattice().column_vector_matrix().shape == (3, 3)
    assert structure.atom_coordinate_frac().shape == (3, 4)
    assert structure.atom_coordinate_cart().shape == (3, 4)
    assert structure.mol_coordinate_cart().shape == (3, 0)
    assert structure.mol_coordinate_frac().shape == (3, 0)
    assert len(structure.atom_type()) == 4
    assert len(structure.atom_properties()) == 1
    assert len(structure.global_properties()) == 1


def test_structure_to_poscar_str_1(example_structure_2):
    poscar_str = example_structure_2.to_poscar_str(
        title="test structure", sort=False, cart_coordinate_mode=False
    )
    # print(poscar_str)
    lines = poscar_str.split("\n")

    assert lines[0] == "test structure"
    assert lines[5] == "A B A "
    assert lines[6] == "1 1 1 "
    assert lines[7] == "Direct"


def test_structure_to_poscar_str_2(example_structure_2):
    poscar_str = example_structure_2.to_poscar_str(
        title="test structure", sort=True, cart_coordinate_mode=True
    )
    # print(poscar_str)
    lines = poscar_str.split("\n")

    assert lines[0] == "test structure"
    assert lines[5] == "A B "
    assert lines[6] == "2 1 "
    assert lines[7] == "Cartesian"


def test_structure_to_poscar_str_3(example_structure_2):
    poscar_str = example_structure_2.to_poscar_str(
        title="test structure", sort=True, ignore=[]
    )
    print(poscar_str)
    lines = poscar_str.split("\n")

    assert lines[0] == "test structure"
    assert lines[5] == "A B Va "
    assert lines[6] == "2 1 1 "
    assert lines[7] == "Direct"


def test_copy_structure(example_structure_1):
    import copy

    structure1 = copy.copy(example_structure_1)
    structure2 = copy.deepcopy(example_structure_1)

    assert isinstance(example_structure_1, xtal.Structure)
    assert isinstance(structure1, xtal.Structure)
    assert structure1 is not example_structure_1
    assert isinstance(structure2, xtal.Structure)
    assert structure2 is not example_structure_1


def test_structure_is_equivalent_to():
    # Lattice vectors
    lattice = xtal.Lattice(
        np.array(
            [
                [1.0, 0.0, 0.0],  # a
                [0.0, 1.0, 0.0],  # a
                [0.0, 0.0, 2.0],  # c
            ]
        ).transpose()
    )
    atom_coordinate_cart = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.5],
            [0.0, 0.0, 1.0],
            [0.5, 0.5, 1.5],
        ]
    ).transpose()

    # atom types - re-ordered
    atom_type = ["A", "A", "B", "B"]

    # atom properties
    atom_disp = np.array(
        [
            [0.1, 0.0, 0.0],
            [0.0, 0.1, 0.0],
            [0.0, 0.0, 0.1],
            [0.1, 0.2, 0.3],
        ]
    ).transpose()
    atom_properties = {"disp": atom_disp}
    print(atom_properties)

    # global properties
    # F = np.array(
    #     [
    #         [1.01, 0.0, 0.0],
    #         [0.0, 1.0, 0.0],
    #         [0.0, 0.0, 1.0],
    #     ]
    # )
    # converter = xtal.StrainConverter('Hstrain')
    # Hstrain_vector = converter.from_F(F)
    Hstrain_vector = np.array([0.009950330853168087, 0.0, 0.0, 0.0, 0.0, 0.0])
    global_properties = {"Hstrain": Hstrain_vector}
    print(global_properties)

    structure1 = xtal.Structure(
        lattice=lattice,
        atom_coordinate_frac=xtal.cartesian_to_fractional(
            lattice, atom_coordinate_cart
        ),
        atom_type=atom_type,
        atom_properties=atom_properties,
        global_properties=global_properties,
    )

    # structure2: re-order atoms

    # atom coordinates - re-ordered
    atom_coordinate_cart = np.array(
        [
            [0.5, 0.5, 0.5],  # 1
            [0.0, 0.0, 1.0],  # 2
            [0.5, 0.5, 1.5],  # 3
            [0.0, 0.0, 0.0],  # 0
        ]
    ).transpose()

    # atom types - re-ordered
    atom_type = ["A", "B", "B", "A"]  # 1, 2, 3, 0

    # atom properties - re-ordered
    atom_disp = np.array(
        [
            [0.0, 0.1, 0.0],  # 1
            [0.0, 0.0, 0.1],  # 2
            [0.1, 0.2, 0.3],  # 3
            [0.1, 0.0, 0.0],  # 0
        ]
    ).transpose()
    atom_properties = {"disp": atom_disp}
    print(atom_properties)

    # global properties - same
    np.array(
        [
            [1.01, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    # converter = xtal.StrainConverter('Hstrain')
    # Hstrain_vector = converter.from_F(F)
    Hstrain_vector = np.array([0.009950330853168087, 0.0, 0.0, 0.0, 0.0, 0.0])
    global_properties = {"Hstrain": Hstrain_vector}

    structure2 = xtal.Structure(
        lattice=lattice,
        atom_coordinate_frac=xtal.cartesian_to_fractional(
            lattice, atom_coordinate_cart
        ),
        atom_type=atom_type,
        atom_properties=atom_properties,
        global_properties=global_properties,
    )

    assert structure1.is_equivalent_to(structure2)
