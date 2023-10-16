
// Function to save input values to Local Storage
function saveInputs() {
    const textInput = document.getElementById('text');
    const shiftInput = document.getElementById('shift');
    const operationInput = document.getElementById('operation');
    const alphabetInput = document.getElementById('alphabet');
    const anpInput = document.getElementById('anp');
    const minLengthInput = document.getElementById('min_length');
    const maxLengthInput = document.getElementById('max_length');
    const tightInput = document.getElementById('tight');
    console.log("ELEMENTS GOT");

    // Save input values to Local Storage
    localStorage.setItem('text', textInput.value);
    localStorage.setItem('shift', shiftInput.value);
    localStorage.setItem('operation', operationInput.value);
    localStorage.setItem('alphabet', alphabetInput.value);
    localStorage.setItem('anp', anpInput.value);
    localStorage.setItem('min_length', minLengthInput.value);
    localStorage.setItem('max_length', maxLengthInput.value);
    localStorage.setItem('tight', tightInput.value);
    console.log("LOCAL STORAGE SET");
}

// Function to load input values from Local Storage
function loadInputs() {
    const textInput = document.getElementById('text');
    const shiftInput = document.getElementById('shift');
    const operationInput = document.getElementById('operation');
    const alphabetInput = document.getElementById('alphabet');
    const anpInput = document.getElementById('anp');
    const minLengthInput = document.getElementById('min_length');
    const maxLengthInput = document.getElementById('max_length');
    const tightInput = document.getElementById('tight');
    console.log("ELEMENTS GOT");
    
    // Load input values from Local Storage
    textInput.value = localStorage.getItem('text') || '';
    shiftInput.value = localStorage.getItem('shift') || '';
    operationInput.value = localStorage.getItem('operation') || 'encode';
    alphabetInput.value = localStorage.getItem('alphabet') || 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    anpInput.value = localStorage.getItem('anp') || 'a';
    minLengthInput.value = localStorage.getItem('min_length') || '26';
    maxLengthInput.value = localStorage.getItem('max_length') || '26';
    tightInput.value = localStorage.getItem('tight') || 'Y';
    console.log("LOCAL STORAGE GOT")
}

// Call the loadInputs function when the page loads
window.addEventListener('load', loadInputs);

// Call the saveInputs function when the form is submitted
document.querySelector('form').addEventListener('submit', saveInputs);
