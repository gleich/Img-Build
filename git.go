package main

import (
	"fmt"
	"log"
	"os/exec"
)

func version() {
	out, err := exec.Command("git", "--version").Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("The date is %s\n", out)
}
