package solution1

import "testing"

type testData struct {
	Nums   []int
	Target int
	Result []int
}

var (
	inputData = []testData{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}
)

func TestTwoSum(t *testing.T) {
	for _, test := range inputData {
		result := twoSum(test.Nums, test.Target)
		for i, v := range result {
			if got, want := v, test.Result[i]; got != want {
				t.Errorf("twoSum(%v, %d): got indices %v: want: %v", test.Nums, test.Target, got, want)
			}
		}
	}
}
