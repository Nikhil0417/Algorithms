import java.util.Arrays;

class Solution {
    public int arrayPairSum(int[] nums) {
        int sum=0;
        int min = nums[0];
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i=i+2){
            if(nums[i]>nums[i+1]){
                min = nums[i+1];
            }
            else{
                min = nums[i];
            }
            sum += min;
        }
        return sum;
    }
}
