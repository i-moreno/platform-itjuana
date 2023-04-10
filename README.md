# Platform-itjuana

This application reads two different txt files and returns the relations between drivers and shipments directly in the console.

* Requirements
  - Python 3

## Usage
Once you cloned the repo, enter to the folder an in the root of the project run the following command


```
python src/app drivers.txt shipments.txt
```

The application expect two different file's path, the firs should be the path to drivers file, 
the second one should be the path to the shipments file. <strong>Order matters!</strong>

In this case the application comes with two demo files so you can test it once you have cloned it.

## Important!
- The order matters, the first path should be to the drivers file the second one should be to the shipments file.
- The program only supports `txt` files.
- The name of the files doesn't matter.
- In some cases you might not have binded python 3 to your terminal and that can lead to issues, in that case you could either create an alias for python 3 or just try te application with python 3 interpreter directly: python3 src/app drivers.txt shipments.txt
