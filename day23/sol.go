package main

import (
	"container/heap"
	"fmt"
	"strings"
)

func main() {
	fmt.Println(search(sample()))
	fmt.Println(search(input()))
}

func sample() *node {
	n := new(node)
	for i, c := range "BACDBCDA" {
		n.spot[LEN+i] = spot(c)
	}
	return n
}
func input() *node {
	n := new(node)
	for i, c := range "ABCABDDC" {
		n.spot[LEN+i] = spot(c)
	}
	return n
}

type spot int8
type node struct {
	spot [11 + 2*4]spot // hallway + corridors
}

type entry struct {
	score_ int
	node   *node
	prev   *node
	cost   int
}

// the past cost of a node is the cost it took to get here
func (e *entry) past() int { return e.score() - e.future() }

// the future of a node is the predicted future cost
// specifically, the cost it would take to move each guy to its goal spot
// assuming no obstacles
func (e *entry) future() int { return e.node.distance() }

// the score of a node is the past + the future
func (e *entry) score() int { return e.score_ }

func less(a, b *entry) bool {
	return a.score() < b.score()
}

type nodelist []entry

func search(start *node) int {
	// A*
	var queue nodelist
	queue = append(queue, entry{node: start, score_: start.distance()})
	//queue = [(distance(start,end),start)] # reduced risk, pos
	seen := make(map[node]bool)
	type pnode = struct{node *node; cost int}
	path := make(map[node]pnode)
	for len(queue) > 0 {
		e := heap.Pop(&queue).(entry)
		if seen[*e.node] {
			continue
		}
		path[*e.node] = pnode{e.prev, e.cost}
		//fmt.Println("--")
		//fmt.Print(e.prev)
		//fmt.Print(e.node)
		//fmt.Println("cost:", e.cost)
		//print(c, here)
		if e.future() == 0 {
			printpath(e.node, path)
			return e.past()
		}
		seen[*e.node] = true
		here := e.node
		base := e.past()
		//checkcost(e.node, path, base)

		pushMove := func(src, dst int) {
			n := here.move(src, dst)
			if !seen[*n] {
				moves := distance(src, dst)
				w := weight(here.spot[src])
				cost := w * moves
				heap.Push(&queue, entry{
					score_: base+cost+n.distance(),
					node: n,
					prev: here,
					cost: cost})
			}
		}

		// Find possible moves
	neighbor:
		for i := range here.spot[:] {
			if here.spot[i] == 0 {
				continue
			}
			if inHallway(i) {
				// hallway spots
				// can move into a corridor only if it would make them home
				// so only a home corridor and only if it's not occupied by another type of thing
				x, _ := i, 0 // coords(i)
				me := here.spot[i]
				h := here.homeOf(i)
				if !here.clearBetween(x, h) {
					continue neighbor
				}
				j := LEN + h - 2
				if here.spot[j] == 0 && here.spot[j+1] == 0 {
					pushMove(i, j+1)
				}
				if here.spot[j] == 0 && here.spot[j+1] == me {
					pushMove(i, j)
				}
			} else {
				// corridor spots
				// if top spot blocked, no move
				x, y := coords(i)
				if y == 2 && here.spot[i-1] != 0 {
					continue neighbor
				}
				// if thing is home already, no moves
				if here.homeOf(i) == x {
					if y == 2 || y == 1 && here.homeOf(i+1) == x {
						continue neighbor
					}
				}
				// search in both hallway directions for unblocked spots
				for j := x - 1; j >= 0; j-- {
					if here.spot[j] != 0 {
						break
					}
					if !isEntrance(j) {
						pushMove(i, j)
					}
				}
				for j := x + 1; j < LEN; j++ {
					if here.spot[j] != 0 {
						break
					}
					if !isEntrance(j) {
						pushMove(i, j)
					}
				}
			}
		}
		/*
		   for n in G.neighbors(here):
		       if n not in seen:
		           r = G.risk(n)
		           if r < MAX:
		               h = distance(n, end)
		               heappush(queue, (c+r+h-k, n))*/
	}
	return -1
}

func checkcost(end *node, path map[node]struct{node *node; cost int}, expected int) {
	c := 0
	t := 0
	for n := end; n != nil; {
		t += c
		c = path[*n].cost
		n = path[*n].node
	}
	if t != expected {
		printpath(end, path)
		fmt.Printf("ERROR actual cost %d != expected %d\n", t, expected)
	}
}

