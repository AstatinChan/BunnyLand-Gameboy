GBASM=gbasm
MAKESELF=makeself

all: run

.PHONY: clean sclean

tileset.gbasm: ./scripts/generate-tiledata.py $(wildcard ./sprites/**/* ./sprites/*)
	@echo "; THIS FILE IS GENERATED AUTOMATICALLY, DO NOT CHANGE" > $@
	python ./scripts/generate-tiledata.py >> $@

%.gbasm: ./%.gbtxt ./scripts/generate_from_gbtxt.py
	@echo "; THIS FILE IS GENERATED AUTOMATICALLY, DO NOT CHANGE" > $@
	python ./scripts/generate_from_gbtxt.py $< >> $@

%.map.gbasm: ./%.ldtk ./scripts/parse-ldtkmap.py
	@echo "; THIS FILE IS GENERATED AUTOMATICALLY, DO NOT CHANGE" > $@
	python ./scripts/parse-ldtkmap.py $< >> $@

map/maps.gbasm: $(subst .ldtk,.map.gbasm,$(wildcard ./map/maps/*.ldtk))
	@echo "; THIS FILE IS GENERATED AUTOMATICALLY, DO NOT CHANGE" > $@
	ls ./map/maps/*.map.gbasm | sed 's/^\.\///' | awk '{print ".INCLUDE \""$$0"\"" }' >> $@

build/main.rom: build/main.rom.unsigned
	cp build/main.rom.unsigned build/main.rom
	python scripts/set_checksums.py build/main.rom

build/main.rom.unsigned: main.gbasm tileset.gbasm text.gbasm dialogues/text.gbasm map/maps.gbasm $(wildcard ./*.gbasm) $(wildcard ./**/*.gbasm) $(wildcard ./**/**/*.gbasm)
	mkdir -p build
	$(GBASM) $< $@ > build/main.sym

build/tileset-dump.rom: scripts/tileset-dump.gbasm
	mkdir -p build
	$(GBASM) $< $@ > /dev/null

build/tileset-dump.rom.vram.dump: build/tileset-dump.rom
	gb --skip-bootrom --stop-dump-state $<

build/tileset.png: build/tileset-dump.rom.vram.dump scripts/extract-vram-tileset.py
	python scripts/extract-vram-tileset.py $< $@

build/makeself/gb_linux-x86_64:
	mkdir -p build/makeself
	wget https://github.com/AstatinChan/gameboy-emulator/releases/download/latest/gb_linux-x86_64 -O $@
	chmod +x $@

build/makeself/main.rom: build/main.rom
	mkdir -p build/makeself
	cp $< $@

build/makeself/start.sh: ./scripts/makeself-start.sh
	mkdir -p build/makeself
	cp $< $@
	chmod +x $@

build/game_linux_x86-64: build/makeself/start.sh build/makeself/main.rom build/makeself/gb_linux-x86_64
	$(MAKESELF) ./build/makeself $@ "Astatin's Bunny Game" ./start.sh

run: build/main.rom
	mkdir -p recordings
	gb $< --record-input "./recordings/$(shell date -Iseconds).record"

sameboy: build/main.rom
	sameboy build/main.rom

gearboy: build/main.rom
	gearboy build/main.rom build/main.sym

clean:
	rm -rf build

sclean: clean
	rm tileset.gbasm
	find . -name "*.gbtxt" | sed 's/\.gbtxt$$/.gbasm/' | xargs rm
	rm map/maps/*.map.gbasm map/maps.gbasm
