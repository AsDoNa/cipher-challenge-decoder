const fileInput = document.getElementById('corpus-file');
const textFileInput = document.getElementById('corpus');

var reader = new FileReader();

reader.addEventListener(
    "load",
    () => {
        textFileInput.value = reader.result
    }
)

fileInput.onchange = () => {
    const selectedFile = fileInput.files[0];
    reader.readAsText(selectedFile, "UTF-8");
}