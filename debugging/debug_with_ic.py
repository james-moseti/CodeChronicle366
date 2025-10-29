from icecream import ic

def add(x, y): 
    return x + y

# result = print(add(10, 30))
# print(result)       # Returns None

result = ic(add(10, 30))
print(result)

data = {'data': [1,2,3,4,5], 
        'labels': ['a', 'b', 'c', 'd', 'e']
        }

print(data['data'][2])      # Returns 3
ic(data['data'][2])

user_data = {
    'users': [
        {
            'id': 1,
            'name': 'Alice',
            'posts': [
                {
                    'title': 'Hello World',
                    'content': 'This is my first post.'
                }, 
                {
                    'title': 'Python Rocks!',
                    'content': 'Why I love Python.'
                }
            ]
        }, 
        {
            'id': 2,
            'name': 'Bob',
            'posts': [
                {
                    'title': 'Travelling the world',
                    'content': 'My experiences travelling.'
                }
            ]
        }
    ],
    'metadata': {
        'version': 1.0,
        'generated_at': '2023-10-03'
    }
}

# print(user_data)
ic(user_data)      # better formatted output compared to just print()

def isEven(value): 
    if value % 2 == 0:
        ic()
        return True
    else: 
        ic()
        return False
    
print(isEven(10))
print(isEven(11))
print(isEven(12))

# ic.disable()    # You can disable ic this way

# print(isEven(10))
# print(isEven(11))
# print(isEven(12))

def output_to_file(text):
    with open('debug_log.txt', 'a') as f:
        f.write(text + '\n')

ic.configureOutput(prefix='Debug| ', outputFunction=output_to_file, includeContext=True)

ic(add(10, 70))