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

func findOptimalFlips(pile string) int {
	return 0
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
