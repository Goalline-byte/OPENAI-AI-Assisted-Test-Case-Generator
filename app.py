from test_generator import generate_test_cases

if __name__ == "__main__":
    user_story = input("Enter user story: ")
    
    result = generate_test_cases(user_story)
    
    print("\nGenerated Output:\n")
    print(result)
