from jovian.pythondsa import evaluate_test_case


def evaluate_test_case(cards, query):
    # Create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while True:

        # Check if element at the current position matche the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position

        # Increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):
            # Number not found, return -1
            return -1


test = {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3}
result = evaluate_test_case(test['input']['cards'], test['input']['query'])
print(result)