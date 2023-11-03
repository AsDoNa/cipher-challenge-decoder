
// Function to save input values to Local Storage
function saveInputs() {
    const textInput = document.getElementById('text');
    const shiftInput = document.getElementById('shift');
    const shiftLengthInput = document.getElementById('shift_length');
    const keyInput = document.getElementById('key');
    const inverseKeyInput = document.getElementById('inverse-key');
    const operationInput = document.getElementById('operation');
    const alphabetInput = document.getElementById('alphabet');
    const anpInput = document.getElementById('anp');
    const minLengthInput = document.getElementById('min_length');
    const maxLengthInput = document.getElementById('max_length');
    const tightInput = document.getElementById('tight');
    console.log("ELEMENTS GOT!")

    // Save input values to Local Storage
    try {
    localStorage.setItem('text', textInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('shift', shiftInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('shift_length', shiftLengthInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('key', keyInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('inverse-key', inverseKeyInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('operation', operationInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('alphabet', alphabetInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('anp', anpInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('min_length', minLengthInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('max_length', maxLengthInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        localStorage.setItem('tight', tightInput.value);
    } catch (err) {
        console.log("ERROR: " + err);
    }
    console.log("LOCAL STORAGE SET");
}

// Function to load input values from Local Storage
function loadInputs() {
    const textInput = document.getElementById('text');
    const shiftInput = document.getElementById('shift');
    const shiftLengthInput = document.getElementById('shift_length');
    const keyInput = document.getElementById('key');
    const inverseKeyInput = document.getElementById('inverse-key');
    const operationInput = document.getElementById('operation');
    const alphabetInput = document.getElementById('alphabet');
    const anpInput = document.getElementById('anp');
    const minLengthInput = document.getElementById('min_length');
    const maxLengthInput = document.getElementById('max_length');
    const tightInput = document.getElementById('tight');
    console.log("ELEMENTS GOT!")

    console.log(localStorage);
    
    // Load input values from Local Storage
    try {
        textInput.value = localStorage.getItem('text') || '';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        shiftInput.value = localStorage.getItem('shift') || '';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        shiftLengthInput.value = localStorage.getItem('shift_length') || '';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        keyInput.value = localStorage.getItem('key') || '';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        inverseKeyInput.value = localStorage.getItem('inverse-key') || '';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        operationInput.value = localStorage.getItem('operation') || 'encode';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        alphabetInput.value = localStorage.getItem('alphabet') || 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        anpInput.value = localStorage.getItem('anp') || 'a';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        minLengthInput.value = localStorage.getItem('min_length') || '26';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        maxLengthInput.value = localStorage.getItem('max_length') || '26';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    try {
        tightInput.value = localStorage.getItem('tight') || 'Y';
    } catch (err) {
        console.log("ERROR: " + err);
    }
    console.log("LOCAL STORAGE GOT")
}

// Call the loadInputs function when the page loads
window.addEventListener('load', loadInputs);

// Call the saveInputs function when the form is submitted
document.querySelector('form').addEventListener('submit', saveInputs);
