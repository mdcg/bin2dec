package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Printf("Welcome to Bin2Dec!\nTo exit, press 'CTRL + C'.\n\n")
	loop()
}

func ConvertBinaryToDecimal(binaryValue string) (int64, error) {
	convertedBinaryToDecimal, err := strconv.ParseInt(binaryValue, 2, 32)
	return convertedBinaryToDecimal, err
}

func loop() {
	reader := bufio.NewReader(os.Stdin)

	for {
		binaryValue := userInput(reader)
		convertedBinarytoDecimal, err := ConvertBinaryToDecimal(binaryValue)
		if err != nil {
			fmt.Printf("\nThe value '%s' is not a binary. Try again.\n\n", binaryValue)
			continue
		}
		fmt.Printf("\nBinary value: %s", binaryValue)
		fmt.Printf("\nDecimal value: %d\n\n", convertedBinarytoDecimal)
	}
}

func userInput(reader *bufio.Reader) string {
	fmt.Println("What value do you want to convert from binary to decimal? ")
	input, _ := reader.ReadString('\n')
	return strings.Replace(input, "\n", "", -1)
}
