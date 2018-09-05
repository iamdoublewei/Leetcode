/*Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for(int i=0;i<nums.length;i++){
	    for(int j=i+1;j<nums.length;j++){
		if(nums[i]+nums[j] == target){
		    result[0] = i;
		    result[1] = j;
		    return result;
		}
	    }
        } 
	result[0] =0;
	result[1] =0;
	return result;
    }

    public static void main(String args[]){
        int[] myNums = {2,7,11,15};
	int myTarget = 22;
	int[] myResult = new int[2];
	Solution mySolution = new Solution();
	myResult = mySolution.twoSum(myNums, myTarget);
	System.out.println("Result: (" + myResult[0] + ", " + myResult[1] + ")");
    }
}
