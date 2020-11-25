package main

// Importing packages
import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
)

// To solve, here are the steps:
// 1. Start at left position and set the flip position
// 2. move to next position
//   - if same move to next
//   - if not same, increment flips and change flip position
//     - move to next position
// 3. Continue 1 and 2 until end of line
// 4. Check 0 position
//   - if - then increment flip and return
//   - if not then return
func findOptimalFlips(pile string) int {
	var flipPosition = pile[0]
	var flips = 0
	for i := 1; i < len(pile); i++ {
		if flipPosition != pile[i] {
			flips++
			flipPosition = pile[i]
		}
	}
	if flipPosition == '-' {
		flips++
	}
	return flips
}

func prepareStack(caseNumber int, pile string) int {
	output := findOptimalFlips(pile)
	fmt.Println(fmt.Sprintf("Case %d: %d", caseNumber, output))
	return output
}

func prepareCustomerStacksTest(count int, piles []string, expectedOutputs []int) {
	for i := 0; i < count; i++ {
		output := prepareStack(i+1, piles[i])
		if output != expectedOutputs[i] {
			fmt.Println(fmt.Sprintf("Error! Expected: %d got %d", output, expectedOutputs[i]))
		}
	}
}

func prepareCustomerStacks(count int, piles []string) {
	for i := 0; i < count; i++ {
		_ = prepareStack(i+1, piles[i])
	}
}

func readPiles(path *string) []string {
	file, err := os.Open(*path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var output = []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		output = append(output, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return output
}

// Main function
func main() {
	stacksPath := flag.String("path", "./setup", "A path to the setup file.")
	runTests := flag.Bool("runTests", false, "Run the tests for this project.")
	flag.Parse()

	specs := readPiles(stacksPath)

	if *runTests {
		prepareCustomerStacksTest(5, []string{"-", "-+", "+-", "+++", "--+-"}, []int{1, 1, 2, 0, 3})
	}

	cases, err := strconv.Atoi(specs[0])
	if err != nil {
		log.Fatal(err)
	}
	if cases > len(specs[1:]) {
		log.Fatal(fmt.Sprintf("Stated cases greater than actual: Stated %d when only %d were given.", cases, len(specs[1:])))
	}
	prepareCustomerStacks(cases, specs[1:])
}
