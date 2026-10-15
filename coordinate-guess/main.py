import random

# grid guess
# guess a secret coordinate (x,y) from a n x n grid using binary search

# def grid_search(x_size, y_size, secret_x, secret_y):
#     min_x, max_x = 0, x_size
#     min_y, max_y = 0, y_size
#     # print(min_x, max_x, min_y, max_y)
#     step = 0
#     guess_x, guess_y = -1, -1
#     while guess_x != secret_x or guess_y != secret_y:
#         guess_x = (max_x + min_x) // 2
#         guess_y = (max_y + min_y) // 2
#         step += 1
#         print(f"Guessing coordinate: ({guess_x}, {guess_y})")
#         if guess_x > secret_x:
#             max_x = guess_x - 1
#             # print(f"New range for x: ({min_x}, {max_x})")
#         elif guess_x < secret_x:
#             min_x = guess_x + 1
#             # print(f"New range for x: ({min_x}, {max_x})")
#         else:
#             continue
#         if guess_y > secret_y:
#             max_y = guess_y - 1
#             # print(f"New range for y: ({min_y}, {max_y})")
#         elif guess_y < secret_y:
#             min_y = guess_y + 1
#             # print(f"New range for y: ({min_y}, {max_y})")
#         else:
#             continue
#     print (f"Found secret coordinate: ({guess_x}, {guess_y}) with {step} steps")

def grid_search(x_size, y_size, secret_x, secret_y):
    range_x = [0, x_size]
    range_y = [0, y_size]
    # print(min_x, max_x, min_y, max_y)
    step = 0
    guess_x, guess_y = -1, -1
    while guess_x != secret_x or guess_y != secret_y:
        guess_x = (range_x[1] + range_x[0]) // 2
        guess_y = (range_y[1] + range_y[0]) // 2
        step += 1

        # print(f"Range for x: {range_x} y: {range_y}")
        # print(f"Guessing coordinate: ({guess_x}, {guess_y})")
        
        if guess_x > secret_x:
            range_x[1] = guess_x - 1
        elif guess_x < secret_x:
            range_x[0] = guess_x + 1
        if guess_y > secret_y:
            range_y[1] = guess_y - 1
            # print(f"New range for y: {range_y}")
        elif guess_y < secret_y:
            range_y[0] = guess_y + 1
            # print(f"New range for y: {range_y}")

    # secret_xy = [guess_x, guess_y]
    # print (f"Found secret coordinate: {secret_xy} with {step} steps")
    return [guess_x, guess_y], step

n = 100

a = random.randint(0, n)
b = random.randint(0, n)
print(f"Secret coordinate: ({a}, {b})")
secret_xy, steps = grid_search(n, n, a, b)
print(f"Found secret coordinate: {secret_xy} with {steps} steps")