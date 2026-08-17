class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
        # curr=|0|,best=[0],jumps=0
        # [|7|,0,9,6,9,6,1,[7],9,0,1,2,9,0,3]
        # curr=|0|,best=[8],jumps=1
        # [7,|0|,9,6,9,6,1,[7],9,0,1,2,9,0,3]
        # curr=1,best=8,jumps=1
        # [7,0,|9|,6,9,6,1,[7],9,0,1,[[2]],9,0,3]

        # [2,4,1,1,1,1]
        best = curr = jumps = 0
        for i in range(len(nums)):
            print("i: ", i)
            print("nums[i]: ", nums[i])
            best = max(best, i+nums[i])
            print("curr: ", curr)
            if i == curr:
                curr = best
                jumps += 1
                if best >= len(nums)-1:
                    return jumps
        