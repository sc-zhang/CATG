## Introduction
MCAAG (Manual Collinearity Assembly Adjuster GUI) is a GUI application base on Qt 5 with PySide2. 
It is a tool that can adjust assembly with collinearity and generate tour files for assembly.

## Dependencies

### Software
* [jcvi](https://github.com/tanghaibao/jcvi)
* [ALLHiC](https://github.com/tangerzhang/ALLHiC)
* Python 3.6+

## Python Modules
* PySide2
* matplotlib

## Installation
```bash
git clone https://github.com/sc-zhang/MCAAG.git
cd /path/to/install/MCAAG
python3 MCAAG.py
```

## Usage
Run jcvi for generating anchors file
```bash
python -m jcvi.compara.catalog ortholog query.bed reference.bed
```
The query.bed, reference.bed, query.reference.anchors, query.agp are all files we need.

### Step 1. Open main form
![](Manual/MainForm.png "Main Form")

Click "Load files" button
### Step 2. Load files
![](Manual/FileLoader.png "File Loader")

Select all 4 required files.

### Step 3. Adjust assembly manually

There are 6 type of operate can be done.

1. **Insert front**  
   Move block with source block id from source chromosome to target chromosome and insert it in front of target block.
2. **Insert back**  
   Move block with source block id from source chromosome to target chromosome and insert it after target block.
3. **Insert head**  
   Move block with source block id from source chromosome to target chromosome and insert it to the head of target chromosome.
4. **Insert tail**  
   Move block with source block id from source chromosome to target chromosome and insert it to the tail of target chromosome.  
   _Operate 1-4 can work with Reverse checkbox, if Reverse checkbox is set checked, the block from source chromosome will be reverse complement before insert to target positiong._
5. **Source chromosome** 6. **Source block**
   These two operate only affect while Reverse checkbox is set checked, then it will reverse the source chromosome or source block.

For example:
![](Manual/Loaded.png "Data loaded")

We can move block 1 to the end of Chr01 with reverse complement.
![](Manual/InsertBlock1ToTail.png "Insert block")

## Generate executable file
If you want executable file, please use pyinstaller, and run commands below
```bash
pip install pyinstaller
pyinstaller --noconsole MCAAG.py -i "coll_asm_adj_gui/ui/MCAAG.ico" --hidden-import PySide2.QtXml --add-data "coll_asm_adj_gui/ui:coll_asm_adj_gui/ui" -F -w
```
After all done, copy MCAAG in dist folder to anywhere with same platform to use it.