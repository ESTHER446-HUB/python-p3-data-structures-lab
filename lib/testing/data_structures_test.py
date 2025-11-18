#!/usr/bin/env python3

from data_structures import (
    get_names,
    get_spiciest_foods,
    print_spicy_foods,
    create_spicy_food,
    get_spicy_food_by_cuisine,
    print_spiciest_foods,
    get_average_heat_level,
)

import io
import sys

class TestDataStructures:
    SPICY_FOODS = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]

    def test_get_names(self):
        """Test that get_names returns all food names."""
        assert get_names(self.SPICY_FOODS) == ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

    def test_get_spiciest_foods(self):
        """Test that get_spiciest_foods returns foods with heat_level > 5."""
        spiciest = get_spiciest_foods(self.SPICY_FOODS)
        for food in spiciest:
            assert food["heat_level"] > 5

    def test_get_spicy_food_by_cuisine(self):
        """Test that get_spicy_food_by_cuisine returns the correct food."""
        result = get_spicy_food_by_cuisine(self.SPICY_FOODS, "American")
        assert result == {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}

    def test_print_spicy_foods(self):
        """Test that print_spicy_foods prints all foods correctly."""
        captured_out = io.StringIO()
        sys.stdout = captured_out

        print_spicy_foods(self.SPICY_FOODS)

        sys.stdout = sys.__stdout__
        output = captured_out.getvalue()
        assert "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶" in output
        assert "Buffalo Wings (American) | Heat Level: 🌶🌶🌶" in output
        assert "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶" in output

    def test_print_spiciest_foods(self):
        """Test that print_spiciest_foods prints only foods with heat_level > 5."""
        captured_out = io.StringIO()
        sys.stdout = captured_out

        print_spiciest_foods(self.SPICY_FOODS)

        sys.stdout = sys.__stdout__
        output = captured_out.getvalue()
        assert "Green Curry (Thai)" in output
        assert "Mapo Tofu (Sichuan)" in output
        assert "Buffalo Wings (American)" not in output

    def test_get_average_heat_level(self):
        """Test that get_average_heat_level returns correct average."""
        avg = get_average_heat_level(self.SPICY_FOODS)
        expected = (9 + 3 + 6) / 3
        assert avg == expected

    def test_create_spicy_food(self):
        """Test that create_spicy_food adds a new spicy food correctly."""
        new_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
        updated_list = create_spicy_food(self.SPICY_FOODS, new_food)
        assert updated_list[-1] == new_food
        assert len(updated_list) == len(self.SPICY_FOODS) + 1
