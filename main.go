package main

import (
	"fmt"
	"github.com/Matt-Gleich/Img-Build/utils/cmd"
)

func main() {
	fmt.Println(cmd.GetOut("git", "--version"))
}
