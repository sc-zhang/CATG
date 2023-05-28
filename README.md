## Introduction
CATG (**C**ollinearity-based **A**ssembly correc**T**or **G**UI) is a GUI application base on Qt with PySide6. 
It is a tool that can adjust assembly with collinearity and generate tour files for assembly.

## Dependencies

### Software
* [jcvi](https://github.com/tanghaibao/jcvi)
* [ALLHiC](https://github.com/tangerzhang/ALLHiC)
* Python 3.7+

### Python Modules
* PySide6
* qt-material
* matplotlib

## Installation

### Download binary file
Download executable file from release.
### Run with source code
```bash
python3 CATG.py
```
### Package your own binary file
```bash
# Python==3.10
python -m venv venv
source venv/bin/activate
# For some reason, these three Packages with the versions show below will
# increase the success rate of packaging.
pip install nuitka==1.5.6
pip install PySide6==6.4.2
pip install packaging==21.3

pip install matplotlib ordered-set zstandard qt-material
# For windows
python -m nuitka --standalone --windows-disable-console --mingw64 --show-memory --show-progress --nofollow-imports --plugin-enable=pyside6 --follow-import-to=matplotlib,qt_material --nofollow-import-to=tkinter --include-data-files="coll_asm_corr_gui/resources/CATG.png"="coll_asm_corr_gui/resources/CATG.png" --include-package-data="qt_material" --windows-icon-from-ico="coll_asm_corr_gui/resources/CATG.ico" --onefile CATG.py
# For macOS
python -m nuitka --standalone --windows-disable-console --show-memory --show-progress --nofollow-imports --plugin-enable=pyside6 --follow-import-to=matplotlib,qt_material --nofollow-import-to=tkinter --include-data-files="coll_asm_corr_gui/resources/CATG.png"="coll_asm_corr_gui/resources/CATG.png" --include-package-data="qt_material" CATG.py --macos-create-app-bundle --macos-app-icon="coll_asm_corr_gui/resources/CATG.icns"
```
## Data preparation
Run jcvi for generating anchors file
```bash
python -m jcvi.compara.catalog ortholog query.bed reference.bed
```
The query.bed, reference.bed, query.reference.anchors, query.agp are all files we need.

## Operations

### Main operations
There are 6 type of operations can be done.

1. **Insert front**  
   Move block with source block id from source chromosome to target chromosome and insert it in front of target block.
2. **Insert back**  
   Move block with source block id from source chromosome to target chromosome and insert it after target block.
3. **Insert head**  
   Move block with source block id from source chromosome to target chromosome and insert it to the head of target chromosome.
4. **Insert tail**  
   Move block with source block id from source chromosome to target chromosome and insert it to the tail of target chromosome.  
   _Operate 1-4 can work with Reverse checkbox, if Reverse checkbox is set checked, the block from source chromosome will be reverse complement before insert to target positiong._
5. **Source chromosome**
6. **Source block**  
   These two operate only affect while Reverse checkbox is set checked, then it will reverse the source chromosome or source block.
7. **Swap chromosome**
8. **Swap block**  
   These two operate can swap regions or chromosomes, and Reverse option won't affect.
9. **Delete block**  
   Delete block from source chromosome.
### Others
You can resize the collinearity figure with wheel, and use mouse to drag it.

## Example

### Step1. Open CATG and click "LOADFILES"
![](Manual/Step1.LoadFiles.png)

### Step2. Select files
![](Manual/Step2.SelectFiles.png)

### Step3. Set Operations
![](Manual/Step3.SetOperations.png)
The red rectangles above means move Block 1 in Chromosome 1 to the tail of Chromosome 1, and convert Block1 to its reverse complement. 

### Step4. Modify
After click "MODIFY" button, the new collinearity figure will be updated, it may take several seconds, please be patient.
![](Manual/Step4.Modified.png)

### Step5. Refresh
If you want cluster less contigs in single block, increase Resolution value may help you.
After that, click "REFRESH" button to update collinearity figure.
![](Manual/Step5.Refresh.png)

### Step6. Save
Click "SAVE FILES" to save the adjusted tour files, after that ALLHiC_build can use for building new chromosome assembly from contig level assembly, or use allhic optimize to determine the order and orientation of contigs.
![](Manual/Step6.SaveFiles.png)
![](Manual/Step7.SavedFiles.png)
