const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const dropArea = document.getElementById("dropArea");
const loading = document.getElementById("loading");
const form = document.querySelector("form");

imageInput.addEventListener(
    "change",
    function(){
        const file = this.files[0];
        if(file){
            previewImage.src = URL.createObjectURL(file);
            previewImage.style.display = "block";
        }
    }
);

[
    "dragenter",
    "dragover",
    "dragleave",
    "drop"

].forEach(eventName => {
    dropArea.addEventListener(
        eventName,
        preventDefaults,
        false
    );
});

function preventDefaults(e){
    e.preventDefault();
    e.stopPropagation();

}

[
    "dragenter",
    "dragover"

].forEach(eventName => {

    dropArea.addEventListener(
        eventName,
        function(){
            dropArea.style.background =
            "rgba(255,255,255,0.15)";
        }
    );
});

[
    "dragleave",
    "drop"

].forEach(eventName => {
    dropArea.addEventListener(
        eventName,
        function(){
            dropArea.style.background =
            "transparent";
        }
    );
});

dropArea.addEventListener(
    "drop",
    function(e){
        let files = e.dataTransfer.files;
        if(files.length > 0){
            imageInput.files = files;
            previewImage.src =
            URL.createObjectURL(files[0]);
            previewImage.style.display =
            "block";
        }
    }
);

form.addEventListener(
    "submit",
    function(){
        loading.style.display =
        "block";
    }
);