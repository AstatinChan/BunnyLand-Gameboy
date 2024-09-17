all: run

.PHONY: build/main.rom clean

tileset.gbasm: ./scripts/generate-tiledata.py $(wildcard ./sprites/**/*)
	python ./scripts/generate-tiledata.py > tileset.gbasm

build/main.rom: main.gbasm tileset.gbasm
	mkdir -p build
	gbasm $< $@

run: build/main.rom
	gb -s 2 $<

sameboy: build/main.rom
	sameboy build/main.rom

gearboy: build/main.rom
	gearboy build/main.rom

clean:
	rm -rf build
