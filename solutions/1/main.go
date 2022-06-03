package twosum

// twoSum return indices of the two numbers such that they add up to target.
func twoSum(nums []int, target int) []int {
	for i, v := range nums {
		for a, av := range nums {
			if i == a {
				continue
			}
			if v+av == target {
				return []int{i, a}
			}
		}
	}
	return []int{}
}
