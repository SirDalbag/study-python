class Solution:
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        return Solution.is_power_of_two(n / 2)

    @staticmethod
    def hamming_weight(n: int) -> int:
        return bin(n).count("1")

    @staticmethod
    def my_sqrt(x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1

    @staticmethod
    def add_binary(a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]

    @staticmethod
    def fizz_buzz(n: int) -> list[str]:
        arr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0:
                arr.append("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
        return arr

    @staticmethod
    def num_unique_emails(emails: list[str]) -> int:
        unique = set()
        for i in emails:
            name, domain = i.split("@")
            name = name.split("+")[0].replace(".", "")
            unique.add(f"{name}@{domain}")
        return len(unique)

    @staticmethod
    def num_jewels_in_stones(jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count

    @staticmethod
    def first_uniq_char(s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return -1

    @staticmethod
    def find_disappeared_numbers(nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

    @staticmethod
    def count_bits(n: int) -> list[int]:
        return [bin(x).count("1") for x in range(n + 1)]

    @staticmethod
    def hamming_distance(x: int, y: int) -> int:
        res = 0
        while x or y:
            res += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1
        return res

    @staticmethod
    def find_content_children(g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        index = 0
        for i in range(len(g)):
            while index < len(s) and g[i] > s[index]:
                index += 1
            if index < len(s):
                res += 1
                index += 1
        return res

    @staticmethod
    def is_perfect_square(num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num // 2
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

    @staticmethod
    def search_insert(nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    @staticmethod
    def can_place_flowers(flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return True if n <= 0 else False

    @staticmethod
    def find_max_consecutive_ones(nums: list[int]) -> int:
        return len(max("".join([str(x) for x in nums]).split("0")))

    @staticmethod
    def find_length_of_LCIS(nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

    @staticmethod
    def plus_one(digits: list[int]) -> list[int]:
        return list(map(int, str(int("".join(str(i) for i in digits)) + 1)))

    @staticmethod
    def single_number(nums: list[int]) -> int:
        return [i for i in nums if nums.count(i) == 1][0]

    @staticmethod
    def missing_number(nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    @staticmethod
    def is_power_of_three(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        return self.isPowerOfThree(n / 3)

    @staticmethod
    def convert_temperature(celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

    @staticmethod
    def title_to_number(column_title: str) -> int:
        result = 0
        for i in column_title:
            result = result * 26 + (ord(i) - ord("A") + 1)
        return result

    @staticmethod
    def to_lower_case(s: str) -> str:
        return s.lower()

    @staticmethod
    def rotate_string(s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)

    @staticmethod
    def majority_element(nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    @staticmethod
    def length_of_last_word(s: str) -> int:
        s = s.split()
        return len(s[len(s) - 1])
