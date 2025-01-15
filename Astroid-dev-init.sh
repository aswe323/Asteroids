go install github.com/bootdotdev/bootdev@latest
export PATH="$PATH:/home/matan/go/bin/"
python3 -m venv venv
set VIRTUAL_ENV "/home/matan/bootdev/Asteroids/venv"
nix-shell -p python312Packages.pygame
