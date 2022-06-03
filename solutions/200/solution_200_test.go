package solution200

import "testing"

var (
	testData = [][]byte{
		[]byte("1"),
		[]byte("1"),
		[]byte("0"),
		[]byte("1"),
		[]byte("0"),
		[]byte("0"),
		[]byte("1"),
	}
	wantIslands = 3
)

func TestSolution(t *testing.T) {
	if got, want := numIslands(testData), wantIslands; got != want {
		t.Errorf("numIslands(%v): got number of islands: %d: want: %d", testData, got, want)
	}
}
