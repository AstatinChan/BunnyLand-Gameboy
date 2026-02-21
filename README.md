# Bunnyland (temporary name)

This is a gameboy game I am coding [live on twitch](https:/www.twitch.tv/astatinchan) ! Come and hang out !

# How to compile

This game is made using Z80 assembly and should be compiled with the assembler I made for it

The assembler is made in golang, check if you have it on your system, If you do not:

```bash
# Arch
sudo pacman -S go

# Debian/Ubuntu
sudo apt install golang

# Windows:
# I don't know lol
```

Clone the assembler:
```bash
git clone https://git.astatin.live/gameboy-asm.git
cd gameboy-asm
```

Compile the assembler:
```bash
go build .
```

And copy it as `gbasm` somewhere in your $PATH
```bash
sudo cp gameboy-asm /usr/local/bin/gbasm
```

We can now download the game sources
```bash
git clone http://git.astatin.live/bunny-game.git
cd bunny-game
```

And assemble the ROM
```bash
make build/main.rom
```

The rom is inside of the build/ directory and can be played with the gameboy emulator of your choice (I also made an emulator you can use [here](https://git.astatin.live/gameboy-emulator.git/about/))
