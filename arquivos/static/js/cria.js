var FilesList;

const storeFiles = files => {
    FilesList = files;
}

const readMultiFiles = () => {
    const div = document.getElementById("div");

        const setup_reader = (file, type) => {
            var reader = new FileReader();

            reader.onload = e => {
                var res;
                res = e.target.result;
                arquivo = Arquivo(texto = res)
            }
            reader.readAsBinaryString(file);
        }

        for (var i = 0; i < FilesList.length; i++) {
            if (FilesList[i].name.indexOf(".txt") != -1) {
                setup_reader(FilesList[i], "text");
            } else {
                setup_reader(FilesList[i], "img");
            }
        }
    }
