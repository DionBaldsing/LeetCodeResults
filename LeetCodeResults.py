class Solution(object):
    # FIRST PROBLEM
    def twoSum(self, nums, target):
        empty_list=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                else:
                    if nums[i]+nums[j]==target:
                        empty_list=i,j
                        return empty_list
                    else:
                        continue
        return false 

    #SECOND PROBLEM
    def reverseString(self, s):
        reversed_list= s.reverse()
        return reversed_list        

    #THIRD PROBLEM
    def isPalindrome(self,x):
        emptyList=[]
        reverseEmptyList=[]
        x=str(x)

        for i in range(len(x)):
            emptyList.append(x[i])
        
        for i in range(len(emptyList)):
            reverseEmptyList+=emptyList[-i-1]
        
        if emptyList==reverseEmptyList:
            return True
        else:
            
            return False 