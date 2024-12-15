def kSum(nums, target, k):
    def twoSum(nums, target):
        # Two-pointer approach for k=2
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while (
                    left < right and nums[left] == nums[left - 1]
                ):  # Skip duplicates
                    left += 1
                while (
                    left < right and nums[right] == nums[right + 1]
                ):  # Skip duplicates
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
        return res

    def recursiveKSum(nums, target, k):
        if not nums:
            return []
        # If k = 2, use two-pointer approach
        if k == 2:
            return twoSum(nums, target)

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            # Recursively solve for (k-1)-Sum
            for subset in recursiveKSum(
                nums[i+1:], target - nums[i], k - 1
            ):
                res.append([nums[i]] + subset)
        return res

    nums.sort()  # Sort the input array to simplify the problem
    return recursiveKSum(nums, target, k)
