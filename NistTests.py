from numpy import ndarray, array, round
from nistrng import *
from MersenneRng import MersenneRng

N = 18
SEED = 15
NUMS_COUNT = 100


def generator(seed, n):
    r = 17 * n ** 2 + 5 * n + 3
    x = seed

    while True:
        x = (7 * r * x + r ** 2 - 11 * r) % 127
        yield x


def print_results(results):
    for result, elapsed_time in results:
        if result.passed:
            print("- PASSED - score: " + str(
                round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")
        else:
            print("- FAILED - score: " + str(
                round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")


def get_array_my_generator(seed, n, nums_count):
    my_generator = generator(seed, n)

    count = 0
    nums = []
    for i in my_generator:
        nums.append(i)
        count += 1
        if count == nums_count:
            break

    return nums


def get_array_mersenne_generator(seed, count):
    rng = MersenneRng(seed)
    nums = []
    for i in range(count):
        nums.append(rng.get_random_number())

    return nums


def test_array(sequence):
    binary_sequence: ndarray = pack_sequence(sequence)
    eligible_battery: dict = check_eligibility_all_battery(binary_sequence, SP800_22R1A_BATTERY)
    print("Eligible test for generator:")
    for name in eligible_battery.keys():
        print("-" + name)

    results = run_all_battery(binary_sequence, eligible_battery, False)

    print("Test results for generator:")
    print_results(results)


def main():
    sequence: ndarray = array(get_array_my_generator(SEED, N, NUMS_COUNT))
    print("Test my generator:\n")
    test_array(sequence)

    print("\n====================================================\n")
    sequence = array(get_array_mersenne_generator(SEED, NUMS_COUNT))
    print("Test Mersenne Twister:\n")
    test_array(sequence)

    print("\n====================================================\n")
    print("Increase the number of numbers for tests")
    print("\n====================================================\n")

    sequence = array(get_array_my_generator(SEED, N, NUMS_COUNT * 10))
    print("Test my generator\n")
    test_array(sequence)

    print("\n====================================================\n")
    sequence = array(get_array_mersenne_generator(SEED, NUMS_COUNT * 10))
    print("Test Mersenne Twister:\n")
    test_array(sequence)


if __name__ == "__main__":
    main()
