import sort
    
if __name__ == "__main__":
    test_cases = [
        {
            # Volume < 100,00,000; Max dimension < 150; Mass < 20;
            # Not heavy, not bulky
            "input": (10, 20, 30, 5), 
            "expected": "STANDARD"
        },
        {
            # Volume < 100,00,000; Max dimension < 150; Mass == 20;
            # Heavy, not bulky
            "input": (10, 20, 30, 20), 
            "expected": "SPECIAL"
        },
        {
            # Volume < 100,00,000; Max dimension < 150; Mass > 20;
            # Heavy, not bulky
            "input": (10, 20, 30, 55), 
            "expected": "SPECIAL"
        },
        {
            # Volume < 100,00,000; Max dimension == 150; Mass < 20;
            # Not heavy, bulky
            "input": (150, 1, 1, 5), 
            "expected": "SPECIAL"
        },
        {
            # Volume < 100,00,000; Max dimension > 150; Mass < 20;
            # Not heavy, bulky
            "input": (1, 200, 3, 5), 
            "expected": "SPECIAL"
        },
        {
            # Volume == 100,00,000; Max dimension < 150; Mass < 20;
            # Not heavy, bulky
            "input": (100, 100, 100, 5), 
            "expected": "SPECIAL"
        },
        {
            # Volume > 100,00,000; Max dimension > 150; Mass < 20;
            # Not heavy, bulky
            "input": (200, 100, 100, 5), 
            "expected": "SPECIAL"
        },
        {
            # Volume > 100,00,000; Max dimension > 150; Mass == 20;
            # Heavy and bulky
            "input": (200, 100, 100, 20), 
            "expected": "REJECTED"
        },
        {
            # Volume == 100,00,000; Max dimension < 150; Mass > 20;
            # Heavy and bulky
            "input": (100, 100, 100, 25), 
            "expected": "REJECTED"
        },
        {
            # Volume < 100,00,000; Max dimension == 150; Mass > 20;
            # Heavy and bulky
            "input": (1, 1, 150, 25), 
            "expected": "REJECTED"
        },
    ]

    for i, test_case in enumerate(test_cases):
        result = sort.sort(*test_case["input"])
        assert result == test_case["expected"], f"Test case {i} failed: expected {test_case['expected']}, got {result}"

    print(f"All {len(test_cases)} test cases passed!")