func printpath(n *node, path map[node]struct{node *node; cost int}) {
	c := 0
	t := 0
	for n != nil {
		t += c
		fmt.Println("--")
		fmt.Print(n)
		//fmt.Println("cost:", c, "\t", "t=", t, " dist=", n.distance())
		fmt.Println("cost:", c)
		c = path[*n].cost
		n = path[*n].node
	}
	fmt.Println("total cost:", t)
}

func (n *node) clearBetween(src, dst int) bool {
	if src == dst {
		return true
	}
	var x0, x1 int
	if src < dst {
		x0, x1 = src+1, dst+1
	} else {
		x0, x1 = dst, src
	}
	for i := x0; i < x1; i++ {
		if n.spot[i] != 0 {
			return false
		}
	}
	return true
}

// returns a new node with the thing at src moved to dst
func (n0 *node) move(src, dst int) *node {
	n := new(node)
	*n = *n0
	if n.spot[src] == 0 {
		panic("attempt to move from unoccupied spot")
	}
	if n.spot[dst] != 0 {
		panic("attempt to move into occupied spot")
	}
	n.spot[dst] = n.spot[src]
	n.spot[src] = 0
	return n
}

// returns the cost to move from src to dst
func (n *node) moveCost(src, dst int) int {
	if n.spot[src] == 0 {
		return 0
	}
	panic("TODO")
}

// #############
// #123456789ab#
// ###c#e#g#i###
//   #d#f#h#e#
//   #########

const LEN = 11

func inHallway(i int) bool { return i < LEN }

func isEntrance(i int) bool {
	return i == 2 || i == 4 || i == 6 || i == 8
}

// decompose a spot into its x, y coords
// where x is the position in the hallway and y is the depth into a corridor
func coords(i int) (x, y int) {
	if i < LEN {
		return i, 0
	} else {
		y := 1 + (i-LEN)%2
		x := 2 + ((i - LEN) / 2 * 2)
		return x, y
	}
}

// returns the number of moves to move from coordinate i to coordinate j
func distance(i, j int) int {
	x0, y0 := coords(i)
	x1, y1 := coords(j)
	return abs(x1-x0) + y0 + y1
}

func abs(a int) int {
	if a < 0 {
		a = -a
	}
	return a
}

/// boring heap interface code
func (h nodelist) Len() int { return len(h) }
func (h nodelist) Less(i, j int) bool {
	return less(&h[i], &h[j])
}
func (h nodelist) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *nodelist) Push(x interface{}) {
	*h = append(*h, x.(entry))
}
func (h *nodelist) Pop() interface{} {
	last := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return last
}

func (n *node) homeOf(i int) int {
	return home(n.spot[i])
}

func home(x spot) int {
	switch x {
	case 'A':
		return 2
	case 'B':
		return 4
	case 'C':
		return 6
	case 'D':
		return 8
	default:
		return 0
	}
}

func weight(x spot) int {
	switch x {
	case 'A':
		return 1
	case 'B':
		return 10
	case 'C':
		return 100
	case 'D':
		return 1000
	default:
		return 10000
	}
}

// converts an x coord into the index of the top of the home corridor

func (n *node) distance() int {
	var total int
	for i := range n.spot[:] {
		total += n.homecost(i)
	}
	return total
}

// estimated cost to get thing at spot i home
func (n *node) homecost(i int) int {
	if n.spot[i] == 0 {
		return 0
	}
	w := weight(n.spot[i])
	x, y := coords(i)
	if y == 1 || y == 2 {
		// if thing is home already, no cost
		if n.homeOf(i) == x {
			if y == 2 || y == 1 && n.homeOf(i+1) == x {
				return 0
			}
			if y == 1 {
				return w * 4
			}
		}
	}
	x1, y1 := n.homeOf(i), 1
	d := abs(x1-x) + y + y1
	return d * w
}

func (n *node) String() string {
	const template = `#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########
`

	s := []byte(template)
	for i := range n.spot {
		if n.spot[i] == 0 {
			continue
		}
		x, y := coords(i)
		j := 0
		for ; y >= 0; y-- {
			if i := strings.Index(template[j:], "\n"); i != -1 {
				j += i + 1
			}
		}
		s[j+x+1] = byte(n.spot[i])
	}
	return string(s)
}
