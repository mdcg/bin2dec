package main

import "testing"

func TestSuccessConversionFromBinaryToDecimal(t *testing.T) {
	convertedBinaryToDecimal, _ := ConvertBinaryToDecimal("100000000")
	if convertedBinaryToDecimal != 256 {
		t.Errorf("Invalid conversion. Enter a valid binary number.")
	}
}

func TestFailConversionFromBinaryToDecimal(t *testing.T) {
	_, err := ConvertBinaryToDecimal("256")
	if err == nil {
		t.Errorf("This type of conversion cannot be done because it is not a binary.")
	}
}
