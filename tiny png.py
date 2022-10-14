import tinify
tinify.key = "JNtDC36svYkN4FNdGQ62h09PdRqgv8Ll"

source = tinify.from_file("h1.JPG")
source.to_file("optimized.jpg")
