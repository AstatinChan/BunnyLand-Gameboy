all: run

.PHONY: build/main.rom clean

build/main.rom: main.gbasm 
	mkdir -p build
	gbasm $< $@

run: build/main.rom
	gb -s 200 $<

sameboy: build/main.rom
	sameboy build/main.rom

gearboy: build/main.rom
	gearboy build/main.rom

clean:
	rm -rf build
