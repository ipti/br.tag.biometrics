#!/bin/bash

echo "Synchronising"
/usr/bin/rsync -a /mnt/c/Users/CoordTI/Projetos/br.tag.biometrics ipti@raspberrypi:/home/ipti/projects
echo "Synchronising finished"
