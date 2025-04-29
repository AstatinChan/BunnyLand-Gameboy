all: run

.PHONY: build/main.rom clean

tileset.gbasm: ./scripts/generate-tiledata.py $(wildcard ./sprites/**/* ./sprites/*)
	python ./scripts/generate-tiledata.py > tileset.gbasm

%.gbasm: ./%.gbtxt ./scripts/generate_from_gbtxt.py
	python ./scripts/generate_from_gbtxt.py $< > $@

build/main.rom: build/main.rom.unsigned
	cp build/main.rom.unsigned build/main.rom
	python scripts/set_checksums.py build/main.rom

build/main.rom.unsigned: main.gbasm tileset.gbasm text.gbasm dialogues/text.gbasm
	mkdir -p build
	gbasm $< $@ > build/main.sym

run: build/main.rom
	mkdir -p recordings
	gb $< --record-input "./recordings/$(shell date -Iseconds).record"

sameboy: build/main.rom
	sameboy build/main.rom

gearboy: build/main.rom
	gearboy build/main.rom build/main.sym

clean:
	rm -rf buil1
