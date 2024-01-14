const textboxA = document.getElementById("grid_a");
const gridTextboxesA = document.querySelectorAll(".grid-textbox-a");
const textboxB = document.getElementById("grid_b");
const gridTextboxesB = document.querySelectorAll(".grid-textbox-b");
const textboxC = document.getElementById("grid_c");
const gridTextboxesC = document.querySelectorAll(".grid-textbox-c");
const textboxD = document.getElementById("grid_d");
const gridTextboxesD = document.querySelectorAll(".grid-textbox-d");

textboxA.addEventListener("input", () => {
    const mainText = textboxA.value;
    let gridIndex = 0;

    gridTextboxesA.forEach(textbox => {
        textbox.value = mainText[gridIndex] || "";
        gridIndex++;
    });
});

gridTextboxesA.forEach(textbox => {
    textbox.addEventListener("input", () => {
        let updatedText = "";
        gridTextboxesA.forEach(textbox => {
            updatedText += textbox.value;
        });
        textboxA.value = updatedText;
    });
});

textboxB.addEventListener("input", () => {
    const mainText = textboxB.value;
    let gridIndex = 0;

    gridTextboxesB.forEach(textbox => {
        textbox.value = mainText[gridIndex] || "";
        gridIndex++;
    });
});

gridTextboxesB.forEach(textbox => {
    textbox.addEventListener("input", () => {
        let updatedText = "";
        gridTextboxesB.forEach(textbox => {
            updatedText += textbox.value;
        });
        textboxB.value = updatedText;
    });
});

textboxC.addEventListener("input", () => {
    const mainText = textboxC.value;
    let gridIndex = 0;

    gridTextboxesC.forEach(textbox => {
        textbox.value = mainText[gridIndex] || "";
        gridIndex++;
    });
});

gridTextboxesC.forEach(textbox => {
    textbox.addEventListener("input", () => {
        let updatedText = "";
        gridTextboxesC.forEach(textbox => {
            updatedText += textbox.value;
        });
        textboxC.value = updatedText;
    });
});

textboxD.addEventListener("input", () => {
    const mainText = textboxD.value;
    let gridIndex = 0;

    gridTextboxesD.forEach(textbox => {
        textbox.value = mainText[gridIndex] || "";
        gridIndex++;
    });
});

gridTextboxesD.forEach(textbox => {
    textbox.addEventListener("input", () => {
        let updatedText = "";
        gridTextboxesD.forEach(textbox => {
            updatedText += textbox.value;
        });
        textboxD.value = updatedText;
    });
});

