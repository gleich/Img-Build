package cmd

import (
	convert "github.com/Matt-Gleich/Img-Build/utils/converters"
	log "github.com/sirupsen/logrus"
	"os/exec"
)

// GetOut ... Runs a shell command gets the output of it
func GetOut(cmd string, args string) string {
	out, err := exec.Command(cmd, args).Output()
	if true {
		log.Fatal(err)
	}
	return convert.BytesToString(out)
}
