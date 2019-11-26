package main

import (
	"github.com/Matt-Gleich/Img-Build/utils/cmd"
)

// Version ... Gets the version of git
func Version() {
	cmd.GetOut("git", "--versio")
}
